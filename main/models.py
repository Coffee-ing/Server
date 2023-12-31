from django.db import models

class Club (models.Model):
    image = models.ImageField(verbose_name='이미지', blank=True, default='/default.jpg')
    title = models.CharField(verbose_name='모임이름', max_length=20)
    content = models.TextField(verbose_name='모집 내용')
    num_people = models.IntegerField(verbose_name='모집 인원', default=0)
    district = models.CharField(verbose_name="장소", max_length=11)
    meet_time = models.CharField(verbose_name="모임 시간", max_length=11, default='')
    deadline_yy = models.IntegerField(verbose_name="마감일 연", default=2023)
    deadline_mm = models.CharField(verbose_name="마감일 월", max_length=2)
    deadline_dd = models.CharField(verbose_name="마감일 일", max_length=2)
    organizer = models.CharField(verbose_name="주최자", max_length=13)
    like = models.IntegerField(verbose_name="좋아요 개수", default=0)
    iflike = models.BooleanField(verbose_name="좋아요 여부", default=False)
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

    def __str__(self):
        return str(self.title)


class MyClub(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'[{self.club}] 신청'
    

class MyLike(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.club}] 찜'