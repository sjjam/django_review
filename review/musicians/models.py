from django.db import models

# Create your models here.
# 객체 생성 (클래스 생성) -> 테이블 명
class Musician(models.Model):
    # 멤버 변수
    # name = '이름이란 사람이 가지는 공통특성'
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    # 인스턴스 호출 시 출력 내용 덮어쓰기
    def __str__(self):
        return f'{self.name} : {self.age}'

class Album(models.Model):
    # Musician과 1:N 관계
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    featuring = models.CharField(max_length=150)
    music_num = models.IntegerField()
    release_date = models.DateField()
    img = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title} : {self.featuring} : {self.music_num}'