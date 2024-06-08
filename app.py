from langserve import RemoteRunnable
import streamlit as st


def app(languege, input_text):
    remote_chain = RemoteRunnable("http://localhost:8000/cohere-translator")
    respone =remote_chain.invoke({"language":languege, "text":input_text})
    
    return respone

def main():
    st.header("LangChain Cohere Translator App")
    st.text("Translate English to other languages")
    language = st.text_input("Enter your language to translate")
    input_text = st.text_input("Enter your text to translate")
    if st.button("Translate"):
        st.write(app(language, input_text))

if __name__ == "__main__":
    main()