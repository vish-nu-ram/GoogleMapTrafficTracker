class Result:
    def __init__(self, route, mode, res):
        self.mode = mode
        self.route = route
        self.duration = res['Duration'] or None
        self.time_in_traffic = res['Time in Traffic'] or None
        self.warnings = res['Warnings'] or None
