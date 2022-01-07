from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views import View
from home.models import Feature, Slider, WorkingProcess
from about.models import About, Vision, Team, Choice
from contact.models import Contact
from gallery.models import Gallery
from service.models import Service

from .forms import (ContactUpdateForm, GalleryUpdateForm, ServiceUpdateForm,
                    FeatureUpdateForm, WorkingProcessUpdateForm, SliderUpdateForm,
                    AboutUpdateForm, TeamUpdateForm, ChoiceUpdateForm, VisionUpdateForm,
                    TeamCreateForm, WorkingProcessCreateForm, CreateGalleryForm, SliderCreateForm,
                    FeatureCreateForm, ChoiceCreateForm, VisionCreateForm, ServiceCreateForm
                    )
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Dashboard
class DashboardView(View):
    def get(self, request):
        print(request.session)
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "Multi International"
        return render(request, 'menu/index.html', greeting)


# -------Home-------
# Feature
class FeatureView(LoginRequiredMixin, View):
    def get(self, request):
        # b = Feature.objects.last()
        # print(b.right_title)
        # greeting = {}
        # greeting['title'] = "Home"
        # greeting['pageview'] = "Feature"
        # greeting['feature'] = Feature.objects.all(),

        context = {
            'feature': Feature.objects.all(),
            'title': "Feature",
            'pageview': "Home"
        }
        return render(request, 'home/feature.html', context)


# edit-feature
class FeatureUpdateView(LoginRequiredMixin, UpdateView):
    model = Feature
    form_class = FeatureUpdateForm
    success_url = reverse_lazy('feature')
    template_name = 'home/edit-feature.html'

    success_message = "feature was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Feature"
        context["pageview"] = "Home"
        return context


# feature create
@login_required
def create_feature(request):
    template_name = 'home/create-feature.html'
    message = ''

    if request.method == 'GET':
        feature_form = FeatureCreateForm(request.GET or None)

    elif request.method == 'POST':
        feature_form = FeatureCreateForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if feature_form.is_valid():
            obj = feature_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('Feature')

    return render(request, template_name, {'feature_form': feature_form, 'message': message, 'title': "Create Feature", 'pageview': "Home"})


# delete Feature
@login_required
def delete_feature(request, id):
    obj = get_object_or_404(Feature, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('feature')
    context = {
        'obj': Feature.objects.get(id=id),
        'title': "Delete Feature",
        'pageview': "Home"
    }

    return render(request, "home/delete-feature.html", context)


# Slider
class SliderView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'slider': Slider.objects.all(),
            'title': "Slider",
            'pageview': "Home"
        }
        return render(request, 'home/slider.html', context)


# edit-slider
class SliderUpdateView(LoginRequiredMixin, UpdateView):
    model = Slider
    form_class = SliderUpdateForm
    success_url = reverse_lazy('slider')
    template_name = 'home/edit-slider.html'

    success_message = "Slider was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Slider"
        context["pageview"] = "Home"
        return context


# slider create
@login_required
def create_slider(request):
    template_name = 'home/create-slider.html'
    message = ''

    if request.method == 'GET':
        slider_form = SliderCreateForm(request.GET or None)

    elif request.method == 'POST':
        slider_form = SliderCreateForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if slider_form.is_valid():
            obj = slider_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('slider')

    return render(request, template_name, {'slider_form': slider_form, 'message': message, 'title': "Create Slider", 'pageview': "Home"})


# delete slider
@login_required
def delete_slider(request, id):
    obj = get_object_or_404(Slider, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('slider')
    context = {
        'obj': Slider.objects.get(id=id),
        'title': "Delete Slider",
        'pageview': "Home"
    }

    return render(request, "home/delete-slider.html", context)


# Working Process
class WorkingProcessView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'process': WorkingProcess.objects.all(),
            'title': "Working Process",
            'pageview': "Home"
        }
        return render(request, 'home/working-process.html', context)


# edit-workingProcess
class WorkingProcessUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkingProcess
    form_class = WorkingProcessUpdateForm
    success_url = reverse_lazy('process')
    template_name = 'home/edit-working-process.html'

    success_message = "Working Process was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Working Process"
        context["pageview"] = "Home"
        return context


# create process
@login_required
def create_process(request):
   if request.method == "POST":
    form = WorkingProcessCreateForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('process')
   else:
      form = WorkingProcessCreateForm()
   return render(request, 'home/create-working-process.html', {'form': form, 'title': "Create Working Process", 'pageview': "Home"})

# def delete_process(request, id):
#    emp = WorkingProcess.objects.get(pk=id)
#    emp.delete()
#    return redirect('process')


# delete process
@login_required
def delete_process(request, id):
    # obj = WorkingProcess.objects.get(id=pk).delete()
    # return redirect('process')
    obj = get_object_or_404(WorkingProcess, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('process')
    context = {
        'obj': WorkingProcess.objects.get(id=id),
        'title': "Delete Working Process",
        'pageview': "Home"
    }

    return render(request, "home/delete-process.html", context)


# ------about-------
# About
class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'about': About.objects.all(),
            'title': "About",
            'pageview': "About",
        }
        return render(request, 'about/about.html', context)


# edit-about
class AboutUpdateView(LoginRequiredMixin, UpdateView):
    model = About
    form_class = AboutUpdateForm
    success_url = reverse_lazy('dash-about')
    template_name = 'about/edit-about.html'

    success_message = "About was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update About"
        context["pageview"] = "About"
        return context


# Choice
class ChoiceView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'choice': Choice.objects.all(),
            'title': "Choice",
            'pageview': "About"
        }
        return render(request, 'about/choice.html', context)


# edit-choice
class ChoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Choice
    form_class = ChoiceUpdateForm
    success_url = reverse_lazy('choice')
    template_name = 'about/choice-edit.html'

    success_message = "About was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Choice"
        context["pageview"] = "About"
        return context


# choice create
@login_required
def create_choice(request):
    template_name = 'about/create-choice.html'
    message = ''

    if request.method == 'GET':
        choice_form = ChoiceCreateForm(request.GET or None)

    elif request.method == 'POST':
        choice_form = ChoiceCreateForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if choice_form.is_valid():
            obj = choice_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('Choice')

    return render(request, template_name, {'choice_form': choice_form, 'message': message, 'title': "Create Choice", 'pageview': "About"})


# delete Choice
@login_required
def delete_choice(request, id):
    obj = get_object_or_404(Choice, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('choice')
    context = {
        'obj': Choice.objects.get(id=id),
        'title': "Delete Choice",
        'pageview': "About"
    }

    return render(request, "about/delete-choice.html", context)


# Vision
class VisionView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'vision': Vision.objects.all(),
            'title': "Vision",
            'pageview': "About"
        }
        return render(request, 'about/vision.html', context)


# edit-vision
class VisionUpdateView(LoginRequiredMixin, UpdateView):
    model = Vision
    form_class = VisionUpdateForm
    success_url = reverse_lazy('vision')
    template_name = 'about/edit-vision.html'

    success_message = "Vision was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Vision"
        context["pageview"] = "About"
        return context


# create vision
@login_required
def create_vision(request):
    template_name = 'about/create-vision.html'
    message = ''

    if request.method == 'GET':
        vision_form = VisionCreateForm(request.GET or None)

    elif request.method == 'POST':
        vision_form = VisionCreateForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if vision_form.is_valid():
            obj = vision_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('Vision')

    return render(request, template_name, {'vision_form': vision_form, 'message': message, 'title': "Create Vision", 'pageview': "About"})


# delete Vision
@login_required
def delete_vision(request, id):
    obj = get_object_or_404(Vision, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('vision')
    context = {
        'obj': Vision.objects.get(id=id),
        'title': "Delete Vision",
        'pageview': "About"
    }

    return render(request, "about/delete-vision.html", context)


# team
class TeamView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'team': Team.objects.all(),
            'title': "Team",
            'pageview': "About"
        }
        return render(request, 'about/team.html', context)


# edit team
class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamUpdateForm
    success_url = reverse_lazy('team')
    template_name = 'about/edit-team.html'

    success_message = "Team was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Team"
        context["pageview"] = "About"
        return context


# Create team
@login_required
def create_team(request):
    template_name = 'about/create-team.html'
    message = ''

    if request.method == 'GET':
        info_form = TeamCreateForm(request.GET or None)

    elif request.method == 'POST':
        info_form = TeamCreateForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if info_form.is_valid():
            obj = info_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('team')

    return render(request, template_name, {'info_form': info_form, 'message': message, 'title': "Create Team", 'pageview': "About"})


# def delete_team(request, pk):
#     Team.objects.get(id=pk).delete()
#     return redirect('team')

# delete Team
@login_required
def delete_team(request, id):
    obj = get_object_or_404(Team, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('team')
    context = {
        'obj': Team.objects.get(id=id),
        'title': "Delete Team",
        'pageview': "About"
    }

    return render(request, "about/delete-team.html", context)


# --------Contact--------
# contact
class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'contact': Contact.objects.all(),
            'title': "Contact",
            'pageview': "Contact"
        }
        return render(request, 'contact/contact.html', context)


# edit-contact
class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactUpdateForm
    success_url = reverse_lazy('dash-contact')
    template_name = 'contact/edit-contact.html'

    success_message = "Contact was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Contact Information"
        context["pageview"] = "Contact"
        return context


# -------gallery------
# gallery
class GalleryView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'gallery': Gallery.objects.all(),
            'title': "Gallery",
            'pageview': "Gallery"
        }
        return render(request, 'gallery/gallery.html', context)


# edit-gallery
class GalleryUpdateView(LoginRequiredMixin, UpdateView):
    model = Gallery
    form_class = GalleryUpdateForm
    success_url = reverse_lazy('dash-gallery')
    template_name = 'gallery/edit-gallery.html'

    success_message = "gallery was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Gallery"
        context["pageview"] = "Gallery"
        return context


# create gallery
@login_required
def create_gallery(request):
   if request.method == "POST":
    # form = CreateGalleryForm(request.POST)
    form = CreateGalleryForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img_obj = form.instance
      return render(request, 'gallery/create-gallery.html', {'form': form, 'img_obj': img_obj})

   else:
      form = CreateGalleryForm()
   return render(request, 'gallery/create-gallery.html', {'form': form, 'title': "Create Gallery", 'pageview': "Gallery"})


# delete Gallery
@login_required
def delete_gallery(request, id):
    obj = get_object_or_404(Gallery, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('gallery')
    context = {
        'obj': Gallery.objects.get(id=id),
        'title': "Delete Gallery",
        'pageview': "Gallery"
    }

    return render(request, "gallery/delete-gallery.html", context)


# -------service------
# service
class ServiceView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'service': Service.objects.all(),
            'title': "Service",
            'pageview': "Service"
        }
        return render(request, 'service/service.html', context)


# edit-service
class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('dash-service')
    template_name = 'service/edit-service.html'

    success_message = "Service was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Service"
        context["pageview"] = "Service"
        return context


# create service
@login_required
def create_service(request):
    template_name = 'service/create-service.html'
    message = ''
    # context = {}
    # context["title"] = "Update Service"
    # context["pageview"] = "Service"
    # print(context)

    if request.method == 'GET':
        service_form = ServiceCreateForm(request.GET or None)

    elif request.method == 'POST':
        service_form = ServiceCreateForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if service_form.is_valid():
            obj = service_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('Service')

    return render(request, template_name, {'service_form': service_form, 'message': message, 'title': "Create Service", 'pageview': "Service"})


# delete service
@login_required
def delete_service(request, id):
    obj = get_object_or_404(Service, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('service')
    context = {
        'obj': Service.objects.get(id=id),
        'title': "Delete Service",
        'pageview': "Gallery"
    }

    return render(request, "service/delete-service.html", context)
