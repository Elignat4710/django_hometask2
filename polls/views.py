from django.shortcuts import get_object_or_404
from .models import (
    Company, Work, Worker, WorkTime, Manager
    )
from .forms import (
    WorkCreate, WorktimeCreateForm, AssignWorkerForm
)
from django.views.generic import (
    CreateView, ListView, DetailView
)
from django.urls import reverse_lazy
import logging


logger = logging.getLogger('sentry_logger')


class CompanyList(ListView):
    model = Company
    template_name = 'polls/company_list.html'
    context_object_name = 'companies'


class ManagerList(ListView):
    model = Manager
    template_name = 'polls/manager_list.html'
    context_object_name = 'managers'

    def get_queryset(self):
        com_name = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return Manager.objects.filter(com_name=com_name)


class CompanyDetail(DetailView):
    model = Company
    template_name = 'polls/companies_details.html'
    context_object_name = 'company'


class WorkerList(ListView):
    model = Worker
    template_name = 'polls/worker_list.html'
    context_object_name = 'worker_list'


class WorkerDetail(DetailView):
    model = Worker
    template_name = 'polls/worker_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = get_object_or_404(Worker, pk=self.kwargs.get('pk'))
        context['worktimes'] = WorkTime.objects.filter(worker=worker)
        # context['works'] = Work.objects.filter(worktime__worker=worker)
        return context


class WorktimeCreate(CreateView):
    template_name = 'polls/worktime_create.html'
    form_class = WorktimeCreateForm

    def get_success_url(self):
        worker_id = self.kwargs.get('pk')
        return reverse_lazy('worker_detail', kwargs={'pk': worker_id})

    def get_initial(self):
        worker = get_object_or_404(Worker, id=self.kwargs.get('pk'))
        return {'worker': worker}

    def form_valid(self, form):
        form.save()
        data = self.request.POST
        logger.debug(
            'start: %s, end: %s, worker: %s, status:%s',
            data['date_start'], data['date_end'], data['worker'],
            data['status'])
        logger.info('worktime create')
        return super().form_valid(form)


class WorkCreate(CreateView):
    template_name = 'polls/create_work.html'
    form_class = WorkCreate

    def get_success_url(self):
        company_id = self.kwargs.get('pk')
        return reverse_lazy('company_details', kwargs={'pk': company_id})

    def get_initial(self):
        self.company = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return {'com_name': self.company}

    def form_valid(self, form):
        form.save()
        data = self.request.POST
        # print(data)
        logger.debug(
            'name work: %s, company name: %s',
            data['name'], data['com_name']
        )
        logger.info('create work')
        return super().form_valid(form)

    


class AssignWorker(CreateView):
    template_name = 'polls/assign_worker.html'
    form_class = AssignWorkerForm

    def get_initial(self):
        work_name = get_object_or_404(Work, id=self.kwargs.get('work_id'))
        return {'work_name': work_name}

    def get_success_url(self):
        company_id = self.kwargs.get('company_id')
        return reverse_lazy('company_details', kwargs={'pk': company_id})

    def form_valid(self, form):
        form.save()
        data = self.request.POST
        logger.debug('worker: %s, work:%s',
                    data['worker_name'], data['work_name'])
        logger.info('assign worker')
        return super().form_valid(form)
