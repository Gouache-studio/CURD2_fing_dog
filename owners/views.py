from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

# 신규 주인 등록 post 
# {
# 		"name" : "위르겐 클롭",
# 		"email" : "liverpool@naver.com",
# 		"age" : 54
# }

# Create your views here.
class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body) 

        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
            )
        
        return JsonResponse({'MESSAGE' : 'CREATED'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results =[]
        for owner in owners:
            results.append(
                {
                    "name" : owner.name,
                    "email": owner.email,
                    "age": owner.age,
                }
            )
        return JsonResponse({'results': results}, status=200)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)

        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner_id = data['owner_id']
        )
        
        return JsonResponse({'MESSAGE' : 'CREATED'}, status = 201)
    
    def get(self, request):
        dogs = Dog.objects.all()
        results =[]
        for dog in dogs:
            results.append(
                {
                    "name" : dog.name,
                    "age": dog.age,
                    "owner_id": dog.owner_id,
                }
            )
        return JsonResponse({'results': results}, status=200)

        


