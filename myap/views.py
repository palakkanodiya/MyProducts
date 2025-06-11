
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .email import *

class RegisterAPI(APIView):

    def post(self,request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()

                #email k bd ab isko call krpayege otp walo ko
                send_otp_vie_email(serializer.data['email'])
                return Response({
                    'status' : 200,
                    'mesage' : 'register succesfully check mail',
                    'data' : serializer.data,          
                    })
            return Response({
                'status' : 400,
                'mesage' : 'something wrong',
                'data' : serializer.errors, 
            })
        except Exception as e:
            print(e)



###########verification

class VerifyOtp(APIView):
    def post(self,request):
        #is email ki ek otp h uske lie ab serializer lege
        try:
            data = request.data
            serializer = VerifyAccSerializer(data = data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                ###account exits h ya nhi
                user = User.objects.filter(email =  email)
                if not user.exists():
                    return Response({
                        'status' : 400,
                        'mesage' : 'something wrong',
                        'data' : 'invalid email',

                    })
                
                if user[0].otp != otp:
                    return Response({
                        'status' : 400,
                        'mesage' : 'something wrong',
                        'data' : 'invalid otp',

                    })

                ### agr otp shi h to  user  + email verified
                user = user.first() 
                user.is_verified = True
                user.save()
                
                return Response({
                    'status' : 200,
                    'mesage' : 'account verifird',
                    'data' : {},          
                    })
            
            return Response({
                'status' : 400,
                'mesage' : 'something wrong',
                'data' : serializer.errors, 
            })
 
           

        except Exception as e:  #e jo contain krta h msg error ko division hoti h zero se or statement print krta h error
            print(e)

##########product
from django.shortcuts import render
from rest_framework import generics
from .models import Buyer, Product

# import http
# Register_url = 'http://127.0.0.1:8000/register/'
class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from rest_framework.permissions import IsAuthenticated ,BasePermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permission import IsVerified

class IsVerified(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_verified
    
class ProductView(APIView):
    permission_classes = [IsAuthenticated,IsVerified]

    def get(self, request):
        # product_name = request.data.get('name')
        # product_price = request.data.get('price')
        return Response({"message": "Here is your product!"}, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        serializer = ProductSerializer(request.POST,request.Files)
        if serializer.is_valid():
            serializer.buyer = request.user
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#############3

from django.shortcuts import render, get_object_or_404
from .models import Buyer

def buyer_detail(request,buyer_id):
    buyer = get_object_or_404(Buyer,id=buyer_id)
    products = buyer.products.all()
    return render(request, 'buyer_detail.html', {'buyer': buyer,'products':products})
