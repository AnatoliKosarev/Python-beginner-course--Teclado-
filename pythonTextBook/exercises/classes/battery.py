class Battery:
    def __init__(self):
        self.battery_size = 75

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        if self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
