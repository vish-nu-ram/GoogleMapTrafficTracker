import googlemaps
from datetime import datetime
from core.config import key

now = datetime.now()


def getRouteDetails(source,
                    destination,
                    mode_of_transport,
                    depart_time):
    gmaps = googlemaps.Client(key=key)
    res = gmaps.directions(source, destination, mode=mode_of_transport, departure_time=depart_time)
    duration = res[0]['legs'][0]['duration']['text']
    try:
        time_in_traffic = res[0]['legs'][0]['duration_in_traffic']['text']
    except:
        time_in_traffic = '0'
    try:
        warnings = res[0]['warnings']
    except:
        warnings = None
    del res
    del gmaps
    return {'Duration': duration,
            'Time in Traffic': time_in_traffic,
            'Warnings': warnings}


if __name__ == '__main__':
    pass
