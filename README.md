# Install Requirements
pip install django

# To execute 
- Move to the folder root directly 
- Execute: PYTHONUNBUFFERED=1 python manage.py runserver

# To run tests
- Move to the folder root directly
- Execute: PYTHONUNBUFFERED=1 python manage.py test boardingpasssorterapp.tests


# REST API Details
URI: /boarding-pass/sort

Method: POST

API Will take list of _boardingPass_ object having the following schema
````{
            "type": "BUS",
            "source": "Barcelona",
            "destination": "Gerona Airport",
````

Supported Boarding Pass Types:
- TRAIN
- FLIGHT
- BUS

Additional attributes for Boarding Pass Type:
- TRAIN
  - trainNumber
  - seatNumber

- FLIGHT
  - flightNumber
  - seatNumber
  - gateNumber
  - baggageCounter
  - flightType (Connecting, Non-Stop)

- BUS
  - seatNumber
  - busType (Airport Bus, Regular)


###Sample Payload
```
{
    "boardingPasses": [
        {
            "type": "BUS",
            "source": "Barcelona",
            "destination": "Gerona Airport",
            "busType": "Airport Bus"
        },
        {
            "type": "FLIGHT",
            "source": "Gerona Airport",
            "destination": "Stockholm",
            "flightNumber": "SK455",
            "gateNumber": "45B",
            "seatNumber": "3A",
            "flightType": "Normal",
            "baggageCounter": "344"
        },
        {
            "type": "TRAIN",
            "source": "Madrid",
            "destination": "Barcelona",
            "trainNumber": "78A",
            "seatNumber": "45B"
        },
        {
            "type": "FLIGHT",
            "source": "Stockholm",
            "destination": "New York",
            "flightNumber": "SK22",
            "gateNumber": "22",
            "seatNumber": "7B",
            "flightType": "Connecting"
        }
    ]
}

```



## Assumptions
- Each destination will appear once in the list
- For case like following, two boarding passes are expected to be provided
```
Take the airport bus from Barcelona to Gerona Airport. No seat assignment. 3. From
Gerona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket
counter 344.
```
Example (Barcelna to Gerona Airport via Bus & Gerona Airport to Stockholm via flight)
```
{
            "type": "BUS",
            "source": "Barcelona",
            "destination": "Gerona Airport",
            "busType": "Airport Bus"
        },
        {
            "type": "FLIGHT",
            "source": "Gerona Airport",
            "destination": "Stockholm",
            "flightNumber": "SK455",
            "gateNumber": "45B",
            "seatNumber": "3A",
            "flightType": "Normal",
            "baggageCounter": "344"
        }
```
