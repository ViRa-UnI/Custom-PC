from odoo.tests.common import TransactionCase

class TestPCConfiguration(TransactionCase):

    def setUp(self):
        super(TestPCConfiguration, self).setUp()
        self.PCConfiguration = self.env['pc.configuration']
        self.Component = self.env['component']
        # Create test components
        self.cpu = self.Component.create({'name': 'Test CPU', 'category': 'CPU', 'price': 250.00})
        self.gpu = self.Component.create({'name': 'Test GPU', 'category': 'GPU', 'price': 400.00})
        self.ram = self.Component.create({'name': 'Test RAM', 'category': 'RAM', 'price': 150.00})

    def test_create_configuration(self):
        # Create a PC configuration
        pc_config = self.PCConfiguration.create({
            'name': 'Custom PC',
            'component_ids': [(6, 0, [self.cpu.id, self.gpu.id, self.ram.id])]
        })
        self.assertTrue(pc_config, "PC Configuration was not created.")

    def test_configuration_total_price(self):
        # Create a PC configuration
        pc_config = self.PCConfiguration.create({
            'name': 'Custom PC',
            'component_ids': [(6, 0, [self.cpu.id, self.gpu.id, self.ram.id])]
        })
        # Check total price
        total_price = pc_config._compute_total_price()
        self.assertEqual(total_price, 800.00, "Total price did not match expected value.")

    def test_component_compatibility(self):
        # Create a PC configuration
        pc_config = self.PCConfiguration.create({
            'name': 'Custom PC',
            'component_ids': [(6, 0, [self.cpu.id, self.gpu.id])]
        })
        # Add incompatible RAM
        incompatible_ram = self.Component.create({'name': 'Incompatible RAM', 'category': 'RAM', 'price': 100.00, 'compatibility_ids': [(6, 0, [self.gpu.id])]})
        pc_config.write({'component_ids': [(4, incompatible_ram.id)]})
        # Check for compatibility issues
        self.assertFalse(pc_config._check_compatibility(), "Compatibility check did not identify incompatible components.")

    def tearDown(self):
        # Clean up test components
        self.cpu.unlink()
        self.gpu.unlink()
        self.ram.unlink()
        super(TestPCConfiguration, self).tearDown()