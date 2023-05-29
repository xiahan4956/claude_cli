from config import *
import anthropic


client = anthropic.Client(API_KEY)
def get_msg(user_input:str,conversation_history:str):
    prompt=f"{anthropic.HUMAN_PROMPT}{user_input}{anthropic.AI_PROMPT}{conversation_history}"
    
    response = client.completion(
        prompt=prompt,
        stop_sequences = [anthropic.HUMAN_PROMPT],
        model=MODEL,
        max_tokens_to_sample=10000,
    )
    print(response["completion"])

    conversation_history = "\n\nthis is our chat history \n" + "user_input:" + user_input + "\n" +"AI answer:" + response["completion"] 
    
    return  conversation_history

if __name__ == '__main__':
    conversation_history = ""
    prompt = ''
    while True:
        user_input = input('Your message: ')
        conversation_history += get_msg(user_input,conversation_history)
        