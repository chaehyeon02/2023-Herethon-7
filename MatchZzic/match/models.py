from django.db import models

class MatchUser(models.Model):
    userName = models.CharField(verbose_name='이름', max_length=10)

    PLAN_CHOICES = [
        ('Y', '계획형'),
        ('N', '즉흥형'),
    ]

    TIGHT_CHOICES = [
        ('Y', '바쁘게 움직이는 여행'),
        ('N', '오직 휴식을 위한 여행'),
    ]

    PHOTO_CHOICES = [
        ('Y', '사진 찍는 거 좋아요'),
        ('N', '사진 찍는 거 싫어요'),
    ]

    PLACE_CHOICES = [
        ('city', '번화가'),
        ('nature', '자연, 시골'),
    ]

    travel_to = models.CharField(verbose_name='여행지'),
