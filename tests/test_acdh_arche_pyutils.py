#!/usr/bin/env python

"""Tests for `acdh_arche_pyutils.client` module."""

import unittest
from acdh_arche_pyutils.client import ArcheApiClient, camel_to_snake


class Test_pyutils_client(unittest.TestCase):
    """Tests for `acdh_arche_pyutils.utils` module.""" 

    def setUp(self):
        """Set up test fixtures, if any."""
        self.endpoint = "https://arche-curation.acdh-dev.oeaw.ac.at/api/"
        self.arche_client = ArcheApiClient(self.endpoint)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_parse_url(self):
        self.assertEqual(self.arche_client.endpoint, self.endpoint)

    def test_002_get_description(self):
        description = self.arche_client.description
        self.assertEqual(type(description), dict)
    
    def test_003_convert_camel_case(self):
        strings = [
            'CamelCase',
            'camel_Case',
            'camel_case',
        ]
        should_be = 'camel_case'
        for x in strings:
            self.assertEqual(camel_to_snake(x), should_be)
