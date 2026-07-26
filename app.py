import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import os


# Load model
model = tf.keras.models.load_model("hand_written_Digit_recog_model.keras")


st.title("✍️ Handwritten Digit Recognition")


# Function for preprocessing
def preprocess_image(image):

    image = image.convert("L")
    image = image.resize((28, 28))

    img_array = np.array(image)

    # MNIST format
    img_array = 255 - img_array

    img_array = img_array / 255.0

    img_array = img_array.reshape(1, 28, 28, 1)

    return img_array



option = st.radio(
    "Choose input method:",
    ["Type Image Name", "Upload Image"]
)


image = None


# Type image name
if option == "Type Image Name":

    file_name = st.text_input(
        "Enter image name (example: 6.png)"
    )

    if file_name:
        if os.path.exists(file_name):
            image = Image.open(file_name)
        else:
            st.error("Image not found in project folder")


# Upload image
else:

    uploaded_file = st.file_uploader(
        "Upload digit image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)



# Prediction
if image is not None:

    st.image(image, caption="Input Image", width=200)

    processed_image = preprocess_image(image)

    if st.button("Predict"):

        prediction = model.predict(processed_image)

        digit = np.argmax(prediction)

        confidence = np.max(prediction) * 100


        st.success(f"Predicted Digit: {digit}")

        st.info(f"Confidence: {confidence:.2f}%")