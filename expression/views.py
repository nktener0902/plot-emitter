from django.views import generic

from .models import InputQuery
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'expression/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return InputQuery.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class HistoryView(LoginRequiredMixin, generic.ListView):
    model = InputQuery
    template_name = 'expression/history.html'

    def get_queryset(self):
        return InputQuery.objects.filter(pub_date__lte=timezone.now())


