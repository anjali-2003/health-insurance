import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
  
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(Age,Diabetes,BP,Transplants,ChronicDiseases,Height,Weight,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries):  
   
    prediction = classifier.predict(
        [[Age,Diabetes,BP,Transplants,ChronicDiseases,Height,Weight,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("PYAR Insurance Company")
    
    with st.sidebar:
        selected = option_menu(
            menu_title = "menu",
            options=["home","predict","contact"],
        )
    html_temp = """
    <div style ="background-color:gray;padding:13px">
    <h1 style ="color:black;text-align:center;">Insurance Prediction </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    if selected == "home":
        st.subheader("heyyyyyyyy!!!!!!!")
        st.markdown("Mission: To be the most preferred choice of customers for General Insurance by building Relationships and grow profitably.")
        st.title("Vision :")
        st.markdown("Leveraging technology to integrate people and processes.")
        st.markdown("To excel in service and performance.")
        st.markdown("To uphold the highest ethical standards in conducting our business.")
        def load_lottiefile(filepath: str):
            with open (filepath, "r") as f:
                return json.load(f)
        hello_lt = load_lottiefile(r'C:\Users\ANIRUDDHA\OneDrive\Desktop\anju\insurance\hello.json')
        st_lottie(
            hello_lt,
            height=100,
            width=100
        )
    
    if selected == "predict":
# =============================================================================
#         Age = st.text_input("Age")
# =============================================================================
# =============================================================================
#         Age = st.slider('How old are you?', 1, 100, 1)
# =============================================================================
        st.subheader("enter your age")        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            Age = st.number_input("age",min_value=1,max_value=100)
        with col2:
            st.header("")
        with col3:
            st.header("")
        with col4:
            st.header("")
        col1, col2 = st.columns(2)
        with col1:
            Height = st.slider('Height(cm)', 10, 200, 1)
        with col2: 
            Weight = st.slider('weight(kg)', 10, 150, 1)
        st.subheader("Give your current health status")
        a = st.checkbox('Diabetes')
        if a:
            Diabetes = 1.0
        else:
            Diabetes = 0.0
        a = st.checkbox('BP')
        if a:
            BP = 1.0
        else:
            BP = 0.0
        a = st.checkbox('Transplants')
        if a:
            Transplants = 1.0
        else:
            Transplants = 0.0
        a = st.checkbox('ChronicDiseases')
        if a:
            ChronicDiseases = 1.0
        else:
            ChronicDiseases = 0.0
        a = st.checkbox('KnownAllergies')
        if a:
            KnownAllergies = 1.0
        else:
            KnownAllergies = 0.0
        a = st.checkbox('HistoryOfCancerInFamily')
        if a:
            HistoryOfCancerInFamily = 1.0
        else:
            HistoryOfCancerInFamily = 0.0
        NumberOfMajorSurgeries = st.number_input("NumberOfMajorSurgeries",min_value=0,max_value=10)
 
        result =""
      
        if st.button("Predict"):
            result = prediction(float(Age), float(Diabetes), float(BP), float(Transplants), float(ChronicDiseases), float(Height), float(Weight), float(KnownAllergies), float(HistoryOfCancerInFamily), float(NumberOfMajorSurgeries))
            st.success('The output is {}'.format(result))
    if selected == "contact": 
        st.header("reach us at: 123@b.com")
     
if __name__=='__main__':
    main()
