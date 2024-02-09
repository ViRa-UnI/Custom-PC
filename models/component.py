from odoo import models, fields

class Component(models.Model):
    _name = 'component'
    _description = 'PC Component'

    name = fields.Char(string='Name', required=True)
    category = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('motherboard', 'Motherboard'),
        ('psu', 'Power Supply Unit'),
        ('case', 'Case'),
        ('cooling', 'Cooling System'),
        ('accessory', 'Accessory')
    ], string='Category', required=True, help="Category of the PC component")
    brand = fields.Char(string='Brand')
    model = fields.Char(string='Model')
    price = fields.Float(string='Price', digits='Product Price')
    compatibility_ids = fields.Many2many('component', 'component_compatibility_rel', 'source_id', 'compatible_id', string='Compatible Components')
    image = fields.Binary(string='Image', attachment=True)
    stock_quantity = fields.Integer(string='Stock Quantity')
    description = fields.Text(string='Description')