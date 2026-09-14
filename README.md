# Stripe Assessment using Python
This project is used to demonstrates how the Stripe Python SDK can be used to help address questions from the merchant introducing their streaming services.

Customer.py:
- Create a new customer.
- Modifying the customer default payment method.
    - Will help to tell Stripe which payment method to use to attempt a payment

PaymentMethod.py:
Providing options to help the merchant address how the payment method should be captured securely.
- Option 1: Create a SetupIntent and pass its client secret to the frontend, where Stripe.js can use it to securely collect and confirm the customer's payment method for future payments.
- Option 2: Use a checkout session to allow customer to enter their payment method securely and use it for future payments.

Plan_A.py and Plan_B.py
Seperate the Plans to make it easier to understand the steps:
- Plan_A.py
    - Fixed Monthly pricing:
        - Create a product 
        - Create a Price for $24.99 per month.
- Plan_B.py
    - Usage based pricing (first 100 GB => $10.99 and subsequently $1 for every 10 GB other that)
        - Create a product (decsribing a tier pricing model based on the usage)
        - Create a Meter to descibe "Streaming Data Usage per 10GB" 
        - Create a Tier Pricing
        - Record usage through Stripe's Meter Events.

Subscription.py
- Create a subscription based on the selected price
- Modiy a subscription using the selected coupon option (added as part of the Coupon questions)

Coupon.py
- Option 1: Create a percentage for the coupon and for how long
- Option 2: Create a amount off for the coupon and for how long

Main.py
- Main entry point for the project
- Orchestrates the different steps in the assessment.

Stripe_config.py
- Loads the Stripe API Key for the environemnt variables.
- Configures the Stripe Python SDK.

payment_stripe.html
- Demonstrates how Stripe.js can securely collect a customer's payment method using the "client Secret" provided from the SetupIntent in the PaymentMethod.py
- Demonstrated the seperation between the Python Bankend and Stripe.js frontend integration.