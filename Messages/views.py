from rest_framework import generics

from .serializers import *


# Create your views here.
class CollectionList(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetail(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class MessageList(generics.ListAPIView):
    queryset = Message.objects.filter(is_single=True)
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.filter(is_single=True)
    serializer_class = MessageSerializer


class PartList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Part.objects.filter(collection=self.kwargs["pk"]).order_by("part_no")
        return queryset

    serializer_class = PartSerializer
