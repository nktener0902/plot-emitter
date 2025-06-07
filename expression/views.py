from decimal import Decimal

import numpy.random as npr
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from sympy import *

from expression.models import InputQuery


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "expression/index.html"
    context_object_name = "latest_query_list"

    def get_queryset(self):
        return InputQuery.objects.filter(published_at__lte=timezone.now()).order_by(
            "-published_at"
        )[:30]

    def post(self, request, *args, **kwargs):
        context = {
            "expression": request.POST["expression"],
            "noise_function": request.POST["noise_function"],
            "noise": request.POST.get("noise"),
            "fineness": request.POST["fineness"],
            "x_min_range": request.POST["x_min_range"],
            "x_max_range": request.POST["x_max_range"],
            "comment": request.POST["comment"],
        }
        x = Symbol("x")
        y = Symbol("y")
        context = deserialized_expression(context, x, y)
        plots_list = []
        p_x = Decimal(context["x_min_range"])
        while round(float(p_x), 7) <= float(context["x_max_range"]):
            noise_val = 0
            if context["noise_function"] == "none":
                noise_val = 0
            elif context["noise_function"] == "uniform":
                noise_val = npr.rand() * float(context["noise"])
            elif context["noise_function"] == "gaussian":
                noise_val = npr.normal(0, float(context["noise"]))
            p_y = context["deserialized_expression"].subs([(x, float(p_x))])
            f_p_y = 0
            try:
                f_p_y = float(p_y)
            except:
                context["plots"] = []
                context["message"] = (
                    "Too complex calcuration such as infinit values. Please review your expression."
                )
                return render(request, "expression/index.html", context)
            plots_list.append({"x": round(float(p_x), 7), "f": f_p_y + noise_val})
            p_x += Decimal(context["fineness"])
        context["plots"] = plots_list
        context["message"] = ""
        iq = create_input_query(context)
        iq.save()
        return render(request, "expression/index.html", context)


def create_input_query(context):
    if context["noise_function"] == "none":
        return InputQuery(
            published_at=timezone.now(),
            expression=context["expression"],
            noise_function=context["noise_function"],
            noise=None,
            fineness=float(context["fineness"]),
            x_min_range=float(context["x_min_range"]),
            x_max_range=float(context["x_max_range"]),
            comment=context["comment"],
        )
    else:
        return InputQuery(
            published_at=timezone.now(),
            expression=context["expression"],
            noise_function=context["noise_function"],
            noise=float(context["noise"]),
            fineness=float(context["fineness"]),
            x_min_range=float(context["x_min_range"]),
            x_max_range=float(context["x_max_range"]),
            comment=context["comment"],
        )


def deserialized_expression(context, x, y):
    try:
        context["deserialized_expression"] = eval(context["expression"])
    except:
        context["deserialized_expression"] = None
        context["message"] = (
            "Invalid expressoin. Please refer to http://mattpap.github.io/scipy-2011-tutorial/html/basics.html."
        )
    return context


class HistoryView(LoginRequiredMixin, generic.ListView):
    model = InputQuery
    template_name = "expression/history.html"
    context_object_name = "histories"

    def get_queryset(self):
        """Return the last five published questions."""
        return InputQuery.objects.order_by("-published_at")[:30]
