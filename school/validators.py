from rest_framework.serializers import ValidationError


class VideoLinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_link_url = value.get(self.field)
        if video_link_url and not video_link_url.startswith("https://www.youtube.com/"):
            raise ValidationError("Don`t use any links, except https://www.youtube.com")
