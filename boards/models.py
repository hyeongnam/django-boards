from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 1. 첫번째 포스트
        return f'{self.id}. {self.title}'


class Comment(models.Model):
    content = models.TextField()  # 댓글의 내용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 어떤 게시물에 대한 코멘트 인지를 정해줘야됨
    # on_delete=models.CASCADE ==> 게시글이 지워지면 댓글도 지워짐
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id} - {self.content})>'