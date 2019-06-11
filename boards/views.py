from django.shortcuts import render, redirect
from .models import Board


# Create your views here
def index(request):
    # Board 의 전체 데이터를 불러온다 - QuerySet
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


# 사용자 입력을 받는 페이지 렌더링
def new(request):
    return render(request, 'boards/new.html')


# 데이터를 받아서 실제 DB 에 작성
def create(request):
    # form 태그가 post 방식이면 post 로 받아야된다.
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    # render 는 GET 요청에서 사용
    # POST 요청시에는 redirect 사용
    # return render(request, 'boards/create.html')
    return redirect(f'/boards/{board.id}/')


# 데이터의 id 값으로 특정 게시글 추출.
def detail(request, id):
    # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
    # context 로 넘겨서 detail.html 페이지에서 title 과 content 를
    # 출력해본다.
    board = Board.objects.get(id=id)
    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html',context)


def delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    # 삭제후 리스트화면으로 이동
    return redirect('/boards/')


# 게시글 수정 페이지 렌더링
def edit(request, id):
    # id 값에 맞는 board 데이터 꺼낸 후 edit.html 로 넘기기
    board = Board.objects.get(id=id)
    context = {'board':board}
    return render(request, 'boards/edit.html', context)


def update(request, id):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # id 값에 맞는 board 데이터를 위에서 주어진 title 과 content 에 맞게
    # 수정한 뒤 저장하는 로직
    # 1. Board 클래스를 통해 id 값에 맞는 데이터를 가져온다.
    board = Board.objects.get(id=id)
    # 2. 해당 데이터의 내용을 주어진 title, content 로 수정한다.
    board.title = title
    board.content = content
    # 3. 저장한다.
    board.save()
    return redirect(f'/boards/{id}/')