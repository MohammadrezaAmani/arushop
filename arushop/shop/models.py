import uuid

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# from arushop.other.models import Comment, Image

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="products", blank=True)
    stock = models.IntegerField()
    discount = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, populate_from="name")
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="dislikes", blank=True)
    views = models.ManyToManyField(User, related_name="views", blank=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name

    @property
    def actual_price(self):
        return self.price - (self.price * self.discount / 100)

    # @property
    # def rating(self):
    #     comments = Comment.objects.filter(product=self)
    #     if comments.count() == 0:
    #         return 0
    #     else:
    #         total = 0
    #         for comment in comments:
    #             total += comment.rate
    #         return total / comments.count()

    # @property
    # def comments(self):
    #     return Comment.objects.filter(product=self, reply=None)

    # @property
    # def count_comments(self):
    #     return Comment.objects.filter(product=self).count()

    @property
    def count_likes(self):
        return self.likes.count()

    @property
    def count_dislikes(self):
        return self.dislikes.count()

    @property
    def count_orders(self):
        return self.orderitem_set.count()

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.slug])

    def get_add_to_cart_url(self):
        return reverse("shop:add_to_cart", args=[self.id])

    def get_remove_from_cart_url(self):
        return reverse("shop:remove_from_cart", args=[self.id])


class Category(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="categories", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category_detail", args=[self.slug])

    @property
    def childs(self):
        return Category.objects.filter(parent=self)

    @property
    def expand_childs(self):
        childs = []
        for child in self.childs:
            if child.childs.count() == 0:
                childs.append(child.expand_childs)
        childs.append(self.products.all())
        return childs

    @property
    def count_views(self):
        views = 0
        for product in self.expand_childs:
            views += product.views.count()
        return views

    @property
    def views(self):
        views = []
        for product in self.expand_childs:
            views += list(product.views.all())
        return views

    @property
    def count_likes(self):
        likes = 0
        for product in self.expand_childs:
            likes += product.likes.count()
        return likes

    @property
    def likes(self):
        likes = []
        for product in self.expand_childs:
            likes += list(product.likes.all())
        return likes

    @property
    def count_dislikes(self):
        dislikes = 0
        for product in self.expand_childs:
            dislikes += product.dislikes.count()
        return dislikes

    @property
    def dislikes(self):
        dislikes = []
        for product in self.expand_childs:
            dislikes += list(product.dislikes.all())
        return dislikes

    @property
    def count_comments(self):
        comments = 0
        for product in self.expand_childs:
            comments += product.count_comments
        return comments

    @property
    def comments(self):
        comments = []
        for product in self.expand_childs:
            comments += list(product.comments.all())
        return comments

    @property
    def count_orders(self):
        orders = 0
        for product in self.expand_childs:
            orders += product.count_orders
        return orders

    @property
    def orders(self):
        orders = []
        for product in self.expand_childs:
            orders += list(product.orderitem_set.all())
        return orders


class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.cart_id)

    @property
    def total(self):
        total = 0
        for item in self.cartitem_set.all().filter(active=True):
            total += item.product.actual_price * item.quantity
        return total

    @property
    def total_discount(self):
        total = 0
        for item in self.cartitem_set.all().filter(active=True):
            total += item.product.price * item.quantity
        return total - self.total

    @property
    def wihout_discount(self):
        total = 0
        for item in self.cartitem_set.all().filter(active=True):
            total += item.product.price * item.quantity
        return total

    @property
    def count(self):
        count = 0
        for item in self.cartitem_set.all().filter(active=True):
            count += item.quantity
        return count

    @property
    def items(self):
        items = []
        for item in self.cartitem_set.all().filter(active=True):
            items.append(item)
        return items

    @property
    def count_items(self):
        count = 0
        for item in self.cartitem_set.all().filter(active=True):
            count += 1
        return count

    @property
    def count_products(self):
        count = 0
        for item in self.cartitem_set.all().filter(active=True):
            count += item.quantity
        return count


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    @property
    def count_orders(self):
        return self.order_set.count()

    @property
    def is_valid(self):
        # TODO: add address validation logic
        return True


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def count_items(self):
        return self.orderitem_set.count()

    @property
    def user(self):
        return self.address.user
