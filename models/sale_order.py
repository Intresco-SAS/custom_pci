# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('payment_term_id')
    def crm_stage(self):
        for record in self:
            if record.opportunity_id:
                actual_stage = record.opportunity_id.stage_id.id
                record.crm_stage_ids = actual_stage
            else:
                record.crm_stage_ids = False
            
        return

    
    crm_stage_ids = fields.Many2one('crm.stage',string="Etapa CRM", compute="crm_stage")
    pipeline  =  fields.Selection([('backlog', 'Backlog'),
                                   ('nuevo', 'Nuevo')],
                                    default='nuevo')