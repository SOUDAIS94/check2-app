import streamlit as st
import pickle 

#--------chargement du modèle --------------
with open ('model2.pkl','rb') as f:
    model = pickle.load(f)
#------chargement des instances "LabelEncoder"-----------
with open ('encoder.pkl','rb') as f:
    label_encoder = pickle.load(f)

with open ('encoder2.pkl','rb') as f:
    label_encoder2 = pickle.load(f)

with open ('encoder3.pkl','rb') as f:
    label_encoder3 = pickle.load(f)


st.title("Bank Account")
# -- variable " type_location" ------
type_map={'Rural': 0, 'Urban': 1}
options = list(type_map.keys())
input_user = st.selectbox("Sélectionner le type de location",options)
location_type=type_map[input_user]
#----variable "cellphone_access" ------
cellphone_map = {'No': 0, 'Yes': 1}
options = list(cellphone_map.keys())
input_user = st.radio ("Un accès au téléphone portable ? ( yes/no)", options)
cellphone_access = cellphone_map[input_user]
# ------ variable "household_size" -------------
household_size = st.number_input("saisir la taille du menage")
#----------variable "age_of_respondent" -------
age_of_respondent = st.number_input ("L'âge du correspondant")
# ---variable "gender_of_respondent" ----
gender_map = {'Male': 0, 'Female': 1}
options = list(gender_map.keys())
input_user = st.selectbox("Quel est le genre ?",options)
gender_of_respondent = gender_map[input_user]
# -----variable "marital_status" --------
options = [ 'Married', 'Widowed', 'Single','Divorced']
input_user = st.selectbox("Quel est le statut marital ?",options)
marital_status =1 if input_user =='Married' else 0
# ----variable "education_level" ------
options = label_encoder.classes_
input_user = st.selectbox ("Quel est le niveau d'éducation ?",options)
education_level =label_encoder.transform([input_user])[0]
# ---- variable "job_type" -----------
options = label_encoder2.classes_
input_user = st.selectbox("Quel est le type de travail ?", options)
job_type = label_encoder2.transform([input_user])[0]
# ----variable "relationship_with_head" -----------
options = label_encoder3.classes_
input_user = st.selectbox("Quel est la relation avec la tête ?",options)
relationship_with_head = label_encoder3.transform([input_user])[0]

#---- import du modèle et prédiction --------
entry =[[location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,marital_status,education_level,job_type,relationship_with_head]]
if st.button("Prédire"):
    prediction = model.predict(entry)
    if prediction[0]==1:
     st.success("Parfait ! Vous avez prédit que le prospect aura un compte bancaire")
    else:
     st.success("Ouff ! Vous avez prédit que le prospect n'a pas droit a un compte bancaire")