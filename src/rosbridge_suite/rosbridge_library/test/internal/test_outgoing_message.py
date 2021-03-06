#!/usr/bin/env python
import rosunit
import sys
import unittest

from rosbridge_library.internal.outgoing_message import OutgoingMessage
from std_msgs.msg import String


PKG = 'rosbridge_library'
NAME = 'test_outgoing_message'


class TestOutgoingMessage(unittest.TestCase):
    def test_json_values(self):
        msg = String(data="foo")
        outgoing = OutgoingMessage(msg)

        result = outgoing.get_json_values()
        self.assertEqual(result['data'], msg.data)

        again = outgoing.get_json_values()
        self.assertTrue(result is again)

    def test_cbor_values(self):
        msg = String(data="foo")
        outgoing = OutgoingMessage(msg)

        result = outgoing.get_cbor_values()
        self.assertEqual(result['data'], msg.data)

        again = outgoing.get_cbor_values()
        self.assertTrue(result is again)


if __name__ == '__main__':
    rosunit.unitrun(PKG, NAME, TestOutgoingMessage)
