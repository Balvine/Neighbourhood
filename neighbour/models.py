from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Neighbour(models.Model):
    """
    Class that defines neighbourhood details
    """
    name = models.CharField(max_length=60)
    loc = (
        ('Rongai', 'Rongai'),
        ('Westlands', 'Westlands'),
        ('South b', 'South b'),
        ('South c', 'South c'),
        ('Langata', 'Langata'),

    )
    description = models.TextField(default="This is home")
    location = models.CharField(max_length=60, choices=loc)
    police = models.CharField(max_length=10, default='0700000000')
    health = models.CharField(max_length=10, default='0700000000')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        hood = Neighbour.objects.get(id=id)
        return hood

    @classmethod
    def search_by_title(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood


class Profile(models.Model):
    """
    Class that contains Profile details
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbour, null='True')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()

    @classmethod
    def get_user_by_hood(cls, id):
        profile = Profile.objects.filter(hood_id=id).all()
        return profile


class Business(models.Model):
    """
    Contains Business details
    """
    name = models.CharField(max_length=30)
    description = models.TextField(default="business")
    email = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbour)

    def __str__(self):
        return self.name

    def save_biz(self):
        self.save()

    def delete_biz(self):
        self.delete()

    @classmethod
    def get_by_bizid(cls, id):
        biz = Business.objects.get(id=id)
        return biz

    @classmethod
    def get_biz_by_hood(cls, id):
        biz = Business.objects.filter(hood_id=id).all()
        return biz

    @classmethod
    def search_biz(cls, name):
        biz = cls.objects.filter(name__icontains=name)
        return biz


class Join(models.Model):
    models.OneToOneField(User)
    hood = models.ForeignKey(Neighbour)

    def __str__(self):
            return self.user


class Posts(models.Model):

    body = models.TextField()
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbour)

    def save_posts(self):
        self.save()

    def del_posts(self):
        self.delete()

    def __str__(self):
        return self.body

    @classmethod
    def get_post_by_hood(cls, id):
        post = Posts.objects.filter(hood_id=id).all()
        return post
