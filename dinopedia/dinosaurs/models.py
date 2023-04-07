from django.db import models

# Create your models here.


class Dinosaur(models.Model):
    class EatingClassificationType(models.TextChoices):
        herbivores = 'herbivores'
        omnivores = 'omnivores'
        carnivores = 'carnivores'

    class PeriodLivedType(models.TextChoices):
        triassic = 'triassic'
        jurassic = 'jurassic'
        cretaceous = 'cretaceous'
        paleogene = 'paleogene'
        neogene = 'neogene'

    class AverageSizeType(models.TextChoices):
        tiny = 'tiny'
        very_small = 'very_small'
        small = 'small'
        medium = 'medium'
        large = 'large'
        very_large = 'very_large'

    name = models.CharField(max_length=64, db_index=True)
    eating_classification = models.CharField(max_length=10, choices=EatingClassificationType.choices,
                                             default=None, blank=True, null=True)
    typical_colour = models.CharField(max_length=32)
    period_lived = models.CharField(max_length=10, choices=PeriodLivedType.choices, default=None, blank=True, null=True)
    average_size = models.CharField(max_length=10, choices=AverageSizeType.choices, default=AverageSizeType.medium)

    def liked(self, user):
        if user.is_anonymous:
            return False
        return DinosaurLike.objects.filter(dinosaur=self, author=user).exists()

    def like_dino(self, user):
        if self.liked(user):
            DinosaurLike.objects.filter(author=user, dinosaur=self).delete()
            return False
        else:
            DinosaurLike.objects.create(author=user, dinosaur=self)
            return True

    def __repr__(self):
        return self.name


class DinosaurMedia(models.Model):
    dinosaur = models.ForeignKey("dinosaurs.Dinosaur", on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='images/')


class DinosaurLike(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='dinosaur_like')
    dinosaur = models.ForeignKey("dinosaurs.Dinosaur", on_delete=models.CASCADE, related_name='like')
