from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def validate_even(value):
    if value <= 18:
        raise ValidationError(
            _('%(value)s Сотрудник должен быть совершеннолетним'),
            params={'value': value},
)   

class Employer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=25)
    surname = models.CharField(verbose_name='Фамилия', max_length=25)
    age = models.IntegerField(verbose_name='Возраст', validators=[validate_even])
    salary = models.FloatField(verbose_name='Зарплата')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Tasks(models.Model):
    title = models.CharField(verbose_name='Задача', max_length=25)
    description = models.TextField(verbose_name='Описание задачи')
    deadline = models.DateTimeField(verbose_name='Дедлайн задачи')
    employer = models.ManyToManyField(Employer,verbose_name='Сотрудник')
    progress = models.CharField(verbose_name='Статус задачи', max_length=30)

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Group(models.Model):
    group_name = models.CharField(verbose_name='Задача', max_length=25)
    leader = models.ManyToManyField(Employer,verbose_name='Тимлид')
    task = models.ManyToManyField(Tasks,verbose_name='Задача группы')

    history = HistoricalRecords()

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'