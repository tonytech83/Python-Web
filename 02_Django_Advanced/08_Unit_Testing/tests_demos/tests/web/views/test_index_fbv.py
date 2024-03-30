from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

"""
`from django.test import TestCase` - Creates a test database for each test
"""

UserModel = get_user_model()


class IndexFbvTests(TestCase):

    def test__what_can_be_tested(self):
        response = self.client.get(reverse('index_fbv'))

        context = response.context
        self.assertEqual('web/users.html', context.template_name)

        self.assertEqual(response.status_code, 200)

    def test__when_no_users__expect_empty_user_list(self):
        # `client` make request as like browser
        response = self.client.get(reverse('index_fbv'))

        context = response.context
        user_list = context['user_list']

        expected_user_list = []

        self.assertListEqual(expected_user_list, list(user_list))

    def test__when_single_user__expect_user_list_with_single_user(self):
        # Arrange
        user = UserModel.objects.create_user(username='test_user', password='1123Qwer')

        # Act
        response = self.client.get(reverse('index_fbv'))

        # Assert
        context = response.context
        user_list = context['user_list']

        expected_user_list = [user]

        self.assertListEqual(expected_user_list, list(user_list))

    def test__when_three_users__expect_user_list_with_three_users(self):
        # Arrange
        users = [
            UserModel.objects.create_user(username=f'test_user_{idx}', password=f'1123Qwer_{idx}')
            for idx in range(3)
        ]

        # Act
        response = self.client.get(reverse('index_fbv'))

        # Assert
        context = response.context
        user_list = context['user_list']

        expected_user_list = users

        self.assertListEqual(expected_user_list, list(user_list))
