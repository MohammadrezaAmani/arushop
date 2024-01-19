# run following scripts in 'python3 manage.py shell' to generate fake data

import random

from django.contrib.auth.hashers import make_password

from arushop.shop.models import Category, Product
from arushop.users.models import User

alphabets = "abcdefghigklmnopqrstuvwxyz" * 10


products = []
for i in range(1000):
    products.append(
        Product(
            name=f"Product {i}",
            description=f"Description {i}",
            price=random.randint(100, 10000),
            stock=random.randint(0, 100),
            discount=random.randint(0, 100),
        )
    )

Product.objects.bulk_create(products)


category = []
for i in range(100, 200):
    c = Category(name=f"Category {i}", slug=f"Category-{i}", description=f"hey! {i}")
    category += [c]
Category.objects.bulk_create(category)


products = Product.objects.all()
cat_data = Category.objects.all()
couner = 0
for i in cat_data:
    couner += 1
    if couner % 10 == 0 and couner <= 20:
        i.parent = None
        continue
    i.parent = Category.objects.filter(id=random.randint(0, couner - 1)).first()

    i.products.set(random.choices(products, k=random.randint(1, 100)))
    i.save()
#     category.append(c)
# Category.objects.bulk_update(category, ['products','parent'])


users = []
for i in range(10000, 20000):
    user = User()
    user.username = f"user-{i}"
    user.name = random.choices(list(alphabets), k=10)
    user.last_name = random.choices(list(alphabets), k=10)
    user.email = f"{random.choices(list(alphabets), k=10)}@gmail.com"
    # user.phone = '0912'+str(random.randint(3567890, 98765430))
    user.password = make_password("string")
    user.first_name = random.choices(list(alphabets), k=10)
    users += [user]

User.objects.bulk_create(users)

from arushop.other.models import Comment
from arushop.shop.models import Product
from arushop.users.models import User

comments = []
products = Product.objects.all()
users = User.objects.all()
for i in products:
    for j in range(random.randint(1, 100)):
        u = random.choices(users)[0]
        c = Comment(
            user=u,
            comment=f"generated comment for {i} - {j} by user {u.username}",
        )
        c.rate = random.randint(1, 5)
        comments += [c]
Comment.objects.bulk_create(comments)
for i in comments:
    if random.randint(0, 1):
        i.likes.set(random.choices(users, k=random.randint(0, 100)))
    if random.randint(0, 1):
        i.dislikes.set(random.choices(users, k=random.randint(0, 100)))
    if random.randint(0, 1):
        i.reply = random.choices(comments)[0]
Comment.objects.bulk_update(comments, ["likes", "dislikes", "reply"])
