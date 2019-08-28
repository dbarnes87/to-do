from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='Learn React')
        Todo.objects.create(description='Learn how to use the react js library in order to add it to your resume, LinkedIn profile, and portfolio.')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'Learn React')
    
    def test_description_content(self):
        todo = Todo.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'Learn how to use the react js library in order to add it to your resume, LinkedIn profile, and portfolio.')
        
