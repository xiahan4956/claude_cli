from config import *
import json

def chat(prompt):
    url = 'https://api.anthropic.com/v1/complete'
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY
    }
    data = {
        'prompt': prompt,
        'model': MODEL,
        'max_tokens': 100,
        'temperature': 0.8
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()
    completion = response_data['completion']
    print(completion)

if __name__ == '__main__':
    prompt = ''
    while True:
        user_input = input('Your message: ')
        prompt += '\nHuman: ' + user_input 
        chat(prompt)