import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import json

# Simple CNN using only basic libraries
try:
    import tensorflow as tf
    from tensorflow.keras import layers, models, optimizers
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    TF_AVAILABLE = True
except ImportError:
    print("TensorFlow not available. Using mock training for demonstration.")
    TF_AVAILABLE = False

class SimpleLeafDiseaseDetector:
    def __init__(self, img_size=(128, 128)):
        self.img_size = img_size
        self.class_indices = {'Diseased': 0, 'Healthy': 1}
        self.class_names = {v: k for k, v in self.class_indices.items()}
        
    def load_data(self, dataset_path):
        """Load and preprocess the dataset"""
        images = []
        labels = []
        
        print(f"Loading data from: {dataset_path}")
        
        # Load diseased images
        diseased_path = os.path.join(dataset_path, 'Diseased')
        if os.path.exists(diseased_path):
            for img_name in os.listdir(diseased_path)[:100]:  # Limit for demo
                if img_name.endswith(('.jpg', '.jpeg', '.png')):
                    img_path = os.path.join(diseased_path, img_name)
                    img = self._preprocess_image(img_path)
                    if img is not None:
                        images.append(img)
                        labels.append(self.class_indices['Diseased'])
        
        # Load healthy images
        healthy_path = os.path.join(dataset_path, 'Healthy')
        if os.path.exists(healthy_path):
            for img_name in os.listdir(healthy_path)[:100]:  # Limit for demo
                if img_name.endswith(('.jpg', '.jpeg', '.png')):
                    img_path = os.path.join(healthy_path, img_name)
                    img = self._preprocess_image(img_path)
                    if img is not None:
                        images.append(img)
                        labels.append(self.class_indices['Healthy'])
        
        return np.array(images), np.array(labels)
    
    def _preprocess_image(self, img_path):
        """Preprocess a single image"""
        try:
            img = cv2.imread(img_path)
            if img is None:
                return None
            
            # Convert BGR to RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Resize
            img = cv2.resize(img, self.img_size)
            
            # Normalize
            img = img.astype(np.float32) / 255.0
            
            return img
        except:
            return None
    
    def build_simple_model(self):
        """Build a simple CNN model"""
        if not TF_AVAILABLE:
            return None
            
        model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(self.img_size[0], self.img_size[1], 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(2, activation='sigmoid')
        ])
        
        model.compile(optimizer='adam',
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])
        
        return model
    
    def train_model(self, X, y):
        """Train the model"""
        if not TF_AVAILABLE:
            print("Mock training completed (TensorFlow not available)")
            return None
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Build and train model
        model = self.build_simple_model()
        
        if model is None:
            return None
        
        print("Training model...")
        history = model.fit(X_train, y_train, epochs=10, 
                           validation_data=(X_test, y_test), verbose=1)
        
        # Save model
        os.makedirs('models', exist_ok=True)
        model.save('models/simple_leaf_model.h5')
        
        # Save class indices
        with open('models/class_indices.json', 'w') as f:
            json.dump(self.class_indices, f)
        
        # Evaluate
        test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
        print(f"Test accuracy: {test_acc:.4f}")
        
        return history
    
    def create_demo_predictions(self):
        """Create demo predictions for the web app"""
        # Create a mock model file for demo purposes
        os.makedirs('models', exist_ok=True)
        
        # Create a simple text file to indicate demo mode
        with open('models/demo_mode.txt', 'w') as f:
            f.write("Demo mode - TensorFlow not available")
        
        # Create class indices file
        with open('models/class_indices.json', 'w') as f:
            json.dump(self.class_indices, f)
        
        print("Demo mode setup completed!")

def main():
    print("🌿 Simple Leaf Disease Detection System 🌿")
    
    dataset_path = r"d:\DS_AI_Internship\src\Day22\leaf_disease_classified_dataset"
    
    detector = SimpleLeafDiseaseDetector()
    
    # Load data
    print("🔄 Loading data...")
    X, y = detector.load_data(dataset_path)
    
    if len(X) == 0:
        print("❌ No data found!")
        return
    
    print(f"✅ Loaded {len(X)} images")
    print(f"📊 Class distribution: {np.bincount(y)}")
    
    if TF_AVAILABLE:
        # Train model
        print("🚀 Training model...")
        history = detector.train_model(X, y)
        
        if history:
            print("✅ Training completed!")
        else:
            print("❌ Training failed!")
    else:
        # Create demo setup
        print("🎭 Setting up demo mode...")
        detector.create_demo_predictions()
        print("✅ Demo mode ready!")

if __name__ == "__main__":
    main()
