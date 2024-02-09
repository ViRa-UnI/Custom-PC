odoo.define('pc_builder.PCBuilder', function(require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');

    publicWidget.registry.PCBuilder = publicWidget.Widget.extend({
        selector: '.pc-builder-container',
        events: {
            'change #component-selector': '_onComponentChanged',
            'click #wishlist-button': '_onAddToWishlist',
            'click #share-button': '_onShareConfiguration'
        },

        start: function() {
            this._super.apply(this, arguments);
            this._updatePrice();
        },

        _onComponentChanged: function(event) {
            var self = this;
            var $target = $(event.currentTarget);
            var componentId = $target.val();
            ajax.jsonRpc('/shop/pc_builder/check_compatibility', 'call', {
                component_id: componentId
            }).then(function(result) {
                if (result.is_compatible) {
                    self._updateVisualization(componentId);
                    self._updatePrice();
                } else {
                    alert("Selected component is not compatible with the current configuration.");
                }
            });
        },

        _updateVisualization: function(componentId) {
            // Placeholder for visualization logic
            console.log('Visualization updated for component ID:', componentId);
        },

        _updatePrice: function() {
            var self = this;
            ajax.jsonRpc('/shop/pc_builder/update_price', 'call', {})
            .then(function(result) {
                $('#price-total').text(result.total_price);
            });
        },

        _onAddToWishlist: function() {
            // Placeholder for wishlist logic
            console.log('Added to wishlist');
        },

        _onShareConfiguration: function() {
            // Placeholder for sharing logic
            console.log('Configuration shared');
        }
    });

    return {
        PCBuilder: publicWidget.registry.PCBuilder
    };
});