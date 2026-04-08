from rest_framework import serializers
from .models import *

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ["subject"]


class MentorSerializer(serializers.ModelSerializer):
    master_subject = serializers.CharField(source='master.subject', read_only=True)

    class Meta:
        model = Mentor
        fields = [
            'firstname',
            'lastname',
            'master_subject',
            'master',
        ]
    

class GroupSerializer(serializers.ModelSerializer):
    mentor_fullname = serializers.StringRelatedField(source='mentor', read_only=True)

    class Meta:
        model = Group
        fields = [
            'title',
            'mentor_fullname',
        ]

    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'firstname',
            'lastname',
            'grade',
        ]
    
    