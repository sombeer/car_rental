from customer_portal.models import Customer

class CustomerAuthenticationBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            customer = Customer.objects.get(username=username)
            if customer.check_password(password):
                return customer
        except Customer.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None
