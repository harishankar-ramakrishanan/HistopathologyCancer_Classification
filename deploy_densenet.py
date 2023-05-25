import streamlit as st
import tensorflow as tf
from PIL import Image

# Load pre-trained model
model = tf.keras.models.load_model('modelpc.h5')

# Define interface for user to upload image
st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader("Choose an image...", type="png")

# Define function to make predictions on uploaded image
@st.cache_data
def predict(image):
   # Load and preprocess image
   img = Image.open(image).resize((224, 224), resample=Image.BILINEAR)
   x = tf.keras.preprocessing.image.img_to_array(img)
   
   x = tf.expand_dims(x, axis=0)

   # Make prediction
   y_pred = model.predict(x)[0]

   # Return predicted class as a string
   class_names = ['Infected', 'Not-infected'] # Replace with your own class names
   return class_names[y_pred.argmax()]

# Run Streamlit app
st.title("POCS Detection")
st.write("")

if uploaded_file is not None:
    st.write("Image uploaded!")
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    if st.button("Classify"):
        predicted_class = predict(uploaded_file)
        st.write("")
        st.write(f"Predicted Class: {predicted_class}")
else:
    st.write("Please upload an image.")
