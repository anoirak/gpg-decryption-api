from django.shortcuts import render
from rest_framework.views import APIView
import gnupg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import RequestSerializer
from decouple import config


class Decrypt_API(APIView):

    def __init__(self):
        homepage = config('HOMEPAGE')
        self.gpg = gnupg.GPG(gnupghome=homepage)

    def decrypt(self, message, passphrase):
        decrypted_data = self.gpg.decrypt(
            message=message, passphrase=passphrase)
        return decrypted_data

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.validated_data['message']
        passphrase = serializer.validated_data['passphrase']
        decrypted_data = self.decrypt(message, passphrase)
        if decrypted_data.ok:
            data = {
                "DecryptedMessage": str(decrypted_data)
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            raise ValidationError({"Error": "Decryption Failed !"})
