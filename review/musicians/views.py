from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import MusicianForm, AlbumForm
from .models import Musician, Album

# Create your views here.
# 함수정의 함수이름(parameter):
def index(request):
    # .all()로 조회하면 querySet형태
    # querySet은 마치 list처럼 사용가능
    Musicians = Musician.objects.all()
    context = {
        'musicians' : Musicians
    }
    return render(request, 'musicians/index.html', context)

def create(request):
    if request.method == "POST":
        # 사용자의 요청 정보를 담아준다.
        form = MusicianForm(request.POST)
        if form.is_valid():
            # Musician가 models에게 받은 메서드
            # ModelForm을 정의 할 때 
            # class Meta : model = Musician을 담아줬다
            musician = form.save()
            # redirect('app_name:path_name')
            return redirect('musicians:index')
    else:
        # MusicianForm 불러오기
        # form은 MusicianForm 인스턴스
        # MusicianForm이 가진 정보를 가짐.
        # MusicianForm은 Musician의 정보
        # template에서 보여줄 tag들
        form = MusicianForm()
        print(form)
    context = {
        'form' : form
    }
    return render(request, 'musicians/create.html', context)

# 함수이름(request, url에 작선한 변수명)
def detail(request, musician_pk):
    # Model.objects.get(조건=변수명)
    musician = Musician.objects.get(pk=musician_pk)
    album_form = AlbumForm()
    albums = musician.album_set.all()
    context = {
        'musician' : musician,
        'album_form' : album_form,
        'albums' : albums
    }
    return render(request, 'musicians/detail.html', context)

def update(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musicians:detail', musician.pk)
    else:
        form = MusicianForm(instance=musician)
    context = {
        'form' : form
    }
    return render(request, 'musicians/create.html', context)

def delete(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    musician.delete()
    return redirect('musicians:index')

@require_POST
def album_create(request, musician_pk):
    musician = get_object_or_404(Musician, pk=musician_pk)
    album_form = AlbumForm(request.POST)
    if album_form.is_valid():
        album = album_form.save(commit=False)
        album.musician = musician
        album.save()
        return redirect('musicians:detail', musician.pk)
    else:
        context = {
            'album_form' : album_form,
            'musician' : musician
        }
    return redirect('musicians:detail', context)

@require_POST
def album_delete(request, musician_pk, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    album.delete()
    return redirect('musicians:detail', musician_pk)