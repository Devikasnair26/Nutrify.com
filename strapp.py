import streamlit as st
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from openai import AzureOpenAI

# Initialize Azure Form Recognizer client
form_recognizer_endpoint = "https://spjdocumentintelligence.cognitiveservices.azure.com/"
form_recognizer_key = "88c92c39f1794aafb2c84d2d7826f9d6"
form_recognizer_client = DocumentAnalysisClient(endpoint=form_recognizer_endpoint, credential=AzureKeyCredential(form_recognizer_key))

# Initialize OpenAI client
openai_api_key = "7d8a1f9f0ace4c19ac8fb19c82827521"
openai_endpoint = "https://spjopenai9902916927.openai.azure.com/openai/deployments/gpt-4-32k/chat/completions?api-version=2023-07-01-preview"
openai_client = AzureOpenAI(api_key=openai_api_key, api_version="2023-07-01-preview", azure_endpoint=openai_endpoint)

# Function to extract DataFrame from PDF
def extract_dataframe_from_pdf(uploaded_file):
    file_content = uploaded_file.read()  # Read file content
    poller = form_recognizer_client.begin_analyze_document("prebuilt-document", file_content)
    result = poller.result()
    table_data = []
    for table in result.tables:
        table_dict = {}
        for cell in table.cells:
            if cell.row_index not in table_dict:
                table_dict[cell.row_index] = {}
            table_dict[cell.row_index][cell.column_index] = cell.content.strip()
        table_data.append(table_dict)
    dfs = []
    for table in table_data:
        headers = sorted(table[0].keys())
        df = pd.DataFrame.from_dict(table, orient='index', columns=headers)
        dfs.append(df)
    if dfs:
        return df.rename(columns=df.iloc[0]).drop(df.index[0])
    else:
        return None

# Function to extract summary from DataFrame
def extract_summary_from_dataframe(openai_client, df):
    text = df.to_string(index=False, header=True)
    prompt = "You are a medical blood test report analyzer. Extract the test values that are higher or lower than the reference range."
    response = openai_client.chat.completions.create(
        model="gpt-4-medical",
        temperature=0.3,
        top_p=0.95,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        max_tokens=800,
        messages=[
            {"role": "system", "content": "Assistant is a medical blood test report analyzer."},
            {"role": "user", "content": f"{prompt}"},
            {"role": "assistant", "content": f"{text}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Function to suggest nutrient intake
def suggest_nutrient_intake(openai_client, df):
    text = df.to_string(index=False, header=True)
    prompt = "You are a medical blood test report analyzer and nutrition expert. Suggest nutrients based on test values outside the reference range."
    response = openai_client.chat.completions.create(
        model="gpt-4-medical",
        temperature=0.3,
        top_p=0.95,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        max_tokens=800,
        messages=[
            {"role": "system", "content": "Assistant is a medical blood test report analyzer and nutrition expert."},
            {"role": "user", "content": f"{prompt}"},
            {"role": "assistant", "content": f"{text}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Streamlit app
def main():
    st.title("NUTRIFY ME!")

    # Create a multi-page layout using Streamlit
    page = st.sidebar.radio("Navigation", ["Upload PDF", "About App"])

    if page == "Upload PDF":
        st.sidebar.title("Upload PDF")
        uploaded_file = st.sidebar.file_uploader("", type=["pdf"])

        if uploaded_file:
            st.info("File uploaded successfully.")

            # Extract DataFrame from PDF
            df = extract_dataframe_from_pdf(uploaded_file)

            if df is not None:
                st.subheader("Test Results")
                st.dataframe(df)

                st.subheader("Summary")
                summary = extract_summary_from_dataframe(openai_client, df)
                st.write(summary)

                st.subheader("Nutrient Intake Suggestions")
                nutrient_intake = suggest_nutrient_intake(openai_client, df)
                st.markdown(f"**Nutrient Intake Suggestions:**\n{nutrient_intake}")

            else:
                st.warning("No table found in the uploaded PDF.")

    elif page == "About App":
        st.title("About the App")
        st.write("This app analyzes medical blood test reports and provides insights into test results and nutrient intake suggestions.")
        # Add more information about the app if needed.

if __name__ == "__main__":
    main()