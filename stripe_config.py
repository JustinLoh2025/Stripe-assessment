import os
from dotenv import load_dotenv
import stripe

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

account = stripe.Account.retrieve()

#print("Account Id: ", account.id)