from django.db.models import QuerySet
from rest_framework import generics
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


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


def tagged_messages(request):
    if request.method == 'GET':
        if'tags' in request.GET:
            msgs = Message.objects.all()
            tags = request.GET['tags'].split(',')

            for i in tags:
                msgs = msgs.filter(tags__name__contains=i)

            data = {'results': list(msgs.values("title", "duration", "author", "time_created", "size", "location", "is_single").distinct())}
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'you must include the tags as query parameters',})
    else:
        return JsonResponse({'error': 'you must send a GET Request'})

