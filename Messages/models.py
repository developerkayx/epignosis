from django.db import models


# Create your models here.
class Tag(models.Model):
    """
        A @Tag is a particular subject relating a bunch of messages
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Collection(models.Model):
    """
        A @Collection of messages that are parts of a single topic.
        More like an album of messages.
        Collections will have an author, time_created and a title
    """
    title = models.CharField(max_length=200)  # the title of a @Collection
    author = models.CharField(max_length=100)  # the author of a @Collection
    time_created = models.DateTimeField(auto_now=True)  # the time a @Collection was created

    def __str__(self):
        return f"{self.title} Collection by {self.author}"


class Message(models.Model):
    """"
        A particular @Message by a preacher that goes into a Collection or is single.
        Messages will have a duration, title, author, time_created, size, location and is_single
    """
    title = models.CharField(max_length=200)  # the title of a @Message
    duration = models.DurationField()  # the duration of a @Message
    author = models.CharField(max_length=100)  # the author of a @Message
    time_created = models.DateTimeField(auto_now=True)  # the time a @Message was created
    size = models.DecimalField(decimal_places=2, max_digits=9)  # the file size of a @Message
    location = models.URLField()  # the URI of a @Message
    is_single = models.BooleanField()  # the type of a @Message (single -> True or part of a @Collection -> False)
    tags = models.ManyToManyField(Tag, related_name="messages")
    thumbnail_url = models.URLField()

    def __str__(self):
        return f"{self.title} by {self.author}"


class Part(models.Model):
    """
        A @Part is a message that belongs in a collection.
        Parts will have part_no, collection and message.
    """
    part_no = models.IntegerField()  # A Number referring to the @Part of the @Collection
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="parts")  # the @Collection containing this @Part
    message = models.OneToOneField(
        Message, on_delete=models.CASCADE, related_name="part")  # the @Message that this @Part is representing

    def __str__(self):
        return f"{self.message.title} {self.part_no} by {self.message.author}"

    