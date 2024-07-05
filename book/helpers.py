import uuid
class SaveMedia(object):
    def save_image(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"book/{uuid.uuid4()}.{image_extension}"
