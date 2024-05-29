from configparser import ConfigParser
from langchain_google_genai import ChatGoogleGenerativeAI


class Gemini:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.llm = ChatGoogleGenerativeAI(
            model=self.config["Gemini"]["model"],
            google_api_key=self.config["Gemini"]["API_KEY"]
        )

    def ask(self, text: str):
        result = self.llm.invoke(text)
        return str(result.content)
