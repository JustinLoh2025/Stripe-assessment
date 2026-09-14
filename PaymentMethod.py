import stripe
import stripe_config

# Lets Payment method using the Stripe Python SDK
#==================================================
# After creating the customer there is 2 ways I can suggest to capture the customer payment method
# 1) Use the Stripe checkout session - provide a link to the customer to create their payment method.
# 2) Use your own payment capture page to capture the payment method. You will however need to:
#   a) Create a SetupIntent with a Client Secret to be passed throught the stripe.js in the frontend.
#   b) Your Payment Capture form will need to confirm the provided payment method details.
#
#==================================================

# ==========================================================================
# 1) Option 1: 
#   - POST /v1/setup_intents
#   - Can use the setupIntent to setting up and save a customer’s payment credentials for future payments.
#       - Shared a sample stripe_payment.html sample with this project.
#   - parameters needed:
#       - [Required for this example] customer => ID of the Customer this SetupIntent belongs to
#       - usage => Indicates how the payment method is intended to be used in the future (off_session, on_session).
# ==========================================================================
def setup_Intents_for_future_payments(customer):
    setupIntent = stripe.SetupIntent.create(
        customer=customer,
        usage="off_session"
    )
    
    return setupIntent


# ==========================================================================
# 2) Option 2: 
#   - POST /v1/checkout/sessions
#   - Create a link that can be shared to the customer to enter create their payment method using the Stripe Checkout Session
#   - parameters needed:
#       - [Required for this example] customer => ID of the Customer this SetupIntent belongs to
#       - [Required] mode => The mode of the Checkout Session (payment, setup, subscription). 
#       - [Required for this example] currency => Three-letter ISO currency code, in lowercase. Must be a supported currency. 
#       - [Required for this example] success_url => The URL to which Stripe should send customers when payment or setup is complete.
#       - [Required for this example] cancel_url => The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site.
# ==========================================================================
def create_checkout_session_for_payment_method(customer):
    checkoutSession = stripe.checkout.Session.create(
        mode="setup",
        customer=customer,
        currency="usd",
        success_url="http://localhost:4242/success",
        cancel_url="http://localhost:4242/cancel"
    )
    return checkoutSession