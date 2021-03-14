from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.conf import settings
import pusher




@csrf_exempt
def webhook(request):
    response = MessagingResponse()
    if request.method == "POST":

        lat, lon = request.POST.get('Latitude'), request.POST.get('Longitude')
        if lat and lon:
            response.message("A Nurse has been assigned to your location,/n if this is a mistake say cancel!")
            pusher_client = pusher.Pusher(
                app_id='yourappid',
                key='yourkey',
                secret='yoursecret',
                encryption_master_key_base64='<output from command above>',
                cluster='yourclustername',
                ssl=True
            )

            pusher_client.trigger('private-encrypted-my-channel', 'my-event', {
                'message': 'hello world'
                })
                
        else:
            response.message("Send your location")

    return HttpResponse(response.to_xml(), content_type='text/xml')
