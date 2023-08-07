# Djangomywebapp

## คำสั่ง runserver 
    python manage.py runserver 
![คำสั่งrunserverเพื่อใช้งาน](https://cdn.discordapp.com/attachments/720477706621419590/1138136295714066554/Screenshot_2023-08-07_224553.png)

## คำสั่ง สร้างแอพ
    python manage.py startapp <ชื่อแอพ>

## คำสั่งสร้าง admin 
    python manage.py createsuperuser
![สร้างadmin](https://cdn.discordapp.com/attachments/720477706621419590/1138131329523912836/Screenshot_2023-08-07_210918.png)

    การเข้าadminที่สร้างใว้
![สร้างข้อมูล](https://cdn.discordapp.com/attachments/720477706621419590/1138134734015303761/Screenshot_2023-08-07_211256.png)

## สร้าง models
```from django.db import models

# Create your models here.

PREFIX = (
    (1, "นาย"),
    (2, "นางสาว"),
    (3, "นาง")
)


class Student(models.Model):
    
    prefix = models.IntegerField(choices=PREFIX)
    
    std_id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    
    phone = models.CharField(max_length=10)
    


```python
from django.db import models

# Create your models here.

class Student(models.Model):
    
    std_id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    
    phone = models.CharField(max_length=10)

```

## Admin register models
```python

@admin.register(models.Student)
class StudentAdmin(Admin.ModelAdmin):
    list_display = (

    )


```
สวัสดีครับ ผม นายอนุชา กัญญา โปรเจคชิ้นนี้เพื่อการศึกษาผมมีความตั้งใจว่าจะทำให้ดีที่สุด

