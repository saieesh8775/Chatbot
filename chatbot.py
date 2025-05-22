import os
from openai import OpenAI
import gradio as gr

# Initialize OpenAI client
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key="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",  # ⚠️ Use environment variable in production
)

# Define the function for both CLI and Gradio
def chat_with_model(user_input):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": user_input}
            ],
            model="openai/gpt-4o-mini",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Gradio Interface
gr_interface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=4, placeholder="Ask something..."),
    outputs="text",
    title="GPT-4o-mini Chat",
    description="Chat with an OpenAI GPT-4o-mini model using a custom endpoint."
)

# Launch the Gradio app in a separate thread or process
gr_interface.launch(share=True)

# Optional: CLI interaction using while True
print("Chatbot ready (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", chat_with_model(user_input))
