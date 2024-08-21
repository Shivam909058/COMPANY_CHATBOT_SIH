# Employee Query Chatbot

This project is a Streamlit web application build a chatbot for handling employee queries. The chatbot can answer questions related to company HR policies, IT support, and company events. It also allows a single company to register and provide its information, which is stored and used to respond to employee queries.

## Features

- **Company Registration:** Only one company can register at a time and provide its HR policies, IT support information, and company events.
- **Dynamic Query Handling:** Employees can query about the company's policies, IT support, and events.
- **Embeddings and Vector Store:** Uses OpenAI embeddings and Chroma vector store for efficient document retrieval.
- **Question Answering:** Uses LangChain for question answering.
- **BHAI baki info dalni padegii company apko**


## Technologies Used

- **Streamlit:** For the web interface.
- **LangChain:** For the retrieval and QA chain.
- **OpenAI:** For embeddings and language model.
- **Chroma:** For the vector store.

## Setup

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/employee-query-chatbot.git
    cd employee-query-chatbot
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. **Run the application:**

    ```bash
    streamlit run app.py
    ```























