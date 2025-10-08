from django.db import models

# Create your models here.

class Users(models.Model):
    full_name = models.CharField('Полное имя', max_length=100)
    mail = models.EmailField('Email', unique=True)
    password = models.CharField('Пароль', max_length=50)
    registration_date = models.DateField('Дата регистрации', auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name

class Sellers(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    login = models.CharField('Логин', max_length=50, unique=True)
    email = models.EmailField('Почта')
    phone_number = models.CharField('Номер телефона', max_length=15)
    rating = models.DecimalField('Рейтинг', max_digits=3, decimal_places=2, default=0.0)
    registration_date = models.DateField('Дата регистрации', auto_now_add=True)

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.login

class Games(models.Model):
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE, verbose_name='Продавец')
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    genre = models.CharField('Жанр', max_length=100)
    release_date = models.DateField('Дата выхода')
    platform = models.CharField('Платформа', max_length=50)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.title

class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    game = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name='Игра')
    rating = models.IntegerField('Рейтинг')
    comment = models.TextField('Комментарий')
    review_date = models.DateField('Дата отзыва', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв от {self.user.full_name}"


class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField('Статус', max_length=20)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ #{self.id}"

class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ')
    game = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name='Игра')
    quantity = models.IntegerField('Количество', default=1)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return f"Позиция заказа #{self.order.id}"