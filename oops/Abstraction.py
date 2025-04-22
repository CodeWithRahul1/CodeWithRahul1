'''
Abstraction is the concept of exposing only the necessary information to the outside world while hiding the internal implementation details.

Properties of Abstraction:

Simplification: Complex systems are simplified by abstracting away unnecessary details.
Modularity: Abstracted modules can be developed and tested independently.
'''


class PaymentGateway:
    def process_payment(self, amount):
        # Simplified payment processing logic
        print(f"Processing payment of ${amount}")

class StripePaymentGateway(PaymentGateway):
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, amount):  # Abstracted implementation
        # Complex payment processing logic using Stripe API
        print(f"Processing payment of ${amount} using Stripe")

class PayPalPaymentGateway(PaymentGateway):
    def __init__(self, client_id):
        self.client_id = client_id

    def process_payment(self, amount):  # Abstracted implementation
        # Complex payment processing logic using PayPal API
        print(f"Processing payment of ${amount} using PayPal")

# Create a PaymentGateway object without knowing the internal implementation
payment_gateway = StripePaymentGateway(" stripe_api_key ")

# Process a payment using the abstracted method
payment_gateway.process_payment(100)