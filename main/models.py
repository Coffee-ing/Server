from django.db import models

class Post (models.Model):
    # image = models.ImageField(verbose_name='이미지')
    title = models.TextField(verbose_name='모임 이름')
    place = models.TextField(verbose_name='모임 장소', default='')
    date = models.DateField(auto_now_add = True, verbose_name='모임 시간')
    num_people = models.IntegerField(verbose_name='모집 인원')
    closing_date = models.TextField(verbose_name='모집 마감 일자')
    writer = models.TextField(verbose_name='주최자')
    
    TAG_CHOICE = [
        ('original', '바리스타 오리지널'),
        ('friend', '동네친구끼리 편하게'),
        ('tour', '핫플 카페 투어'),
        ('worker', '직장인 커피 모임'),
        ('beginner', '커피 입문자 환영'),
        ('why', '커피모임 왜하지')
    ]
    
    tag = models.CharField(
        max_length=8,
        choices=TAG_CHOICE,
        default='original'
    )

    content = models.TextField(verbose_name='모집 내용')