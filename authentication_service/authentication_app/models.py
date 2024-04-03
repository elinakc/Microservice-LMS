from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
#CustomManager for user creation and management

class CustomUserManager(BaseUserManager):
  #Method for creating normal user
  def create_user(self, username, email, password=None): 
    #When we set password=None, it means that create_user method can be called without specifying password
    if not email:
      raise ValueError("Email must be set")
    
    #The self.normalize_email(email) method is commonly used in Django user
    #models to ensure that email addresses are stored and processed in a consistent format
    email = self.normalize_email(email)
    
    user = self.model(username=username, email=email) #The line creates a new instance of the CustomUser model with the provided username and email values. 
    user.set_password(password) #It hashes the password
    user.save(using = self._db)
    return (user)
  
  #Method for creating superuser
  def create_superuser(self ,email,username, password=None):
    
    user = self.create_user(email= email, username=username, password=password)
    user.is_staff =True
    user.is_admin = True
    user.is_superuser = True
    user.save(using= self._db)
    return(user)
  
class CustomUser(AbstractBaseUser):
  email = models.EmailField(verbose_name= "email_address", max_length=33, unique=True)
  username = models.CharField(max_length=111)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  
  
  objects = CustomUserManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS =[ 'username']
  
  def __str__(self):
    return self.username 
  

  
  