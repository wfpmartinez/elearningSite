from django.db import models

'''
Curso
Estudiante -> Curso (estudiante se registra a un curso)
Asignación -> Curso (varias asignaciones son creadas en un curso, pueden ser tareas, trabajos, exámenes, etc.)
RespuestaAsignacion -> Asignación, Estudiante
Comments -> RespuestaAsignacion
Calificación -> RespuestaAsignacion
'''
class Course(models.Model):
    course_name = models.CharField('Nombre del Curso', max_length=200)
    pub_date = models.DateTimeField('Fecha Apertura')

    def __str__(self):
        return self.course_name

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


'''
class Section(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    test = models.TextField()

    class Meta:
        unique_together = ('course', 'number', )

    def __str__(self):
        return self.title

    def get_test_url(self):
        return reverse('do_test', args=(self.id,))

    def get_absolute_url(self):
        return reverse('do_test', args=(self.id,))

    def get_next_section_url(self):
        next_section = Section.objects.get(number=self.number+1)
        return reverse('do_section', args=(next_section.id,))


class Question(models.Model):
    section = models.ForeignKey(Section)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text


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

'''
