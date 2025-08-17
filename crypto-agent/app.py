import chainlit as cl
from main import agent
from agents import Runner
from typing import Optional, Dict, Any

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, Any],
    default_user: cl.User,
) -> Optional[cl.User]:
    """Handle OAuth callback (currently defaults to provided user)."""
    print(f"Provider: {provider_id}")
    print(f"User Data: {raw_user_data}")
    return default_user

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! How can I help you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    try:
        result = await Runner.run(agent, message.content)
        await cl.Message(content=result.final_output).send()

    except Exception as e:
        print(f"Error occurred: {e}")
        await cl.Message(content=f"⚠️ Error: {str(e)}").send()
