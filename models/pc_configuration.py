from odoo import models, fields, api

class PCConfiguration(models.Model):
    _name = 'pc.configuration'
    _description = 'Custom PC Configuration'

    name = fields.Char(string='Configuration Name', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    component_ids = fields.Many2many('pc.component', string='Components')
    price = fields.Float(compute='_compute_price', string='Total Price', store=True, readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    @api.depends('component_ids.price')
    def _compute_price(self):
        for record in self:
            record.price = sum(component.price for component in record.component_ids)

    @api.constrains('component_ids')
    def _check_compatibility(self):
        for record in self:
            components = record.component_ids
            # Placeholder for compatibility logic
            # This should be replaced with actual compatibility check logic
            incompatible_components = self.env['pc.component'].check_components_compatibility(components)
            if incompatible_components:
                raise ValidationError("Incompatible components detected: %s" % ", ".join(incompatible_components))

class Component(models.Model):
    _name = 'pc.component'
    _description = 'PC Component'

    name = fields.Char(string='Name', required=True)
    category = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('motherboard', 'Motherboard'),
        ('psu', 'Power Supply Unit'),
        ('case', 'Case')
    ], string='Category', required=True)
    brand = fields.Char(string='Brand')
    model = fields.Char(string='Model')
    price = fields.Float(string='Price')
    compatibility_ids = fields.Many2many('pc.component', 'component_compatibility_rel', 'src_id', 'dest_id', string='Compatible Components')

    @api.model
    def check_components_compatibility(self, components):
        # Placeholder for compatibility check logic
        # This should be replaced with actual compatibility check logic
        incompatible_components = []
        # Logic to determine incompatible components
        return incompatible_components
