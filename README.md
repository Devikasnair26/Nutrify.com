What is happening in capstone in a professional way:-
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
   
##What is happening in capstone for understanding purpose:-
we built a website called nutrify for our capstone project. the app analyzes blood reports, tells what is abnormal increased or decresed. analyses what nutrients need to be intake to fix this. the first two phases are done. 
phase 1:-we used azure document intelligence( analyses any type of document like invoice, reports , essays etc) we connected it to resource group which is linked to open ai(a service which is llm ie. large language mode).....now, a function extracts dataframe from pdf and another function extracts summary from dataframe. so we extracted data from a pdf and converted to dataframe and then asked llm to summarise it( summary tells what is low or high). 
phase 2:- we created a suggest nutrient intake function using open ai again. we converted the dataframe to string so that we get it as text so its easy for llm to analyze. now we did prompt engineering to tell us what nutrients is missing and the nutrients we need to take. it takes this from national institute of health us information website. the above is backbone of our project. now we used streamlit for now to implement this backbone in a front end. 
we might change the front end as per the needs of our sponsors but for now... so you can upload your blood reports and it will analyse it and tell you the nutrients needed. plan from here:- now we plan on implementing translation services. and we will try to implement image recognition ..like you post a pic of whatever is available in the fridge (raw food) and you will get the output as what to consume. if we can't de image recognition , we will go back to providing text output as to what food to consume.
