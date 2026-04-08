from django.db import models


class Master(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject


class Mentor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='mentors'
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

 
class Group(models.Model):
    title = models.CharField(max_length=100)
    mentor = models.ForeignKey(
        Mentor,
        on_delete=models.CASCADE,
        related_name='groups'
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname or ''}".strip()



