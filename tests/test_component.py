from odoo.tests.common import TransactionCase

class TestComponent(TransactionCase):

    def setUp(self):
        super(TestComponent, self).setUp()
        self.Component = self.env['component']
        self.cpu = self.Component.create({
            'name': 'Test CPU',
            'category': 'CPU',
            'price': 250.00
        })
        self.gpu = self.Component.create({
            'name': 'Test GPU',
            'category': 'GPU',
            'price': 400.00
        })

    def test_create_component(self):
        """Test the creation of a component"""
        self.assertEqual(self.cpu.name, 'Test CPU')
        self.assertEqual(self.cpu.category, 'CPU')
        self.assertEqual(self.cpu.price, 250.00)

    def test_component_compatibility(self):
        """Test the compatibility logic between components"""
        # Assuming compatibility logic is implemented in the component model
        self.cpu.compatibility_ids = [(6, 0, [self.gpu.id])]
        self.assertIn(self.gpu, self.cpu.compatibility_ids)

    def test_update_component_price(self):
        """Test the price update of a component"""
        self.cpu.price = 275.00
        self.assertEqual(self.cpu.price, 275.00)

    def tearDown(self):
        self.cpu.unlink()
        self.gpu.unlink()
        super(TestComponent, self).tearDown()