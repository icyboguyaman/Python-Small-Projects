import openai
import prompt_toolkit

# Enter your API key here
openai.api_key = "YOUR_API_KEY"

# Set up the prompt toolkit
history = []
prompt_session = prompt_toolkit.PromptSession()

# Define the callback function for the prompt toolkit
def get_input():
    user_input = prompt_session.prompt("> ")
    history.append(user_input)
    return user_input

# Initialize the ChatGPT engine
model_engine = "text-davinci-002"
chat_engine = "davinci"
model_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nUser: Hello, how are you?\nAI: I'm doing great, thanks for asking! How can I help you today?\n\n"

# Define the function to generate a response from ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine=chat_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Start the conversation loop
print(model_prompt)
while True:
    user_input = get_input()
    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        print("AI: Goodbye!")
        break
    prompt = model_prompt + "User: " + "\nUser: ".join(history) + "\nAI: "
    response = generate_response(prompt + user_input)
    print("AI:", response)
    history.append(response)
