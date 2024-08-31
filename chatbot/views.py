from rest_framework.decorators import api_view
from rest_framework.response import Response

from chatbot.services import create_thread, send_message_to_thread, create_run_from_thread, check_completed_run, get_latest_message

@api_view(['POST'])
def create_conversation_thread(request):
    thread_id = create_thread()
    return Response({'thread_id': thread_id})

@api_view(['POST'])
def send_message_and_receive_chat_response(request):
    thread_id = request.data.get('thread_id')
    message = request.data.get('message')
    
    if not thread_id or not message:
        return Response({'error': 'Thread ID and message are required'}, status=400)
    
    updated_thread_id = send_message_to_thread(thread_id, message)
    
    run_response = create_run_from_thread(updated_thread_id)

    completed_run = check_completed_run(run_response.thread_id, run_response.id)
    if (completed_run == None or (completed_run != None and completed_run.status == 'failed')):
        return Response({'response': { 'message': 'Estamos presentando inconvenientes, intente de nuevo en unos minutos' }})

    response = get_latest_message(completed_run.thread_id)
    
    return Response({'response': response })
