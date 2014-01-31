from django.db import models
from django.contrib.auth.models import User

# Create your models here.

        
class Card(models.Model):
    
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)  
    trainer = models.CharField(max_length=50, blank=True, null=True)  
    
    #Card status
    subscription = models.DateField(auto_now_add=True)
    card_expiration = models.DateField(blank=True, null=True)
    
    #Member account status
    account_expiration = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return u'%s %s' % (self.surname, self.name)
        
    class Meta:
        unique_together = (("number"),)

    @models.permalink
    def get_absolute_url(self):
        return ('lephysique.views.show_card', [str(self.number)])



class Exercise(models.Model):

    name = models.CharField(max_length=50)
    
    def __str__(self):
        return u'%s' % (self.name)
    
    class Meta:
        unique_together = (("name"),)


class Series(models.Model):

    number = models.IntegerField()
    
    def __str__(self):
        return u'%s' % (self.number)
        
    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'
        unique_together = (("number"),)
        

class Repetitions(models.Model):

    number = models.IntegerField()
    
    def __str__(self):
        return u'%s' % (self.number)
        
    class Meta:
        verbose_name = 'Repetition'
        verbose_name_plural = 'Repetitions'
        unique_together = (("number"),)
        

class Executions(models.Model):

    mode = models.CharField(max_length=50)
    
    def __str__(self):
        return u'%s' % (self.mode)
    
    class Meta:
        verbose_name = 'Execution'
        verbose_name_plural = 'Executions'
        unique_together = (("mode"),)
        

class Rest(models.Model):

    time = models.IntegerField()
    
    def __str__(self):
        return u'%s' % (self.time)

    class Meta:
        verbose_name = 'Rest'
        verbose_name_plural = 'Rest'
        unique_together = (("time"),)


class Exercise1(models.Model):

    card = models.ForeignKey(Card)
    exercise = models.ForeignKey(Exercise)
    series = models.ForeignKey(Series, blank=True, null=True)
    repetitions = models.ForeignKey(Repetitions, blank=True, null=True)
    executions = models.ForeignKey(Executions, blank=True, null=True)
    rest = models.ForeignKey(Rest, blank=True, null=True)

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Workout 1'

    def __str__(self):
        return u'%s' % (self.exercise) 

class Exercise2(models.Model):

    card = models.ForeignKey(Card)
    exercise = models.ForeignKey(Exercise)
    series = models.ForeignKey(Series, blank=True, null=True)
    repetitions = models.ForeignKey(Repetitions, blank=True, null=True)
    executions = models.ForeignKey(Executions, blank=True, null=True)
    rest = models.ForeignKey(Rest, blank=True, null=True)

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Workout 2'

    def __str__(self):
        return u'%s' % (self.exercise) 
        
        
class Exercise3(models.Model):

    card = models.ForeignKey(Card)
    exercise = models.ForeignKey(Exercise)
    series = models.ForeignKey(Series, blank=True, null=True)
    repetitions = models.ForeignKey(Repetitions, blank=True, null=True)
    executions = models.ForeignKey(Executions, blank=True, null=True)
    rest = models.ForeignKey(Rest, blank=True, null=True)

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Workout 3'

    def __str__(self):
        return u'%s' % (self.exercise) 
        
        
class Exercise4(models.Model):

    card = models.ForeignKey(Card)
    exercise = models.ForeignKey(Exercise)
    series = models.ForeignKey(Series, blank=True, null=True)
    repetitions = models.ForeignKey(Repetitions, blank=True, null=True)
    executions = models.ForeignKey(Executions, blank=True, null=True)
    rest = models.ForeignKey(Rest, blank=True, null=True)

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Workout 4'

    def __str__(self):
        return u'%s' % (self.exercise) 
        
        
class Exercise5(models.Model):

    card = models.ForeignKey(Card)
    exercise = models.ForeignKey(Exercise)
    series = models.ForeignKey(Series, blank=True, null=True)
    repetitions = models.ForeignKey(Repetitions, blank=True, null=True)
    executions = models.ForeignKey(Executions, blank=True, null=True)
    rest = models.ForeignKey(Rest, blank=True, null=True)

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Workout 5'

    def __str__(self):
        return u'%s' % (self.exercise) 