from django.contrib.auth.models import User
from django.db import models
from solve.calculator import solve


class Session(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)

    def __unicode__(self):
        return u"Session: %s - %s - %s" % (self.id, self.name, self.user)


class Equation(models.Model):
    session = models.ForeignKey(Session)
    equation = models.TextField()
    result = models.CharField(max_length=512, editable=False)
    valid = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.equation

    def save(self, *args, **kwargs):
        # create session if needed
        session = Session.objects.create(name="")
        self.session = session
        # Calculate result
        try:
            self.result = solve(self.equation)
        except Exception as e:
            self.valid = False
            self.result = e
        return super(Equation, self).save(*args, **kwargs)