from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator

# Create your models here
class UserManager(BaseUserManager):

    def create_user(self, email, password, pronombre, curp, nombre,nombre_id, reg_id, bg):
        user = self.model(
            email=email,
            pronombre=pronombre,
            CURP=curp,
            nombre=nombre,
            nombre_id=nombre_id,
            reg_id=reg_id,
            bg=bg,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    
class Info_General(models.Model):
    nombre = models.CharField(max_length=70)
    ape_Pri = models.CharField(max_length=70)
    ape_Seg = models.CharField(max_length=70)
    genero = models.CharField(max_length=2)
    imagen = models.CharField(max_length=50)
    class Meta:
        db_table = 'Info_General'
        app_label = 'Usuarios'
        managed = False

    

class Usuario(AbstractBaseUser):
    email = models.EmailField(max_length=256, unique=True)
    pronombre = models.CharField(max_length=5)    
    CURP = models.CharField(max_length=18, unique=True)
    nombre_id = models.ForeignKey(Info_General, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    reg_id = models.ForeignKey('self', on_delete=models.CASCADE)
    BG = models.PositiveIntegerField(validators=[MaxValueValidator(13)],default=0)
    last_login = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['CURP', 'nombre_id', 'reg_id']

    objects = UserManager()

    def __str__(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'usuario'
        app_label = 'Usuarios'
        managed = False

