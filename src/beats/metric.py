# MIT License
#
# Copyright (c) 2021 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import uuid
import json


class Metric():
    """Metric Class"""

    def __init__(self, key, value, id=None, meta={}):
        self._key = key
        self._value = value
        self._id = str(uuid.uuid4()) if id is None else id
        self._meta = meta

    @property
    def key(self):
        """
        Gets the metric key

        Returns:
            The metric key
        """
        return self._key

    @property
    def value(self):
        """
        Gets the metric value

        Returns:
            The metric value
        """
        return self._value

    @property
    def id(self):
        """
        Gets the metric id

        Returns:
            The metric id
        """
        return self._id

    @property
    def meta(self):
        """
        Gets the metric meta data

        Returns:
            The metric meta data
        """
        return self._meta

    @classmethod
    def from_json(cls, data):
        """
        Get metric from JSON string

        Args:
            data: the JSON string

        Returns:
            An instance of this class
        """
        data = json.loads(data)

        return cls(
            data['key'],
            data['value'],
            data['id'],
            data['meta']
        )

    def __str__(self):
        """
        Convert the Object to string

        Returns:
            A JSON representation of this instance
        """
        return json.dumps({
            'key': self._key,
            'value': self._value,
            'id': self._id,
            'meta': self._meta,
        })
