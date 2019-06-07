from django.shortcuts import render
from django.views import generic
from django.http import FileResponse,HttpResponse
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = "post_list.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"


def indexpage(request):
    return render(request, 'index.html')


def resume(request):
    return FileResponse(open("./files/jeetendra_kashyap_Resume.pdf","rb"),as_attachment=False,filename="Jeetendra_Kashyap_Resume.pdf")