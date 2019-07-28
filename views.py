from django.shortcuts import render


from .models import Post
posts = [
    {  'author' : 'saidul islam' ,
       'title' : 'Heart specialist' ,
       'content' : 'sher e bangla',
       'date_posted'  : 'Aug 27, 2019'
    },

    {  'author' : 'shefa' ,
       'title' : 'Medicine' ,
       'content' : 'Dhaka medical college',
       'date_posted' : 'aug 28, 2019'
    }

]


def home(request):



    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'Home/home.html', context)

def about(request):
    return render(request, 'Home/about.html', {'title': 'about'})





