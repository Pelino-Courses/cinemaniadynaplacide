from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class User_manager(BaseUserManager):
    def create_user(self, username, email, firstname, lastname, age, password, profile_pic=None, gender=None, registration_date=None):
        email = self.normalize_email(email)
        user = self.model(username=username, registration_date=registration_date, firstname=firstname,
                          lastname=lastname, email=email, age=age, profile_pic=profile_pic, password=password, gender=gender)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, age, password, firstname, lastname, gender, profile_pic=None, registration_date=None):
        user = self.create_user(username=username, age=age, email=email,
                                firstname=firstname, lastname=lastname, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    registration_date = models.DateField(auto_now=True)
    profile_pic = models.ImageField(
        default="profile.png", upload_to="images/")
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=32, unique=True)
    gender_choices = [("Male", "Male"), ("Female", "Female")]
    gender = models.CharField(choices=gender_choices,
                              default="Male", max_length=6, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["username", "firstname",
                       "lastname", "age", "gender", "profile_pic"]
    USERNAME_FIELD = "email"
    objects = User_manager()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
# Create your models here.


class Movie(models.Model):
    movie_title = models.CharField(max_length=250)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    main_actor = models.CharField(max_length=250)
    genre_choices = [("Action", "Action"), ("Comedy", "Comedy"), ("Romatic",
                                                                  "Romantic"), ("Adventure", "Adventure"), ("Horror", "Horror"),("Scientific Fictions","Scientific Fictions")]
    genre = models.CharField(choices=genre_choices, max_length=250)
    caption = models.CharField(max_length=200)
    movie_link = models.CharField(max_length=200)
    trailler = models.FileField(upload_to="movies/%y")
    posted = models.CharField(max_length=200)
    wallpaper = models.ImageField(default="wall.jpg", upload_to="images/movie_walls/")

    def __str__(self):
        return self.movie_title
