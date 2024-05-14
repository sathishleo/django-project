import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from travallo.service.productservice import Product_service
from travallo.data.request.productrequest import Product_request
