from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

from django.urls import reverse


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)






        """The code you provided is a set of test cases for a Django application, specifically for 
        testing the behavior of models and views related to a polling application. These tests are 
        written using Django's built-in testing framework and follow the practice of writing unit tests
          to ensure the correctness of the application. Let's break down the code and its purpose:

    Import Statements:

        from django.test import TestCase: This imports the TestCase class, which is the base class for 
        writing test cases in Django.

        Additional import statements include modules and classes needed for testing, such as datetime, 
        timezone, models (Question), and URL reversing using reverse.

    QuestionModelTests Class:

        This class inherits from TestCase and is used to test the behavior of the Question model, 
        particularly the custom method was_published_recently().

        It includes three test methods, each testing different scenarios:
            test_was_published_recently_with_future_question: Verifies that was_published_recently() 
            returns False for a question with a future pub_date.
            test_was_published_recently_with_old_question: Checks that was_published_recently() returns 
            False for a question with a pub_date older than 1 day.
            test_was_published_recently_with_recent_question: Ensures that was_published_recently() 
            returns True for a question with a pub_date within the last day.

        These tests validate the behavior of the was_published_recently() method by creating Question 
        instances with different pub_date values and asserting the expected results.

    create_question Function:
        This function is used to create Question instances with specified text and an offset in days 
        from the current time. It returns a Question object with the specified characteristics.

    QuestionIndexViewTests Class:

        This class is used to test views associated with the "index" page for questions.

        It includes several test methods that verify different aspects of the view:
            test_no_questions: Checks if an appropriate message is displayed when no questions exist.
            test_past_question: Ensures that questions with a pub_date in the past are displayed on the 
            index page.
            test_future_question: Verifies that questions with a pub_date in the future are not 
            displayed on the index page.
            test_future_question_and_past_question: Tests that only past questions are displayed even
              when both past and future questions exist.
            test_two_past_questions: Verifies that the index page can display multiple past questions.

        These tests simulate various scenarios for the index view, such as the presence of no questions,
         past questions, and future questions. They use the create_question function to create Question
           instances for testing.

    QuestionDetailViewTests Class:

        This class tests views related to the "detail" page for a specific question.

        It includes two test methods:
            test_future_question: Ensures that the detail view of a question with a future pub_date 
            returns a 404 not found status.
            test_past_question: Verifies that the detail view of a question with a past pub_date 
            displays the question's text.

        These tests check how the detail view behaves for questions with different pub_date values, 
        both in the future and the past.

Overall, this code is part of a comprehensive test suite for a Django polling application. It helps 
ensure that the models and views behave as expected and handle various scenarios correctly. Running 
these tests is essential to verify the application's functionality and detect potential issues early 
in the development process.
"""