from django.shortcuts import render

def exmaple_view(request):
    #localhost:8000/my_app/example.html
    return render(request, 'my_app/example.html')

# def variable_view(request):

#     my_var = {'first_name':'johnWick', 'last_name':'Smith',
#         'some_list':[1,2,3] , 'some_dict':{'inside_key':'inside_value'}
#     }
#     #localhost:8000/my_app/variable.html
#     return render(request, 'my_app/variables.html', context=my_var)

def variable_view(request):
    return render(request, 'my_app/variables.html')