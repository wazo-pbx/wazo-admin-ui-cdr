# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView


class OutcallView(BaseView):

    resource = 'cdr'

    @classy_menu_item('.cdrs', 'CDR', order=4, icon="newspaper-o")
    def index(self):
        return super(CdrView, self).index()
