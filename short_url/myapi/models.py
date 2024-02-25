from django.db import models

import random
import string


class Token(models.Model):
    full_url = models.URLField(unique=True, max_length=400)
    short_url = models.CharField(max_length=6, unique=True, db_index=True, blank=True)
    number_transitions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.short_url} ({self.full_url[:15]})"

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.gen_token()
        super().save(*args, **kwargs)

    @staticmethod
    def gen_token():
        while True:
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            if not Token.objects.filter(short_url=token).exists():
                return token
