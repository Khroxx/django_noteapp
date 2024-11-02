from django.db import models

from django_noteapp.users.models import User


class Note(models.Model):
    # Core Fields
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_notes",
    )
    collaborators = models.ManyToManyField(
        User,
        blank=True,
        related_name="collaborator_notes",
    )
    color = models.CharField(
        max_length=7,
        blank=True,
        default="",
    )  # HEX COLOR
    category = models.ManyToManyField("Category", blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
