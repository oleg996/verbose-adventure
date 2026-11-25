import streamlit as st
import pickle
import numpy as np
from datetime import datetime

start_time = datetime.now()

filename = 'model.h5'

model = pickle.load(open(filename,'rb'))

sex_dict = {0:"Female",1:"Male"}

pclas = {1:"First",2:"Second",3:"Third"}

embarked = {0:"Cherborg",1:"Queenstown",2:'Southampton'}

def main():
    st.set_page_config(page_title="Would you survive the titanic?")
    overview = st.container()

    left,right = st.columns(2)

    prdiction = st.container()

    st.image("https://media1.popsugar-assets.com/files/thumbor/7CwCuGAKxTrQ4wPyOBpKjSsd1JI/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2017/04/19/743/n/41542884/5429b59c8e78fbc4_MCDTITA_FE014_H_1_.JPG")

    with overview:
        st.title("Would you survive the titanic?")

    with left:
        sex_radio = st.radio("Sex",list(sex_dict.keys()),format_func= lambda x : sex_dict[x])
        pclas_radio = st.radio("Clas",list(pclas.keys()),format_func= lambda x : pclas[x])

        embarked_radio = st.radio("Embarked",list(embarked.keys()),index=2
                                  ,format_func= lambda x : embarked[x])


    with right:
        age_slider = st.slider("Age",value=50,min_value=1,max_value=100)
        sibling_slider = st.slider("Partners",min_value=0,max_value=8)
        parch_slider = st.slider("Parents or kids",min_value=1,max_value=8)
        fare_slider = st.slider("Fare",min_value=0,max_value=500,step=10)


    data = [pclas_radio,age_slider,sibling_slider,parch_slider,fare_slider,embarked_radio,sex_radio]

    data = np.array([data,])

    survival = model.predict(data)

    confidance = model.predict_proba(data)

    with prdiction:
        st.header("With this person survive? {0}".format('Yes' if survival else 'No'))
        st.subheader("Confidance:{0:.2f}%".format(confidance[0][survival][0]*100))    
if __name__ == "__main__":
    main()