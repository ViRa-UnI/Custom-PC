from odoo import http
from odoo.http import request

class CustomPCBuilderController(http.Controller):

    @http.route('/pc_builder/save_configuration', type='json', auth='user', methods=['POST'])
    def save_configuration(self, **kw):
        configuration_data = kw.get('configuration_data')
        PCConfiguration = request.env['pc.configuration']
        new_configuration = PCConfiguration.create(configuration_data)
        return {'success': True, 'configuration_id': new_configuration.id}

    @http.route('/pc_builder/check_compatibility', type='json', auth='user', methods=['POST'])
    def check_compatibility(self, **kw):
        component_id = kw.get('component_id')
        existing_components = kw.get('existing_components')
        Component = request.env['component']
        is_compatible = Component.check_compatibility(component_id, existing_components)
        return {'compatible': is_compatible}

    @http.route('/pc_builder/update_price', type='json', auth='user', methods=['POST'])
    def update_price(self, **kw):
        component_ids = kw.get('component_ids')
        Component = request.env['component']
        total_price = Component.calculate_total_price(component_ids)
        return {'total_price': total_price}

    @http.route('/pc_builder/get_component_details', type='json', auth='user', methods=['POST'])
    def get_component_details(self, **kw):
        component_id = kw.get('component_id')
        Component = request.env['component']
        component_details = Component.browse(component_id).read(['name', 'price', 'image', 'compatibility_ids'])
        return {'component_details': component_details}

    @http.route('/pc_builder/add_to_wishlist', type='json', auth='user', methods=['POST'])
    def add_to_wishlist(self, **kw):
        configuration_id = kw.get('configuration_id')
        Wishlist = request.env['pc.wishlist']
        wishlist_item = Wishlist.create({'configuration_id': configuration_id})
        return {'success': True, 'wishlist_item_id': wishlist_item.id}

    @http.route('/pc_builder/share_configuration', type='http', auth='user', methods=['GET'])
    def share_configuration(self, **kw):
        configuration_id = kw.get('configuration_id')
        # Logic to share the configuration via social media or email goes here
        # This is a placeholder for the actual implementation
        return request.render('custom_pc_builder.share_template', {'configuration_id': configuration_id})