from django.shortcuts import render

# Create your views here.

def index(request):
    result = None
    if request.method == "POST":
        name1 = request.POST.get("your_name", "")
        name2 = request.POST.get("lover_name", "")
        try:
            love = int(request.POST.get("years", 0))
        except ValueError:
            love = 0

        j = [ord(char) for char in name1]
        k = [ord(char) for char in name2]
        set1 = set(j)
        set2 = set(k)
        set3 = set1.union(set2)
        p = sum(set3)

        if p >= 500 and love >= 4:
            o = (p / 1000) * 100
        else:
            o = (p / 500) * 100

        result = f"{min(round(o, 2), 100)}%"

    return render(request, "index.html", {"result": result})