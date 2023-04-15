import json
import os

import django
from django.test import TestCase

from boardingpasssorterapp.exceptions import InvalidJourneyException
from boardingpasssorterapp.services import sort_boarding_pass
from django.test import RequestFactory

from boardingpasssorterapp.views import sort


class SortBoardingPassServiceTest(TestCase):
    def test_sort_boarding_pass_correct_journey(self):
        data = read_test_data("correct-journey-case-1.json")
        expected_journey = [
            "Take train 78A from Madrid to Barcelona. Seat in 45B",
            "Take the Airport Bus from Barcelona to Gerona Airport. No seat assignment",
            "From Gerona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket counter 344",
            "From Stockholm, take flight SK22 to New York. Gate 22, seat 7B. Baggage will be automatically transferred from your last leg.",
            "You have arrived at your final destination."
        ]
        response = sort_boarding_pass(data)
        self.assertEqual(5, len(response))
        self.assertEqual(expected_journey, response)

    def test_sort_boarding_pass_incorrect_jounrye(self):
        data = read_test_data("incorrect-journey-case-1.json")
        with self.assertRaises(InvalidJourneyException):
            sort_boarding_pass(data)


class SortBoardingPassApiTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        django.setup()

    def test_sort_boarding_pass_correct_journey(self):
        data = read_test_data("correct-journey-case-1.json")
        request = self.factory.post("/boarding-pass/sort", data=data, content_type="application/json")
        expected_journey = [
            "Take train 78A from Madrid to Barcelona. Seat in 45B",
            "Take the Airport Bus from Barcelona to Gerona Airport. No seat assignment",
            "From Gerona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket counter 344",
            "From Stockholm, take flight SK22 to New York. Gate 22, seat 7B. Baggage will be automatically transferred from your last leg.",
            "You have arrived at your final destination."
        ]
        response = sort(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.data["success"])
        self.assertEqual(5, len(response.data["journey"]))
        self.assertEqual(expected_journey, response.data["journey"])

    def test_sort_boarding_pass_incorrect_journey(self):
        data = read_test_data("incorrect-journey-case-1.json")
        request = self.factory.post("/boarding-pass/sort", data=data, content_type="application/json")
        response = sort(request)
        self.assertEqual(400, response.status_code)

    def test_sort_boarding_pass_invalid_payload(self):
        data = '{"a"}'
        request = self.factory.post("/boarding-pass/sort", data=data, content_type="application/json")
        response = sort(request)
        self.assertEqual(400, response.status_code)


def read_test_data(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/testdata/{file_name}', 'r') as file:
        return json.load(file)