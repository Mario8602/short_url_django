from django.db import models
from django.conf import settings
import random

class Token(models.Model):
    full_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=20, unique=True, db_index=True)
    number_transitions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.short_url} ---- {self.full_url}'
    
    def gen_token(self) -> str:
        self.short_url = ''.join(random.choices(population=settings.POPULATION, k=settings.TOKEN_LENGTH))
        return self.short_url