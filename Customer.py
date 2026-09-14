import stripe
import stripe_config

# ==========================================================================
# 1) Create a customer account
#   - POST /v1/customers
#   - parameters needed:
#       - name => The customer’s full name
#       - email => Customer’s email address. 
# ==========================================================================
def create_customer(name, email):
    customer = stripe.Customer.create(
        name=name,
        email=email
    )
    
    return customer


# ==========================================================================
# 2) Modify a customer account and set the default payment method
#   - POST /v1/customers/:id
#   - parameters needed:
#       - [Required for this example] id => customer id required to be updated.
#       - [Required for this example] invoice_settings => Default invoice settings for this customer.
#           - default_payment_method =>  ID of a payment method that’s attached to the customer, to be used as the customer’s default payment method for subscriptions and invoices.
# ==========================================================================
def modify_customer_default_payment(customer, payment):
    customer = stripe.Customer.modify(
        id=customer,
        invoice_settings={
            "default_payment_method": payment
        }
    )
    
    return customer