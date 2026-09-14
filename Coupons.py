import stripe
import stripe_config

# ==========================================================================
# 1) Create a percentage for the coupon and for how long
#   - POST /v1/coupons
#   - parameters needed:
#       - percent_off => A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if amount_off is not passed).
#       - duration => Specifies how long the discount will be in effect if used on a subscription. Defaults to once (once, forever, repeating).
# ==========================================================================
# Create a precentage for the coupon and for how long
def create_precentage_coupon(amountOff, duration):
    coupon = stripe.Coupon.create(
        percent_off=amountOff,
        duration=duration
    )
    
    return coupon


# ==========================================================================
# 2) Create a amount off for the coupon and for how long
#   - POST /v1/coupons
#   - parameters needed:
#       - amount_off => A positive integer representing the amount to subtract from an invoice total (required if percent_off is not passed).
#       - duration => Specifies how long the discount will be in effect if used on a subscription. Defaults to once (once, forever, repeating).
# ==========================================================================
# Create a fix amount for the coupon and for how long
def create_fixed_amount_coupon(amountOff, duration):
    coupon = stripe.Coupon.create(
        amount_off=amountOff,
        duration=duration
    )
    return coupon