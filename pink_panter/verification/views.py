from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.utlis import generate_otp, send_otp_email
from .models import CustomUser
from pink_panter.settings import logger

class LoginWithOTP(APIView):
    def post(self, request):
        logger.info("start")
        email = request.GET.get('email', '')
        # try:
        #     user = CustomUser.objects.get(email=email)
        # except CustomUser.DoesNotExist:
        #     return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        otp = generate_otp()
        # user.otp = otp
        # user.save()

        send_otp_email(email, otp)
        # send_otp_phone(phone_number, otp)

        return Response({'message': 'OTP has been sent to your email.'}, status=status.HTTP_200_OK)