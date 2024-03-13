import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import WorkoutPlan


class WorkoutPlanTests(APITestCase):
    def setUp(self):
        # Create a user and workout plan
        self.user = get_user_model().objects.create(
            email='testuser@email.com', password='password'
        )
        self.client.force_authenticate(self.user)

        self.workout_plan = WorkoutPlan.objects.create(
            user=self.user,
            goal='WL',
            frequency_per_week=1,
            exercise_types='GE',
            session_duration=datetime.timedelta(minutes=90)
        )

    def test_list_workout_plans(self):
        url = reverse('workout_plan-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_workout_plans(self):
        url = reverse('workout_plan-detail',
                      kwargs={"pk": self.workout_plan.pk})
        response = self.client.get(url).data
        self.assertEqual(response['goal'], "WL")
        self.assertEqual(response['frequency_per_week'], 1)
        self.assertEqual(response['exercise_types'], "GE")
        self.assertEqual(response['session_duration'], "01:30:00")

    def test_update_workout_plan(self):
        url = reverse('workout_plan-detail',
                      kwargs={'pk': self.workout_plan.pk})
        data = {
            'user': self.user,
            'goal': 'MG',
            'frequency_per_week': 2,
            'exercise_types': 'GE',
            'session_duration': datetime.timedelta(minutes=90)
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['goal'], 'MG')
        self.assertEqual(response.data['exercise_types'], 'GE')
        self.assertEqual(response.data['frequency_per_week'], 2)

    def test_delete_workout_plan(self):
        url = reverse('workout_plan-detail',
                      kwargs={'pk': self.workout_plan.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(WorkoutPlan.objects.count(), 0)




