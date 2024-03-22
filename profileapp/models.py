from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #on_delete = 유저가 없어질때 프로파일 객체도 같이 사라질건지 안사라질건지. 여기서 CASCADE는 같이 사라지게 된다는 설정.
    #OneToOneField는 유저와 모델의 객체를 1대1 연결?

    image = models.ImageField(upload_to='profile/',null=True)
    #media 밑에 profile경로에 이미지 저장.

    nickname= models.CharField(max_length=20,unique=True, null=True)
    # unique == 중복불가능

    message = models.CharField(max_length=100,null=True)

