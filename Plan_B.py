import stripe
import stripe_config

# Lets Create Plan B first using the Stripe Python SDK
# Plan B: $10.99 for the first 100 GB and $1.00 per subsequent 10 GB

# ==========================================================================
# 1) Create a product first for Plan B.
#   - POST /v1/products
#   - parameters needed:
#       - [Required] Name
#       - description
# ==========================================================================
def step_1_create_product():
    product = stripe.Product.create(
        name="Plan B - Tier pricing",
        description="$10.99 for the first 100 GB and $1.00 per subsequent 10 GB"
    )
    
    print("Product Id: ", product.id)
    print("Product Name: ", product.name)
    
    return product


# ==========================================================================
# 2) Create a meter first for Plan B.
#   - POST /v1/billing/meters
#   - Break up the the meter recording for 10 GB because after 100 GB, every 10 GB will have a $1.00 addition.
#   - parameters needed:
#       - [Required] display_name => The meter’s name. Not visible to the customer.
#       - [Required] event_name => The name of the meter event to record usage for. Corresponds with the event_name field on meter events.
#       - [Required] default_aggregation => The default settings to aggregate a meter’s events with (count,last,sum).
# ==========================================================================
def step_2_create_meter():
    meter = stripe.billing.Meter.create(
        display_name="Streaming Data Usage per 10GB",
        event_name="StreamingData10GB",
        default_aggregation={
            "formula":"sum"
        }
    )
    return meter


# ==========================================================================
# 3) Create price for Plan B.
#   - POST /v1/prices
#   - parameters needed:
#       - [Required] currency => Three-letter ISO currency code, in lowercase. Must be a supported currency.
#       - [Required for this example] product => The ID of the Product that this Price will belong to.
#       - [Required for this example] unit_amount => A positive integer in the smallest currency unit (or 0 for a free price) representing how much to charge. One of unit_amount, unit_amount_decimal, or custom_unit_amount is required, unless billing_scheme=tiered.
#       - [Required for this example] tiers => Each element represents a pricing tier. This parameter requires billing_scheme to be set to tiered. See also the documentation for billing_scheme.
#           - tiers[].up_to => Specifies the upper bound of this tier. The lower bound of a tier is the upper bound of the previous tier adding one. Use inf to define a fallback tier.
#           - tiers[].flat_amount => The flat billing amount for an entire tier, regardless of the number of units in the tier.
#           - tiers[].unit_amount => The per unit billing amount for each individual unit for which this tier applies.
#       - [Required for this example] billing_scheme => Describes how to compute the price per period (per_unit, tiered).
#       - [Required for this example] tiers_mode => Defines if the tiering price should be graduated or volume based. 
#       - [Required] recurring
#           - [Required] interval => Specifies billing frequency. Either day, week, month or year.
#           - [Required for this example] usage_type = Configures how the quantity per period should be determined (metered, licensed).
#           - [Required for this example] meter => The meter tracking the usage of a metered price
# ==========================================================================
def step_3_create_price(meter, product):
    price = stripe.Price.create(
        currency="usd",
        billing_scheme="tiered",
        tiers_mode="graduated",
        tiers=[{
            "up_to": 10,
            "flat_amount": 1099
        },
        {
            "up_to": "inf",
            "unit_amount": 100          
        }],
        recurring={
            "interval": "month",
            "usage_type": "metered",
            "meter": meter
        },
        product=product
    )
    
    return price
    
# ==========================================================================
# 4) Create Meter Event to build up the usage for Plan B.
#   - POST /v1/billing/meter_events
#   - The streaming services will need initiate the meter event based on the customer usage.
#   - parameters needed:
#       - [Required] payload
#           - [Required] value => Report usage in 10 GB billing unit, where 1 meter event unit represents 10 GB of usage. Partial 10 GB amounts should be rounded up to the next unit.
#           - [Required] stripe_customer_id => which customer generates the usage
#       - [Required] event_name => The name of the meter event. Corresponds with the event_name field on a meter.
# ==========================================================================
def step_4_create_meter_event(customer, amount):
    meterEvent = stripe.billing.MeterEvent.create(
        event_name="StreamingData10GB",
        payload={
            "value":amount,
            "stripe_customer_id": customer           
        }
    )