# coding: utf-8


from openerp import models, fields, api
from datetime import datetime

import time
import pytz


class SendAutomatic(models.Model):
    _name = 'send.automatic'

    template_id = fields.Many2one('email.template', 'Plantilla')
    stage_id = fields.Many2one('crm.case.stage', 'Estado')
    days = fields.Integer('Nro dias')

    def send_demo(self, cr, uid, context=None):
        email_template = self.pool['email.template']
        crm_lead = self.pool['crm.lead']
        date_now = datetime.now()
        if context is None:
            context = {}

        obj_id = self.search(cr, uid, [])
        for obj in self.browse(cr, uid, obj_id):
            email_template = self.pool['email.template']
            # crm_lead_id = crm_lead.search(cr, uid, [('state', '=', obj.stage_id.id)])
            crm_lead_id = crm_lead.search(cr, uid, [('name', '=', 'demo')])
            if crm_lead_id:
                for crm_obj  in crm_lead.browse(cr, uid, crm_lead_id):
                    date_create = datetime.strptime(crm_obj.create_date, '%Y-%m-%d %H:%M:%S')
                    user = self.pool['res.users'].browse(cr, uid, uid)
                    tz = pytz.timezone(user.tz) if user.tz else pytz.utc
                    date_create = pytz.utc.localize(date_create).astimezone(tz)
                    date_substract = date_now - date_create.replace(tzinfo=None)
                    date_substract = date_substract.days
                    context.update({
                        'lang': 'es_PE',
                        'tz': 'America/Lima',
                        'uid': uid,
                        'default_body_html': u'',
                        'active_model': 'crm.lead',
                        'default_subject': 'Re: demo',
                        'stage_type': 'opportunity',
                        'active_ids': [crm_obj.id],
                        'default_model': 'crm.lead',
                        'active_id': crm_obj.id})
                    if obj.days == date_substract:
                        values = email_template.generate_email(cr, uid, obj.template_id.id, crm_obj.id, context=context)
                        mail_mail_obj = self.pool['mail.mail']
                        msg_id = mail_mail_obj.create(cr, uid, values)

                        if msg_id:
                            mail_mail_obj.send(cr, uid, [msg_id])
        return True
