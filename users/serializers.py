from rest_framework import serializers

from users.models import BankDetails, CustomUser, HouseAgent


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name","phone", "password"]
        extra_fields = [{"password":{"write_only": True}}]
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = CustomUser.objects.create(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance
    
    
    def validate_password(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("password is too short")
        return value
        
       
class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankDetails
        fields = [
            "bank_name",
            "account_name",
            "account_number"
        ]
        
    def validate_account_number(self, value):
        unique = BankDetails.objects.filter(account_number=value)
        if unique.exists():
            raise serializers.ValidationError("User Account Details already Exist")
        
        if len(value) < 11 or len(value) > 11:
            raise serializers.ValidationError("Invalid Account Number")
        return value
    

        
class UserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "phone", "is_agent", "full_name"]
    
    def get_full_name(self,obj):
        try:
            return f'{obj.first_name} {obj.last_name}'
        except :
            return ""


class AgentProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    bank_details = BankDetailsSerializer()
    class Meta:
        model = HouseAgent
        fields = ["id", "user","bank_details","office","image_url" ]

class AgentCreateSerializer(serializers.ModelSerializer):
    bank_details = BankDetailsSerializer()
    class Meta:
        model = HouseAgent
        fields = ["id", "office","valid_id","NIN","image","bank_details","user",
        ]
        
    def create(self, validated_data):
        bank_details = validated_data.pop('bank_details')
        user_bank_details = BankDetails.objects.create(**bank_details)
        agent = HouseAgent.objects.create(**validated_data, bank_details=user_bank_details)
        agent.save()
        return agent