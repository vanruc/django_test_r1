from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import status, permissions

from unity.models import Leads, Store


class LeadsSubscribe(APIView):
    def post(self, request):
        permission_classes = [permissions.IsAuthenticated,
                              TokenHasReadWriteScope]
        # validate email address
        email_address = request.data['email']
        try:
            validate_email(email_address)
        except ValidationError as e:
            return Response({
                'msg': e.message
            })

        # get user from authentication information through request.user
        user = User.objects.get(username = request.user)
        # get user's store
        try:
            store = get_object_or_404(Store, store_owner=user)
        except Http404 as e:
            return Response(
                data={
                    'msg': 'Cannot find Store Information',
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # check if leads already subscribed this store
        if Leads.objects.filter(store=store, email_address=email_address)\
                .count():
            return Response(
                data={
                    'msg': 'You already subscribed to this store before, no action needed'
                },
                status=status.HTTP_200_OK
            )
        else:
            # create leads and store to the database
            leads = Leads(store=store, email_address=email_address)
            leads.save()

        return Response(
            data={
                'subscribed': 'success',
            },
            status=status.HTTP_201_CREATED
        )
