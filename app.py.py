import os
import shutil
import random

# Define paths
dataset_path = r"C:\Users\parma\Downloads\Image Dataset of Indian Coins\Image Dataset of Indian Coins\Indian Coins Image Dataset\Indian Coins Image Dataset"
train_path = r"C:\Users\parma\Downloads\Image Dataset of Indian Coins\train"
val_path = r"C:\Users\parma\Downloads\Image Dataset of Indian Coins\val"
test_path = r"C:\Users\parma\Downloads\Image Dataset of Indian Coins\test"

# Create directories
for folder in ['train', 'val', 'test']:
    os.makedirs(os.path.join(train_path), exist_ok=True)
    os.makedirs(os.path.join(val_path), exist_ok=True)
    os.makedirs(os.path.join(test_path), exist_ok=True)

# Split dataset
for class_folder in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_folder)
    if os.path.isdir(class_path):
        images = os.listdir(class_path)
        random.shuffle(images)

        # Calculate splits
        train_count = int(len(images) * 0.7)
        val_count = int(len(images) * 0.15)

        # Create class directories
        os.makedirs(os.path.join(train_path, class_folder), exist_ok=True)
        os.makedirs(os.path.join(val_path, class_folder), exist_ok=True)
        os.makedirs(os.path.join(test_path, class_folder), exist_ok=True)

        for i, image in enumerate(images):
            src = os.path.join(class_path, image)
            if i < train_count:
                dst = os.path.join(train_path, class_folder, image)
            elif i < train_count + val_count:
                dst = os.path.join(val_path, class_folder, image)
            else:
                dst = os.path.join(test_path, class_folder, image)
            shutil.copy(src, dst)

print("Data split into train, validation, and test sets.")
