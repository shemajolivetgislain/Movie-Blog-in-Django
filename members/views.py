from members.form import RegisterForm, UpdateForm, UpdateProfileForm
from django.shortcuts import get_list_or_404, render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from blog.models import Post, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def UserEditProfile(request):
    if request.method == 'POST':
        u_form = UpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('show_profile', request.user.id)

    else:
        u_form = UpdateForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'registration/edit_profile.html', context)


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        members = get_list_or_404(Profile, id=self.kwargs['pk'])
        posts = Post.objects.filter(author=members[0].id)
        member = members[0]
        number_of_posts = len(posts)
        context = {
            'member': member,
            'posts': posts,
            'number_of_posts': number_of_posts
        }
        return context
