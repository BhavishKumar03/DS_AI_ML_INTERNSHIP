import os
import cv2
import numpy as np
from simple_app import analyze_leaf_features, demo_predict

def test_prediction_logic():
    """Test the prediction logic with sample images"""
    
    dataset_path = r"d:\DS_AI_Internship\src\Day22\leaf_disease_classified_dataset"
    
    # Test a few diseased images
    diseased_path = os.path.join(dataset_path, 'Diseased')
    healthy_path = os.path.join(dataset_path, 'Healthy')
    
    print("🧪 Testing Prediction Logic")
    print("=" * 50)
    
    # Test diseased leaves
    print("\n🔴 Testing DISEASED leaves:")
    diseased_files = [f for f in os.listdir(diseased_path) if f.endswith('.jpg')][:3]
    
    for filename in diseased_files:
        img_path = os.path.join(diseased_path, filename)
        health_score = analyze_leaf_features(img_path)
        prediction = demo_predict(img_path)
        
        print(f"  {filename}:")
        print(f"    Health Score: {health_score:.3f}")
        print(f"    Predicted: {prediction['class']} ({prediction['confidence']:.1%})")
        print()
    
    # Test healthy leaves
    print("\n🟢 Testing HEALTHY leaves:")
    healthy_files = [f for f in os.listdir(healthy_path) if f.endswith('.jpg')][:3]
    
    for filename in healthy_files:
        img_path = os.path.join(healthy_path, filename)
        health_score = analyze_leaf_features(img_path)
        prediction = demo_predict(img_path)
        
        print(f"  {filename}:")
        print(f"    Health Score: {health_score:.3f}")
        print(f"    Predicted: {prediction['class']} ({prediction['confidence']:.1%})")
        print()
    
    print("✅ Prediction logic test completed!")

if __name__ == "__main__":
    test_prediction_logic()
