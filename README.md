# ✍️ Handwritten Digit Recognition using CNN

## 📌 Project Overview

Handwritten Digit Recognition is a Computer Vision project that uses a Convolutional Neural Network (CNN) to classify handwritten digits from input images.

The project uses a trained CNN model built with TensorFlow/Keras and provides an interactive web application using Streamlit. Users can provide handwritten digit images through different input methods, and the application predicts the digit along with the confidence score.

---

## 🚀 Features

- Recognizes handwritten digits from 0 to 9
- CNN-based image classification
- Interactive Streamlit web application
- Supports image upload for prediction
- Supports providing image names from the project folder
- Image preprocessing before prediction
- Displays predicted digit with confidence score

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- OpenCV
- Pillow (PIL)

---

## 🧠 Model Details

- Model Type: Convolutional Neural Network (CNN)
- Framework: TensorFlow/Keras
- Input Image Size: 28 × 28 pixels
- Output Classes: 10 (Digits 0-9)

The CNN model learns patterns from handwritten digit images and predicts the correct digit class from the given input image.

---

## ⚙️ How It Works

1. User selects an input method:
   
   - Enter image name from the project folder (example: `6.png`)
     
   - Upload a handwritten digit image

2. The input image is converted into grayscale.

3. The image is resized to 28×28 pixels.

4. Pixel values are normalized for model input.

5. The processed image is passed to the trained CNN model.

6. The CNN model predicts the handwritten digit.

7. The application displays:
   - Predicted digit
   - Prediction confidence score

---

## 📂 Project Structure

handwritten_digit_recognition/

│
├── app.py
├── hand_written_Digit_recog_model.keras
├── 0.png
├── 1.png
├── 2.png
├── 3.png
├── 4.png
├── 5.png
├── 6.png
├── 7.png
├── 8.png
└── 9.png

---


## ▶️ How to Run the Project

 1. Clone the repository

git clone https://github.com/Anshika31Kumari/handwritten_digit_recognition.git

2. Navigate to project directory
 
   cd handwritten_digit_recognition

3. Install required libraries
   
   pip install -r requirements.txt

4. Run the Streamlit application
   
   python -m streamlit run app.py

The Streamlit application will start running, and it will open automatically in your default web browser.

---

📸 Application Output

The application provides:

Input image preview

Predicted handwritten digit

Confidence percentage

---

🔮 Future Improvements

Add real-time digit drawing canvas

Improve model performance using data augmentation

Deploy the application on cloud platforms

Add model evaluation metrics

Add prediction history feature

👩‍💻 Author
Anshika Kumari

GitHub:
https://github.com/Anshika31Kumari
