from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

from django.urls import reverse


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Recipe(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    preview = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)
    last_change_at = models.DateTimeField(blank=True, null=True)
    likes = GenericRelation(Like)
    comments = GenericRelation(Comment)

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'recipe_id': self.pk})

    def __str__(self):
        return self.title

    def change(self):
        last_change_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'



class Complaint(models.Model):
    M = 'Мат'
    O = 'Оскорбления'
    D = 'Другое'
    complaint_reasons_choice = (
        (M, 'ненормативная лексика'),
        (O, 'оскорбления'),
        (D, 'другое'),
    )
    reason = models.CharField(
        max_length=255,
        choices=complaint_reasons_choice,
        default=D,
    )
    article = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=255, db_index=True)
    dish = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    veg = models.BooleanField(default=False)
