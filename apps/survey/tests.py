from rest_framework import status
from rest_framework.test import APITestCase

from apps.survey.models import Survey, Question, Choice, Answer, View, Like
from apps.user.models import User


class SurveyTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/survey/'
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True)
        self.data = {
            'survey_name': 'test',
            'user': self.user,
        }

        self.survey = Survey.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_survey(self):
        """Survey creation testing """
        data = {
            'survey_name': 'test1',
            'user': self.user.pk,
        }
        response = self.client.post(f'{self.url}add_survey/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Survey.objects.all().count(), 2)

    def test_2_list_survey(self):
        """Survey list testing """
        response = self.client.get(f'{self.url}surveys/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.survey.pk, 'question_count': 0, 'questions': [], 'likes': 0, 'survey_name': 'test',
              'description': None,
              'user': self.user.pk}]
        )

    def test_3_retrieve_survey(self):
        """Survey retrieve testing """

        response = self.client.get(f'{self.url}surveys/{self.survey.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.survey.pk, 'question_count': 0, 'questions': [], 'likes': 0, 'survey_name': 'test',
             'description': None,
             'user': self.user.pk}
        )

    def test_4_update_survey(self):
        """Survey update testing """
        data = {
            'survey_name': 'test1'
        }

        response = self.client.put(f'{self.url}surveys/update/{self.survey.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.survey.pk, 'question_count': 0, 'questions': [], 'likes': 0, 'survey_name': 'test1',
             'description': None,
             'user': self.user.pk}
        )

    def test_5_update_partial_survey(self):
        """Survey partial update testing """
        data = {
            'survey_name': 'test1'
        }
        response = self.client.patch(f'{self.url}surveys/update/{self.survey.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.survey.pk, 'question_count': 0, 'questions': [], 'likes': 0, 'survey_name': 'test1',
             'description': None,
             'user': self.user.pk}
        )

    def test_6_destroy_survey(self):
        """Survey destroying testing """
        response = self.client.delete(f'{self.url}surveys/delete/{self.survey.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Survey.objects.all().exists())

    def test_7_str_survey(self):
        """Survey str method testing"""
        self.assertEqual(str(self.survey), f'{self.survey.survey_name} by {self.user}')


class QuestionTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/survey/'
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True)
        self.survey = Survey.objects.create(survey_name='test', user=self.user)
        self.data = {
            'survey': self.survey,
            'text': 'test',
        }
        self.question = Question.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_question(self):
        """Question creation testing """
        data = {
            'survey': self.survey.pk,
            'text': 'test',
        }
        response = self.client.post(f'{self.url}add_question/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Question.objects.all().count(), 2)

    def test_2_list_question(self):
        """Question list testing """
        response = self.client.get(f'{self.url}questions/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.question.pk, 'choices': [], 'text': 'test', 'survey': self.survey.pk}]
        )

    def test_3_retrieve_question(self):
        """Question retrieve testing """

        response = self.client.get(f'{self.url}questions/{self.question.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.question.pk, 'choices': [], 'text': 'test', 'survey': self.survey.pk}
        )

    def test_4_update_question(self):
        """Question update testing """
        data = {
            'survey': self.survey.pk,
            'text': 'test1',
        }

        response = self.client.put(f'{self.url}questions/update/{self.question.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.question.pk, 'choices': [], 'text': 'test1', 'survey': self.survey.pk}
        )

    def test_5_update_partial_question(self):
        """Question partial update testing """
        data = {
            'text': 'test1'
        }
        response = self.client.patch(f'{self.url}questions/update/{self.question.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.question.pk, 'choices': [], 'text': 'test1', 'survey': self.survey.pk}
        )

    def test_6_destroy_question(self):
        """Question destroying testing """
        response = self.client.delete(f'{self.url}questions/delete/{self.question.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Question.objects.all().exists())

    def test_7_str_question(self):
        """Question str method testing"""
        self.assertEqual(str(self.question), self.question.text)


class ChoiceTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/survey/'
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True)
        self.survey = Survey.objects.create(survey_name='test', user=self.user)
        self.question = Question.objects.create(survey=self.survey, text='test')
        self.data = {
            'question': self.question,
            'text': 'test',
        }
        self.choice = Choice.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_choice(self):
        """Choice creation testing """
        data = {
            'question': self.question.pk,
            'text': 'test',
        }
        response = self.client.post(f'{self.url}add_choice/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Choice.objects.all().count(), 2)

    def test_2_destroy_choice(self):
        """Choice destroying testing """
        response = self.client.delete(f'{self.url}choice/delete/{self.choice.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Choice.objects.all().exists())

    def test_3_str_choice(self):
        """Choice str method testing"""
        self.assertEqual(str(self.choice), self.choice.text)


class AnswerTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/survey/'
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True)
        self.survey = Survey.objects.create(survey_name='test', user=self.user)
        self.question = Question.objects.create(survey=self.survey, text='test')
        self.choice = Choice.objects.create(question=self.question, text='test')
        self.data = {
            'user': self.user,
            'question': self.question,
            'choice': self.choice,
        }
        self.answer = Answer.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_answer(self):
        """Answer creation testing """
        data = {
            'user': self.user.pk,
            'question': self.question.pk,
            'choice': self.choice.pk,
        }
        response = self.client.post(f'{self.url}add_answer/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Answer.objects.all().count(), 2)

    def test_2_destroy_answer(self):
        """Answer destroying testing """
        response = self.client.delete(f'{self.url}answer/delete/{self.answer.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Answer.objects.all().exists())

    def test_3_str_answer(self):
        """Answer str method testing"""
        self.assertEqual(str(self.answer), f'User answer to question {self.answer.question}')


class ViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/survey/'
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True)
        self.survey = Survey.objects.create(survey_name='test', user=self.user)
        self.data = {
            'user': self.user,
            'survey': self.survey,
        }
        self.view = View.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_view(self):
        """View creation testing """
        data = {
            'user': self.user.pk,
            'survey': self.survey.pk,
        }
        response = self.client.post(f'{self.url}add_view/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(View.objects.all().count(), 2)

    def test_2_list_view(self):
        """View list testing """
        response = self.client.get(f'{self.url}views/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.view.pk, 'user': self.user.pk, 'survey': self.survey.pk}]
        )

    def test_3_destroy_view(self):
        """View destroying testing """
        response = self.client.delete(f'{self.url}views/delete/{self.view.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(View.objects.all().exists())

    def test_4_str_view(self):
        """Question str method testing"""
        self.assertEqual(str(self.view), f'Views of {self.user}, survey: {self.survey}')


class LikeTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/survey/'
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True)
        self.survey = Survey.objects.create(survey_name='test', user=self.user)
        self.data = {
            'user': self.user,
            'survey': self.survey,
            'like': True,
        }
        self.like = Like.objects.create(**self.data)
        self.client.force_authenticate(user=self.user)

    def test_1_create_like(self):
        """Like creation testing """
        data = {
            'user': self.user.pk,
            'survey': self.survey.pk,
            'like': True,
        }
        response = self.client.post(f'{self.url}add_like/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Like.objects.all().count(), 2)

    def test_2_list_like(self):
        """Like list testing """
        response = self.client.get(f'{self.url}likes/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'id': self.like.pk, 'like': True, 'dislike': False, 'user': self.user.pk, 'survey': self.survey.pk}]
        )

    def test_3_update_like(self):
        """Like update testing """
        data = {
            'user': self.user.pk,
            'survey': self.survey.pk,
            'like': False,
            'dislike': True,
        }

        response = self.client.put(f'{self.url}likes/update/{self.like.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.like.pk, 'like': False, 'dislike': True, 'user': self.user.pk, 'survey': self.survey.pk}
        )

    def test_4_update_partial_like(self):
        """Like partial update testing """
        data = {
            'like': False,
            'dislike': True,
        }
        response = self.client.patch(f'{self.url}likes/update/{self.like.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'id': self.like.pk, 'like': False, 'dislike': True, 'user': self.user.pk, 'survey': self.survey.pk}
        )

    def test_5_destroy_like(self):
        """Like destroying testing """
        response = self.client.delete(f'{self.url}likes/delete/{self.like.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Like.objects.all().exists())

    def test_6_str_like(self):
        """Like str method testing"""
        self.assertEqual(str(self.like), f'Like of {self.user}, survey: {self.survey}')
