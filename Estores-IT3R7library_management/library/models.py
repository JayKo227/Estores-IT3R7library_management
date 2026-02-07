from django.db import models


class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"Library {self.library_id}"
    
    class Meta:
        db_table = 'library'
        verbose_name_plural = 'Libraries'


class Author(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_birth_year = models.DateField()
    
    def __str__(self):
        return self.author_name
    
    class Meta:
        db_table = 'author'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=300)
    date_published = models.DateField()
    
    def __str__(self):
        return self.book_name
    
    class Meta:
        db_table = 'book'


class Member(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    member_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_year = models.DateField()
    
    def __str__(self):
        return self.member_name
    
    class Meta:
        db_table = 'member'
