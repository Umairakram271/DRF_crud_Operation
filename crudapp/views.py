
from crudapp.serializers import StudentSerializer, SubjectSerializer
from rest_framework.decorators import api_view
from crudapp.models import Student, subject
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST', 'PUT','PATCH','DELETE'])
def Student_create(request, pk=None):
    if request.method == 'GET':
        id = pk 
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
            
        stu = Student.objects.all()
        print(stu)
        serializer = StudentSerializer(stu, many=True) 
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'mas':'Data created'}
            return Response(res)
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mas': 'data Updated'})
        return Response(serializer.error)
        

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'mas': 'data Deleted'})

# ----------------- subject --------------------------------

@api_view(['GET', 'POST', 'PUT','PATCH','DELETE'])
def Subject_create(request, pk=None):
    if request.method == 'GET':
        id = pk 
        if id is not None:
            stu = subject.objects.get(id=id)
            serializer = SubjectSerializer(stu)
            return Response(serializer.data)
            
        stu = subject.objects.all()
        print(stu)
        serializer = SubjectSerializer(stu, many=True) 
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SubjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'mas':'Data created'}
            return Response(res)
        return Response(serializer.error)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mas': 'data Updated'})
        return Response(serializer.error)
        

    if request.method == 'DELETE':
        id = pk
        stu = subject.objects.get(pk=id)
        stu.delete()
        return Response({'mas': 'data Deleted'})