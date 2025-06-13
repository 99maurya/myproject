
from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User
from .models import Product, SubCategory




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('id','product_name', 'product_price')
        # fields = ('product_name','product_price')


class ProductImageSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    class Meta:
        model = ProductImage
        fields = ('id','product','image')


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        # read_only_fields = ('id','booking_date','delivery_date','status','user','price')
        # exclude = ('price',)

class AddToCart(serializers.ModelSerializer):
    class Meta:
        models = AddToCart
        fields = ('id', 'user', 'product', 'price', 'quantity', 'booking_date', 'delivery_date', 'status', 'shipping_address', 'payment_method')

class  SubCategoryByCategoryIdserializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        read_only_fields = ('user','name','image')


class  ProductBySubCategoryIdserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('product_name','product_price','product_description')

class ReviewSerializer(serializers.Serializer):

    review_text = serializers.CharField(max_length=100)
    rating = serializers.IntegerField()
    product_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields = '__all__'
        read_only_fields = ('user','product','quantity','price','booking_date','delivery_date','status','shipping_address','payment_method')



# class UserSerializer(models.Model):
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254, unique=True)





# class CategorySerializer(serializers.Serializer):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="Category_images/", null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


#     def __str__(self):
#         return self.name
    
# class SubCategorySerializer(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#     image = models.ImageField(upload_to="subcategory_images/", null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.name
    
# class ProductSerializer(models.Model):
#     product_name = models.CharField(max_length=80)
#     product_price = models.DecimalField(max_length=10, decimal_places=2, null=True, blank=True)
#     product_description = models.TextField(null=True, blank=True)
#     color = models.CharField(max_length=50, null=True, blank=True)
#     material = models.CharField(max_length=100, null=True, blank=True)
#     stock = models.IntegerField(null=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.product_name
    

# class ProductImageSerializer(models.Model):
#     product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_images/')

#     def __str__(self):
#         return f"Image for {self.product.product_name}"


