from django.db import models



class Category(models.Model):
     name = models.CharField(max_length=300, verbose_name="Kategoriya nomi:")


     def __str__(self):
          return self.name


class Author(models.Model):
     full_name = models.CharField(max_length=200, verbose_name="Ism Familiyasi:")
     bio = models.TextField()
     img = models.ImageField(upload_to="image/", verbose_name="rasm yuklash:")


     def __str__(self):
         return self.full_name


class Book(models.Model):
     name = models.CharField(max_length=100, verbose_name="Kitob nomi:")
     title = models.TextField(verbose_name="Kitob haqida:")
     price = models.IntegerField()
     author  = models.ForeignKey(Author, on_delete=models.CASCADE)
     category  = models.ForeignKey(Category, on_delete=models.CASCADE)


     def __str__(self):
          return self.name


     class Meta:
          verbose_name = "Kitoblar_"



class BotUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    lang_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)


    def __str__(self):
         return str(self.chat_id)

    class Meta:
         verbose_name = "Foydalanuvchi_"


class Suggestion(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


    class Meta:
          verbose_name  = "Takliflar_"


class Complaint(models.Model):
     user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
     location = models.CharField(max_length=255)
     area = models.CharField(max_length=255)
     photo = models.ImageField(upload_to='complaints/')
     coordinates = models.CharField(max_length=255)
     category = models.CharField(max_length=255, null=True, blank=True)

     def __str__(self):
              return self.area

     class Meta:
          verbose_name = "Shikoyatlar_"



class Categories(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')