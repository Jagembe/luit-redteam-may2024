# List of connections between cities with their respective flight durations (in minutes)
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

# Initialize variables to track flight data
flight_time = 0
num_flights = 0
rome_flights = []  # List to store flight durations to Rome
departure_cities_to_rome = []  # List to store departure cities with flights to Rome
all_destinations = set()  # Set to store all unique destination cities

# Loop through each connection to analyze flight data
for connection in connections:
    destination = connection[1]  # Destination city of the flight
    flight_duration = connection[2]  # Duration of the flight in minutes
    all_destinations.add(destination)  # Add destination city to the set of all destinations

    # Check if the destination is Rome
    if destination.lower() == 'rome':
        num_flights += 1  # Increment the count of flights to Rome
        flight_time += flight_duration  # Add the flight duration to the total flight time to Rome
        rome_flights.append(flight_duration)  # Append the flight duration to the list of flights to Rome
        departure_cities_to_rome.append(connection[0])  # Append the departure city to the list

# Calculate the average flight time to Rome if there are flights to Rome
average_flight_time_to_rome = flight_time / num_flights if num_flights > 0 else 0

# Determine the longest and shortest flight durations to Rome
longest_flight_to_rome = max(rome_flights) if rome_flights else None
shortest_flight_to_rome = min(rome_flights) if rome_flights else None

# Sort the list of flight durations to Rome
rome_flights_sorted = sorted(rome_flights)

# Calculate the total flight time for all connections
total_flight_time = sum([connection[2] for connection in connections])

# Print the analysis results
print(f'{num_flights} connections lead to Rome with an average flight time of {average_flight_time_to_rome:.2f} minutes.')
print(f'The longest flight to Rome is {longest_flight_to_rome} minutes.')
print(f'The shortest flight to Rome is {shortest_flight_to_rome} minutes.')
print(f'Flights to Rome sorted by time: {rome_flights_sorted}')
print(f'Departure cities with direct flights to Rome: {departure_cities_to_rome}')
print(f'Total flight time for all connections: {total_flight_time} minutes.')
print(f'All unique destination cities: {all_destinations}')
