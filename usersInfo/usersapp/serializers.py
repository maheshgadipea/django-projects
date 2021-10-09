from django.db.models import fields
import re
from rest_framework import serializers
from .models import UserAccount
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAccount
        fields=['username','email','password','role']

    def validate(self,data):
        patternUsername=re.compile('^[a-zA-Z]+$')
        patternPassword = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$')
        usernameMatch=patternUsername.match(data['username'].strip())
        passwordMatch=patternPassword.match(data['password'].strip())

        if usernameMatch is None:
            raise serializers.ValidationError('Username should only contain alphabets.')
        if passwordMatch is None:
            raise serializers.ValidationError('Password must contain at least one uppercase letter, one lowercase letter, one number and one special character[@, $, !, %, *, ?, &].')
        
        return data
