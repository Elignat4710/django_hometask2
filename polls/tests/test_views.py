from django.test import TestCase
from django.urls import reverse
from polls.models import (
    Company, Manager, Work, Worker,
    WorkTime, NEW, WorkPlace
    )
from django.utils import timezone


class CompanyListViewTest(TestCase):
    def setUp(self):
        Company.objects.create(
            name='company_1'
        )

    def test_company_list(self):
        response = self.client.get(reverse('companies_list'))
        self.assertTrue(response.context['companies'])


class ManagerListViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        Manager.objects.create(
            name='manager_1',
            com_name=self.company
        )

    def test_manager_list(self):
        response = self.client.get(reverse(
            'manager_list',
            kwargs={'pk': self.company.id}))
        self.assertTrue(response.context['managers'])


class CompanyDetailViewtest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )

    def test_company_detail(self):
        response = self.client.get(reverse(
            'company_details',
            kwargs={'pk': self.company.id}))
        self.assertEqual(response.status_code, 200)


class WorkCreateViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.work = Work.objects.create(
            name='work',
            com_name=self.company
        )

    def test_work_create_post(self):
        work_dict = {
            'name': 'work_1',
            'com_name': self.company.id
        }
        url = reverse('work_create', kwargs={'pk': self.company.id})
        self.client.post(url, work_dict)
        work = Work.objects.last()
        self.assertEqual(work.name, 'work_1')

    def test_work_create_get(self):
        response = self.client.get(reverse(
            'work_create', kwargs={'pk': self.company.id}
        ))
        self.assertIsNotNone(response)


class WorkTimeCreateViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.work = Work.objects.create(
            name='work',
            com_name=self.company
        )
        self.worker = Worker.objects.create(
            name='worker_1'
        )
        self.worktime = WorkTime.objects.create(
            date_start=timezone.now(),
            date_end=timezone.now(),
            worker=self.worker,
            work=self.work
        )

    def test_work_time_get(self):
        response = self.client.get(reverse(
            'worktime_create', kwargs={'pk': self.worker.id}
        ))
        self.assertEqual(response.status_code, 200)


class AssignWorkerViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.work = Work.objects.create(
            name='work',
            com_name=self.company
        )
        self.worker = Worker.objects.create(
            name='worker_1'
        )

    def test_assign_worker_post(self):
        data_dict = {
            'name': 'work_place_1',
            'worker_name': self.worker.id,
            'work_name': self.work.id,
            'status': NEW
        }
        url = reverse('assign_worker', kwargs={
            'company_id': self.company.id,
            'work_id': self.work.id
        })
        self.client.post(url, data_dict)
        self.assertIsNotNone(WorkPlace.objects.all())
