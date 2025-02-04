class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        print(self.first_name)

    def get_last_name(self):
        print(self.first_name)

    def get_full_name(self):
        print(self.first_name, self.last_name)

Veronika = User("Veronika", "Ivanova")
Ivanova = User("Ivanova", "Veronika")
Veronika_Ivanova = User("Veronika", "Ivanova")

Veronika.get_first_name()
Ivanova.get_last_name()
Veronika_Ivanova.get_full_name()