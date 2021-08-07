# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_session_key = models.CharField(blank=True, null=True, max_length=40)

    # def set_session_key(self, key):
    #     if self.last_session_key and not self.last_session_key == key:
    #         try:
    #             data_last_session = Session.objects.get(session_key=self.last_session_key)
    #             data_last_session.delete()
    #         except Session.DoesNotExist:
    #             pass
    #     self.last_session_key = key
    #     self.save()


@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()
