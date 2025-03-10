import enum
from typing import cast

from pydantic import BaseModel

from openai.types.chat import ChatCompletionMessageParam

class Role(str, enum.Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

class MessageType(str, enum.Enum):
    text = "text"
    image = "image_url"

class Message(BaseModel):
    role: Role
    content: str
    type: str = MessageType.text

class Conversation:
    def __init__(self):
        self.messages: list[Message] = []

    def add_message(self, message: Message) -> None:
        self.messages.append(message)
    
    def add_user_message(self, content: str) -> None:
        self.add_message(Message(role=Role.user, content=content))

    def add_assistant_message(self, content: str) -> None:
        self.add_message(Message(role=Role.assistant, content=content))

    def add_system_message(self, content: str) -> None:
        self.add_message(Message(role=Role.system, content=content))

    def to_openai_messages(self):
        return [cast(ChatCompletionMessageParam, {"role": m.role, "content": m.content}) for m in self.messages]
    
    @classmethod
    def from_system_message(cls, content: str) -> "Conversation":
        conversation = cls()
        conversation.add_system_message(content)
        return conversation
    
    @classmethod
    def from_user_message(cls, content: str) -> "Conversation":
        conversation = cls()
        conversation.add_user_message(content)
        return conversation

    @classmethod
    def from_assistant_message(cls, content: str) -> "Conversation":
        conversation = cls()
        conversation.add_assistant_message(content)
        return conversation