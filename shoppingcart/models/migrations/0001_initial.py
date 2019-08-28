# Generated by Django 2.2.4 on 2019-08-28 10:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_seller', models.BooleanField(default=False)),
                ('phone', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_address', models.CharField(max_length=250)),
                ('shipping_address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Addresses')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Address',
            },
        ),
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20)),
                ('usage_limit', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('discount_value', models.FloatField()),
                ('min_amount_spent', models.FloatField()),
                ('apply_once_per_order', models.BooleanField(default=False)),
                ('apply_once_per_customer', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('total_net', models.FloatField()),
                ('status', models.CharField(choices=[('unshipped', 'Unshipped'), ('shipped', 'Shipped'), ('pending', 'Pending'), ('cancelled', 'Cancelled'), ('delivered', 'Delivered')], max_length=20)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.CustomerAddress')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Discounts')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('background_image', models.ImageField(default='product/default.png', upload_to='product/')),
                ('seo_title', models.CharField(max_length=20)),
                ('seo_description', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Product Category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('price', models.FloatField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('is_published', models.BooleanField(default=False)),
                ('seo_title', models.CharField(max_length=20)),
                ('seo_description', models.TextField(max_length=100)),
                ('tax', models.FloatField()),
                ('weight', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ProductCategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ShippingZones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('countries', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('postal_code', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Shipping Zones',
            },
        ),
        migrations.CreateModel(
            name='WishlistItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='models.Products')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Wishlist Items',
            },
        ),
        migrations.CreateModel(
            name='ShippingMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('max_order_price', models.FloatField()),
                ('max_order_weight', models.FloatField()),
                ('min_order_price', models.FloatField()),
                ('min_order_weight', models.FloatField()),
                ('price', models.FloatField()),
                ('type', models.CharField(max_length=20)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ShippingZones')),
            ],
            options={
                'verbose_name_plural': 'Shipping Methods',
            },
        ),
        migrations.CreateModel(
            name='SellerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Seller Address',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='product/default.png', upload_to='product/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Products')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='ProductColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.TextField(max_length=20)),
                ('product', models.ManyToManyField(to='models.Products')),
            ],
            options={
                'verbose_name_plural': 'Product Color',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gateway', models.CharField(max_length=20)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('cc_name', models.CharField(max_length=30)),
                ('cc_exp_month', models.IntegerField()),
                ('cc_exp_year', models.IntegerField()),
                ('cc_first_digits', models.IntegerField()),
                ('cc_last_digits', models.IntegerField()),
                ('orders', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='models.Orders')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.SellerAddress')),
            ],
            options={
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='shipping_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ShippingMethods'),
        ),
        migrations.AddField(
            model_name='discounts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.ProductCategory'),
        ),
        migrations.AddField(
            model_name='discounts',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Products'),
        ),
    ]
