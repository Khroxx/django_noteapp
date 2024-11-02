from rest_framework import serializers

from django_noteapp.users.models import User

from .models import Category
from .models import Note


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    collaborators = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
    )
    category = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
    )

    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
            "is_completed",
            "author",
            "collaborators",
            "color",
            "category",
            "category_ids",
        ]

    def create(self, validated_data):
        category_ids = validated_data.pop("category_ids", [])
        note = Note.objects.create(**validated_data)
        note.category.set(category_ids)
        return note

    def update(self, instance, validated_data):
        category_ids = validated_data.pop("category_ids", [])
        instance = super().update(instance, validated_data)
        instance.category.set(category_ids)
        return instance
