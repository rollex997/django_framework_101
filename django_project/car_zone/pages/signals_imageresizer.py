# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from PIL import Image
# from io import BytesIO
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from pages.models import Team

# @receiver(post_save, sender=Team)
# def resize_image(sender, instance, **kwargs):
#     # Check if the instance has a profile image and it's newly created or modified
#     if instance.photo and (kwargs.get('created') or kwargs.get('update_fields')):
#         img = Image.open(instance.photo)
#         # Resize the image to 300x300
#         img.thumbnail((300, 300))
#         # Convert image to BytesIO buffer
#         buffer = BytesIO()
#         img.save(buffer, format='JPEG')
#         buffer.seek(0)
#         # Update the profile image field with the resized image
#         instance.photo = InMemoryUploadedFile(buffer, None, f"{instance.photo.name.split('.')[0]}.jpg", 'image/jpeg', buffer.getbuffer().nbytes, None)
#         instance.save()
