import google.generativeai as genai

# 1. Plug in your "Key" (like a password for the AI)
genai.configure(api_key="AIzaSyDMTm7Jvilz82RUiQcphHxDZGq8LCDciKM")

# 2. Choose which "Brain" to use
model = genai.GenerativeModel('gemini-pro')

# 3. Ask your question
response = model.generate_content("Give me a cool name for a robot I built in my garage.")

# 4. Print the answer to the screen
print(response.text)
