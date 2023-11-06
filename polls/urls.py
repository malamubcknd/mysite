from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]




























"""The code you provided is a part of Django's URL configuration, particularly for the "polls" app, and 
it defines URL patterns that map to views within your Django project. Let's break down this code:

    Import Statements:

        from django.urls import path: This line imports the path function from Django's URL handling 
        framework, which is used to define URL patterns.

        from . import views: This line imports the views module from the current directory (package) 
        of your Django app. These views contain the functions that will be called when the associated 
        URLs are accessed.

    Namespace:
        app_name = "polls": This line sets the namespace for the "polls" app. Namespacing helps avoid 
        naming conflicts between apps in a Django project. It allows you to reference views and templates
          specific to the "polls" app using the namespace.

    URL Patterns:
        urlpatterns = []: This is a Python list that will contain the URL patterns for the "polls" app.

    URL Patterns with path:

        path("", views.IndexView.as_view(), name="index"): This line defines a URL pattern that matches 
        the root URL of the "polls" app (e.g., "/polls/"). When this URL is accessed, it associates it 
        with the IndexView class-based view. The name parameter provides a unique identifier for this 
        URL pattern.

        path("<int:pk>/", views.DetailView.as_view(), name="detail"): This line defines a URL pattern 
        that matches URLs with an integer parameter (referred to as pk for primary key). For example, 
        it matches URLs like "/polls/1/", "/polls/2/", and so on. It associates these URLs with the 
        DetailView class-based view and provides the name "detail" for reference.

        path("<int:pk>/results/", views.ResultsView.as_view(), name="results"): Similar to the previous 
        pattern, this line defines a pattern that matches URLs with an integer parameter and the 
        "/results/" suffix. For example, it matches URLs like "/polls/1/results/", "/polls/2/results/", 
        and associates them with the ResultsView view.

        path("<int:question_id>/vote/", views.vote, name="vote"): This line defines a pattern that 
        matches URLs with an integer parameter and the "/vote/" suffix. It associates these URLs with 
        the vote view function (a regular function, not a class-based view).

In summary, this code sets up URL patterns for the "polls" app in your Django project. It maps 
different URLs to specific views, both class-based views and a function-based view. The name parameter 
in each URL pattern provides a unique identifier that can be used in your templates or in your code to 
reference these URLs. The use of angle brackets (<int:pk> and <int:question_id>) indicates URL 
parameters, allowing you to capture values from the URL and pass them to your views."""