# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time

from greenlight.harness.testcase import FirefoxTestCase
from greenlight.harness.decorators import uses_lib

class TestSetHomePage(FirefoxTestCase):

    def setUp(self):
        FirefoxTestCase.setUp(self)
        self.marionette.navigate('about:preferences')
        self.marionette.set_context('content')

    @uses_lib('preferences', 'toolbar')
    def test_set_home_page(self):
        url = self.marionette.absolute_url('layout/mozilla.html')

        pane = self.preferences.open_pane('General')
        textbox = pane.startup.homepage_textbox
        import pdb
        pdb.set_trace()
        textbox.send_keys(url)
        time.sleep(5)

        with self.marionette.using_context('chrome'):
            self.toolbar.home_button.click()
        
        self.assertEquals(self.marionette.get_url(), url)
        
