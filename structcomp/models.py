from django.core.exceptions import ValidationError
from django.db import models
from datetime import date, datetime, timezone
import datetime

class Employee(models.Model):
    LEVELS = [
        ('DEPARTMENT_1', (
            ('DEP1_1', '1'),
            ('DEP1_2', '2'),
            ('DEP1_3', '3'),
            ('DEP1_4', '4'),
            ('DEP1_5', '5'),
        )
        ),
        ('DEPARTMENT_2', (
            ('DEP2_1', '1'),
            ('DEP2_2', '2'),
            ('DEP2_3', '3'),
            ('DEP2_4', '4'),
            ('DEP2_5', '5'),
        )
        ),
        ('DEPARTMENT_3', (
            ('DEP3_1', '1'),
            ('DEP3_2', '2'),
            ('DEP3_3', '3'),
            ('DEP3_4', '4'),
            ('DEP3_5', '5'),
        )
        ),
        ('DEPARTMENT_4', (
            ('DEP4_1', '1'),
            ('DEP4_2', '2'),
            ('DEP4_3', '3'),
            ('DEP4_4', '4'),
            ('DEP4_5', '5'),
        )
        ),
        ('DEPARTMENT_5', (
            ('DEP5_1', '1'),
            ('DEP5_2', '2'),
            ('DEP5_3', '3'),
            ('DEP5_4', '4'),
            ('DEP5_5', '5'),
        )
        ),
        ('DEPARTMENT_6', (
            ('DEP6_1', '1'),
            ('DEP6_2', '2'),
            ('DEP6_3', '3'),
            ('DEP6_4', '4'),
            ('DEP6_5', '5'),
        )
        ),
        ('DEPARTMENT_7', (
            ('DEP7_1', '1'),
            ('DEP7_2', '2'),
            ('DEP7_3', '3'),
            ('DEP7_4', '4'),
            ('DEP7_5', '5'),
        )
        ),
        ('DEPARTMENT_8', (
            ('DEP8_1', '1'),
            ('DEP8_2', '2'),
            ('DEP8_3', '3'),
            ('DEP8_4', '4'),
            ('DEP8_5', '5'),
        )
        ),
        ('DEPARTMENT_9', (
            ('DEP9_1', '1'),
            ('DEP9_2', '2'),
            ('DEP9_3', '3'),
            ('DEP9_4', '4'),
            ('DEP9_5', '5'),
        )
        ),
        ('DEPARTMENT_10', (
            ('DEP10_1', '1'),
            ('DEP10_2', '2'),
            ('DEP10_3', '3'),
            ('DEP10_4', '4'),
            ('DEP10_5', '5'),
        )
        ),
        ('DEPARTMENT_11', (
            ('DEP11_1', '1'),
            ('DEP11_2', '2'),
            ('DEP11_3', '3'),
            ('DEP11_4', '4'),
            ('DEP11_5', '5'),
        )
        ),
        ('DEPARTMENT_12', (
            ('DEP12_1', '1'),
            ('DEP12_2', '2'),
            ('DEP12_3', '3'),
            ('DEP12_4', '4'),
            ('DEP12_5', '5'),
        )
        ),
        ('DEPARTMENT_13', (
            ('DEP13_1', '1'),
            ('DEP13_2', '2'),
            ('DEP13_3', '3'),
            ('DEP13_4', '4'),
            ('DEP13_5', '5'),
        )
        ),
        ('DEPARTMENT_14', (
            ('DEP14_1', '1'),
            ('DEP14_2', '2'),
            ('DEP14_3', '3'),
            ('DEP14_4', '4'),
            ('DEP14_5', '5'),
        )
        ),
        ('DEPARTMENT_15', (
            ('DEP15_1', '1'),
            ('DEP15_2', '2'),
            ('DEP15_3', '3'),
            ('DEP15_4', '4'),
            ('DEP15_5', '5'),
        )
        ),
        ('DEPARTMENT_16', (
            ('DEP16_1', '1'),
            ('DEP16_2', '2'),
            ('DEP16_3', '3'),
            ('DEP16_4', '4'),
            ('DEP16_5', '5'),
        )
        ),
        ('DEPARTMENT_17', (
            ('DEP17_1', '1'),
            ('DEP17_2', '2'),
            ('DEP17_3', '3'),
            ('DEP17_4', '4'),
            ('DEP17_5', '5'),
        )
        ),
        
        ('DEPARTMENT_18', (
            ('DEP18_1', '1'),
            ('DEP18_2', '2'),
            ('DEP18_3', '3'),
            ('DEP18_4', '4'),
            ('DEP18_5', '5'),
        )
        ),
        ('DEPARTMENT_19', (
            ('DEP19_1', '1'),
            ('DEP19_2', '2'),
            ('DEP19_3', '3'),
            ('DEP19_4', '4'),
            ('DEP19_5', '5'),
        )
        ),
        ('DEPARTMENT_20', (
            ('DEP20_1', '1'),
            ('DEP20_2', '2'),
            ('DEP20_3', '3'),
            ('DEP20_4', '4'),
            ('DEP20_5', '5'),
        )
        ),
        ('DEPARTMENT_21', (
            ('DEP21_1', '1'),
            ('DEP21_2', '2'),
            ('DEP21_3', '3'),
            ('DEP21_4', '4'),
            ('DEP21_5', '5'),
        )
        ),
        ('DEPARTMENT_22', (
            ('DEP22_1', '1'),
            ('DEP22_2', '2'),
            ('DEP22_3', '3'),
            ('DEP22_4', '4'),
            ('DEP22_5', '5'),
        )
        ),
        ('DEPARTMENT_23', (
            ('DEP23_1', '1'),
            ('DEP23_2', '2'),
            ('DEP23_3', '3'),
            ('DEP23_4', '4'),
            ('DEP23_5', '5'),
        )
        ),
        ('DEPARTMENT_24', (
            ('DEP24_1', '1'),
            ('DEP24_2', '2'),
            ('DEP24_3', '3'),
            ('DEP24_4', '4'),
            ('DEP24_5', '5'),
        )
        ),
        ('DEPARTMENT_25', (
            ('DEP25_1', '1'),
            ('DEP25_2', '2'),
            ('DEP25_3', '3'),
            ('DEP25_4', '4'),
            ('DEP25_5', '5'),
        )
        ),
    ]
    
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date_acceptance = models.DateField()
    salary = models.IntegerField()
    department = models.CharField(max_length=20, choices=LEVELS)
    
    def __str__(self):
        return self.full_name
    
    # проверка на валидность даты приема на работу
    
    def save(self, *args, **kwargs): 
        if self.date_acceptance > date.today():
            raise ValidationError('Wrong date')
        super(Employee, self).save(*args, **kwargs)
        

    
    
# Create your models here.
