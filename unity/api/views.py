from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from unity.models import Leads, Store


class LeadsSubscribe(APIView):
    def post(self, request):
        """
        1. validate email
        2. get store object from authentication information
        3. check if leads already belong to the store
        4. create leads
        5. save leads
        6. response
        """
        # validate email address
        email_address = request.data['email']
        try:
            validate_email(email_address)
        except ValidationError as e:
            return Response({

            })

        # get store
        store = Store.objects.get(id=1)
        return Response({
            'subscribed': 'success',
        })