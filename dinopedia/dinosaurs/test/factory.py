import factory
from faker import Faker
from dinopedia.dinosaurs.models import (
    Dinosaur,
    DinosaurLike,
    DinosaurMedia
)
from django.contrib.auth.models import User

Faker.seed(0)
fake = Faker(locale=['en_GB'])


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = fake.text(32)
    email = fake.email()
    is_active = True
    is_staff = False
    is_superuser = False


class DinosaurFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dinosaur

    name = factory.Faker("name")
    eating_classification = Dinosaur.EatingClassificationType.carnivores
    typical_colour = fake.text(32)
    period_lived = Dinosaur.PeriodLivedType.jurassic
    average_size = Dinosaur.AverageSizeType.medium


class DinosaurMediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DinosaurMedia

    dinosaur = factory.SubFactory(DinosaurFactory)
    image = fake.url()


class DinosaurLikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DinosaurLike

    author = factory.SubFactory(UserFactory)
    dinosaur = factory.SubFactory(DinosaurFactory)
