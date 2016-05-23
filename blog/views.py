from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

from django.http import HttpResponseRedirect

from .forms import NameForm

from .models import Product

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
def name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            your_name = form.cleaned_data['your_name']
            if your_name is not None:
                f = open( 'your_name.txt', 'w+')
                f.write(your_name)
                f.write(',')
                f.write(your_name)
                f.close()
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
            return redirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'blog/name.html', {'form': form})

def thanks(request):
    #if request.POST and request.FILES:
    #    csvfile = request.FILES['your_name.txt']
    #    dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
    #    csvfile.open()
    #    reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
    
    f = open('your_name.txt', 'r')  
    for line in f:  
        line =  line.split(',')  
        foo = line[1]
    f.close()
    
    # do some stuff with foo and write to file
    
    f = open( 'output.txt', 'w+')
    f.write('clean,stool,pool,cue')
    f.write(',')
    f.write(foo)
    f.close()
    
    f = open('output.txt', 'r')  
    for line in f:  
        line =  line.split(',')  
        result = line[4]
    f.close()
        
    return render(request, 'blog/thanks.html', {'result' : result})