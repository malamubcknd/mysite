from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)







"""The code you provided is related to customizing the Django admin interface for managing the models 
Question and Choice in a polling application. It uses the Django admin site to define how these models 
are displayed and managed within the admin interface. Let's break down the code step by step:

    Import Statement: The code starts by importing the admin module from Django. This module provides 
    classes and functions for customizing the Django admin interface.

    QuestionAdmin Class: A custom admin class named QuestionAdmin is defined for the Question model. 
    This class inherits from admin.ModelAdmin and is used to customize the admin interface for the 
    Question model.
        fieldsets: This attribute defines how the fields of the Question model are grouped in the 
        admin interface. It specifies two groups: "None" and "Date information." The "fields" list 
        within each group determines which model fields are displayed in that group.

    admin.site.register(Question, QuestionAdmin): This line registers the Question model with the 
    custom QuestionAdmin class, which means that the Question model will be managed through the custom
      admin interface defined in QuestionAdmin.

    ChoiceInline Class: This class defines an inline editing interface for the Choice model, which 
    allows choices to be managed within the context of a Question model. It inherits from 
    admin.TabularInline, which displays the choices in a tabular format.
        model: Specifies the related model, which is Choice in this case.
        extra: Sets the number of empty choice forms to be displayed for adding new choices. 
        In this case, it's set to 3.

    QuestionAdmin Class (Revisited): This part of the code appears to redefine the QuestionAdmin class. 
    It includes the fieldsets attribute as before, but it also makes several additions and 
    customizations:

        inlines: This attribute specifies that the ChoiceInline class should be used as an inline 
        interface for managing choices within questions.

        list_display: Determines what fields are displayed in the list view of the admin interface 
        for the Question model. It includes "question_text," "pub_date," and "was_published_recently" 
        as columns in the list view.

        list_filter: This attribute enables filtering by the "pub_date" field in the admin list view.

        search_fields: Allows searching for questions based on the "question_text" field.

    admin.site.register(Question, QuestionAdmin) (Revisited): This line re-registers the Question model 
    with the updated QuestionAdmin class. It applies the customizations made to the admin interface for 
    the Question model.

In summary, this code customizes the Django admin interface for the Question and Choice models. 
It defines custom admin classes, field groupings, and inline editing for related models to provide 
a more user-friendly and organized admin interface for managing poll questions and choices. The Question 
model's fields and list view display are adjusted to include additional information like publication 
date and whether the question was published recently.
"""