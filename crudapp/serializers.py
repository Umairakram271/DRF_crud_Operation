from rest_framework import serializers
from crudapp.models import Student, subject

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']
    def validate_roll(self, value):
            if int(value)>=200:
                print("pakistanss")
                raise serializers.ValidationError("seatfull")
            return value
    def validate(self, data):
        nm = data.get('name')
        cy = data.get('city')
        if nm=="umair" and cy !="lahore":
            raise serializers.ValidationError("city must be lahore")
        return data
        


class SubjectSerializer(serializers.ModelSerializer):
    enroll = serializers.SerializerMethodField()
    def get_enroll(self, obj):
        print('object',obj)
        dat = StudentSerializer(obj.stu_id).data
        print(dat)
        return [StudentSerializer(dat).data for dat in Student.objects.filter(id=dat['id'])]
    
    class Meta:
        model = subject
        fields = ['stu_id','CourseName', 'credithours', 'enroll']
