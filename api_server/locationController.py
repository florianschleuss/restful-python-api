import customerController

class Controller:
    def get_locations(self, customers):
        locations = []
        for customer in customers: 
            location = customers[customer]['city']
            if not location in locations:
                locations.append(location)
        return locations
