from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=25, unique=True)

  def __str__(self):
    return self.name

  # class Meta:
    # model = Cat


class Blog(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)  #! forengkey one-to-many ilişki demek
  # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  #! category i silme içindeklerin yerine null yaz
  is_published = models.BooleanField(default=False)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  # class Meta:
  #   ordering = ("-name",)
  #   verbose_name = "category"
