from rest_framework import serializers
from . models import User,Library

class LibrarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Library
        fields=('book_name','auther','count')


class UserSerializer(serializers.ModelSerializer):
   
    

    class Meta:
        model=User
        fields=('name','email')
        depth=1
        




   

    