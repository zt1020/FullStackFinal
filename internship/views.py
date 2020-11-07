"""
views.py
Contributors: Harshani, Snehitha
Created : 11/3/2020
Updated : 11/7/2020
"""
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    """
    This creates class based HomepageView
    """
    template_name = 'index.html'
