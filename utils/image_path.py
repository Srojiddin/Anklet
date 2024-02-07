import os


def upload_avatar_for_user(instance, filename):
    return f"avatars/{instance.username}/{filename}"


def upload_products(instance, filename):
    return f"products/{instance.product.title}/{filename}"



