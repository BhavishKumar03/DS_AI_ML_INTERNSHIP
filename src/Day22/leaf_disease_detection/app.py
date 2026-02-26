import os
import json
import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import cv2
from config import *
from model import LeafDiseaseModel
from data_preprocessing import DataPreprocessor

app = Flask(__name__)
CORS(app)

# Configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('models', exist_ok=True)

# Initialize model and preprocessor
model = LeafDiseaseModel()
preprocessor = DataPreprocessor()

# Load trained model and class indices
try:
    model.load_model(MODEL_PATH)
    preprocessor.load_class_indices(CLASS_INDICES_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    print("Please train the model first by running: python train_model.py")

def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    """Preprocess uploaded image"""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read image")
    
    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Resize
    img = cv2.resize(img, IMG_SIZE)
    
    # Normalize
    img = img.astype(np.float32) / 255.0
    
    return img

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "model_loaded": model.model is not None})

@app.route('/predict', methods=['POST'])
def predict():
    """Predict leaf disease from uploaded image"""
    try:
        # Check if model is loaded
        if model.model is None:
            return jsonify({"error": "Model not loaded. Please train the model first."}), 500
        
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": f"File type not allowed. Allowed types: {ALLOWED_EXTENSIONS}"}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Preprocess image
        img = preprocess_image(filepath)
        
        # Make prediction
        result = model.predict_class(img, preprocessor.class_names)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify({
            "success": True,
            "prediction": result,
            "message": f"The leaf appears to be {result['class'].lower()} with {result['confidence']:.2%} confidence."
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    """Predict multiple images"""
    try:
        if model.model is None:
            return jsonify({"error": "Model not loaded. Please train the model first."}), 500
        
        if 'files' not in request.files:
            return jsonify({"error": "No files uploaded"}), 400
        
        files = request.files.getlist('files')
        results = []
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                try:
                    img = preprocess_image(filepath)
                    result = model.predict_class(img, preprocessor.class_names)
                    results.append({
                        "filename": filename,
                        "prediction": result
                    })
                except Exception as e:
                    results.append({
                        "filename": filename,
                        "error": str(e)
                    })
                finally:
                    os.remove(filepath)
        
        return jsonify({
            "success": True,
            "results": results,
            "total_processed": len(results)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/model_info')
def model_info():
    """Get model information"""
    try:
        if model.model is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        return jsonify({
            "input_shape": model.input_shape,
            "num_classes": model.num_classes,
            "class_names": preprocessor.class_names,
            "model_path": MODEL_PATH
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🌿 Leaf Disease Detection API Server 🌿")
    print("🚀 Starting server on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
