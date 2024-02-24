from abc import ABC, abstractmethod


class ITemperatureSensor(ABC):
    @abstractmethod
    def set_temperature(self, temperature):
        pass

    @abstractmethod
    def get_temperature(self):
        pass


class CelsiusTemperatureSensor(ITemperatureSensor):
    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature(self):
        return getattr(self, '_temperature', None)


class FahrenheitTemperatureSensor(ITemperatureSensor):
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature


class TemperatureSensorAdapter(ITemperatureSensor):
    def __init__(self, fahrenheit_sensor: FahrenheitTemperatureSensor):
        self._fahrenheit_sensor = fahrenheit_sensor

    def set_temperature(self, temperature):
        self._fahrenheit_sensor.set_temperature(temperature)

    def get_temperature(self):
        fahrenheit_temperature = self._fahrenheit_sensor.get_temperature()
        return (fahrenheit_temperature - 32) * 5 / 9


def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature():.2f} °C")


celsius_sensor = CelsiusTemperatureSensor()
fahrenheit_sensor = FahrenheitTemperatureSensor()

adapter = TemperatureSensorAdapter(fahrenheit_sensor)

celsius_sensor.set_temperature(20)
fahrenheit_sensor.set_temperature(54)

display_temperature(celsius_sensor)
display_temperature(adapter)
