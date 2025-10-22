class Galaxy:
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years, number_of_stars):
        # private Attribute (mit _ gekennzeichnet)
        self._name = name
        self._radius_in_m = radius_in_m
        self._mass_in_kg = mass_in_kg
        self._mean_temperature_in_celsius = mean_temperature_in_celsius
        self._age_in_years = age_in_years
        self._number_of_stars = number_of_stars

        # eigenes Attribut hinzufügen
        self._type = "Spiral"  # Beispiel: Spiral, Elliptical, Irregular

    # Getter-Methoden (lesen)
    def get_name(self):
        return self._name

    def get_radius(self):
        return self._radius_in_m

    def get_mass(self):
        return self._mass_in_kg

    def get_temperature(self):
        return self._mean_temperature_in_celsius

    def get_age(self):
        return self._age_in_years

    def get_number_of_stars(self):
        return self._number_of_stars

    def get_type(self):
        return self._type

    # Setter-Methoden (ändern)
    def set_name(self, name):
        self._name = name

    def set_type(self, galaxy_type):
        self._type = galaxy_type

    # Methode zur Zusammenfassung (Abstraktion)
    def summary(self):
        return (
            f"Galaxy '{self._name}' ({self._type}):\n"
            f" - Radius: {self._radius_in_m:.2e} m\n"
            f" - Mass: {self._mass_in_kg:.2e} kg\n"
            f" - Mean Temperature: {self._mean_temperature_in_celsius} °C\n"
            f" - Age: {self._age_in_years:.2e} years\n"
            f" - Number of Stars: {self._number_of_stars:.2e}\n"
        )


# Beispiel erstellen
milky_way = Galaxy("Milky Way", 4.3e20, 1.5e42, 10000000, 13.6e9, 250_000_000_000)

# Zusammenfassung ausgeben
print(milky_way.summary())
