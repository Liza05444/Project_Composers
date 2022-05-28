from django.db import models
from django.urls import reverse
import uuid


class GenreModel(models.Model):
	name = models.CharField(max_length=30, help_text='Введите жанр музыкального произведения')
	definition = models.TextField(help_text='Введите определение жанра')
	history = models.TextField(help_text='Введите историю жанра', null=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('genre-detail', args=[str(self.id)])


class ComposerModel(models.Model):
	fio = models.CharField(max_length=50, help_text='Введите ФИО композитора')
	biography = models.TextField(help_text='Введите биографию композитора', null=True)
	date_of_birth = models.CharField(max_length=30, help_text='Введите дату рождения композитора')
	date_of_death = models.CharField(max_length=30, help_text='Введите дату смерти композитора', null=True)
	photo = models.TextField(help_text='Введите ссылку на фото композитора', null=True)

	class Meta:
		ordering = ['fio']

	def __str__(self):
		return self.fio

	def get_absolute_url(self):
		return reverse('composer-detail', args=[str(self.id)])


class CompositionModel(models.Model):
	composer = models.ForeignKey('ComposerModel', on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=65, help_text='Введите название музыкального произведения')
	description = models.TextField(help_text='Введите краткое описание произведения')
	first_night = models.CharField(max_length=30, help_text='Введите дату премьеры', null=True)
	genre = models.ForeignKey('GenreModel', on_delete=models.SET_NULL, null=True)
	audio = models.TextField(help_text='Введите ссылку на аудиозапись', null=True)
	description_of_audio = models.TextField(help_text='Описание аудиозаписи', null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('composition-detail', args=[str(self.id)])
