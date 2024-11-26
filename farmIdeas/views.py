from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import ContactUs, Idea, Comment
from .forms import IdeaForm, CommentForm
import requests

from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def home(request):
    """
    Renders the homepage with the
    latest 3 ideas and the total number of ideas.
    """
    ideas = Idea.objects.order_by('-date_posted')[:3] 
    total_ideas = Idea.objects.count() 

    context = {
        'seo': 'home',
        'ideas': ideas,
        'total_ideas': total_ideas,  
    }
    return render(request, "home/index.html", context)




def about(request):
    """
    Renders the about page.
    """
    return render(request, "about/about.html", {'seo': 'about'})




def policy(request):
    """
    Renders the policy page.
    """
    return render(request, "policy/policy.html", {'seo': 'policy'})




def contact(request):
    """
    Handles the contact form submission. 
    Saves the contact message to the database
    and displays a success message to the user.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        ContactUs.objects.create(name=name, email=email, message=message)

        messages.success(request, "We have received your message. Thank you for reaching out!")
        return redirect('contact')  

    return render(request, "contact/contact.html", {'seo': 'contact'})






def submit_idea(request):
    """
    Handles the submission of a new idea. 
    Saves the idea to the database.
    """
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        Idea.objects.create(title=title, description=description)  
        return redirect('idea_list')  
    return render(request, 'ideas/submit_ideas.html')  






def idea_list(request):
    """
    Renders the list of ideas. Filters by search query if provided and 
    handles AJAX requests for dynamic loading.
    """
    query = request.GET.get('q')  
    ideas = Idea.objects.filter(title__icontains=query) if query else Idea.objects.all().order_by('-date_posted')

    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('ideas/idea_list_items.html', {'ideas': ideas})
        return JsonResponse({'html': html})

      

    return render(request, 'ideas/idea_list.html', {'ideas': ideas,  'seo': 'ideas'})








def idea_page(request, slug):
    """
    Renders the detailed page for a specific idea, including all associated comments.
    """
    idea = get_object_or_404(Idea, slug=slug)  
    comments = idea.comments.all()  
    return render(request, 'ideas/idea_page.html', {'idea': idea, 'comments': comments,  'seo': 'comment'})









def submit_comment(request, idea_id):
    """
    Handles the submission of a comment for a specific idea.
    Returns the new comment's details as JSON for updating the UI dynamically.
    """
    if request.method == "POST":
        comment_text = request.POST.get('comment_text')  
        idea = get_object_or_404(Idea, id=idea_id)  
        comment = Comment.objects.create(idea=idea, comment_text=comment_text)  
        return JsonResponse({
            'comment_text': comment.comment_text,  
            'date_posted': comment.date_posted.strftime('%Y-%m-%d %H:%M')  
        })








def resources(request):
    """
    Renders the resources page.
    """
    return render(request, "resources/resources.html", {'seo': 'resources'})










def news(request):
    """
    Fetches news articles related to agriculture from 
    an external API, handles pagination and errors.
    """
    api_url = 'https://newsdata.io/api/1/news?apikey=pub_56416db84b6c50c290d2822789bea16d2ab99&q=agriculture'
    articles = []

    try:
        response = requests.get(api_url)  
        response.raise_for_status()  
        data = response.json()  
        articles = data.get('results', [])  
    except requests.exceptions.RequestException:
        articles = None  

    # Get pagination parameters from the URL query string
    page_size = int(request.GET.get('page_size', 5)) 
    page_number = int(request.GET.get('page', 1))  

    if articles is None:  
        context = {
            'articles': [],
            'page_size': page_size,
            'current_page': page_number,
            'total_pages': 1,
            'seo': 'news',
            'error_message': 'No network available. Please try again later.'  
        }
    else:
        paginator = Paginator(articles, page_size)  
        try:
            current_page = paginator.page(page_number)  
        except (PageNotAnInteger, EmptyPage):
            current_page = paginator.page(1)  

        context = {
            'articles': current_page.object_list,  
            'page_size': page_size,
            'current_page': current_page.number,
            'total_pages': paginator.num_pages,  
            'seo': 'news',
            'error_message': None  
        }

    return render(request, 'news/news.html', context)
