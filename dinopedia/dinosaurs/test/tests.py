from rest_framework.test import APITestCase, APIClient
from .factory import (
    UserFactory,
    DinosaurFactory,
    DinosaurLikeFactory,
    DinosaurMediaFactory
)
from ..models import (
    Dinosaur,
    DinosaurMedia,
    DinosaurLike,
)


class CreateDinosaurTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()

    def test_create_dinosaurs_success(self):
        data = {
            "name": "my dino",
            "eating_classification": "carnivores",
            "typical_colour": "red",
            "period_lived": "jurassic",
            "average_size": "large",
        }
        response = self.client.post('/dinosaurs/', data=data)
        dinosaurs = Dinosaur.objects.first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(dinosaurs.name, data["name"])
        self.assertEqual(dinosaurs.period_lived, data["period_lived"])

    def test_create_dinosaurs_fail(self):
        data = {
            "name": "my dino",
            "eating_classification": "random",
            "typical_colour": "red",
            "period_lived": "jurassic",
            "average_size": "large",
        }
        response = self.client.post('/dinosaurs/', data=data)
        self.assertEqual(response.status_code, 400)


class GetDinosaurTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.dinosaur1 = DinosaurFactory()
        self.dinosaur2 = DinosaurFactory()
        self.dinosaur_media = DinosaurMediaFactory()
        self.dinosaur_like = DinosaurLikeFactory(author=self.user, dinosaur=self.dinosaur1)

    def test_get_dinosaurs_all(self):
        response = self.client.get('/dinosaurs/')
        dinosaurs = Dinosaur.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(dinosaurs[0].name, self.dinosaur1.name)
        self.assertEqual(dinosaurs[0].average_size, self.dinosaur1.average_size)

    def test_get_liked_dinosaurs_unauthenticated(self):
        response = self.client.get('/dinosaurs/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        self.assertFalse(response.json()[0]['liked'])

    def test_get_liked_dinosaurs_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/dinosaurs/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        self.assertTrue(response.json()[0]['liked'])

    def test_get_dinosaurs_by_name(self):
        response = self.client.get(f'/dinosaurs/?name={self.dinosaur1.name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], self.dinosaur1.name)

    def test_delete_dinosaurs(self):
        response = self.client.delete(f'/dinosaurs/{self.dinosaur1.id}/')
        self.assertEqual(response.status_code, 204)
        dinosaur = Dinosaur.objects.filter(id=self.dinosaur1.id).exists()
        self.assertFalse(dinosaur)

    def test_like_dinosaurs(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(f'/dinosaurs/{self.dinosaur2.id}/like/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['liked'])


class NextTest(APITestCase):

    def test_create_dinosaurs_media(self):
        # TODO here in the same style we would test the image upload endpoint
        pass

    def test_delete_dinosaurs_media(self):
        # TODO here in the same style we would test the removal of the uploaded endpoint
        pass
