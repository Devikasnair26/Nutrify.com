What is happening :-
Project Overview:
Our capstone project, Nutrify, is a comprehensive web application designed to analyze blood reports and provide personalized nutritional recommendations to address any abnormalities detected. 

Phase 1: Document Analysis and Data Extraction
- Leveraging Azure Document Intelligence, Nutrify seamlessly analyzes various types of documents, including reports, invoices, and essays.
- This process is facilitated through a resource group connection to OpenAI, specifically utilizing its Large Language Model (LLM) capabilities.
- Our system incorporates functions to extract pertinent data from PDF documents and transform it into structured dataframes. Additionally, another function extracts a succinct summary from these dataframes, highlighting abnormal increases or decreases in various parameters.

Phase 2: Nutrient Recommendation Engine
- Building upon the data extracted in Phase 1, Nutrify features a robust nutrient recommendation engine powered by OpenAI.
- Through innovative prompt engineering techniques, we convert the dataframe into text format, enabling seamless analysis by the LLM.
- The recommendation engine utilizes data from the National Institute of Health (NIH) in the United States to suggest optimal nutrient intake based on individual requirements.

Frontend Implementation with Streamlit
- To provide users with a user-friendly interface, we've integrated our project backbone into the Streamlit framework. (subject to change as per sponsors demands)
- Users can easily upload their blood reports, and Nutrify will promptly analyze the data and deliver personalized nutritional insights.

Future Plans:
1. Translation Services Integration: We aim to enhance accessibility by implementing translation services, ensuring Nutrify is accessible to users worldwide.
2. Image Recognition: In an effort to further streamline user experience, we plan to integrate image recognition capabilities. Users will be able to simply upload images of their food items, and Nutrify will provide tailored dietary recommendations. If image recognition proves challenging, we'll pivot to providing text-based recommendations.
   
