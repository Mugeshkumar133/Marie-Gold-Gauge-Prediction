import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
import streamlit as st
from streamlit_option_menu import option_menu
import re
import plotly.express as px
import PIL 
from PIL import Image
st.set_page_config(page_title ="Marie Gold Gauge Prediction",layout="wide")

st.write("""

<div style='text-align:center'>
    <h1 style='color:#009999;'>Marie Gold regression Modeling Application</h1>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
     opt = option_menu("Marie Gold Gauge Prediction",
                      ["Home","Algorithms","Prediction","Contact"],
                      menu_icon="cast",
                      styles={
                          "container":{"padding":"4!important","background-color":"gray"},
                          "icon":{"color":"red","font-size":"20px"},
                          "nav-link":{"font-size":"20px","text-align":"left"},
                          #"nav-link-selected":{"background-color":"yellow"}
                      })

if opt == "Home":
    col1,col2, = st.columns(2)
    col1.image(Image.open("C:/Users/muges/Downloads/Britannia_images_Hero_600x400.jpg"),width = 300)
    with col1:
        st.subheader("Established in Kolkata in 1892, Britannia is a household name in India, and one of the country’s leading food products companies. Our key businesses are in bakery, dairy, and adjacent snacking categories and our operations span over 80 countries in the world.")

    with col2:
        st.image(Image.open("C:/Users/muges/Downloads/download.jpg"),width = 300)



if opt == "Algorithms":
    st.markdown("# :blue[Predicting Results based on Trained Models]")
    st.markdown("# :blue[Here we tried with three algorithms namely Linear Regression using Stats Model, Linear Regression Using Sklearn and Decision Tree Regressor]")
    st.markdown("# :blue[Out of these Linear Regression Using Stats Model showed a R2_Valued which is nothing but the Co-efficient of determination (i.e) The variation in the dependent variable can be explained by the independent variable is 90.5%  percentage from StatsModel ]")
    st.markdown("# :blue[Hence Linear Regression using StatsModel is chosen for Model Building and proceeded with feature selection]")
    

    

if opt == "Prediction":
 with st.form("my_form"):


    st.markdown(
        """
        <style>
            .st-ax{
                background-color: lightblue;
            }

            .stTextInput input{
                background-color: lightblue;
            }
            .stNumberInput input{
                background-color: lightblue;
            }

            .stDateInput Input{
                background-color: lightblue;
            }

        </style>
        """
    ,unsafe_allow_html=True
    )

    st.write( f'<h5 style="color:rgb(0, 153, 153,0.4);">NOTE: Min & Max given for reference, you can enter any value</h5>', unsafe_allow_html=True )
    Sheeter_int_conveyor = st.number_input('Sheeter_int_conveyor', min_value=948.0, max_value=1288.0)
    Gauge_roller_3_top = st.number_input('Gauge_roller_3_top',min_value= 642.0, max_value=903.0)
    Dough_consistency = st.number_input('Dough_consistency', min_value=157.0, max_value=214.0)
    Zone_6_bottom = st.number_input('Zone_6_bottom',min_value= 294.0, max_value=302.9)
    Process_dust = st.number_input('Process_dust', min_value=60, max_value= 100)
    Wet_weight_working = st.number_input('Wet_weight_working',min_value=62.5, max_value= 67.5)
    Zone_2_bottom = st.number_input('Zone_2_bottom', min_value=254.7, max_value=289.4)
    Int_conveyor_1 = st.number_input('Int_conveyor_1',min_value=183.0, max_value=217.0)
    Scrap_sheeter = st.number_input('Scrap_sheeter',min_value=226.0, max_value=322.0)
    Wet_weight_non_working = st.number_input('Wet_weight_non_working',min_value=62.5, max_value=67.5)
    Pre_int_conveyor_1 = st.number_input('Pre_int_conveyor_1',min_value=264.0, max_value=357.0)
    Wet_weight_middle = st.number_input('Wet_weight_middle',min_value= 62.5, max_value=67.5)
    Cutting_web = st.number_input('Cutting_web',min_value= 620.0, max_value=710.0)
    submit_button = st.form_submit_button(label="PREDICT Gauge of Marie Gold")
    st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #009999;
                        color: white;
                        width: 100%;
                    }
                    </style>
                """, unsafe_allow_html=True)
    if submit_button is not None:
                  predicted_gauge = 130.6740 + (Sheeter_int_conveyor * 	0.0149 ) + (Gauge_roller_3_top * -0.0212 ) + (Dough_consistency * 0.1206 ) + (Zone_6_bottom * -0.5271  ) + (Process_dust * -0.0071 ) + (Wet_weight_working * 	1.1400  ) + (	0.0613 * Zone_2_bottom) + (Int_conveyor_1 * -0.0962 ) + (Scrap_sheeter * -0.0142 ) + (Wet_weight_non_working * -0.5254 ) + (Pre_int_conveyor_1 * -0.0163 ) + (Wet_weight_middle * 0.3364 ) + ( Cutting_web * 	0.0082 )
                  st.write('## :green[Predicted gauge:] ', predicted_gauge)
    # flag=0
    # pattern = "^(?:\d+|\d*\.\d+)$"
    # for i in ["transactionRevenue","num_interactions","count_hit","historic_session_page","time_on_site","avg_session_time","avg_session_time_page","historic_session","visits_per_day"]:
    #     if re.match(pattern, i):
    #         pass
    #     else:
    #         flag=1
    #         break
        # if submit_button :
        #     if len(i)==0:
        #       st.write("please enter a valid number and space  is not allowed")
        #     else:
        # #       st.write("You have entered an invalid value: ",i)

        # if submit_button :
        #     import pickle
        #     with open(r"C:/Users/muges/Downloads/cmodel.pkl", 'rb') as file:
        #         loaded_model = pickle.load(file)
        #     with open(r"C:/Users/muges/Downloads/cscaler.pkl", 'rb') as f:
        #         scaler_loaded = pickle.load(f)

        #     with open(r"C:/Users/muges/Downloads/ct.pkl", 'rb') as f:
        #         t_loaded = pickle.load(f)

        # # Predict the has_converted for a new sample
        # # transactionRevenue,num_interactions,count_hit,historic_session_page,time_on_site,avg_session_time,avg_session_time_page,historic_session,visits_per_day
        #     new_sample = np.array([[float(transactionRevenue),float(num_interactions),float(count_hit),float(historic_session_page),float(time_on_site),float(avg_session_time),float(avg_session_time_page),float(historic_session),float(visits_per_day)]])
        #     # new_sample_ohe = t_loaded.transform(new_sample[:, [9]]).toarray()
        #     new_sample = np.array((new_sample[:, [0,1,2, 3, 4, 5, 6,7,8]]))
        #     new_sample = scaler_loaded.transform(new_sample)
        #     new_pred = loaded_model.predict(new_sample)
        #     if new_pred== 1:
        #          st.write('## :green[The Status is Converted] ')
        #          break
        #     else:
        #          st.write('## :red[The Status is Not Converted] ')
        #          break
if opt == "Contact":
    Name = (f'{"Name :"}  {"BRITANNIA INDUSTRIES LIMITED"}')
    mail = (f'{"Mail :"}  {"feedback@britindia.com"}')
    description = "If there were a soundtrack for life, whenever something cool happens, the background would go TING! Life at Britannia is about chasing the TINGs. Our vision is to be a Responsible Total Foods Company, serving products that brim with exciting goodness, through the day. We do that by working together as a creative, energetic and passionate team.!"
    social_media = {
        "YOUTUBE": "https://www.youtube.com/channel/UC1Qp6V_rPNEqTsD9oc-5szQ",
        "LINKEDIN": "https://www.linkedin.com/company/britannia-industries-limited/",
        "INSTAGRAM":"https://www.instagram.com/britanniasnackinc/",
        "FACEBOOK":"https://www.facebook.com/BritanniaIndustriesLimited/",
        "TWITTER":"https://twitter.com/britanniaindltd"}
    
    col1, col2, col3 = st.columns(3)
    col3.image(Image.open("C:/Users/muges/Downloads/Britannia_images_Hero_600x400.jpg"), width=300)
    st.subheader(Name)
    st.subheader(mail)
    with col1:
        st.title('MARIE GOLD DATA VISUALIZATION')
        st.write("The goal of this project is to create a visualized dashboard showcasing the correlation between various parameters which helps in determing the required output (gauge in Working,center,Non-Working side) for better efficient run of products with quality compliance.")
        st.write("---")
        
        
    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")

uploaded_file=st.sidebar.file_uploader(label="Upload your csv or excel file.max(200mb)",type=["csv","xlsx"])

if uploaded_file is not None:
    print(uploaded_file)
    
    try:
       df=pd.read_csv(uploaded_file)
    except Exception as e:
       print(e)
       df=pd.read_excel(uploaded_file)
try:
    st.write(df)
    numeric_columns= list(df.select_dtypes(["float","int"]).columns)
    categorical_column=list(df.select_dtypes("object").columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")
#add a select widget tot the  sidebar
chart_select=st.sidebar.selectbox(label="select the chart type",
                                  options=["Scatterplots","Barcharts","Boxplot","Histogram","Heatmap"])

if chart_select=="Scatterplots":
    st.sidebar.subheader("Scatterplot settings")
    try:
        x_values= st.sidebar.selectbox("X axis",options=numeric_columns)
        y_values= st.sidebar.selectbox("Y axis",options=numeric_columns)
        plot=px.scatter(data_frame=df,x=x_values,y=y_values)
        #display the chart 
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select=="Barcharts":
    st.sidebar.subheader("Barcharts settings")
    try:
        x_values= st.sidebar.selectbox("X axis",categorical_column)
        y_values= st.sidebar.selectbox("Y axis",options=numeric_columns)
        plot=px.bar(data_frame=df,x=x_values,y=y_values)
        #display the chart 
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select=="Boxplot":
    st.sidebar.subheader("Boxplot settings")
    try:
        x_values= st.sidebar.selectbox("X axis",categorical_column)
        y_values= st.sidebar.selectbox("Y axis",options=numeric_columns)
        plot=px.box(data_frame=df,x=x_values,y=y_values)
        #display the chart 
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select=="Histogram":
    st.sidebar.subheader("Barcharts settings")
    try:
        # x_values= st.sidebar.selectbox("X axis",categorical_column)
        y_values= st.sidebar.selectbox("Y axis",options=numeric_columns)
        plot=px.histogram(data_frame=df,x=y_values,nbins=20)
        #display the chart 
        st.plotly_chart(plot)
    except Exception as e:
        print(e)



if chart_select=="Heatmap":
    st.sidebar.subheader("Heatmap Visualization")
    try:
        plot = px.imshow(df.corr(), labels=dict(color="Productivity"), text_auto=True,aspect="auto")
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


st.write( f'<h6 style="color:rgb(0, 153, 153,0.35);">App Created by Britannia Industries Limited,Perundurai (Sipcot) </h6>', unsafe_allow_html=True )