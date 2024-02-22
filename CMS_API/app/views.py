from .serializers import *
from .models import *
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            data = request.data
            response = {"status": "success", "data": "", "message":"", "http_status": HTTP_201_CREATED}
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                password = make_password(data.get('password'))
                serializer.validated_data['password'] = password

                serializer.save()
                response['status'] = "success"
                response['data'] = serializer.data
                response["message"] = "Registration Seccessfully!!!"
            else:
                response["status"] =   "error"
                response["message"] = "Registration Failed!!!"
                response["http_status"] = HTTP_400_BAD_REQUEST
                response["data"] = serializer.errors

        except Exception as e:
            response["status"] = "error"
            response["message"] = "Registration Failed!!!"
            response["http_status"] = HTTP_400_BAD_REQUEST
            response["data"] = str(e)

        return JsonResponse(response, status=response.get('http_status', HTTP_200_OK))



class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        response = {"status": "success", "data": "", "message":"", "http_status": HTTP_201_CREATED}
        email = request.data.get("email")
        password = request.data.get("password")

        if email and password:  
            user = authenticate(request=request, username=email, password=password)

            if user is not None:
                login(request, user)
                
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                response['access_token'] = access_token
                response['status'] = "success"
                response['message'] = "logged in successfully"

                resp = JsonResponse(response, status=response.get(
                            'httpstatus', HTTP_200_OK))
                resp.set_cookie('access_token', access_token)
                return resp 
            else:
                response['status'] = "failed"
                response['message'] = "invalid credentials"
                response['http_status'] = HTTP_400_BAD_REQUEST
        else:
            response["status"] = "error"
            response["http_status"] = HTTP_400_BAD_REQUEST
            response["message"] = "email and password are required"

        return Response(response, status=response.get('http_status',HTTP_200_OK))

class UserLogoutView(APIView):
    def get(self, request):
        response = {"status": "success", "data": "", "message":"", "http_status": HTTP_201_CREATED}
        try:
            logout(request)         
            request.session.clear()
            request.session.pop('access_token', None)
            response['message'] = "logged out successfully"
            return Response(response, status=response.get('http_status',HTTP_200_OK))

        except Exception as e:
            response['status'] = "error"
            response['message'] = "Logout faild"
            response['httpstatus'] = HTTP_400_BAD_REQUEST

        return Response(response, status=response.get('http_status',HTTP_200_OK))


class ContentItems(APIView):
    def get(self, request):
        response = {"status": "success", "data": "", "message":"", "http_status": HTTP_201_CREATED}
        user = request.user
        if user.is_superuser ==False:
            search_item = request.query_params.get('search',None)
            if search_item:
                content_items = ContentItem.objects.filter(
                    Q(title__icontains=search_item) |
                    Q(body__icontains=search_item) |
                    Q(summary__icontains=search_item) |
                    Q(category__icontains=search_item),
                    author=user
                )
            else:
                content_items = ContentItem.objects.filter(author=user)
            serializer = ContentItemSerializer(content_items, many=True)
            if serializer.data:
                response["data"]=serializer.data
                response["message"]="Data Fetch successfully"
            else:
                response["message"]="Data not found"
                return Response(response, status=response.get('http_status',HTTP_404_NOT_FOUND))
            return Response(response, status=response.get('http_status',HTTP_200_OK))
        else:
            response["status"]="error"
            response["data"]=serializer.errors
            return Response(response, status=response.get('http_status',HTTP_400_BAD_REQUEST))


    def post(self, request):
        response = {"status": "success", "data": "", "message":"", "http_status": HTTP_201_CREATED}
        username = request.user
        data = request.data
        data['author'] = request.user.id
        if username.is_superuser ==False:
            serializer = ContentItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response["data"]=serializer.data
                response["message"]="Data Saved"
                return Response(response, status=response.get('http_status',HTTP_200_OK))
            else:
                response["status"]="error"
                response["data"]=serializer.errors
                return Response(response, status=response.get('http_status',HTTP_400_BAD_REQUEST))



    def patch(self, request, pk):
        response = {"status": "success", "data": "", "message":"", "http_status": HTTP_201_CREATED}
        username = request.user
        if username.is_superuser ==False:
            content_item = ContentItem.objects.get(id=pk)
            serializer = ContentItemSerializer(content_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response["message"]="Data update successfully"
                response["data"]=serializer.data
                return Response(response, status=response.get('http_status',HTTP_200_OK))
            else:
                response["message"]="Failed to update"
                response["data"]=serializer.errors
            return Response(response, status=response.get('http_status',HTTP_400_BAD_REQUEST))
        response["message"]="Failed to update"
        response["data"]="error"
        return Response(response, status=response.get('http_status',HTTP_400_BAD_REQUEST))


    def delete(self, request, pk):
        response = {"status": "success", "data": "", "message":"", "http_status": HTTP_201_CREATED}
        username = request.user
        if username.is_superuser==False:
            try:
                content_item = ContentItem.objects.get(id=pk)
            except ContentItem.DoesNotExist as e:
                response["message"] = "Data not found"
                return Response(response, status=response.get('http_status',HTTP_404_NOT_FOUND))
            
            serializer = ContentItemSerializer(content_item, data=request.data, partial=True)
            content_item.delete()
            if serializer.is_valid():
                response["message"]="Data has been deleted"
                return Response(response, status=response.get('http_status',HTTP_200_OK))
            else:
                response["data"]=serializer.errors
                response["message"]="Failed to delete"
            return Response(response, status=response.get('http_status',HTTP_200_OK))
        response["message"]="Failed to delete"
        response["data"]="error"
        return Response(response, status=response.get('http_status',HTTP_200_OK))