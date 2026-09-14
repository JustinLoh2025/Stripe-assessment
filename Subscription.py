import stripe
import stripe_config

# Lets Create Subscription using the Stripe Python SDK
# Provide the description and the price to determine which Plan will be used for the subscription

# ==========================================================================
# 1) Create a subscription based on the selected price
#   - POST /v1/subscriptions
#   - parameters needed:
#       - [Required] items
#           - [Required] price => The ID of the price object.
#       - description => The subscription’s description, meant to be displayable to the customer.
#       - customer => The identifier of the customer to subscribe.
# ==========================================================================
def step_create_subscription(price, customer, description):
    subscription = stripe.Subscription.create(
        customer=customer,
        description=description,
        items=[{
            "price": price
        }]
    )
    return subscription


# ==========================================================================
# 2) Modiy a subscription using the selected coupon option
#   - POST /v1/subscriptions/:id
#   - parameters needed:
#       - [Required] subscription
#       - [Required for this example] discount => The coupons to redeem into discounts for the subscription.
#           - [Required for this example] coupons => ID of the coupon to create a new discount for.
# ==========================================================================
def step_subscription_mofidy(subscription, coupon):
    subscription = stripe.Subscription.modify(
        subscription, discounts=[
            {
                "coupon": coupon
            }
        ]
    )
    return subscription