import os
import numpy as np
import pandas as pd
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Define paths
train_dir = 'dataset/train'
test_dir = 'dataset/test'

# Image dimensions
IMG_HEIGHT = 224
IMG_WIDTH = 224

# Load images and labels
def load_data(data_dir):
    images = []
    labels = []
    for label in os.listdir(data_dir):
        for file in os.listdir(os.path.join(data_dir, label)):
            img_path = os.path.join(data_dir, label, file)
            image = cv2.imread(img_path)
            image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
            images.append(image)
            labels.append(label)
    return np.array(images), np.array(labels)

# Load training and testing data
train_images, train_labels = load_data(train_dir)
test_images, test_labels = load_data(test_dir)

# Map labels to integers
label_map = {'no_oa': 0, 'mild_oa': 1, 'severe_oa': 2}
train_labels = np.array([label_map[label] for label in train_labels])
test_labels = np.array([label_map[label] for label in test_labels])

# Normalize images
train_images = train_images / 255.0
test_images = test_images / 255.0

# Convert labels to one-hot encoding
train_labels = to_categorical(train_labels, num_classes=3)
test_labels = to_categorical(test_labels, num_classes=3)
