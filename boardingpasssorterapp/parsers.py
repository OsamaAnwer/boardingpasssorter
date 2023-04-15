import json
import logging

from boardingpasssorterapp.boarding_pass import TrainPass, FlightPass, BussPass, BoardPassType


def parse_boarding_pass_request(request_body):
    passes_data = request_body.get('boardingPasses', [])
    boarding_passes = []
    for pass_data in passes_data:
        try:
            pass_type = pass_data.get('type')
            source = pass_data.get('source')
            destination = pass_data.get('destination')
            pass_type_enum = BoardPassType[pass_type]
            if pass_type_enum == BoardPassType.TRAIN:
                train_number = pass_data.get('trainNumber')
                seat_number = pass_data.get('seatNumber')
                train_pass = TrainPass(pass_type, source, destination, train_number, seat_number)
                boarding_passes.append(train_pass)
            elif pass_type_enum == BoardPassType.FLIGHT:
                flight_number = pass_data.get('flightNumber')
                flight_type = pass_data.get('flightType')
                gate_number = pass_data.get('gateNumber')
                seat_number = pass_data.get('seatNumber')
                baggage_counter = pass_data.get('baggageCounter')
                flight_pass = FlightPass(pass_type, source, destination, flight_number, flight_type, gate_number, seat_number, baggage_counter)
                boarding_passes.append(flight_pass)
            elif pass_type_enum == BoardPassType.BUS:
                bus_number = pass_data.get('trainNumber')
                seat_number = pass_data.get('seatNumber')
                bus_type = pass_data.get('busType')
                bus_pass = BussPass(pass_type, source, destination, bus_number, bus_type, seat_number)
                boarding_passes.append(bus_pass)
            else:
                raise NotImplementedError("Type not supported")
        except KeyError:
            raise NotImplementedError("Type not supported")
        except TypeError as e:
            print(e)
            raise Exception("Invalid input data")

    return boarding_passes
