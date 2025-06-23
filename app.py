import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()
api_key = os.getenv("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")

# Initialize the LLM
llm = ChatGroq(api_key=api_key, model="llama3-8b-8192")

# Prompt template for student doubt solving
doubt_prompt = PromptTemplate(
    template="""
You are a helpful, friendly, and knowledgeable tutor for school and college students.

Here is a student's question:

Subject: {subject}
Question: {question}

Give a clear, easy-to-understand answer. If possible, add a simple example or analogy.
Avoid too much jargon.
""",
    input_variables=["subject", "question"]
)

# Streamlit UI
st.title("🎓 Student Doubt Solver")

subject = st.selectbox("📘 Select Subject", ["General", "Math", "Physics", "Biology", "Computer Science", "Chemistry"])
question = st.text_area("❓ Ask your doubt here:")

if st.button("🧠 Get Answer"):
    if question:
        with st.spinner("Thinking..."):
            response = llm.invoke(doubt_prompt.format(subject=subject, question=question))
            st.markdown("### ✅ Answer:")
            st.write(response.content)
    else:
        st.warning("Please enter your doubt.")


