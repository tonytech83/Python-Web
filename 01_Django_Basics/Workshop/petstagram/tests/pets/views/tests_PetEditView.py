from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.helpers.pet_helpers import create_valid_pet
from tests.test_base import TestBase

UserModel = get_user_model()


class EditPetViewTests(TestBase):
    def test_get__when_owner__expect_200_with_correct_pet_and_template(self):
        user = self._create_user()
        pet = create_valid_pet(user)

        self.client.login(**self.USER_DATA)
        response = self.client.get(
            reverse('edit-pet', kwargs={
                'username': self.USER_DATA['email'],
                'pet_slug': pet.slug,
            }),
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/pet-edit-page.html')

    def test_post_edit__when_owner__expect_302_with_correct_redirect_and_edited_pet_with_unchanged_slug(self):
        pass

    def test_get__when_not_owner__expect_404_with_redirect_to_home(self):
        pass

    def test_post__when_not_owner__expect_404_with_redirect_to_home(self):
        pass
