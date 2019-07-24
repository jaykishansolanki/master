from django.shortcuts import render
from .models import Post

# post = [{
# 	'name': 'abcd',
# 	'city': 'qwe',
# 	'mo': '98566'
# },
# {
#     'name': 'lkjh',
# 	'city': 'zxcv',
# 	'mo': '32145'	
# }

# ]

def home(request):
	context = {
	'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')