from boardingpasssorterapp.exceptions import InvalidJourneyException
from boardingpasssorterapp.parsers import parse_boarding_pass_request


def sort_boarding_pass(request_body):
    passes = parse_boarding_pass_request(request_body)
    src_dst_map = {}
    for p in passes:
        src_dst_map[p.source] = p

    starting_point = determine_boarding_pass_order(src_dst_map)
    return prepare_journey_description(starting_point, src_dst_map)


def determine_boarding_pass_order(src_dst_map):
    starting_point = ''
    src_map_len = len(src_dst_map)
    for k, v in src_dst_map.items():
        if starting_point:
            break
        next_destination = v.destination
        for i in range(src_map_len):
            if next_destination in src_dst_map:
                next_destination = src_dst_map.get(next_destination).destination
            elif i == src_map_len-1:
                starting_point = k
                break
            else:
                break

    return starting_point


def prepare_journey_description(starting_point, src_dst_map):
    if not starting_point:
        raise InvalidJourneyException("Invalid journey")

    journey_description = list()
    src = starting_point
    if src:
        while src in src_dst_map:
            boarding_pass = src_dst_map[src]
            journey_description.append(boarding_pass.description())
            src = boarding_pass.destination

    journey_description.append("You have arrived at your final destination.")
    return journey_description

