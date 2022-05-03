
from django.db import models

    

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    
    def __str__(self) -> str:
        return f'Категория: {self.title}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Катагерии'
        ordering = ['title']
        


        

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наимование')
    content = models.TextField(blank=True,verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикация')
    update_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='фото',blank=True)
    is_published = models.BooleanField(default=True,verbose_name='опубликовано')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,verbose_name='катигория')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']  
        
# class Category(models.Model):
#     title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    
#     def __str__(self):
#         return f'Категория: {self.title}'
    
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Катагерии'
#         ordering = ['title']
        
        


        
  
    
    
