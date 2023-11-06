from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.urls import reverse
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Question
from .models import Choice

from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    






    """The code you provided is a set of Django views for a "polls" application. These views define 
    how different URLs in your Django web application should be handled. Let's break down this code 
    and explain each part:

    Imports:

        from django.shortcuts import render: This imports the render function, which is used to 
        render HTML templates with context data and return HTTP responses.In summary, the render 
        function in Django is a powerful tool for generating web pages. It combines an HTML template,
        context data, and an HTTP response into a single function call, making it easier to create 
        dynamic and user-friendly web applications. It simplifies the process of rendering web pages, 
        allowing developers to focus on the content and functionality of their application rather than 
        manual HTML generation

        from django.shortcuts import get_object_or_404: This imports the get_object_or_404 function,
          which is used to retrieve an object from the database or raise a 404 error if the object 
          does not exist.

        from django.urls import reverse: This imports the reverse function, which is used to generate 
        URLs based on their view names.

        from django.views import generic: This imports Django's generic views, which provide commonly 
        used patterns for displaying lists of objects, detail views, etc.

        from django.http import HttpResponse and from django.http import HttpResponseRedirect: 
        These import classes for constructing HTTP responses.

        from .models import Question and from .models import Choice: These import the Question and 
        Choice models from the current app's models module.

        from django.utils import timezone: This imports the timezone module from Django's utilities.

    IndexView:
        IndexView is a class-based view derived from generic.ListView. It's responsible for displaying
          a list of the latest published questions. It sets the template to "polls/index.html" and 
          defines the context object name as "latest_question_list." It overrides the get_queryset 
          method to filter and return the last five published questions.

    DetailView:
        DetailView is a class-based view derived from generic.DetailView. It's used to display the 
        details of a specific question. It sets the model to Question, the template to 
        "polls/detail.html," and filters out questions that aren't published yet.

    ResultsView:
        ResultsView is another class-based view derived from generic.DetailView. It's used to display 
        the results of a specific question and sets the template to "polls/results.html."

    vote:
        vote is a function-based view. It handles the logic for processing user votes on a particular 
        question. It first retrieves the question using get_object_or_404, then checks if the selected 
        choice is valid and increments the choice's vote count. It finally redirects the user to the 
        results view for that question.

This code is part of a Django web application for managing and displaying poll questions and their 
choices. It demonstrates the use of class-based views for displaying lists and details of objects and 
a function-based view for handling user interactions and form submissions. Additionally, it leverages 
Django's utilities and generic views to simplify common view patterns.
"""