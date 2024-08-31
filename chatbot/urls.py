from django.urls import path

from chatbot.views import create_conversation_thread, send_message_and_receive_chat_response

urlpatterns = [
    path('create-thread/', create_conversation_thread),
    path('send-message-to-thread/', send_message_and_receive_chat_response)
]
