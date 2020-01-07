from django.db import models


class Owner(models.Model):
    name = models.TextField()


class Code(models.Model):
    ISBN = models.CharField(max_length=10)


class Book(models.Model):
    title = models.TextField("Title")
    code = models.OneToOneField("Book Code", Code)
    owner = models.ForeignKey("Owner", Owner, null=True,)
    author = models.ForeignKey("Author", Owner, on_delete=None, blank=True)
    coocoo = models.ForeignKey(
        "Coocoo",
        Owner,
        null=True,
        blank=True,
        verbose_name="A really long and boring string or some sort",
        related_name="coocoo_coocoo",
    )
