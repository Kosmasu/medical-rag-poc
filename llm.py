import asyncio
import enum
from openai import AsyncOpenAI, OpenAI
from openai.types.chat.chat_completion import ChatCompletion

from conversations import Conversation
from settings import DEEPINFRA_API_KEY

client = OpenAI(api_key=DEEPINFRA_API_KEY, base_url="https://api.deepinfra.com/v1/openai")

class LLMName(str, enum.Enum):
    LLAMA_3_3_70B_TURBO = "meta-llama/Llama-3.3-70B-Instruct-Turbo"
    LLAMA_3_2_90B_VISION = "meta-llama/Llama-3.2-90B-Vision-Instruct"
    LLAMA_3_1_8B_TURBO = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

class LLM:
    def __init__(self, model_name: LLMName):
        self.model_name = model_name

    def stream(self, convo: Conversation):
        pass

    def generate(self, convo: Conversation) -> str:
        chat_completion: ChatCompletion = client.chat.completions.create(
            model=self.model_name,
            messages=convo.to_openai_messages(),
        )
        response: str | None = chat_completion.choices[0].message.content
        print(f"{response=}")
        if not response:
            raise ValueError("Empty response from model")
        return response


if __name__ == "__main__":
    convo = Conversation()
    convo.add_user_message("Hello")
    convo.add_assistant_message("Hi, how can I help you?")
    convo.add_user_message("Can you say `Hello World`?")
    llm = LLM(LLMName.LLAMA_3_3_70B_TURBO)
    response = llm.generate(convo)
    print(response)