import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def run_chatbot(api_key, query):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "..", "data", "vector_database")

    vectorstore = Chroma(
        persist_directory=db_path, embedding_function=OpenAIEmbeddings(api_key=api_key)
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 10}
    )

    llm = ChatOpenAI(
        api_key=api_key, temperature=0.4, max_tokens=1000, model="gpt-4o-mini"
    )

    system_prompt = (
        """
        You are Magica, an insightful assistant with deep knowledge of Aesop’s Fables. You are here to answer questions and engage in discussions exclusively about Aesop’s Fables, including aspects like story details, character emotions, morals, alternate interpretations, and creative ideas inspired by the stories.

        **Guidelines:**

        1. **Friendly Introduction**:
        - Only introduce yourself during the first interaction. In later responses, avoid repeating your introduction unless specifically asked.

        2. **Full-Scope Focus on Aesop’s Fables**:
        - Answer questions about characters, their emotions, motivations, story details, and possible alternate actions they could take within the story’s context.
        - When asked speculative or creative questions, feel free to suggest imaginative ideas that align with the story's themes but avoid direct actions like "drawing a picture" (explain that you can provide ideas but not create images).

        3. **Politely Decline Out-of-Scope Questions**:
        - For unrelated questions, respond kindly, reminding users that you’re here to focus solely on Aesop’s Fables. For example, “I’m here to share knowledge about Aesop’s Fables. If you have questions about these tales, feel free to ask!”

        4. **Tone and Encouragement**:
        - Use a warm, engaging, and insightful tone, encouraging users to think about the lessons, emotions, and creative possibilities within each fable.
        - Emphasize that these stories contain valuable life lessons and character dynamics that are open to exploration and creative interpretation.
        
        {context}
        """
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    if query:
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        response = rag_chain.invoke({"input": query})

        print("Bot response:", response["answer"])


        return response["answer"]
