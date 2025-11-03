from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    image_src = models.CharField(max_length=200)  # chemin de l'image
    description = models.TextField()
    skills = models.JSONField()  # pour stocker la liste ["React", "Express", ...]
    demo = models.URLField(blank=True, null=True)
    source = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Skills(models.Model):
    category = models.CharField(max_length=100, default="Autres")  # valeur par défaut
    title = models.CharField(max_length=100)
    image_src = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category} - {self.title}"


from django.db import models

class History(models.Model):
    role = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)  # ex: "Jul, 2024"
    end_date = models.CharField(max_length=50)    # ex: "Aug, 2024"
    experiences = models.JSONField()               # liste de strings
    image_src = models.CharField(max_length=200)  # chemin de l'image

    def __str__(self):
        return f"{self.role} at {self.organisation}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"