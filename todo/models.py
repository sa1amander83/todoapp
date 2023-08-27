from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# class Profile(models.Model):
#     class Meta:
#         verbose_name = 'пользователь'
#         verbose_name_plural = "пользователи"
#
#     # USERNAME_FIELD = 'user'
#     # GENDER = [
#     #     ('м', "м"), ("ж", "ж")
#     # ]
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
#
#     # runner_age = models.PositiveIntegerField(verbose_name='возраст')
#     # runner_gender = models.CharField(max_length=1, choices=GENDER, verbose_name='пол участника', default='м')
#
#     # is_admin = models.BooleanField(verbose_name='Участник МыZaБег', default=False, null=True)
#
#     def __str__(self):
#         return str(self.user)


class TodoModel(models.Model):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    todo_user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_short_description = models.CharField(max_length=300, verbose_name='Введите краткое описание задачи')
    todo_full_description = models.CharField(max_length=300, verbose_name='Полное описание задачи')
    todo_date_created = models.DateField(verbose_name="Дата создания задачи", auto_now_add=True)
    todo_start_date = models.DateField(verbose_name='Дата начала задачи')
    todo_start_time = models.TimeField(verbose_name='Время начала задачи')
    todo_status = models.BooleanField(verbose_name="Статус выполнения задачи", default=False)

    def __str__(self):
        return str(self.todo_user)