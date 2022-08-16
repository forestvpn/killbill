# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.22-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import killbill
from killbill.api.invoice_api import InvoiceApi  # noqa: E501
from killbill.rest import ApiException


class TestInvoiceApi(unittest.TestCase):
    """InvoiceApi unit test stubs"""

    def setUp(self):
        self.api = killbill.api.invoice_api.InvoiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_adjust_invoice_item(self):
        """Test case for adjust_invoice_item

        Adjust an invoice item  # noqa: E501
        """
        pass

    def test_commit_invoice(self):
        """Test case for commit_invoice

        Perform the invoice status transition from DRAFT to COMMITTED  # noqa: E501
        """
        pass

    def test_create_external_charges(self):
        """Test case for create_external_charges

        Create external charge(s)  # noqa: E501
        """
        pass

    def test_create_future_invoice(self):
        """Test case for create_future_invoice

        Trigger an invoice generation  # noqa: E501
        """
        pass

    def test_create_instant_payment(self):
        """Test case for create_instant_payment

        Trigger a payment for invoice  # noqa: E501
        """
        pass

    def test_create_invoice_custom_fields(self):
        """Test case for create_invoice_custom_fields

        Add custom fields to invoice  # noqa: E501
        """
        pass

    def test_create_invoice_tags(self):
        """Test case for create_invoice_tags

        Add tags to invoice  # noqa: E501
        """
        pass

    def test_create_migration_invoice(self):
        """Test case for create_migration_invoice

        Create a migration invoice  # noqa: E501
        """
        pass

    def test_create_tax_items(self):
        """Test case for create_tax_items

        Create tax items  # noqa: E501
        """
        pass

    def test_delete_cba(self):
        """Test case for delete_cba

        Delete a CBA item  # noqa: E501
        """
        pass

    def test_delete_invoice_custom_fields(self):
        """Test case for delete_invoice_custom_fields

        Remove custom fields from invoice  # noqa: E501
        """
        pass

    def test_delete_invoice_tags(self):
        """Test case for delete_invoice_tags

        Remove tags from invoice  # noqa: E501
        """
        pass

    def test_generate_dry_run_invoice(self):
        """Test case for generate_dry_run_invoice

        Generate a dryRun invoice  # noqa: E501
        """
        pass

    def test_get_catalog_translation(self):
        """Test case for get_catalog_translation

        Retrieves the catalog translation for the tenant  # noqa: E501
        """
        pass

    def test_get_invoice(self):
        """Test case for get_invoice

        Retrieve an invoice by id  # noqa: E501
        """
        pass

    def test_get_invoice_as_html(self):
        """Test case for get_invoice_as_html

        Render an invoice as HTML  # noqa: E501
        """
        pass

    def test_get_invoice_audit_logs_with_history(self):
        """Test case for get_invoice_audit_logs_with_history

        Retrieve invoice audit logs with history by id  # noqa: E501
        """
        pass

    def test_get_invoice_by_item_id(self):
        """Test case for get_invoice_by_item_id

        Retrieve an invoice by invoice item id  # noqa: E501
        """
        pass

    def test_get_invoice_by_number(self):
        """Test case for get_invoice_by_number

        Retrieve an invoice by number  # noqa: E501
        """
        pass

    def test_get_invoice_custom_fields(self):
        """Test case for get_invoice_custom_fields

        Retrieve invoice custom fields  # noqa: E501
        """
        pass

    def test_get_invoice_mp_template(self):
        """Test case for get_invoice_mp_template

        Retrieves the manualPay invoice template for the tenant  # noqa: E501
        """
        pass

    def test_get_invoice_tags(self):
        """Test case for get_invoice_tags

        Retrieve invoice tags  # noqa: E501
        """
        pass

    def test_get_invoice_template(self):
        """Test case for get_invoice_template

        Retrieves the invoice template for the tenant  # noqa: E501
        """
        pass

    def test_get_invoice_translation(self):
        """Test case for get_invoice_translation

        Retrieves the invoice translation for the tenant  # noqa: E501
        """
        pass

    def test_get_invoices(self):
        """Test case for get_invoices

        List invoices  # noqa: E501
        """
        pass

    def test_get_payments_for_invoice(self):
        """Test case for get_payments_for_invoice

        Retrieve payments associated with an invoice  # noqa: E501
        """
        pass

    def test_modify_invoice_custom_fields(self):
        """Test case for modify_invoice_custom_fields

        Modify custom fields to invoice  # noqa: E501
        """
        pass

    def test_search_invoices(self):
        """Test case for search_invoices

        Search invoices  # noqa: E501
        """
        pass

    def test_upload_catalog_translation(self):
        """Test case for upload_catalog_translation

        Upload the catalog translation for the tenant  # noqa: E501
        """
        pass

    def test_upload_invoice_mp_template(self):
        """Test case for upload_invoice_mp_template

        Upload the manualPay invoice template for the tenant  # noqa: E501
        """
        pass

    def test_upload_invoice_template(self):
        """Test case for upload_invoice_template

        Upload the invoice template for the tenant  # noqa: E501
        """
        pass

    def test_upload_invoice_translation(self):
        """Test case for upload_invoice_translation

        Upload the invoice translation for the tenant  # noqa: E501
        """
        pass

    def test_void_invoice(self):
        """Test case for void_invoice

        Perform the action of voiding an invoice  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()