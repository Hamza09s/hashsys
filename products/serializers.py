from unicodedata import category
from rest_framework import serializers

from tenant_shared.models import City, Country, State
from tenant_shared.serializers import CitySerializer, CountrySerializer, StateSerializer
from .models import Product, Category, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        validated_data.pop("user")
        category = Category(**validated_data)
        category.save()
        return category


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

    def create(self, validated_data):
        validated_data.pop("user")
        brand = Brand(**validated_data)
        brand.save()
        return brand


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    country = CountrySerializer()
    city = CitySerializer()
    state = StateSerializer()

    class Meta:
        model = Product
        fields = ["user", "title", "country", "city", "state", "brand", "category"]

    def create(self, validated_data):
        country = validated_data.get("country")
        city = validated_data.get("city")
        state = validated_data.get("state")
        country = Country(**country)
        country.save()
        city = City(**city)
        country = validated_data.get("country")
        city = validated_data.get("city")
        state = validated_data.get("state")
        city.save()
        state = State(**state)
        state.save()
        validated_data["country"] = country
        validated_data["city"] = city
        validated_data["state"] = state

        product = Product(**validated_data)
        return product
