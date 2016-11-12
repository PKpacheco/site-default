from django.views.generic import TemplateView, View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse as r
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from contents.models import Content


class HomeSiteView(View):
    model = Content
    context_object_name = 'contents'
    template_name = 'homesite/index.html'
