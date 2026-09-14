import stripe
import stripe_config

import Plan_A
import Plan_B
import Customer
import Subscription
import PaymentMethod
import Coupons


def main():
    
    # Create PLAN A
    product_a = Plan_A.step_1_create_product()
    price_a = Plan_A.step_2_create_price(product_a.id)

    # Create PLAN B
    product_b = Plan_B.step_1_create_product()
    meter_b = Plan_B.step_2_create_meter()
    price_b = Plan_B.step_3_create_price(meter_b.id, product_b.id)
    
    
    # ==============================================================================================
    # OPTIONAL: If customer is require run the information below as sample:
    # ==============================================================================================
    # # Step 1 = Create a new customer
    # customerNew = Customer.create_customer("TestCustomer01","test@gmail.com")
        
    # # Step 2 = Create a payment method
    # paymentMethodNew = PaymentMethod.setup_Intents_for_future_payments(customerNew.id)
    # # OR
    # paymentMethodNew = PaymentMethod.create_checkout_session_for_payment_method(customerNew.id)
        
    # # Step 3 = Set the payment method to default
    # # The payment method retrieved from checkout session or from the stripe.js (frontend HTML) with "pm_" will be the payment method added to the {{payment_method}}.
    # defaultPaymentMethod = Customer.modify_customer_default_payment(customerNew.id, "{{payment_method}}")
        
    # Note: Create Customer => Create Payment Method => set to default payment method to be used
    # ==============================================================================================
        
    
    # ==============================================================================================
    # NEXT: Depending on the Plan selected, proceed to update the information below before creating the subscription.
    # ==============================================================================================
    # # Create a subscription after that
    # createSubscription = Subscription.step_create_subscription(price_a.id, customerNew.id, "{{customerNew.id}} created using Plan A")
    # # OR
    # createSubscription = Subscription.step_create_subscription(price_b.id, customerNew.id, "{{customerNew.id}} created using Plan B")
    
    
    # ==============================================================================================
    # OPTIONAL if PLAN B is used:
    # Provide the usage for Plan B with report usage in 10 GB billing unit, where 1 "meter event" unit represents 10 GB of usage. 
    # Partial 10 GB amounts should be rounded up to the next unit. The example below has the meter event unit of 3 (representing 30 GB usage)
    # ==============================================================================================
    # # Part of PLAN B - Create meter event to calculate the usage of the customer
    # meterEvent_b = Plan_B.step_4_create_meter_event(customerNew.id, 3)
    
    
    # ==============================================================================================
    # OPTIONAL if coupons discount is required:
    # Modify the subscription using the coupon in the discount item layer. Depending on the duration, invoices will be created with a discount (starting from the next invoice).
    # Below is 2 options to create different coupons for discount.
    # Update the subscription with the coupons for the discount.
    # ==============================================================================================
    # # STEP 1: Create a coupon based on percentage or fixed amount for the subscription.
    # discountCoupon = coupons.create_precentage_coupon("10", "once")
    # # OR
    # discountCoupon = coupons.create_fixed_amount_coupon("2", "once")
    # # STEP 2: Modify the subscription discount for the coupons.
    # discountSubscription = Subscription.step_subscription_mofidy(createSubscription.id, discountCoupon.id)
    
    
if __name__ == "__main__":
    main()