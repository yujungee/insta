from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(request, 'Community/feed.html')

def edit(request):
    return render(request, 'Community/edit.html')

def create(request):
    return render(request, 'Community/create.html')

# def index(request):
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             user = get_object_or_404(user_model, pk=request.user.id)
#             following = user.following.all()
#             posts = models.Post.objects.filter(
#                 Q(author__in=following) | Q(author=user)
#             )
#
#             serializer = serializers.PostSerializer(posts, many=True)
#             print(serializer.data)
#
#             return render(request, 'MyPage/myPage.html', {"posts": serializer.data})
