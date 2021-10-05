import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.elements.arrow import Data

# Read data
data = pd.read_csv("train.csv")
# Display text
st.title("TRUNG TÂM TIN HỌC")
st.header("Chào bạn Trí đến với data science")

menu = ["Display Text", "Display Data", "Display Chart", "Display Interactive Widget"]
choice = st. sidebar.selectbox ('Menu', menu)


if choice == "Display Text":
    st.subheader("How to run streamlit app")
    st.text("Khóa học được thiết kế bởi nhằm ôn tập và bổ sung kiến thức cho HV Data Science")
    st.markdown("### Có 5 chủ đề")
    st.write("""
        - Chủ để 1
        - Chủ đề 2
        - ...
    """)
    st.write("### Ngôn ngữ lập trình python")
    st.code("st.display_text_function ('Nội dung')", language="python")
elif choice == "Display Data":
    # Display data
    st.write("### Display data")
    st.dataframe(data.head(5))
    #st.table(data.head(3))
    #st.json(data.head(2).to_json())
elif choice == "Display Chart":
    # Visuazation display
    st.write("## Display Chart")
    count_Pclass = data[['PassengerId', 'Pclass']].groupby(['Pclass']).count()
    st.bar_chart(count_Pclass)

    fig, ax = plt.subplots()
    ax = sns.boxplot(x = 'Pclass', y='Fare', data = data)

    st.pyplot(fig)

else:
    st.write("## Display Interactive Widget") 
    st.write("### Input your information") 
    name = st.text_input("Name:") 
    sex = st.radio("Sex", options=['Male', 'Female']) 
    age = st.slider("Age", 1, 100, 1) 
    jobtime = st. selectbox("You have", options=['Part time job', 'Full time job']) 
    hobbies = st. multiselect("Hobbies", options=["Cooking", "Reading", "Writing", "Travel", "Others"]) 
    house = st.checkbox ("Have house/ apartment") 
    submit = st.button("Submit") 
    if submit:
        st.write("#### Your Information:") 
        st.write("Name:", name, 
        "- Sex:", sex, 
        "- Age:", age, 
        " - You have a", jobtime, 
        "and a house/apartment" if house else "", 
        "- Hobbies:", ', '.join(map(str, hobbies)))






