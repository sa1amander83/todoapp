from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView

from todo.forms import LoginForm, RegisterUserForm, AddTodoForm
from todo.models import TodoModel


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_success_url(self):

        return reverse_lazy('profile', self.request.user)

    def form_valid(self, form):

        form_data = form.cleaned_data

        form_data['data'] = form.cleaned_data['username']
        # nextform = RegisterUserFormNextStep(initial=form_data)
        getuser = User.objects.get(username=form.cleaned_data['username'])
        print(getuser)
        if getuser.pk == 1:
            login(self.request, getuser)

        obj = get_object_or_404(User, pk=getuser.pk - 1)
        print(obj)
        if obj:
            login(self.request, getuser)
            return redirect('profile', getuser)

        else:
            return redirect('register', user=form_data['username'])


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form, **kwargs):
        user = form.save()

        login(self.request, user)

        return redirect('profile', user)
        # else:
        #     messages.error(self.request, 'Неверно ')
        # return redirect('register')

def addtodo(request, todo_user):
    pass
    form = AddTodoForm(request.POST or None)
    # if request.method=='POST':
    #
    #     if form.is_valid():
    #         form.save()
    #
    #         all_tasks= TodoModel.objects.filter(todo_user__user__username=todo_user)
    #         messages.success(request,'Задача была успешно добавлена!')
    #         return render(request, 'profile.html', {'todo_list':all_tasks)
    # else:
    #     # all_tasks = TodoModel.objects.filter(todo_user__user__username=todo_user)
    #     return render(request, 'profile.html', )





class AddTodo(LoginRequiredMixin, CreateView):
    form_class = AddTodoForm
    template_name = 'addform.html'
    success_url = reverse_lazy('profile')
    # slug_url_kwarg = 'runner'
    login_url = reverse_lazy('profile')

    def get_queryset(self):
        return TodoModel.objects.all()
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        return context

    def post(self, request, *args, **kwargs):
        form =  self.form_class(request.POST)
        user=self.kwargs.get('todo_user')
        if form.is_valid():

            item = form.save(commit=False)
            print(self.request.user.pk)
            userid=User.objects.get(pk=self.request.user.pk)
            item.user_id=userid.id
            print(item.user_id)
            item.short = form.cleaned_data['todo_short_description']
            item.full = form.cleaned_data['todo_full_description']
            item.start_data = form.cleaned_data['todo_start_date']
            item.start_time = form.cleaned_data['todo_start_time']
            userid = User.objects.get(pk=self.request.user.pk)
            item.todo_user_id=userid.id
            item.save()
            return redirect('profile', todo_user=user)
        else:
            messages.error(request,('Errorrs'))
            return redirect('profile',todo_user=user)




@login_required()
def deltodo(request, todo_user, todo_id):
    task = TodoModel.objects.get(id=todo_id)
    task.delete()
    return redirect('profile', todo_user=todo_user )



@login_required()
def edittodo(request,  todo_user, todo_id):
    task = TodoModel.objects.get(id=todo_id)
    print(task)
    form = AddTodoForm(instance=task)
    if  request.method=='POST':
        form = AddTodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("profile", todo_user=todo_user)
        return
    return render(request, "editpage.html", {"form": form, 'todo_id':todo_id})

@login_required()
def update_status(request, todo_user, todo_id):


    if request.method == 'POST':

        todo = TodoModel.objects.get(pk=todo_id)

        todo.todo_status = True
        todo.save()

    return redirect('profile', todo_user=todo_user)

def logout_user(request):
    logout(request)
    return redirect('login')




class Profile(DetailView):
    model = TodoModel
    template_name = 'profile.html'
    slug_url_kwarg = "todo_user"
    slug_field = "todo_user"

    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None

    context_object_name = 'profile'

    def get_object(self, queryset=None):

        slug = self.kwargs.get('todo_user', '')
        print(slug)
        try:
            return slug
        except:
            raise Http404('Ох, нет объекта;)')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = TodoModel.objects.filter(todo_user__username=self.kwargs['todo_user']).order_by('id')

        # task_id = self.kwargs['task_id']
        # is_true = self.kwargs['is_true']

        return context

    def post(self, request, *args, **kwargs):
        task_id=request.POST.get('task_id')
        is_true = request.POST.get('is_true')
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        todo = TodoModel.objects.get(id=task_id)
        if is_true == 'true':
            todo.todo_status = True
            todo.save()
        else:
            todo.todo_status = False
            todo.save()
        return self.render_to_response(context)


    def update_status(self, todo_user, todo_id):

        if self.request.method == 'POST':
            return redirect('profile', todo_user=todo_user)


def page_not_found_view(request, exception=None):
    return render(request, '404.html', status=404)