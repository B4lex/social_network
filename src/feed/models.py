from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class Action(models.Model):
    user = models.ForeignKey(
        'auth.User', 
        related_name='actions',
        db_index=True, 
        on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=255)

    target_ct = models.ForeignKey(
        ContentType, 
        blank=True, 
        null=True, 
        related_name='target_obj', 
        on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)


class Contact(models.Model):
    user_from = models.ForeignKey(
        'auth.User',
        related_name='rel_from_set',
        on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        'auth.User', 
        related_name='rel_to_set',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

User.add_to_class('following',
    models.ManyToManyField('self',
    through=Contact,
    related_name='followers',
    symmetrical=False))

class Post(models.Model):
    user = models.ForeignKey('auth.User', related_name='posts',db_index=True, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)