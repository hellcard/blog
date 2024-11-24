from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'name', db_index = True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        ordering = ['name']
        

class Projects(models.Model):
    title = models.CharField(max_length = 20, verbose_name = 'name of project', db_index = True)
    description = models.CharField(max_length = 30, verbose_name='description')
    url = models.URLField(verbose_name = 'url of project')
    
    category = models.ForeignKey(Category, null = True, on_delete = models.PROTECT, verbose_name = 'category')
    
    class Meta:
        verbose_name_plural = 'projects'
        verbose_name = 'project'
        ordering = ['title']