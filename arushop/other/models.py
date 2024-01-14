from django.db import models
from django.contrib.auth import get_user_model
import PIL
from django.urls import reverse
import uuid

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerChoices("rate", "1 2 3 4 5")
    comment = models.TextField()
    reply = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20, null=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="comment_dislikes", blank=True)

    def __str__(self):
        return self.comment

    def is_reply(self):
        return self.reply != None

    @property
    def count_likes(self):
        return self.likes.count()

    @property
    def count_dislikes(self):
        return self.dislikes.count()

    @property
    def comment_rate(self):
        likes = self.count_likes
        dislikes = self.count_dislikes
        return (self.count_likes - self.count_dislikes) / (likes + dislikes) if likes + dislikes != 0 else 0

    @property
    def count_replies(self):
        return self.replies.count()

    @property
    def replies(self):
        return Comment.objects.filter(reply=self)

class Image(models.Model):
    
    image = models.ImageField(upload_to="products", blank=True)
    alt = models.CharField(max_length=256, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.name
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.product.slug])
    
    def thumbnail(self, width: int = 256, height: int = 256, scale: int = None):
        img = PIL.Image.open(self.image)
        if scale:
            width = img.width * scale
            height = img.height * scale
            return img.resize((width, height), PIL.Image.ANTIALIAS)    
        return img.resize((width, height), PIL.Image.ANTIALIAS)