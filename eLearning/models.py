from django.db import models

'''
Curso
Estudiante -> Curso (estudiante se registra a un curso)
Asignación -> Curso (varias asignaciones son creadas en un grupo, pueden ser tareas, trabajos, exámenes, etc.)
RespuestaAsignacion -> Asignación, Estudiante
Comments -> RespuestaAsignacion
Calificación -> RespuestaAsignacion
'''
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha Apertura')

    def __str__(self):
        return self.course_name
