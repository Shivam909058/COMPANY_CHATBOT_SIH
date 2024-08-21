import openai
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# apni comapny register kar le bhai
def main():
    st.title("Employee Query Chatbot")

    if "company_data" not in st.session_state:
        st.session_state.company_data = {}

    if not st.session_state.company_data:
        st.write("No company registered yet.")
        st.write("Please register your company to use the chatbot.")

        with st.form("register_company"):
            company_name = st.text_input("Company Name")
            hr_policies = st.text_area("HR Policies")
            it_support = st.text_area("IT Support")
            company_events = st.text_area("Company Events")
            submitted = st.form_submit_button("Register")

            if submitted:
                st.session_state.company_data = {
                    "name": company_name,
                    "hr_policies": hr_policies,
                    "it_support": it_support,
                    "company_events": company_events,
                }
                st.success(f"Company {company_name} registered successfully!")

    else:
        company_name = st.session_state.company_data["name"]
        st.write(f"Company: {company_name} is registered.")
        user_query = st.text_input("What would you like to know?")

        if st.button("Submit"):
            documents = [
                st.session_state.company_data["hr_policies"],
                st.session_state.company_data["it_support"],
                st.session_state.company_data["company_events"]
            ]
            metadata = [
                {"company": company_name, "section": "HR Policies"},
                {"company": company_name, "section": "IT Support"},
                {"company": company_name, "section": "Company Events"}
            ]

            
            embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
            vector_store = Chroma.from_texts(documents, embeddings, metadatas=metadata)
            llm = OpenAI(temperature=0.7)
            qa_chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=vector_store.as_retriever())
            response = qa_chain.invoke({"query": user_query})
            st.write(response["output"])

if __name__ == "__main__":
    main()
