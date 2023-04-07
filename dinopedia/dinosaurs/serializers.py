from rest_framework import serializers
from .models import Dinosaur, DinosaurMedia, DinosaurLike


class DinosaurSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Dinosaur
        fields = (
            "id",
            "name",
            "eating_classification",
            "typical_colour",
            "period_lived",
            "average_size",
            "images",
            "liked",
        )
        read_only_fields = (
            "id",
            "images",
        )

    def get_images(self, instance):
        return DinosaurMediaSerializer(instance.image, many=True, context=self.context).data

    def get_liked(self, instance):
        return instance.liked(self.context['request'].user)


class DinosaurMediaSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = DinosaurMedia
        fields = (
            "id",
            "dinosaur",
            "image",
        )
        read_only_fields = (
            "id",
        )

    # TODO here we could add validation to check whenever the image uploaded is not over the 2 per dinosaur limit


class DinosaurLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DinosaurLike
        fields = (
            "author",
            "dinosaur",
        )
