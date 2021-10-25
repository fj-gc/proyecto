from django.db import models

# Create your models here.
class Quote(models.Model):
	text = models.TextField(null=True)
	quote_start = models.IntegerField(null=True)
	quote_end = models.IntegerField(null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True)
	updated_at = models.DateTimeField(auto_now=True,null=True)