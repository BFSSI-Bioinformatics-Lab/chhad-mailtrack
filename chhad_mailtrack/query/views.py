from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from api.models import Query
from chhad_mailtrack.users.models import User
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# from . import forms
# Create your views here.


class QueryView(LoginRequiredMixin, ListView):
    model = Query
    template_name = 'Query/home_page.html'
    context_object_name = 'queries'
    # paginate_by = 20
#     order entries from newest to oldest
    ordering = ['-updated']

    # def get_queryset(self):
    #     qs = Query.objects.all()
        # entry_number_query = self.request.GET.get('entry_id')
        # entry_status_query = self.request.GET.get('entry_status')
        # entry_keywords_query = self.request.GET.get('entry_keywords')
        # entry_quarter_query = self.request.GET.get('entry_quarter')
        # entry_text_query = self.request.GET.get('entry_content')
        # sort_by = self.request.GET.get('sort_by')
        # sort_order = self.request.GET.get('sort_order')
        #
        # # Use elif to make search "OR" and use if to make it "AND"
        # # Filtering logic based on search criteria
        # if entry_number_query != '' and entry_number_query is not None:
        #     qs = qs.filter(id__icontains=entry_number_query)
        # if entry_status_query != '' and entry_status_query is not None:
        #     qs = qs.filter(Q(status__icontains=entry_status_query) | Q(
        #         status__icontains=entry_status_query))
        # if entry_keywords_query != '' and entry_keywords_query is not None:
        #     qs = qs.filter(key_words__icontains=entry_keywords_query)
        # if entry_quarter_query != '' and entry_quarter_query is not None:
        #     qs = qs.filter(quarter__icontains=entry_quarter_query).distinct()
        # if entry_text_query != '' and entry_text_query is not None:
        #     qs = qs.filter(Q(query_response__icontains=entry_text_query))
        #     # | Q( author__name__icontains=entry_type_author_query))

        # Sorting logic based on selected option
        # if sort_by:
        #     if sort_order == 'asc':
        #         if sort_by == 'id':
        #             qs = qs.order_by('id')
        #         elif sort_by == 'rau':
        #             qs = qs.order_by('rau')
        #         elif sort_by == 'number_RDIMS':
        #             qs = qs.order_by('number_RDIMS')
        #     elif sort_order == 'desc':
        #         if sort_by == 'id':
        #             qs = qs.order_by('-id')
        #         elif sort_by == 'rau':
        #             qs = qs.order_by('-rau')
        #         elif sort_by == 'number_RDIMS':
        #             qs = qs.order_by('-number_RDIMS')
        #
        # if not sort_by:
        #     qs = qs.order_by('-updated')
        #
        # return qs
        # return qs.order_by('-updated')

# class UserListView(LoginRequiredMixin, ListView):
#     model = Query
#     template_name = 'Query/user_query.html'
#     context_object_name = 'queries'
#     paginate_by = 5
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Query.objects.filter(evaluator=user).order_by('-updated')

class QueryDetailView(LoginRequiredMixin, DetailView):
    model = Query
    template_name = 'Query/detail_page.html'
    context_object_name = 'query'
