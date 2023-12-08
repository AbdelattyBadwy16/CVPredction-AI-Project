import streamlit as st
import pickle
import re

Cvect = pickle.load(open('CVect.pkl','rb'))
clf = pickle.load(open('clf.pkl','rb'))
clf1 = pickle.load(open('clf1.pkl','rb'))


def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text


category_mapping = {
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate",
}


def main():
    st.title("Cv Prediction")

    html_temp = """
    <div style="background-color:black ;padding:10px">
    <h2 style="color:white;text-align:center;">Cv prediction ML App </h2>
    </div>
    """
    Acc_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Your Cv will be delivered to the Recuriter </h2>
    </div>
    """

    Rej_temp = """
    <div style="background-color:red ;padding:10px">
    <h2 style="color:white;text-align:center;">Sorry , Your Cv won`t be delivered to the Recuriter </h2>
    </div>
    """
    
 
    st.markdown(html_temp, unsafe_allow_html=True)

    resume = st.text_input("resume","Type Here")
    if resume == "Type Here" :
        return
    
    cleaned_resume = clean_resume(resume)
    input = Cvect.transform([cleaned_resume])
    prediction = clf.predict(input)[0]
    
    if prediction == 'Accept':
        st.markdown(Acc_temp, unsafe_allow_html=True)
    else :
        st.markdown(Rej_temp, unsafe_allow_html=True)

    prediction = clf1.predict(input)[0]
    category_name = category_mapping.get(prediction, "Unknown")
    st.markdown(category_name, unsafe_allow_html=True)

if __name__=='__main__':
    main()