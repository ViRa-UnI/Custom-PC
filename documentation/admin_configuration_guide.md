# Admin Configuration Guide for Custom PC Building Module

## Introduction
This guide is intended for administrators who will manage the Custom PC Building Module within the Odoo Version 16 Community Edition. It provides instructions on how to set up and configure the module to enable customers to build their custom PCs through your eCommerce platform.

## Getting Started
Before you begin, ensure that you have installed the Custom PC Building Module. Follow the standard Odoo module installation process by navigating to `Apps` in the Odoo dashboard and searching for the Custom PC Building Module.

## Configuring Component Data
1. Navigate to the `Inventory` module.
2. Under the `Products` menu, select `Products`.
3. To add a new component, click on `Create`.
4. Fill in the necessary details such as `Product Name`, `Product Type`, and `Sales Price`.
5. Under the `Custom PC Building` tab, specify the component attributes like `Brand`, `Model`, and `Compatibility`.
6. Save the new component by clicking on `Save`.

Refer to the `data/component_data.xml` file for the initial data structure and example entries.

## Setting Up Access Rights
1. Go to `Settings` > `Users & Companies` > `Users`.
2. Select a user to configure access rights.
3. Under the `Access Rights` tab, scroll down to the `Custom PC Building` section.
4. Assign the appropriate access level for `PC Configuration` and `Component` models using the `access_pc_configuration` and `access_component` IDs.

## Managing PC Configurations
1. Access the `Custom PC Building` module from the main dashboard.
2. Here, you can view all saved PC configurations by customers.
3. Use the `pc_configuration_form` and `pc_configuration_summary` views to inspect and manage these configurations.

## Integrating with Inventory Management
Ensure that the module is correctly integrated with the inventory management system to reflect real-time stock levels and prevent overselling. This is handled automatically by the module, but you should periodically check the inventory levels for accuracy.

## Testing the Module
Conduct regular tests using the `tests/test_pc_configuration.py` and `tests/test_component.py` scripts to ensure that the module functions as expected. This includes testing component selection, compatibility checks, and pricing calculations.

## Updating the Module
To update the module, follow the standard Odoo module update process. Navigate to `Apps`, search for the Custom PC Building Module, and click on `Upgrade`.

## Conclusion
This guide provides the basic steps for configuring and managing the Custom PC Building Module. For detailed instructions and troubleshooting, refer to the `documentation/customer_pc_building_guide.md` for customer-facing documentation. Your feedback is valuable in improving this module, so please share your experiences and suggestions.