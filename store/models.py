from django.db import models

from users.models import User

from django.core.validators import RegexValidator
# from phone_field import PhoneField

# from django.contrib.auth.models import User
from PIL import Image

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    # amount = models.ForeignKey(Product, on_delete=models.CASCADE)
    # total amount
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def total_amount(self):
        return self.quantity * self.product.amount  

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name



class Bill(models.Model):
    name=models.CharField(max_length=40)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    issued_date = models.DateField(auto_now_add=True)







class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField()

def upload_profile_to(instance,filename):
	return f'profile_picture/{instance.user.username}/{filename}'

def upload_cover_to(instance,filename):
	return f'coverImage/{instance.user.username}/{filename}'

# class Profile(models.Model):
# 	gen = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
# 	user = models.OneToOneField(User, on_delete = models.CASCADE)
# 	about_me = models.CharField(max_length=250, null=True)
# 	birthday = models.DateField(null=True)
# 	profile_pic = models.ImageField(upload_to = upload_profile_to, null=True, default = 'defaults/profile_pic.jpg')
# 	cover_image = models.ImageField(upload_to = upload_cover_to, null = True, default= 'defaults/cover_image.jpg')
# 	gender = models.CharField(choices=gen, max_length=6, null=True)
# 	followers = models.ManyToManyField(User, related_name='followers', blank=True)
# 	following = models.ManyToManyField(User, related_name="following", blank=True)

# 	def __str__(self):
# 		return self.user.username

# 	def save(self, *args, **kwargs):
# 		super().save(*args, **kwargs)

# 		img = Image.open(self.profile_pic.path)
# 		if img.height > 300 or img.width > 300:
# 			output_size = (300, 300)
# 			img.thumbnail(output_size)
# 			img.save(self.profile_pic.path)

# 		img2 = Image.open(self.cover_image.path)
# 		if img2.height > 500 or img2.width > 500:
# 			output_size = (500, 500)
# 			img2.thumbnail(output_size)
# 			img2.save(self.cover_image.path)

# 	def non_followed_user(self):
# 		return set(User.objects.filter(is_active=True))-set(self.following.all())-{self.user}

# 	def get_notifications(self):
# 		return Notification.objects.filter(user=self.user, seen = False)

# class Notification(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	message = models.CharField(max_length=500)
# 	link = models.CharField(max_length=500)
# 	seen = models.BooleanField(default=False)