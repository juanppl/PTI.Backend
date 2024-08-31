import json
import time
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def create_thread():
    response = openai.beta.threads.create()
    return response.id

def send_message_to_thread(thread_id, user_message):
    response = openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )
    return response.thread_id

def create_run_from_thread(thread_id):
    response = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id='asst_Hmpa7tZ04FIw1ythNVkTMjFf'
    )
    print("Response from Thread")
    print(response)
    return response

def check_completed_run(thread_id, run_id):
    response = openai.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )

    print(response)

    if ( response.status == 'completed' or response.status == 'failed' ):
        return response
    
    time.sleep(5)

    check_completed_run(thread_id, run_id)


def get_latest_message(thread_id):
    messageList = openai.beta.threads.messages.list(thread_id)

    messages = [
        {
            'role': message['role'],
            'content': [content['text']['value'] for content in message['content']]
        }
        for message in messageList['data']
    ]
    
    return list(reversed(messages))[0] if messages else None


