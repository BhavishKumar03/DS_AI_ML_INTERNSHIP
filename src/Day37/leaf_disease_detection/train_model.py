import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from config import *
from data_preprocessing import DataPreprocessor
from model import LeafDiseaseModel

def plot_training_history(history, save_path='training_history.png'):
    """Plot training history"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Loss
    ax1.plot(history.history['loss'], label='Training Loss')
    ax1.plot(history.history['val_loss'], label='Validation Loss')
    ax1.set_title('Model Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.legend()
    
    # Accuracy
    ax2.plot(history.history['accuracy'], label='Training Accuracy')
    ax2.plot(history.history['val_accuracy'], label='Validation Accuracy')
    ax2.set_title('Model Accuracy')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.legend()
    
    # Precision
    ax3.plot(history.history['precision'], label='Training Precision')
    ax3.plot(history.history['val_precision'], label='Validation Precision')
    ax3.set_title('Model Precision')
    ax3.set_xlabel('Epoch')
    ax3.set_ylabel('Precision')
    ax3.legend()
    
    # Recall
    ax4.plot(history.history['recall'], label='Training Recall')
    ax4.plot(history.history['val_recall'], label='Validation Recall')
    ax4.set_title('Model Recall')
    ax4.set_xlabel('Epoch')
    ax4.set_ylabel('Recall')
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def plot_confusion_matrix(y_true, y_pred, class_names, save_path='confusion_matrix.png'):
    """Plot confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig(save_path)
    plt.show()

def main():
    print("🌿 Leaf Disease Detection System - Training 🌿")
    
    # Initialize components
    preprocessor = DataPreprocessor(img_size=IMG_SIZE)
    model = LeafDiseaseModel(input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3), num_classes=2)
    
    print(f"📁 Loading dataset from: {DATASET_PATH}")
    
    # Load and preprocess data
    print("🔄 Loading and preprocessing data...")
    X, y = preprocessor.load_and_preprocess_data(DATASET_PATH)
    print(f"✅ Loaded {len(X)} images with {len(np.unique(y))} classes")
    print(f"📊 Class distribution: {np.bincount(y)}")
    
    # Create data generators
    print("🔄 Creating data generators...")
    train_gen, val_gen, test_gen, (X_test, y_test) = preprocessor.create_data_generators(
        X, y, validation_split=VALIDATION_SPLIT, test_split=TEST_SPLIT, batch_size=BATCH_SIZE
    )
    
    # Save class indices
    os.makedirs(os.path.dirname(CLASS_INDICES_PATH), exist_ok=True)
    preprocessor.save_class_indices(CLASS_INDICES_PATH)
    
    # Build and compile model
    print("🏗️ Building model...")
    model.build_model()
    model.compile_model(learning_rate=LEARNING_RATE)
    model.summary()
    
    # Train model
    print(f"🚀 Starting training for {EPOCHS} epochs...")
    history = model.train(train_gen, val_gen, EPOCHS, MODEL_PATH)
    
    # Fine-tune model
    print("🔧 Fine-tuning model...")
    fine_tune_history = model.fine_tune(train_gen, val_gen, 10, MODEL_PATH)
    
    # Plot training history
    print("📈 Plotting training history...")
    plot_training_history(history, 'training_history.png')
    
    # Evaluate model
    print("📊 Evaluating model on test set...")
    results = model.evaluate(test_gen)
    print(f"Test Results: {results}")
    
    # Generate predictions for confusion matrix
    print("🔍 Generating predictions...")
    y_pred_probs = model.model.predict(test_gen)
    y_pred = np.argmax(y_pred_probs, axis=1)
    
    # Classification report
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, 
                               target_names=list(preprocessor.class_names.values())))
    
    # Plot confusion matrix
    plot_confusion_matrix(y_test, y_pred, list(preprocessor.class_names.values()), 
                         'confusion_matrix.png')
    
    print(f"✅ Training completed! Model saved to: {MODEL_PATH}")
    print(f"📁 Class indices saved to: {CLASS_INDICES_PATH}")

if __name__ == "__main__":
    main()
