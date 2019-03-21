from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)
    
# def create(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         board = Board(title=title, content=content)
#         board.save()
#         return redirect('boards:index')
        
#     else:
#         return render(request, 'boards/create.html')
        
# def create(request):
#     # POST 요청이면 FORM 데이터를 처리한다
#     if request.method == 'POST':
#         # 저 FORM 구조가 전체를 받아옴
#         # 정제된 데이터 받아옴
#         # form이 title, content 를 다 한번에 받아옴, 데이터를 들고옴
#         # 이 처리과정은 'binding'으로 불리는데, form의 유효성 체크를 할수있도록 해줌(class에 작성한 것들)
#         form = BoardForm(request.POST)
#         # form 유효성 체크, 안전한 데이터인지
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             # 검증을 통과한 깨끗한 데이터를 form에서 가져와서 board를 만든다
#             board = Board.objects.create(title=title, content=content)
#       # 별도로 세이브하지 않음
#             return redirect('boards:detail', board.pk)
#       # GET요청(혹은 다른 메서드)이면 기본 폼을 생성한다
#     else:
#         form = BoardForm()
#         # 포스트 요청이고, 유효성 문제에 있어서 문제가 있는 데이터일때
#     context = {'form': form }
#     return render(request, 'boards/create.html', context)

def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            # 저장한 하나의 게시글을 반환
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form }
    return render(request, 'boards/form.html', context)










def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board':board }
    return render(request, 'boards/detail.html', context)
    
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
        
    else:
        return redirect('boards:detail', board.pk)
        
# def update(request, board_pk):
#     board = get_object_or_404(Board, pk=board_pk)
#     if request.method == 'POST':
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             board.title = form.cleaned_data.get('title')
#             board.content = form.cleaned_data.get('content')
#             board.save()
#             return redirect('boards:detail', board.pk)
#     # GET 요청이면(수정하기 버튼을 눌렀을때)
    
#     else:
#         # BoardForm을 초기화(사용자 입력 값으 넣어준 상태로)
#         # form = BoardForm(initial={'title':board.title, 'content':board.content}
#         form = BoardForm(initial=board.__dict__)
#     # 1. POST: 요청에서 검증에 실패하였을때, 오류 메세지가 포함된 상태
#     # 2. GET: 요청에서 초기화된 상태 
#     context = {'form':form}
#     return render(request, 'boards/create.html', context)
    
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board) #1
        if form.is_valid(): # validation을 다 해주는것
            board = form.save()             #2
            return redirect('boards:detail', board.pk)
    
    else:
        form = BoardForm(instance=board) # 3
  
    context = {
        'form':form,
        'board': board,
    }
    return render(request, 'boards/form.html', context)
        
    