from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import query_form
from home.models import working_data
import json
# Create your views here.



def home_view(request) :
    if request.method == 'POST':
        data = query_form(request.POST)
        obj = working_data.objects.all()
        final_data = {}
        if data.is_valid(): 
            que = data.cleaned_data['query']
            for i in obj:
                temp = {}
                dic_str = (i.items)
                dic_data = json.loads(dic_str)
                for j in dic_data.keys():
                    if que in j :
                        temp[j] = dic_data[j]
                if temp :
                    temp = sorted(temp.items(), key = lambda x: x[1])
                    final_data[i.name] = temp
                    
                    
            return render(request, 'result.html', {'data': final_data})
        # return render(request, 'result.html', {'data': obj})

    else :
        data = query_form()
    return render(request, 'home.html', {'form':data})