from django.test import TestCase
from matricula.models import Animal

class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(abrev="1BAC", denom="Bachiller", imagen="fotos/yo.png")
       

    def test_curso(self):
        """Animals that can speak are correctly identified"""
        bac = Curso.objects.get(abrev="1BAC")
        bachiller = Curso.objects.get(denom="Bachiller")
        self.assertEqual(bac.speak(), 'La abreviatura es  "1BAC"')
        self.assertEqual(bachiller.speak(), 'Y el nombre es "Bachiller"')

        