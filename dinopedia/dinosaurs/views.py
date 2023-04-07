from rest_framework import generics, permissions, status, views, mixins
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Dinosaur, DinosaurMedia, DinosaurLike
from .serializers import DinosaurSerializer, DinosaurMediaSerializer, DinosaurLikeSerializer


class DinosaurView(generics.ListCreateAPIView):
    serializer_class = DinosaurSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Dinosaur.objects.filter()

    def get_queryset(self):
        qs = Dinosaur.objects.filter().order_by('pk')
        name = self.request.query_params.get('name')
        liked = self.request.query_params.get('liked')
        if name:
            qs = qs.filter(name__icontains=name)
        if liked and not self.request.user.is_anonymous:
            qs = qs.filter(like__isnull=False)
        return qs


class DinosaurDeleteView(generics.DestroyAPIView):
    serializer_class = DinosaurSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Dinosaur.objects.filter()


class DinosaurMediaCreateView(generics.CreateAPIView):
    serializer_class = DinosaurMediaSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    queryset = DinosaurMedia.objects.filter()


class DinosaurMediaDeleteView(generics.DestroyAPIView):
    serializer_class = DinosaurMediaSerializer
    permission_classes = [permissions.AllowAny]
    queryset = DinosaurMedia.objects.filter()


class DinosaurLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def patch(self, request, pk):
        try:
            dinosaur = Dinosaur.objects.get(pk=pk)
            liked = dinosaur.like_dino(request.user)
            return Response({"liked": liked,
                             'dinosaur': DinosaurSerializer(dinosaur, context={'request': request}).data})
        except Dinosaur.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
