from .models import Action, User, Post

class Feed:
    def __init__(self, user):
        self.user = user

class UserFeed(Feed):
    def get_feed_data(self):
        actions = Action.objects.exclude(user=self.user)
        following_ids = self.user.following.values_list('id', flat=True)
        actions = actions.filter(user_id__in = following_ids)
        actions.select_related('user', 'user__profile').prefetch_related('target')[:10]
        if len(actions)==0:
            self.get_popular_posts()
            return False
        self.data = actions
        return True

    def get_popular_posts(self):
        posts = Action.objects.exclude(user=self.user).filter(verb="post")[:10]
        self.data = posts

class ProfileFeed(Feed):
    def get_feed_data(self):
        actions = Action.objects.filter(
            user=self.user, verb="post"
        ).select_related(
            'user', 'user__profile'
        ).prefetch_related('target')[:10]
        self.data = actions


