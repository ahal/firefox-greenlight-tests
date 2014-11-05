# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import inspect
import sys

from marionette import NoSuchElementException

from . import DOMElement


class Preferences(object):
    _categories = None

    def __init__(self, client):
        self.client = client

    @property
    def categories(self):
        if not self._categories:
            self._categories = Categories.create(self.client.find_element('id', 'categories'))
        return self._categories

    def open_pane(self, category):
        self.categories.select(category)

        for cls in inspect.getmembers(sys.modules[__name__], inspect.isclass):
            print(cls)
            if cls[0].startswith(category):
                return cls[1].create(self.client.find_element('id', 'mainPrefPane'))
        return self.client.find_element('id', 'mainPrefPane')


class Categories(DOMElement):
    def select(self, category):
        items = self.find_elements('tag name', 'richlistitem')
        for item in items:
            if item.get_attribute('tooltiptext') == category:
                return item.click()
        raise NoSuchElementException("Could not find '{}' in the preferences pane".format(category))

class GeneralPane(DOMElement):
    @property
    def startup(self):
        return self.StartupGroup.create(self.find_element('id', 'startupGroup'))

    @property
    def downloads(self):
        return self.DownloadsGroup.create(self.find_element('id', 'downloadsGroup'))

    @property
    def tabs(self):
        return self.TabsGroup.create(self.find_element('id', 'paneGeneral'))

    class StartupGroup(DOMElement):

        @property
        def homepage_textbox(self):
            return self.find_element('id', 'browserHomePage')

    class DownloadsGroup(DOMElement):
        pass

    class TabsGroup(DOMElement):
        pass
