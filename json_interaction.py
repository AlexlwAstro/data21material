import json


class RatesParser:
    def __init__(self, rates_input_file):
        rates_info = self._open_json_file(rates_input_file)
        self.base = rates_info['base']
        self.rates = rates_info['rates']
        self.GBP = self.rates['GBP']

    def _open_json_file(self, file):
        with open(file) as rates_file:
            return json.load(rates_file)


rates_reader = RatesParser('exchange_rates.json')
print(rates_reader.GBP)
