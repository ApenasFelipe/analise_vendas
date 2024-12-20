# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customer_id = models.TextField(blank=True, null=True)
    customer_unique_id = models.TextField(blank=True, null=True)
    customer_zip_code_prefix = models.IntegerField(blank=True, null=True)
    customer_city = models.TextField(blank=True, null=True)
    customer_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Geolocation(models.Model):
    geolocation_zip_code_prefix = models.IntegerField(blank=True, null=True)
    geolocation_lat = models.FloatField(blank=True, null=True)
    geolocation_lng = models.FloatField(blank=True, null=True)
    geolocation_city = models.TextField(blank=True, null=True)
    geolocation_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geolocation'


class LeadsClosed(models.Model):
    mql_id = models.TextField(blank=True, null=True)
    seller_id = models.TextField(blank=True, null=True)
    sdr_id = models.TextField(blank=True, null=True)
    sr_id = models.TextField(blank=True, null=True)
    won_date = models.TextField(blank=True, null=True)
    business_segment = models.TextField(blank=True, null=True)
    lead_type = models.TextField(blank=True, null=True)
    lead_behaviour_profile = models.TextField(blank=True, null=True)
    has_company = models.IntegerField(blank=True, null=True)
    has_gtin = models.IntegerField(blank=True, null=True)
    average_stock = models.TextField(blank=True, null=True)
    business_type = models.TextField(blank=True, null=True)
    declared_product_catalog_size = models.FloatField(blank=True, null=True)
    declared_monthly_revenue = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads_closed'


class LeadsQualified(models.Model):
    mql_id = models.TextField(blank=True, null=True)
    first_contact_date = models.TextField(blank=True, null=True)
    landing_page_id = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads_qualified'


class OrderItems(models.Model):
    order_id = models.TextField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    product_id = models.TextField(blank=True, null=True)
    seller_id = models.TextField(blank=True, null=True)
    shipping_limit_date = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    freight_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'


class OrderPayments(models.Model):
    order_id = models.TextField(blank=True, null=True)
    payment_sequential = models.IntegerField(blank=True, null=True)
    payment_type = models.TextField(blank=True, null=True)
    payment_installments = models.IntegerField(blank=True, null=True)
    payment_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_payments'


class OrderReviews(models.Model):
    review_id = models.TextField(blank=True, null=True)
    order_id = models.TextField(blank=True, null=True)
    review_score = models.IntegerField(blank=True, null=True)
    review_comment_title = models.TextField(blank=True, null=True)
    review_comment_message = models.TextField(blank=True, null=True)
    review_creation_date = models.TextField(blank=True, null=True)
    review_answer_timestamp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_reviews'


class Orders(models.Model):
    order_id = models.TextField(blank=True, null=True)
    customer_id = models.TextField(blank=True, null=True)
    order_status = models.TextField(blank=True, null=True)
    order_purchase_timestamp = models.TextField(blank=True, null=True)
    order_approved_at = models.TextField(blank=True, null=True)
    order_delivered_carrier_date = models.TextField(blank=True, null=True)
    order_delivered_customer_date = models.TextField(blank=True, null=True)
    order_estimated_delivery_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class ProductCategoryNameTranslation(models.Model):
    product_category_name = models.TextField(blank=True, null=True)
    product_category_name_english = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_name_translation'


class Products(models.Model):
    product_id = models.TextField(blank=True, null=True)
    product_category_name = models.TextField(blank=True, null=True)
    product_name_lenght = models.FloatField(blank=True, null=True)
    product_description_lenght = models.FloatField(blank=True, null=True)
    product_photos_qty = models.FloatField(blank=True, null=True)
    product_weight_g = models.FloatField(blank=True, null=True)
    product_length_cm = models.FloatField(blank=True, null=True)
    product_height_cm = models.FloatField(blank=True, null=True)
    product_width_cm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Sellers(models.Model):
    seller_id = models.TextField(blank=True, null=True)
    seller_zip_code_prefix = models.IntegerField(blank=True, null=True)
    seller_city = models.TextField(blank=True, null=True)
    seller_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellers'
