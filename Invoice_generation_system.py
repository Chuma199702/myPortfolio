"""
PSEUDOCODE

Capture invoice information

Capture vendor information

Capture customer information

Capture quantity and unit price

Calculate subtotal

Calculate VAT

Calculate total

Display invoice

End
"""

VAT_RATE = 0.15

# Invoice Information
invoice_number = input("Enter Invoice Number: ")
invoice_date = input("Enter Invoice Date: ")
due_date = input("Enter Due Date: ")

# Vendor Information
vendor_name = input("Enter Vendor Name: ")
vendor_email = input("Enter Vendor Email: ")

# Customer Information
customer_name = input("Enter Customer Business Name: ")

# Goods or Services
description = input("Enter Description of Goods/Services: ")

quantity = int(input("Enter Quantity: "))
unit_price = float(input("Enter Unit Price: R"))

# Additional Information
po_number = input("Enter Purchase Order Number: ")
payment_terms = input("Enter Payment Terms: ")

# Calculations
subtotal = quantity * unit_price

vat_amount = subtotal * VAT_RATE

total_amount = subtotal + vat_amount

# Invoice Output

print("\n")
print("=" * 50)
print("                    INVOICE")
print("=" * 50)

print(f"Invoice Number: {invoice_number}")
print(f"Invoice Date: {invoice_date}")
print(f"Due Date: {due_date}")

print("\nVendor Details")
print(f"Vendor Name: {vendor_name}")
print(f"Vendor Email: {vendor_email}")

print("\nCustomer Details")
print(f"Business Name: {customer_name}")

print("\nInvoice Details")
print(f"Description: {description}")
print(f"Quantity: {quantity}")
print(f"Unit Price: R{unit_price:.2f}")

print(f"\nSubtotal: R{subtotal:.2f}")
print(f"VAT (15%): R{vat_amount:.2f}")
print(f"Total Amount: R{total_amount:.2f}")

print(f"\nPO Number: {po_number}")
print(f"Payment Terms: {payment_terms}")

print("=" * 50)
