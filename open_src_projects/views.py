from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse
from django.views import generic
from django.template import RequestContext
from .forms import OpenSrcProjectForm
from django.utils import timezone


from .models import OpenSrcProject


class IndexView(generic.ListView):
    template_name = 'open_src_projects/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return OpenSrcProject.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = OpenSrcProject
    template_name = 'open_src_projects/detail.html'



class ResultsView(generic.DetailView):
    model = OpenSrcProject
    template_name = 'open_src_projects/results.html'

def add_project(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = OpenSrcProjectForm(request.POST)

        # Have we been provided a valid form?
        if form.is_valid():
            # Save new project
            model_instance = form.save(commit=False)
            model_instance.pub_date = timezone.now()
            model_instance.save()
            return redirect('open_src_projects:index')
        else:
            # Print errors
            print form.errors
    else:
        form = OpenSrcProjectForm()

    return render(request, 'open_src_projects/add_project.html', {'form':form})

def vote(request, project_id):
    project = get_object_or_404(OpenSrcProject, pk=project_id)

    if request.method == 'POST':
        project.num_votes += 1
        project.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('open_src_projects:detail', args=(project.id,)))
    else:
        return render(request, 'open_src_projects/detail.html', {
            'open_src_project': project,
            'error_message': 'Something went wrong'
        })

def add_comment(request, project_id):
    context = RequestContext(request)
    project = get_object_or_404(OpenSrcProject, pk=project_id)

    if request.method == 'POST':
        project.comment_set.create(comment_text = request.POST['comment_text'])

        return HttpResponseRedirect(reverse('open_src_projects:detail', args=(project.id,)))
    else:
        return render(request, 'open_src_projects/detail.html', {
            'open_src_project': project,
            'error_message': 'Something went wrong'
        })
