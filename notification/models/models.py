# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HREmployee(models.Model):
    _inherit = 'hr.attendance'

    def action_check_in(self):
        super(HREmployee, self).action_check_in()

        self._create_check_in_notification()

    def _create_check_in_notification(self):
        for employee in self:
            manager = employee.parent_id
            if manager and manager.user_id:
                self.env['mail.activity'].create({
                    'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                    'res_model_id': self.env['ir.model']._get_id('hr.attendance'),
                    'res_id': employee.id,
                    'user_id': manager.user_id.id,
                    'summary': 'Check-In Notification',
                    'note': f'{employee.name} has checked in.'
                })




