from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Company, Shareholder
from .forms import ShareholderFormSet, CompanyForm


class CompanySearchView(ListView):
    """ Avalehe otsinguvaade """
    template_name = 'companies/home.html'
    model = Company

    def get_queryset(self):
        company = self.request.GET.get('company')
        shareholder = self.request.GET.get('shareholder')
        object_list = ''
        if company:
            object_list = Company.objects.filter(
                Q(name__icontains=company.strip()) | Q(reg_code__icontains=company.strip()))
        if shareholder:
            shareholders = (Shareholder.objects.filter(
                Q(name__icontains=shareholder.strip()) | Q(code__icontains=shareholder.strip()))
                            .values_list('company_id'))
            if company:
                object_list = object_list.filter(Q(id__in=shareholders))
            else:
                object_list = Company.objects.filter(Q(id__in=shareholders))
        return object_list


class CompanyDetailView(DetailView):
    """ Osaühingu andmete vaade """
    template_name = 'companies/company_details.html'
    model = Company
    slug_field = 'reg_code'
    slug_url_kwarg = 'reg_code'


class CompanyCreateView(CreateView):
    """ Osaühingu asutamise vaade """
    form_class = CompanyForm
    model = Company

    def get_context_data(self, **kwargs):
        data = super(CompanyCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['shareholders'] = ShareholderFormSet(self.request.POST)
        else:
            data['shareholders'] = ShareholderFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        shareholders = context['shareholders']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save(commit=False)
                if shareholders.is_valid():
                    shareholders.instance = self.object
                    total_capital = 0
                    for shareholder in shareholders:
                        shareholder.instance.is_founder = True
                        if shareholder.cleaned_data:
                            if not shareholder.cleaned_data['DELETE']:
                                total_capital += shareholder.instance.share
                    if total_capital == self.object.total_capital:
                        self.object = form.save()
                        shareholders.save()
                        return redirect('/companies/company/' + self.object.reg_code)
                    else:
                        message = ('Osaühingu osanike osakapitalide summa '
                                   'peab olema võrdne kogukapitaliga.')  # parim lause
                        return render(self.request, 'companies/company_form.html',
                                      {'form': form, 'shareholders': shareholders, 'error_message': message})
                else:
                    return render(self.request, 'companies/company_form.html',
                                  {'form': form, 'shareholders': shareholders})


class CompanyUpdateView(UpdateView):
    """ Osaühingu osanike muutmise/lisamise vaade """
    template_name = 'companies/edit_shareholders.html'
    model = Company
    form_class = ShareholderFormSet
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def form_valid(self, form):
        shareholders = form
        with transaction.atomic():
            total_capital = 0
            if shareholders.is_valid():
                for shareholder in shareholders:
                    if shareholder.cleaned_data:
                        if not shareholder.cleaned_data['DELETE']:
                            total_capital += shareholder.instance.share
                if total_capital >= 2500:
                    self.object.total_capital = total_capital
                    self.object.save()
                    shareholders.instance = self.object
                    shareholders.save()
                    return redirect('/companies/company/' + self.object.reg_code)
                else:
                    message = 'Osakapitalide summa peab olema võrdne kogukapitaliga ning vähemalt 2500€.'
                    return render(self.request, 'companies/edit_shareholders.html',
                                  {'company': self.object, 'form': form, 'error_message': message})
            else:
                return render(self.request, 'companies/edit_shareholders.html',
                              {'company': self.object, 'form': form})
