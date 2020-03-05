from django.db import models
from django.core.exceptions import ValidationError
def validate_title(value):
    if '@' in value and len(value.split())<3:
        raise ValidationError ("@ symbol cannot be used and the words must be greater than 3")
    else:
        return value

def minlengthvalidation(value):
    if len(value.split())>=3:
        return value
    else:
        raise ValidationError("atleast 3 words are required")
# Create your models here.
class NewsCategory(models.Model):
    title = models.CharField(max_length=100,unique=True, validators=[validate_title])

    def __str__(self):
        return  self.title

class News(models.Model):  # Here models is a package whereas Model is a class inside the model package.
    title = models.CharField(max_length=100, validators=[validate_title])
    description = models.TextField(blank=True, null=True, validators=[minlengthvalidation])
    image = models.ImageField(upload_to='news/')
    publish_date = models.DateField(auto_now=True)
    time= models.TimeField(auto_now=True)
    publish= models.BooleanField(default=True)
    category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    class Meta:
        db_table ='news'