from core.constants import coordinates
from datetime import time


class Route:
    """
    Route class to standardise different routes with required and optional properties.
    """
    def __init__(self,
                 source: str,
                 destination: str,
                 save_to_file: str = None,
                 mode=None,
                 stops=None,
                 start_record_time=time(0, 0),
                 stop_record_time=time(23, 59)
                 ):

        self.destination = None
        self.destination_name = None
        self.mode_of_transport = []
        self.save_to_file = None
        self.source = None
        self.source_name = None
        self.start_record_time = start_record_time
        self.stop_record_time = stop_record_time
        self.stops = []

        self.setSource(source=source)
        self.setDestination(destination=destination)
        self.setModeOfTransit(mode=mode)
        self.addStop(stop=stops)
        self.setSaveFile(file=save_to_file)

    def setSource(self, source):
        if source in coordinates.keys():
            self.source = coordinates[source]
            self.source_name = source
        else:
            raise f'Source: {source} not configured'

    def setDestination(self, destination):
        if destination in coordinates.keys():
            self.destination = coordinates[destination]
            self.destination_name = destination
        else:
            raise f'Destination: {destination} not configured'

    def setModeOfTransit(self, mode):
        if type(mode) == str:
            if mode not in self.mode_of_transport:
                self.mode_of_transport.append(mode)
        if type(mode) == list:
            for m in mode:
                if m not in self.mode_of_transport:
                    self.mode_of_transport.append(m)
        if not(mode and self.mode_of_transport):
            self.mode_of_transport = ['driving']

    def setSaveFile(self, file):
        if not file:
            self.save_to_file = 'data_dump/'\
                                + self.source_name.replace(" ", "")\
                                + '_to_'\
                                + self.destination_name.replace(" ", "")+'.csv'
        else:
            self.save_to_file = file

    def addStop(self, stop):
        self.stops.append(stop)

    def delStop(self, stop):
        if stop in self.stops:
            self.stops.remove(stop)

    def setStartTime(self, start_time: time = time(0, 0)):
        self.start_record_time = start_time

