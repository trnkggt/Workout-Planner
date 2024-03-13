from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Exercise

User = get_user_model()

class ExerciseViewSetTestCaseCommonUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@email.com",
            password="password"
        )
        self.admin = User.objects.create(
            email="admin@email.com",
            password="password",
            is_staff=True,
            is_superuser=True
        )

        self.exercise1 = Exercise.objects.create(
            name="Test exercise 1",
            muscle_group="CH",
            equipment='BW',
            description="test exercise",
            instructions="test exercise instructions"
        )
        self.exercise2 = Exercise.objects.create(
            name="Test exercise 2",
            muscle_group="QD",
            equipment='BB',
            description="test exercise",
            instructions="test exercise instructions"
        )

    def test_user_content(self):
        self.assertEquals(self.user.email, "test@email.com")
        self.assertEqual(self.admin.email, "admin@email.com")

    def test_exercise_list(self):
        url = reverse('exercise-list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_exercise_list_admin(self):
        url = reverse('exercise-list')
        self.client.force_authenticate(self.admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_exercise_detail(self):
        url = reverse('exercise-detail', kwargs={'pk': self.exercise1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_exercise_detail_admin(self):
        url = reverse('exercise-detail', kwargs={'pk': self.exercise1.pk})
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_exercise_create(self):
        data = {
            "name": "Test exercise 3",
            'muscle_group': "CH",
            "equipment": 'BW',
            "description": "test exercise",
            "instructions": "test exercise instructions"
        }
        create_url = reverse("exercise-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.post(create_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_exercise_create_admin(self):
        data = {
            "name": "Test exercise 3",
            'muscle_group': "CH",
            "equipment": 'BW',
            "description": "test exercise",
            "instructions": "test exercise instructions"
        }
        create_url = reverse("exercise-list")
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_exercise_update(self):
        data = {
            "name": "Test exercise 1",
            'muscle_group': "BK",
            "equipment": 'DB',
            "description": "test exercise",
            "instructions": "test exercise instructions"
        }
        put_url = reverse("exercise-detail",
                             kwargs={"pk":self.exercise1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(put_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_exercise_update_admin(self):
        data = {
            "name": "Test exercise 1",
            'muscle_group': "BK",
            "equipment": 'DB',
            "description": "test exercise",
            "instructions": "test exercise instructions"
        }
        put_url = reverse("exercise-detail",
                             kwargs={"pk":self.exercise1.pk})
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(put_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_exercise_delete(self):

        delete_url = reverse("exercise-detail",
                             kwargs={"pk": self.exercise2.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_exercise_delete_admin(self):

        delete_url = reverse("exercise-detail",
                             kwargs={"pk": self.exercise2.pk})
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
