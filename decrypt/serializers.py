from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    """
    Validate the request data.
    """
    message = serializers.CharField(required=True, allow_blank=True, error_messages={
                                    'required': 'This field is required'})
    passphrase = serializers.CharField(required=True, allow_blank=True, error_messages={
                                       'required': 'This field is required'})

    # def validate_message(self, data):
    #     """
    #     Clean message
    #     """
    #     data = data.replace('   ', '\n')
    #     print(data)
    #     return data
