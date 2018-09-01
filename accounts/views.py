from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Account

class ViewAllBalances(TemplateView):
	template_name = 'account/balances.html'
	def get_context_data(self, **kwargs):
		context = super(ViewAllBalances, self).get_context_data(**kwargs)
		context.update({'queryset': Account.objects.all()})
		return context

# Create your views here.

