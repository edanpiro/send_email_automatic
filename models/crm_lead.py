# coding: utf-8


from openerp import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'


    def send_demo(self, cr, uid):
        email_template = self.pool['email.template']
        template_ids = email_template.search(cr, uid, [('name', '=', 'Invoice - Send by Email')])
        if template_ids:
            print "template", template_ids
            values = email_template.generate_email(cr, uid, template_ids[0], 1)
            values['subject'] = 'subject'
            values['email_to'] = 'pimentelrojas@gmail.com'
            values['body_html'] = 'hola mundo'
            values['body'] = 'hola'
            values['res_id'] = False

            mail_mail_obj = self.pool['mail.mail']
            msg_id = mail_mail_obj.create(cr, uid, values)
            print "msddd", msg_id

            if msg_id:
                mail_mail_obj.send(cr, uid, [msg_id])
        return True
