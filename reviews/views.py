from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        grade = float(request.POST.get("grade"))
        if form.is_valid() and 0 <= grade <= 5:
            Review.objects.create(
                title=form.data.get("title"),
                content=form.data.get("content"),
                movie_name=form.data.get("movie_name"),
                grade=grade,
            )
            return redirect("reviews:index")
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)
