from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#! Bununla json formata çeviriyoruz ve HttpResponse kullanmıyoruz. Hangi meodu kullanaçağımızı belirtiyoruz. defaılt  get tir
@api_view()
def home(request):
  return Response({'home':'This is home page...'})

  #? http methods ------------> get, post, delete, put, patch
 #! GET: Sunucudan bir belge veya veri almak için kullanılır. GET isteği yalnızca veriyi okumak için kullanılmalıdır, çünkü GET isteği tarayıcı ve proxy sunucuları tarafından önbelleğe alınabilir ve bu nedenle birkaç kez çalıştırılabilir.
#?HEAD: Sunucudan bir belge veya verinin üstbilgilerini almak için kullanılır. HEAD isteği, GET isteğine benzerdir, ancak sunucudan geri dönen veri yoktur. Bu, sunucudaki bir belgenin varlığını veya önbelleklenme durumunu kontrol etmek için kullanılabilir.
#!POST: Sunucuya bir belge veya veri göndermek için kullanılır. POST isteği, veritabanı güncelleştirmesi gibi veri oluşturan ve değiştiren işlemler için kullanılır.
#?PUT: Sunucuya bir belge veya veri yüklemek için kullanılır. PUT isteği, bir belge veya verinin tamamının yerine koyulması için kullanılır.
#!DELETE: Sunucudaki bir belge veya veriyi silmek için kullanılır.
#?CONNECT: Sunucuyla bir iletişim kanalı oluşturmak için kullanılır.
#!OPTIONS: Sunucunun desteklediği HTTP metotlarının bir listesini almak için kullanılır.
#?TRACE: Sunucudan gönderilen bir isteğin yolunu takip etmek için kullanılır.
#!PATCH: Sunucudaki bir belge veya verinin bir parçasını değiştirmek için kullanılır.

@api_view(['GET'])
def students_list(request):
  students = Student.objects.all()
  print(students)
  #! Birden fazla data döneçeği için many=True diyoruz
  serializer = StudentSerializer(students, many=True)
  print(serializer)
  print(serializer.data)
  return Response(serializer.data)



@api_view(['POST'])
def student_create(request):
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {"message":f"Student updated successfull..."}
    return Response(message,status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET'])
def student_detail(request,pk):
  # student = Student.objects.get(id=pk)
  student = get_object_or_404(Student, id=pk)
  serializer = StudentSerializer(student)
  return Response(serializer.data)


@api_view(['PUT'])
def student_update(request,pk):
  student = get_object_or_404(Student, id=pk)
  serializer = StudentSerializer(instance=student, data=request.data, )
  if serializer.is_valid():
    serializer.save()
    message = {"message":f"Student updated successfull..."}
    return Response(message)
  return Response(serializer.data)



@api_view(['DELETE'])
def student_delete(request,pk):
  student = get_object_or_404(Student, id=pk)
  student.delete()
  message = {
    'message': 'Student deleted succesfull...'
  }
  return Response(message)



  #!Bir yerde toplanmış hali

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data,partial=True)
        #!parça parça güncelleme işlemleri için kullanılan method. PATCH için.
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)