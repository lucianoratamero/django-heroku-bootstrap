from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('app:index')

    def test_should_use_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'app/index.html')
