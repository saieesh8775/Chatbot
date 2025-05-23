import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
load_dotenv()
base_url=os.getenv("Base_url")
api_key=os.getenv("Chatbot_api")
client = OpenAI(
    base_url=base_url,
    api_key=api_key,
     )
def chat_with_model(user_input):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": user_input}
            ],
            model="openai/gpt-4.1",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
gr_interface = gr.Interface(fn=chat_with_model,
    inputs=gr.Textbox(lines=4, placeholder="Ask something..."),
    outputs="text",
    title="GPT-4o-mini Chat",
    description="Chat with an OpenAI GPT-4o-mini model using a custom endpoint."
)
gr_interface.launch()
print("Chatbot ready (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", chat_with_model(user_input))
