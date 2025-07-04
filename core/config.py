from core.constants import *
from core.route import Route
from datetime import time

routes = [Route(source=Harpur_Lane, destination=Bank_of_America, mode=Driving),
          Route(source=Harpur_Lane, destination=Aon, mode=[PublicTransport, Driving]),
          Route(source=Bank_of_America, destination=Harpur_Lane, mode=Driving, start_record_time=time(12, 0)),
          Route(source=Aon, destination=Harpur_Lane, mode=[PublicTransport, Driving], start_record_time=time(12, 0)),
          ]

# Example of a Route with ALL parameters passed:

test_route = Route(source=Harpur_Lane,  # Mandatory,
                   # Ideally configured with coordinates in core/constants.py: coordinates{}
                   destination=Aon,  # Mandatory,
                   # Ideally configured with coordinates in core/constants.py: coordinates{}
                   mode=[PublicTransport, Driving],  # Optional, default 'driving'
                   start_record_time=time(9, 0),  # Optional, default 0:00
                   stop_record_time=time(20, 0),  # Optional, default 23:59
                   save_to_file='test_file.csv',  # Optional,
                   # default file created with source and destination names in data_dump folder
                   stops=[Redford, Kilmainham_Goal],  # Optional, to add stops in route, not implemented yet
                   )

key = 'AIzaSy qwrqwerqwerqwer'
