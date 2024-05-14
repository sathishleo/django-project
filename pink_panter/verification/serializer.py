# class VerifyAccountSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     otp = serializers.CharField()


# class EmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']
#     def create(self, validated_data):
#         user = User.objects.create(
#             username="Username",
#             email=validated_data['email'],
#         )
#         user.save()
#         return user