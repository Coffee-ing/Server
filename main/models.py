from django.db import models

class Club (models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True, default='')
    title = models.CharField(verbose_name='모임이름', max_length=20)
    district = models.CharField(verbose_name="장소", max_length=11)
    meet_time = models.CharField(verbose_name="모임 시간", max_length=11, default='')
    deadline_yy = models.IntegerField(verbose_name="마감일 연", default=2023)
    deadline_mm = models.CharField(verbose_name="마감일 월", max_length=2)
    deadline_dd = models.CharField(verbose_name="마감일 일", max_length=2)
    organizer = models.CharField(verbose_name="주최자", max_length=13)
    like = models.IntegerField(verbose_name="좋아요 개수", default=0)
    iflike = models.BooleanField(verbose_name="좋아요 여부", default=False)

    def __str__(self):
        return str(self.title)

class MyClub(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'[{self.program}] 신청'