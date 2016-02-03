# coding: utf-8


from openerp import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def send_demo(self, cr, uid, context=None):
        if context is None:
            context = {}
            context.update({
                'lang': 'es_PE',
                'tz': 'America/Lima',
                'uid': 1,
                'default_body_html': u'',
                'active_model': 'crm.lead',
                'default_subject': 'Re: demo',
                'stage_type': 'opportunity',
                #'params': {'action': 60},
                #'search_disable_custom_filters': True,
                'active_ids': [8],
                'default_model': 'crm.lead',
                #'tpl_partners_only': True,
                'active_id': 8})
        email_template = self.pool['email.template']
        template_ids = email_template.search(cr, uid, [('name', '=', 'Plantilla1')])
        self_id = self.search(cr, uid, [('name', '=', 'demo')])
        if template_ids:
            values = email_template.generate_email(cr, uid, template_ids[0], self_id[0], context=context)
            mail_mail_obj = self.pool['mail.mail']
            msg_id = mail_mail_obj.create(cr, uid, values)

            if msg_id:
                mail_mail_obj.send(cr, uid, [msg_id])
        return True
