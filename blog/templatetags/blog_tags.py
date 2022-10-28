from django import template
from blog.models import Post,Comment
from blog.models import Category
from django.db.models import Count, Q

register = template.Library()

@register.inclusion_tag("blog/latest-posts.html")
def latest_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts': posts}


@register.inclusion_tag("blog/blog-post-category.html")
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict}

@register.inclusion_tag("blog/most-viewed-posts.html")
def most_viewed_posts():
    posts = Post.objects.filter(status=1).order_by('-counted_views')[:3]
    return {'posts': posts}