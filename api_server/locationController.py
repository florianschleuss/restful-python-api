import customerController

class Controller:
    def get_locations(self, customers_list):
        locations = []
        for customer in customers_list: 
            location = customers_list[customer]['city']
            if not location in locations:
                locations.append(location)
        return locations

    def get_location(self, location, customers_list):
        location_list = {location: []}
        for name, customer in customers_list.items():
            if customer['city'] == location:
                location_list[location].append(customer)
        return location_list
