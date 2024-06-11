# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_auth.services.helpers import BaseService


class EmailService(BaseService):
    def __init__(self):
        self.dao = None
        self.tenant_uuid = None

    def load(self, dependencies):
        dao = dependencies['dao']
        tenant_uuid = dependencies['tenant_uuid']
        template_formatter = dependencies['template_formatter']
        config = dependencies['config']

        super().__init__(dao, tenant_uuid)

    def confirm(self, email_uuid):
        print(f'Email confirm: {email_uuid}')

    def send_confirmation_email(
        self, username, email_uuid, email_address, connection_params
    ):
        print(f'Send email confirmation to {email_address}')

    def send_reset_email(self, user_uuid, username, email_address, connection_params):
        print(f'Send email reset to {email_address}')
