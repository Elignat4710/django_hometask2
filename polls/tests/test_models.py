from django.test import TransactionTestCase
from ..models import (
    Company, Manager, Worker, Work,
    WorkPlace, NEW, WorkTime
)
from django.urls import reverse
from django.utils import timezone


class CompanyModelTest(TransactionTestCase):
    def setUp(self):
        self.company = Company.objects.create(name='company1')

    def test_company(self):
        self.assertIsNotNone(self.company.id)
        self.assertEqual(self.company.name, 'company1')


class ManagerModelTest(TransactionTestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.manager = Manager.objects.create(
            name='manage_1', com_name=self.company
            )

    def test_manager(self):
        self.assertIsNotNone(self.manager.id)
        self.assertEqual(self.manager.com_name, 'company_1')
        self.assertEqual(self.manager.name, 'manage_1')


class WorkerModelTest(TransactionTestCase):
    def setUp(self):
        self.worker = Worker.objects.create(name='worker_1')

    def test_worker(self):
        self.assertIsNotNone(self.worker.id)
        self.assertEqual(self.worker.name, 'worker_1')

    def test_context_worker(self):
        response = self.client.get(
            reverse('worker_detail', kwargs={'pk': self.worker.id})
        )
        self.assertEqual(response.context['worker'], self.worker)


class WorkModeltest(TransactionTestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.work = Work.objects.create(
            name='work_1', com_name=self.company
        )

    def test_work(self):
        self.assertIsNotNone(self.work)
        self.assertEqual(self.work.name, 'work_1')
        self.assertEqual(self.work.com_name, 'company_1')


class WorkPlaceModelTest(TransactionTestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.work = Work.objects.create(
            name='work_1', com_name=self.company
        )
        self.worker = Worker.objects.create(name='worker_1')
        self.workplace = WorkPlace.objects.create(
            name='workplace_1',
            worker_name=self.worker,
            work_name=self.work,
            status=1
        )

    def test_workplace(self):
        self.assertIsNotNone(self.workplace.pk)
        self.assertEqual(self.workplace.worker_name, self.worker)
        self.assertEqual(self.workplace.status, NEW)


class WorkTimeModelTest(TransactionTestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.work = Work.objects.create(
            name='work_1', com_name=self.company
        )
        self.worker = Worker.objects.create(name='worker_1')
        self.worktime = WorkTime.objects.create(
            date_start=timezone.now(),
            date_end=timezone.now(),
            status=NEW,
            worker=self.worker,
            work=self.work
        )

    def test_worktime(self):
        self.assertIsNotNone(self.worktime)

    def test_default_status(self):
        worktime_new = WorkTime.objects.create(
            date_start=timezone.now(),
            date_end=timezone.now(),
            # status=NEW,
            worker=self.worker,
            work=self.work
        )
        self.assertEqual(worktime_new.status, NEW)
