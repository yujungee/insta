from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from djangogram.users.models import User as user_model
from djangogram.posts import models, serializers
# Create your views here.
def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, pk=request.user.id)
            following = user.following.all()
            posts = models.Post.objects.filter(
                Q(author__in=following) | Q(author=user)
            )

            serializer = serializers.PostSerializer(posts, many=True)
            print(serializer.data)

            return render(request, 'MyPage/myPage.html', {"posts": serializer.data})


def edit(request):
    return render(request, 'MyPage/edit.html')
