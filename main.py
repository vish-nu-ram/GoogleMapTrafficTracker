from core.CSVHandler import updateCSV
from datetime import datetime, time
from time import sleep

from core.config import routes
from core.maps import getRouteDetails
import gc

from core.result import Result

_15_minutes = 60 * 15
_1_minute = 60
_1_second = 1

_6_30_AM = time(6, 30)
_9_30_PM = time(21, 30)


def saveRouteDetails(route):
    """
    Pass a route to the function to save the travel details
    onto the configured save file based on other configurations of the route

    Saves result from API call into an object of type core.result.Result to standardize outputs
    before writing them to configured CSV files

    :param route: Route object of type core.route.Route
    :return: N/A
    """
    now = datetime.now()

    if now.time() < route.start_record_time or now.time() > route.stop_record_time:
        return

    for mode in route.mode_of_transport:
        res = getRouteDetails(source=route.source,
                              destination=route.destination,
                              mode_of_transport=mode,
                              depart_time=now)
        result = Result(route, mode, res)
        print(f'Updated file : {route.save_to_file},{now}')
        updateCSV(route.save_to_file, [
            route.source_name,
            route.destination_name,
            result.duration,
            now,
            result.mode,
            result.warnings,
            result.time_in_traffic
        ])
        del result


if __name__ == '__main__':
    '''
    Waits for the ideal start and stop time for execution, sleeps otherwise.
    Iteratively runs the saveRouteDetails function for each route configured in core/config.py: routes[]
    if the current time fits within the configured start and stop time.
    '''

    while datetime.now().minute not in {0, 15, 30, 45}:
        sleep(_1_second)


    def run():
        for route in routes:
            saveRouteDetails(route)

    while True:
        now = datetime.now()
        while now.time() < _6_30_AM or now.time() > _9_30_PM:
            sleep(_15_minutes)
            now = datetime.now()
        run()
        gc.collect()
        sleep(_15_minutes)

