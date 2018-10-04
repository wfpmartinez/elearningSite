from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

'''
* Curso
Estudiante -> Curso (estudiante se registra a un curso)
* Asignación -> Curso (varias asignaciones son creadas en un curso, pueden ser tareas, trabajos, exámenes, etc.)
RespuestaAsignacion -> Asignación, Estudiante, Calificación
Comments -> RespuestaAsignacion
'''

# Define custom user types, in this case we will have only students and teachers
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

# Define user types
# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)

# Course is created by a teacher
class Course(models.Model):
    course_name = models.CharField('Nombre del Curso', max_length=200)
    pub_date = models.DateTimeField('Fecha Apertura')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

# Assignments are related to a course
# these can be of different types, such as, indidivual tasks,
# groupal works and exams
class Assignment(models.Model):
    ASSIGNMENT_TYPE_CHOICES = (
        (1, 'Tarea'),
        (2, 'Trabajo en Grupo'),
        (3, 'Examen')
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_name = models.CharField('Asignación', max_length=200)
    assignament_description = models.CharField ('Descripción de la Asignación', max_length=1000)
    assignment_type = models.PositiveSmallIntegerField('Tipo de Asignación',choices=ASSIGNMENT_TYPE_CHOICES)
    spec_document_url = models.URLField('Documento Adjunto', max_length=1000)
    deadline_date = models.DateTimeField('Fecha de Entrega')
    pub_date = models.DateTimeField('Fecha de Publicación')
    is_active = models.BooleanField('Activo')

    def __str__(self):
        return self.assignment_name

    class Meta:
        verbose_name = _('Asignación')
        verbose_name_plural = _('Asignaciones')
#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     Courses = models.ManyToManyField(Course, through='StudentCourse')
#     student_name = models.CharField()




'''
class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=1000)
    correct = models.BooleanField()

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        unique_together = ('question', 'user', )

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')
'''
