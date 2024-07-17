from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category' 
        # название таблицы в базе данных
        verbose_name = 'Категорию' 
        # Альтернативное название таблицы (для админ панели)
        verbose_name_plural = 'Категории' # Для мн.ч. 

    def __str__(self) -> str:
        return self.name


class Products(models.Model): 
    # Наследование от базового класса позволяет производить CRUD операции
    # Взаимодейстовать с Django
    name = models.CharField(max_length=25, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='URL')
    descripton = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods.images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.name