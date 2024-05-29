from configparser import ConfigParser
from langchain_google_genai import ChatGoogleGenerativeAI


class LLM:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.llm = ChatGoogleGenerativeAI(
            model=self.config["Gemini"]["model"],
            google_api_key=self.config["Gemini"]["API_KEY"]
        )

    def invoke(self, text: str):
        result = self.llm.invoke(text)
        return result
