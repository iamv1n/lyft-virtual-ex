from Serviceable import Serviceable 


class Car(Serviceable):
    def __init__(self, last_service_date, engine, battery, tires):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()