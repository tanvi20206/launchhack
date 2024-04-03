from binascii import a2b_base64
import streamlit as st 
import tensorflow as tf 
import os


import numpy as np

def model_pred(test_image):
    model_path="traintmodel_model.h5"
    model = tf.keras.models.load_model(model_path)
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input=tf.keras.preprocessing.image.img_to_array(image)
    
    input = np.array([input]) 
    #img_array = np.expand_dims(input, axis=0)
    # Scale the image values to [0, 1]
    #img_array = img_array.astype('float32') / 255.
    #return img_array 
    prediction=model.predict(input)
    result_index=np.argmax(prediction)
    return result_index





st.set_page_config(page_title="Plant Disease Detection System", page_icon=":herb:",layout="wide",initial_sidebar_state="expanded")
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select What YOU Want See ?",[" 🏠Home","📚About","🤖Prediction","☎️contact"])


st.markdown(
    """
    <style>
    body {
        background-color: #90EE90; 
    }
    </style>
    """,
    unsafe_allow_html=True
)
if (app_mode == " 🏠Home"):   
    # Add title with custom color, font, and shadow effect
    st.markdown("<h1 style='text-align: center; color: #196F3D; font-family: Arial, sans-serif; text-shadow: 2px 2px 4px #A9DFBF;'>Welcome to 🌿GREEN HEALTH MONITOR </h1>", unsafe_allow_html=True)
    st.write("<h3 style='text-align: center; color: black; font-family:  sans-serif; text-shadow: 1px 1px 2px #A9DFBF;'>A Plant Disease Detection System </h3>", unsafe_allow_html=True)

    
    st.image("plant.jpg", use_column_width=True, output_format='JPEG', channels='RGB', clamp=True)

   
    # Add description with custom font size, color, and shadow effect
    st.write("  This web application is designed to efficiently detect diseases in plants, helping to protect crops and ensure a healthier harvest.")
    st.write(
        """
    ### How it works 👁️ 
    To use the system, simply follow these steps:

    1. Select a picture of a plant's leaf that you want to analyze.
    2. Upload the selected image to the application.
    3. Our system will then analyze the image to identify any diseases present in the plant.

    By leveraging advanced technology, we aim to provide accurate and timely detection of plant diseases, enabling farmers and growers to take proactive measures to protect their crops and optimize yields.
    
    ### Get Started Now !🌱

    Click on the Prediction 🤖 page in the sidebar to upload an image and experience the power of our 🌿GREEN HEALTH MONITOR !

     
  """   )
  #  st.markdown("<p style='font-size: 18px; color: #145A32; text-shadow: 1px 1px 2px #A9DFBF;'>Upload an image of a plant leaf, and our system will identify any diseases present.</p>", unsafe_allow_html=True)

elif(app_mode=="📚About"):
    st.markdown("<h1 style='text-align: center; color: light green; font-family: Arial, sans-serif; text-shadow: 1px 1px 2px #A9DFBF;'> About Our Green Health Monitor ☘️</h1>", unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown ( "<p style= 'text-align: center;'font-size: 20px; color:  green; text-shadow: 1px 1px 2px  green;'>🌱 Welcome to the About page of our website! </p>",unsafe_allow_html=True)
    st.markdown ( "<p style= 'text-align: center;'font-size: 20px; color: green; text-shadow: 1px 1px 2px  green;'>Here, you'll find information about our project, its goals, and the team behind its development. </p>", unsafe_allow_html=True)
    

     
    st.write(
    """
    
    ### Our Mission
    Our mission is to revolutionize agriculture by providing farmers and gardeners with a powerful
    tool to detect and manage plant diseases effectively. By leveraging the latest advancements in
    machine learning and computer vision, we aim to empower users to make informed decisions about crop health and maximize yields.

    ### Project Goals

    🍂 Accuracy: We strive for high accuracy in disease detection to ensure reliable results for our users.

    🍂 User-Friendly Interface: We prioritize user experience, aiming to create an intuitive and easy-to-use platform for farmers and gardeners of all skill levels.

    🍂 Accessibility: Our system is designed to be accessible to users worldwide, with support for multiple languages and device compatibility.
""")     
   
elif(app_mode=="🤖Prediction"):
  
    st.markdown(
        """
        <style>
        /* Add background color and padding */
        .prediction-section {
            background-color: #c1e1c5;
            padding: 20px;
            border-radius: 10px;
        }
        /* Style for the header */
        .prediction-header {
            color: #196F3D;
            font-size: 30px;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Style for the prediction result */
        .prediction-result {
            color: #145A32;
            font-size: 18px;
            margin-top: 20px;
        }
        /* Style for the success message */
        .success-message {
            color: #1F618D;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="prediction-section">', unsafe_allow_html=True)
    st.markdown('<div class="prediction-header"> <h1> Disease Prediction 🤖</h1></div>', unsafe_allow_html=True)
    
    test_image = st.file_uploader("Choose an image")
    if(st.button("Show Image")):
        st.image(test_image, use_column_width=True)
    
    if(st.button("Predict")):
        with st.spinner("Please Wait ..."):
            st.write("Our Prediction ")
            result_index = model_pred(test_image)
            class_name = ['Apple___Apple_scab', 
                      'Apple___Black_rot', 
                      'Apple___Cedar_apple_rust', 
                      'Apple___healthy', 
                      'Blueberry___healthy',
                      'Cherry_(including_sour)___Powdery_mildew',
                      'Cherry_(including_sour)___healthy', 
                      'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                      'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 
                   'Corn_(maize)___healthy', 'Grape___Black_rot',
                       'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
        st.markdown('<div class="prediction-result">Model is predicting it is a {} </div>'.format(class_name[result_index]), unsafe_allow_html=True)
  
    st.markdown('</div>', unsafe_allow_html=True)  # Closing the prediction-section div

    
elif(app_mode=="☎️contact"):
    st.markdown(
    """
    <style>
    
    /* Style for the heading */
    .contact-header {
        color: #627254 ;
        font-size: 40px;
        text-align: center;
        margin-bottom: 20px;
        
    }
    /* Style for the contact information */
    .contact-info {
        font-size: 16px;
        margin-bottom: 10px;
        
    }
    /* Style for the suggestion box */
    .suggestion-box {
        margin-top: 20px;
    }
    /* Style for the submit button */
    .submit-button {
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contact Us section
    st.markdown('<div class="contact-section">', unsafe_allow_html=True)
    st.markdown('<div class="contact-header"><h1> CONTACT ☎️ </h1></div>', unsafe_allow_html=True)

# Contact information
    st.markdown('<div class="contact-info">If you have any questions, suggestions, or feedback, please feel free to contact us or otherwise write the suggestion in suggestion box👇.</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-info">📩Email: tanvigupta@gmail.com & merceng@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-info">📞Phone: +8810564058</div>', unsafe_allow_html=True)

    suggestion = st.text_area("Enter your suggestion here:", "")

# Submit button
    if st.button("Submit"):
      st.success("Thank you for your suggestion!")
st.markdown('</div>', unsafe_allow_html=True)  # Closing the contact-section div



    
        
         
   
    


