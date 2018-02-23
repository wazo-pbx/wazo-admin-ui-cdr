# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, IndexAjaxViewMixin


class CdrView(IndexAjaxViewMixin, BaseView):
    form = object
    resource = 'cdr'

    @classy_menu_item('.cdrs', l_('CDR'), order=4, icon="newspaper-o")
    def index(self):
        return super(CdrView, self).index()
