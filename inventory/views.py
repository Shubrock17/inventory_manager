from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Product, Supplier, Buyer, Order


@login_required
def home(request):
	if request.method == "POST":
		text = request.POST.get('text')
		img = request.FILES.get('post_image')
		post = Post(user = request.user, text = text, picture=img)
		post.save()
		mess = f"{request.user.first_name} {request.user.last_name} added a Post."
		for usr in request.user.profile.followers.all():
			noti = Notification(user = usr, message=mess, link = f"/#post{post.id}")
			noti.save()
		return redirect('home')

	following_users = list(request.user.profile.following.all())
	following_users.append(request.user)
	posts = Post.objects.filter(user__in = following_users).order_by('-created_at')

	all_post = Paginator(posts,10)
	page = request.GET.get('page')
	try:
		posts = all_post.page(page)
	except PageNotAnInteger:
		posts = all_post.page(1)
	except EmptyPage:
		posts = all_post.page(all_post.num_pages)

	parms = {
		'non_followed_user': request.user.profile.non_followed_user,
		'posts': posts,
	}
	return render(request, 'base/home.html', parms)


@login_required
def search(request):
	q = request.GET.get('q')
	if q:
		users = User.objects.filter(
		Q(username__icontains = q) |
		Q(first_name__icontains = q) |
		Q(last_name__icontains = q)
		).distinct()
	else:
		users = request.user.profile.non_followed_user
	return render(request, 'main/search.html', {'users': users})
    


@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)
