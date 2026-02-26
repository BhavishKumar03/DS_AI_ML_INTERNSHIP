import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
import json

class DataPreprocessor:
    def __init__(self, img_size=(224, 224)):
        self.img_size = img_size
        self.class_indices = {'Diseased': 0, 'Healthy': 1}
        self.class_names = {v: k for k, v in self.class_indices.items()}
        
    def load_and_preprocess_data(self, dataset_path):
        """Load and preprocess the dataset"""
        images = []
        labels = []
        
        # Load diseased images
        diseased_path = os.path.join(dataset_path, 'Diseased')
        for img_name in os.listdir(diseased_path):
            if img_name.endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(diseased_path, img_name)
                img = self._preprocess_image(img_path)
                images.append(img)
                labels.append(self.class_indices['Diseased'])
        
        # Load healthy images
        healthy_path = os.path.join(dataset_path, 'Healthy')
        for img_name in os.listdir(healthy_path):
            if img_name.endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(healthy_path, img_name)
                img = self._preprocess_image(img_path)
                images.append(img)
                labels.append(self.class_indices['Healthy'])
        
        return np.array(images), np.array(labels)
    
    def _preprocess_image(self, img_path):
        """Preprocess a single image"""
        # Read image
        img = cv2.imread(img_path)
        if img is None:
            raise ValueError(f"Could not read image: {img_path}")
        
        # Convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Resize
        img = cv2.resize(img, self.img_size)
        
        # Normalize to [0, 1]
        img = img.astype(np.float32) / 255.0
        
        return img
    
    def create_data_generators(self, X, y, validation_split=0.2, test_split=0.1, batch_size=32):
        """Create train, validation, and test data generators"""
        # Split data
        X_temp, X_test, y_temp, y_test = train_test_split(
            X, y, test_size=test_split, random_state=42, stratify=y
        )
        
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=validation_split/(1-test_split), 
            random_state=42, stratify=y_temp
        )
        
        # Data augmentation for training
        train_datagen = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        
        # Only rescaling for validation and test
        val_test_datagen = ImageDataGenerator()
        
        # Create generators
        train_generator = train_datagen.flow(
            X_train, y_train, batch_size=batch_size, shuffle=True
        )
        
        val_generator = val_test_datagen.flow(
            X_val, y_val, batch_size=batch_size, shuffle=False
        )
        
        test_generator = val_test_datagen.flow(
            X_test, y_test, batch_size=batch_size, shuffle=False
        )
        
        return train_generator, val_generator, test_generator, (X_test, y_test)
    
    def save_class_indices(self, filepath):
        """Save class indices to JSON file"""
        with open(filepath, 'w') as f:
            json.dump(self.class_indices, f)
    
    def load_class_indices(self, filepath):
        """Load class indices from JSON file"""
        with open(filepath, 'r') as f:
            self.class_indices = json.load(f)
        self.class_names = {v: k for k, v in self.class_indices.items()}
