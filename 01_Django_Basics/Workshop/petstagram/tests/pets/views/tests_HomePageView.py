from django.urls import reverse

from tests.helpers.pet_helpers import create_valid_pet
from tests.helpers.photo_helpers import create_valid_photo
from tests.test_base import TestBase


class HomePageViewTests(TestBase):

    def test_get_index__when_no_pets__expects_200_and_empty_object_list_in_context(self):
        response = self.client.get(reverse('home-page'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-page.html')
        self.assertListEmpty(response.context['object_list'])

    def test_get_index__when_pets__expects_200_and_single_pet_in_context(self):
        # Arrange
        user = self._create_user()
        pet = create_valid_pet(user)
        photo = create_valid_photo(user, pet)

        # Act
        response = self.client.get(reverse('home-page'))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-page.html')
        self.assertListEqual([photo], list(response.context['object_list']))
