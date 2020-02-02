from django.test import TestCase
from Student.models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            first_name="first_name",
            last_name="last_name",
            email="test@gmail.com",
            phone="0999999999",
        )

    def test_student_list(self):
        count = Student.objects.all().count()
        self.assertTrue(count)

    def test_student_edit(self):
        f = Student.objects.get(first_name="first_name")
        _l = Student.objects.get(last_name="last_name")

        self.assertEqual(f.first_name, 'first_name')
        self.assertEqual(_l.last_name, 'last_name')
