class Controller:
    def __init__ (self):
        self.customer = {}

    def get_customers(self):
        return self.customer

    def get_customer(self, customer_id):
        if customer_id in self.customer:
            return self.customer[customer_id]
        else:
            return {'success': False, 'message': 'customer not found'}, 404

    def post_customer(self, customer_id, customer):
        if not customer_id in self.customer:
            self.customer[customer_id] = customer
            return {'success': True}
        else:
            return {'success': False, 'message': 'customerID already present'}

    def patch_customer(self, customer_id, customer):
        if customer_id in self.customer:
            self.customer[customer_id] = customer
            return {'success': True}
        else:
            return {'success': False, 'message': 'customer not found'}, 404
            
    def delete_customer(self, customer_id):
        if customer_id in self.customer:
            del self.customer[customer_id]
            return {'success': True}
        else:
            return {'success': False, 'message': 'customer not found'}, 404