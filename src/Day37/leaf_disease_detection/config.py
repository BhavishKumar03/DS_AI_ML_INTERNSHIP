import os

# Dataset paths
DATASET_PATH = r"d:\DS_AI_Internship\src\Day22\leaf_disease_classified_dataset"
DISEASED_PATH = os.path.join(DATASET_PATH, "Diseased")
HEALTHY_PATH = os.path.join(DATASET_PATH, "Healthy")

# Model parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 20
LEARNING_RATE = 0.001

# Training parameters
VALIDATION_SPLIT = 0.2
TEST_SPLIT = 0.1

# Model save path
MODEL_PATH = "models/leaf_disease_model.h5"
CLASS_INDICES_PATH = "models/class_indices.json"

# Flask app configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
