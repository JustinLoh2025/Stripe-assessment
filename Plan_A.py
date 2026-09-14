import stripe
import stripe_config

# Lets Create Plan A first using the Stripe Python SDK
# Plan A: Flat rate of $24.99 per month for unlimited usage of the service

# ==========================================================================
# 1) Create a product first for Plan A.
#   - POST /v1/products
#   - parameters needed:
#       - [Required] Name
#       - description
# ==========================================================================
def step_1_create_product():
    product = stripe.Product.create(
        name="Plan A - Flat rate per month",
        description="Flat rate of $24.99 per month for unlimited usage"
    )
        
    return product


# ==========================================================================
# 2) Create a price (replace plans) for Plan A.
#   - POST /v1/prices
#   - parameters needed:
#   - [Required] currency => Three-letter ISO currency code, in lowercase. Must be a supported currency.
#       - [Required for this example] product => The ID of the Product that this Price will belong to.
#       - [Required for this example] unit_amount => A positive integer in the smallest currency unit (or 0 for a free price) representing how much to charge. One of unit_amount, unit_amount_decimal, or custom_unit_amount is required, unless billing_scheme=tiered.
#       - [Required] recurring
#           - [Required] interval => Specifies billing frequency. Either day, week, month or year.
# ==========================================================================
def step_2_create_price(product):
    price = stripe.Price.create(
        currency="usd",
        unit_amount=2499,
        recurring={
            "interval": "month"
        },
        product=product
    )
    
    return price