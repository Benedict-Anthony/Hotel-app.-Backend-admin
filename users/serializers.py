from rest_framework import serializers

from users.models import CustomUser


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name","password"]
        extra_fields = [{"password":{"write_only": True}}]
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        print(validated_data)
        if password is None:
            raise ValueError("password can not be None")
        
        instance = CustomUser.objects.create(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance