from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from .models import Board


# Create your views here
@require_GET
def index(request):
    # Board 의 전체 데이터를 불러온다 - QuerySet
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


# 사용자 입력을 받는 페이지 렌더링
@require_http_methods(['GET','POST'])
def new(request):
    # GET
    if request.method == 'GET':
        return render(request, 'boards/new.html')
    # POST
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.id)

# 데이터를 받아서 실제 DB 에 작성
# def create(request):
#     # form 태그가 post 방식이면 post 로 받아야된다.
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     board = Board(title=title, content=content)
#     board.save()
#     # render 는 GET 요청에서 사용
#     # POST 요청시에는 redirect 사용
#     # return render(request, 'boards/create.html')
#     return redirect('boards:detail', board.id)


# 데이터의 id 값으로 특정 게시글 추출.
@require_GET
def detail(request, id):
    # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
    # context 로 넘겨서 detail.html 페이지에서 title 과 content 를
    # 출력해본다.
    # board = Board.objects.get(id=id)
    board = get_object_or_404(Board, id=id)
    context = {'board': board}
    return render(request, 'boards/detail.html',context)


# POST 만 접근 허용
@require_POST
def delete(request, id):
    # GET 요청으로 들어오면 detail page 로 다시 redirect
    if request.method == 'GET':
        return redirect('boards:detail',id)
    # POST 요청으로 들어오면 정상 삭제
    else:
        board = get_object_or_404(Board, id=id)
        board.delete()
    # 삭제후 리스트화면으로 이동
        return redirect('boards:index')


# 게시글 수정 페이지 렌더링
@require_http_methods(['GET','POST'])
def edit(request, id):
    # 1. 사용자의 요청이 GET 인지 POST 인지 확인한다.
    board = get_object_or_404(Board, id=id)
    if request.method == 'GET':
        # 2. GET 요청이면 사용자에게 수저할 페이지를 보여준다.
        context = {'board': board}
        return render(request, 'boards/edit.html', context)
    else:
        # 3. POST 요청이면 사용자가보낸 데이터를 받아서 수정한 뒤
        title = request.POST.get('title')
        content = request.POST.get('content')
        board.title = title
        board.content = content
        board.save()
        # detail page 로 redirect 한다.
        return redirect('boards:detail', id)
    # id 값에 맞는 board 데이터 꺼낸 후 edit.html 로 넘기기



# def update(request, id):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     # id 값에 맞는 board 데이터를 위에서 주어진 title 과 content 에 맞게
#     # 수정한 뒤 저장하는 로직
#     # 1. Board 클래스를 통해 id 값에 맞는 데이터를 가져온다.
#     board = Board.objects.get(id=id)
#     # 2. 해당 데이터의 내용을 주어진 title, content 로 수정한다.
#     board.title = title
#     board.content = content
#     # 3. 저장한다.
#     board.save()
#     return redirect('boards:detail', id)
