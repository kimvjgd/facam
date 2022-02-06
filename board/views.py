from django.shortcuts import render

from board.forms import BoardForm
from .models import Board

# Create your views here.

def board_write(request):
    form = BoardForm()
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})