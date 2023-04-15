from enum import Enum


class BoardingPass:
    def __init__(self, pass_type, source, destination):
        self.pass_type = pass_type
        self.source = source
        self.destination = destination


class TrainPass(BoardingPass):
    def __init__(self, pass_type, source, destination, train_number, seat_number):
        super().__init__(pass_type, source, destination)
        self.train_number = train_number
        self.seat_number = seat_number

    def description(self):
        s = f'Take train {self.train_number} from {self.source} to {self.destination}.'
        if self.seat_number:
            s = s + f' Seat in {self.seat_number}'
        else:
            s = s + ' No seat assignment'
        return s


class FlightPass(BoardingPass):
    def __init__(self, pass_type, source, destination, flight_number, flight_type, gate_number, seat_number, baggage_counter):
        super().__init__(pass_type, source, destination)
        self.flight_number = flight_number
        self.flight_type = flight_type
        self.gate_number = gate_number
        self.seat_number = seat_number
        self.baggage_counter = baggage_counter

    def description(self):
        s = f'From {self.source}, take flight {self.flight_number} to {self.destination}. Gate {self.gate_number}, seat {self.seat_number}.'
        if self.baggage_counter:
            s = s + f' Baggage drop at ticket counter {self.baggage_counter}'
        elif self.flight_type == 'Connecting':
            s = s + ' Baggage will be automatically transferred from your last leg.'
        return s


class BussPass(BoardingPass):
    def __init__(self, pass_type, source, destination, bus_number, bus_type, seat_number):
        super().__init__(pass_type, source, destination)
        self.bus_number = bus_number
        self.bus_type = bus_type
        self.seat_number = seat_number

    def description(self):
        s = f'Take the {self.bus_type} from {self.source} to {self.destination}.'
        if self.seat_number:
            s = s + f' Seat {self.seat_number}'
        else:
            s = s + ' No seat assignment'
        return s


class BoardPassType(Enum):
    TRAIN = 1
    FLIGHT = 2
    BUS = 3

