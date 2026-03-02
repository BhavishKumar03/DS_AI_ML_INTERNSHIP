import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import os

class LeafDiseaseModel:
    def __init__(self, input_shape=(224, 224, 3), num_classes=2):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = None
        
    def build_model(self):
        """Build the CNN model using transfer learning"""
        # Load pre-trained MobileNetV2 without top layer
        base_model = MobileNetV2(
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Freeze the base model
        base_model.trainable = False
        
        # Build the complete model
        model = models.Sequential([
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(64, activation='relu'),
            layers.Dropout(0.3),
            layers.Dense(self.num_classes, activation='sigmoid')
        ])
        
        self.model = model
        return model
    
    def compile_model(self, learning_rate=0.001):
        """Compile the model"""
        if self.model is None:
            raise ValueError("Model not built. Call build_model() first.")
        
        optimizer = optimizers.Adam(learning_rate=learning_rate)
        
        self.model.compile(
            optimizer=optimizer,
            loss='binary_crossentropy',
            metrics=['accuracy', 'precision', 'recall']
        )
    
    def get_callbacks(self, model_save_path):
        """Get training callbacks"""
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=5,
                restore_best_weights=True,
                verbose=1
            ),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.2,
                patience=3,
                min_lr=1e-7,
                verbose=1
            ),
            ModelCheckpoint(
                filepath=model_save_path,
                monitor='val_accuracy',
                save_best_only=True,
                verbose=1
            )
        ]
        return callbacks
    
    def train(self, train_generator, val_generator, epochs, model_save_path):
        """Train the model"""
        if self.model is None:
            raise ValueError("Model not built. Call build_model() first.")
        
        # Create model directory if it doesn't exist
        os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
        
        callbacks = self.get_callbacks(model_save_path)
        
        history = self.model.fit(
            train_generator,
            epochs=epochs,
            validation_data=val_generator,
            callbacks=callbacks,
            verbose=1
        )
        
        return history
    
    def fine_tune(self, train_generator, val_generator, epochs, model_save_path):
        """Fine-tune the model by unfreezing some layers"""
        if self.model is None:
            raise ValueError("Model not built. Call build_model() first.")
        
        # Unfreeze the top layers of the model
        base_model = self.model.layers[0]
        base_model.trainable = True
        
        # Freeze all layers except the last 20
        for layer in base_model.layers[:-20]:
            layer.trainable = False
        
        # Recompile with a lower learning rate
        self.compile_model(learning_rate=1e-5)
        
        callbacks = self.get_callbacks(model_save_path)
        
        history = self.model.fit(
            train_generator,
            epochs=epochs,
            validation_data=val_generator,
            callbacks=callbacks,
            verbose=1
        )
        
        return history
    
    def load_model(self, model_path):
        """Load a trained model"""
        self.model = tf.keras.models.load_model(model_path)
    
    def predict(self, image):
        """Make prediction on a single image"""
        if self.model is None:
            raise ValueError("Model not loaded. Call load_model() or train() first.")
        
        # Ensure image has batch dimension
        if len(image.shape) == 3:
            image = np.expand_dims(image, axis=0)
        
        prediction = self.model.predict(image)
        return prediction
    
    def predict_class(self, image, class_names):
        """Predict class name for a single image"""
        prediction = self.predict(image)
        class_idx = np.argmax(prediction[0])
        confidence = prediction[0][class_idx]
        class_name = class_names[class_idx]
        
        return {
            'class': class_name,
            'confidence': float(confidence),
            'probabilities': {
                'Diseased': float(prediction[0][0]),
                'Healthy': float(prediction[0][1])
            }
        }
    
    def evaluate(self, test_generator):
        """Evaluate the model on test data"""
        if self.model is None:
            raise ValueError("Model not loaded. Call load_model() or train() first.")
        
        results = self.model.evaluate(test_generator, verbose=1)
        return dict(zip(['loss', 'accuracy', 'precision', 'recall'], results))
    
    def summary(self):
        """Print model summary"""
        if self.model is None:
            raise ValueError("Model not built. Call build_model() first.")
        
        self.model.summary()
