import streamlit as st
import google.generativeai as genai

# Configure Google Gemini
genai.configure(api_key="AIzaSyD392GOaf1UL77NqqSq7jM9ITfUly4Zw0Q")

# Title of the app
st.title("🤖 Chatbot App with Google Gemini")

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate chatbot response using Google Gemini
    with st.chat_message("assistant"):
        # Initialize the Gemini model
        model = genai.GenerativeModel("gemini-pro")

        # Generate response
        response = model.generate_content(prompt)
        st.markdown(response.text)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})





from atlassian import Confluence

# Connect to Confluence
confluence = Confluence(
    url="https://your-confluence-site.atlassian.net",
    username="your_username",
    password="your_api_token",
)

# Fetch a page
page_id = "12345"  # Replace with your page ID
page = confluence.get_page_by_id(page_id)
content = page["body"]["storage"]["value"]



from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient("http://localhost:6333")

# Create a collection
client.create_collection(
    collection_name="confluence_data",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)

# Add vectors to the collection
client.upsert(
    collection_name="confluence_data",
    points=[
        {
            "id": 1,
            "vector": embedding,  # Replace with your embedding
            "payload": {"content": "Sample Confluence content"},
        }
    ],
)

# Query the collection
results = client.search(
    collection_name="confluence_data",
    query_vector=query_embedding,  # Replace with your query embedding
    limit=5,
)