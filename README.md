# Partner Naming
Odoo modul for adding firstname and lastnamea to the res.partner model.
All fields are added to the model itself, the base view and the eCommerce checkout form.

## Features
* The res.partner model from the base module is extended by the two fields "firstname" and "lastname".
* The new fields replace the name field in the "base.view_partner_form" view.
* The name field is also replaced by the new fields in the "website_sale.checkout" template. The name value is set from a combination of the firstname and lanstname value.
* "firstname" and "lastname" are defined as mandatory in the controller of the eCommerce module.

## Install
* Download the folder and copy it to your Odoo module folder
* Restart Odoo
* Update Local Module list (Settings -> Update Modules List -> Update)
* Locate the module
* Click on the module and select "Install"

## Dependencies
To make full use of all the features the following modules need to be installed:
* Base (base)
* eCommerce (website_sale)
