from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):
    user = models.ForeignKey('auth.User', related_name='actions',db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)

    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

class Feed:
    def __init__(self, user):
        self.user = user

class UserFeed(Feed):
    def get_feed_data(self):
        actions = Action.objects.exclude(user=self.user)
        # following_ids = self.user.following.values_list('id', flat=True)
        # actions = actions.filter(user_id__in = following_ids)
        actions.select_related('user', 'user__profile').prefetch_related('target')[:10]
        self.data = actions

class ProfileFeed(Feed):
    def get_feed_data(self):
        pass

