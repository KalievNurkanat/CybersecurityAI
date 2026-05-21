from rest_framework import viewsets
from api.models import RequestData
from api.serializers import RequestDataSerializer
from api.services import analyze_request
from rest_framework.response import Response
from common.permissions import IsAuthorized
from users.gmail_utils import get_latest_email

class RequestDataViewSets(viewsets.ModelViewSet):
    queryset = RequestData.objects.all()
    serializer_class = RequestDataSerializer
    permission_classes = [IsAuthorized]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]
        url = serializer.validated_data["url"]
        sender = serializer.validated_data["sender"]

        result = analyze_request(text, url, sender)

        RequestData.objects.create(text=text, url=url, sender=sender)


        return Response({"result":result}, status=201)
    

class RequestGmailDataViewSets(viewsets.ModelViewSet):
    queryset = RequestData.objects.all()
    permission_classes = [IsAuthorized]
    serializer_class = RequestDataSerializer

    def create(self, request, *args, **kwargs):
        access_token = request.data.get("google_access_token")

        if not access_token:
            return Response(
                {"Error": "Access token is required"},
                  status=400
                )
        
        gmail_data = get_latest_email(access_token)

        if not gmail_data:
            return Response(
                {"Error": "No email messages found"},
                status=400
            )
        
        text = gmail_data["text"]
        url = gmail_data["url"]
        sender = gmail_data["sender"]
        subject = gmail_data["subject"]

        result = analyze_request(text, url, sender)

        RequestData.objects.create(text=text, url=url, sender=sender)

        return Response({"result":result,
                        "sender": sender,
                        "url": url,
                        "text": text,
                        "subject": subject
                        }, status=201)