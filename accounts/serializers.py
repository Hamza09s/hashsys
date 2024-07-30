from rest_framework import serializers
from django.db import transaction
from django.contrib.auth import get_user_model
from tenant_shared.models import Buisness, Domain
from django.core.exceptions import ValidationError


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "is_mobile_verified",
            "buisness_name",
            "password",
        ]

    def create(self, validated_data):
        email = validated_data.get("email").lower()
        buisness_name = validated_data.get("buisness_name")
        validated_data["email"] = email

        try:
            with transaction.atomic():
                if User.objects.filter(email=email).exists():
                    raise ValidationError(
                        {"email": "A user with this email already exists."}
                    )
                schema_name = buisness_name.lower().replace(" ", "_")
                tenant = Buisness(schema_name=schema_name, name=buisness_name)
                tenant.save()

                validated_data["buisness"] = tenant
                user = User.objects.create_user(**validated_data)

                user.save()

                domain = Domain(
                    domain=f"{schema_name}.localhost",
                    tenant=tenant,
                    is_primary=True,
                )
                domain.save()

        except Exception as e:
            raise ValidationError(f"An error occurred while creating the tenant: {e}")

        return user


class BuisnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buisness
        fields = "__all__"
