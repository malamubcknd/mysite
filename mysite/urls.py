"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("", admin.site.urls)
]













"""
CODE EXPLAINED
The code you provided is part of Django's URL configuration, specifically the urlpatterns list. 
It defines how URLs (Uniform Resource Locators) in your Django web application map to views and other 
parts of your application. Let's break down the code:

    Import Statements:

        from django.contrib import admin: This line imports the Django admin module, which allows you to 
        set up and customize the admin interface for managing your application's data.

        from django.urls import include, path: This line imports the include and path functions from 
        Django's URL handling framework. include is used to include other URL patterns from other apps, 
        and path is used to define URL patterns.

    URL Patterns:
        urlpatterns = []: This is a Python list that will contain the URL patterns for your application.

    path Function:

        path("polls/", include("polls.urls")),: This line defines a URL pattern. It specifies that when 
        a user visits a URL like "yourwebsite.com/polls/", Django should include the URL patterns defined
          in the "polls.urls" module.

        polls.urls refers to a Python module within your Django project (likely in the "polls" app) that 
        contains URL patterns specific to the "polls" feature of your application.

        The include function allows you to "include" the URL patterns from another module, which is a 
        common way to organize and modularize your URL patterns.

    Admin URL:

        path("admin/", admin.site.urls),: This line defines a URL pattern for the Django admin interface. 
        When a user visits a URL like "yourwebsite.com/admin/", Django will direct them to the admin site.

        admin.site.urls specifies the URL patterns for the Django admin site.
"""