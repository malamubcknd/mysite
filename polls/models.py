# Create your models here.
from django.db import models
import datetime
from datetime import timedelta
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
        )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    





"""
The code you provided defines Django models for a simple polling application. These models represent 
the structure of your database tables and provide a way to interact with the database. Here's an 
explanation of this code:

    Import Statements:

        from django.db import models: This imports the models module from Django, which provides the 
        necessary classes and functions for defining database models.

        import datetime: This imports the datetime module for working with dates and times.

        from datetime import timedelta: This imports the timedelta class from the datetime module. 
        timedelta is used for calculating date and time differences.

        from django.utils import timezone: This imports the timezone module from Django's utilities. 
        It's used for working with time zones and getting the current time.

        from django.contrib import admin: This imports the admin module from Django, which is used for
          customizing the Django admin interface.

    Question Model:

        Question is a Django model that represents a poll question. It has the following fields:
            question_text: A character field (text) with a maximum length of 200 characters to store 
            the text of the question.
            pub_date: A DateTimeField that represents the date and time when the question was published.

        __str__ Method: This method defines a human-readable representation of the Question model. 
        It returns the text of the question when the model instance is printed.

        was_published_recently Method: This method is a custom method added to the model using the
          @admin.display decorator. It checks if the question was published within the last day 
          (24 hours) and returns a boolean value. This method is used for customizing the display of 
          the question in the Django admin interface.

    Choice Model:

        Choice is a Django model that represents a choice for a poll question. It has the following 
        fields:
            question: A foreign key that establishes a relationship with the Question model, indicating 
            which question this choice belongs to.
            choice_text: A character field to store the text of the choice.
            votes: An integer field to store the number of votes received for the choice, with a 
            default value of 0.

        __str__ Method: This method defines a human-readable representation of the Choice model. It 
        returns the text of the choice when the model instance is printed.

These models define the structure of the database tables for your polling application. The Question
 model represents the questions, and the Choice model represents the choices associated with each 
 question. The was_published_recently method is a custom method used for displaying questions in the 
 Django admin interface, indicating if they were published recently.
"""