# Copyright 2011 Element 34
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest2 as unittest

class BaseTestCase(unittest.TestCase):
    def verify_equal(self, want, got):
        try:
            self.assertEqual(want, got)
        except AssertionError, e:
            self.verificationErrors.append(str(e))

    def verify_text_present(self, text):
        try:
            self.assertTrue(self.selenium.is_text_present(text))
        except AssertionError, e:
            self.verificationErrors.append(str(e))

    def verify_element_present(self, locator):
        try:
            self.assertTrue(self.selenium.is_element_present(locator))
        except AssertionError, e:
            self.verificationErrors.append(str(e))

    def verify_visible(self, locator):
        try:
            self.assertTrue(self.selenium.is_visible(locator))
        except AssertionError, e:
            self.verificationErrors.append(str(e))

    def verify_true(self, condition):
        try:
            self.assertTrue(condition)
        except AssertionError, e:
            self.verificationErrors.append(str(e))