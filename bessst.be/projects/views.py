# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from projects.models import Project
from axis.models import Axis

def projects(request, slug=False):
    tpl_params = {}
    tpl_params['object_list'] = Project.objects.filter(published=True)
    tpl_params['axis_list'] = Axis.objects.all()
    if slug:
        tpl_params['slug'] = slug
    return render_to_response("projects/project_list.html", tpl_params, context_instance = RequestContext(request))
