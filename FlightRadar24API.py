from FlightRadar24 import FlightRadar24API

fr_api = FlightRadar24API()
flights = fr_api.get_flights()
