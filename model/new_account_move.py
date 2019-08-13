# -*- coding: utf-8 -*-

from odoo import fields,api,models

class AccountMove(models.Model):
    _inherit="account.move"
    
    new_name = fields.Char(compute='_get_seq', string="New Sequence", readonly=False, store=True)
    #new_name = fields.Char(string="New Sequence", readonly=False)
    
#     @api.model
#     def create(self,vals):
#         print"\n\n\n\n\n\n vals",vals
#         res = super(AccountMove,self).create(vals)
#         print"\n\n\n\n\n\n after vals",vals
# #         if res:
# #             new_seq = self.env['account.invoice'].search([('move_id','=',res.name)])
# #             print"\n\n\n\n\n\n\n\n\n new name",new_seq
# #             if new_seq:
# #                 res.new_move_sequence = new_seq.new_accnt_sequence
#         return res   
    
#     @api.multi
#     def write(self,vals):
#         print"\n\n\n\n\n\n write vals",vals
#         res = super(AccountMove,self).write(vals)
#         print"\n\n\n\n\n\n wafteriter vals",str(self.name).strip()
#         string3=self.name
#         print string3
#         print string3.strip()        
#         
#         if self:
#             new_seq = self.env['account.invoice'].search([('number','=',self.name)],limit=1)
#             print"\n\n\n\n\n\n\n\n\n new name",new_seq
#             if new_seq:
#                 self.new_move_sequence = new_seq.new_accnt_sequence
#         return res      
     
    @api.multi
    @api.depends('name')
    def _get_seq(self):
        if self:
            for rec in self:
                new_seq = self.env['account.invoice'].search([('number','=',rec.name)],limit=1)
                rec.new_name = new_seq.new_accnt_sequence