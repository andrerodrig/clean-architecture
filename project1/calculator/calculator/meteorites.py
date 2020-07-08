import urllib.request
import json

from calculator import calculator as calc

URL = ('https://data.nasa.gov/resource/y77d-th95.json')

class MeteoriteStats:
    def get_data(self):
        with urllib.request.urllopen(URL) as url:
            return json.loads(url.read().decode())

    def average_mass(self, data):
        c = calc.Calc()
        masses = [float(d['mass']) for d in data if 'mass' in d]

        return c.avg(masses)
