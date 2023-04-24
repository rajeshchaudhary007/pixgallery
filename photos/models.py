from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(blank=False, null=False)
    title = models.CharField(max_length=50,null=True)
    descriptions = models.TextField()

    def __str__(self):
        return self.descriptions