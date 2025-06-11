from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['email','username','is_verified']


# class RegisterSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ['email','password','username']
        
#         def create(self, validated_data):
#             user = User.objects.create_user(
#                 validated_data['username'],
#                 validated_data['email'],
#                 validated_data['password'],
#             )
#             return user
        

# class LoginSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(required=True)
#     # email = serializers.CharField(required=True)
#     password = serializers.CharField(required=True,write_only=True)



#####verify email k lie serializer

class VerifyAccSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


from .models import Product

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        fields = (
               'id',
               'product_name',
               'product_price',
               'product_details',
               'date_created',
        )
        read_only_fields = ['buyer_id'] 
        model = Product
     

# class BuyerSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Product
#         fields = ['id', 'password', 'email'] 
