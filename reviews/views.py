from django.shortcuts import render

# Create your views here.
def review(request):
   
    return render(request,"reviews/review.html")

def submitCliked(request):
    if request.method=="POST":
        entered_username=request.POST['inputEntered']
        print(entered_username)
    return render(request,"reviews/thankyou.html")
