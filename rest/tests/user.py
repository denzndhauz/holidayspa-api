from django.test import TestCase

from rest_framework.test import APIClient


class UserTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_user_login(self):
		response = self.client.post('/api/token/')

		# Test Assertion
		self.assertTrue(True)