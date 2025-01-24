import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_response(user_input):
    prompt = "너는 옷 코디네이터야 오늘 입을 옷을 추천해줘 그리고 이모티콘을 사용해"
    messages = [{"role": "system", "content": prompt}, {"role": "user", "content": user_input}]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply


    
