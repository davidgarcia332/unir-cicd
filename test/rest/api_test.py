import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
    
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_logarithm(self):
        url = f"{BASE_URL}/calc/logarithm/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_logarithm(self):
        url = f"{BASE_URL}"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        content =  response.read().decode(response.headers.get_content_charset())
        
        self.assertEqual(
            content , "Hello from The Calculator!\n", f"Error en la petición API a {url}"
        )
