# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from wazo_admin_ui.helpers.call_logd import calllogd

logger = logging.getLogger(__name__)


class CdrService(object):

    resource_calllogd = 'cdr'

    def list(self, limit=None, order=None, direction=None, offset=None, search=None, **kwargs):
        resource_client = getattr(calllogd, self.resource_calllogd)
        return resource_client.list(search=search,
                                    order=order,
                                    limit=limit,
                                    direction=direction,
                                    offset=offset,
                                    **kwargs)
