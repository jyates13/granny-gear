## =============================================================================================================
## PROGRAM NAME: activity.py
## CREATED BY: Jack
## CREATED ON: 2016-01-23
##==============================================================================================================
## DESCRIPTION:
##  Defines the Activity class which contains all the information about a single activity (e.g. a run). Also 
##  defines classes required for the Activity class.  
##==============================================================================================================
## USED BY:
##  Probably everything!
##==============================================================================================================

import datetime as dt

class RoutePoint:
    def __init__(self, latitude, longitude, timedate, elevation=None):
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError('latitude should be between 90 and -90.')
        if not (-180.0 < longitude <= 180.0):
            raise ValueError('longitude should be between -180 and 180.')
        if not isinstance(timedate, dt.datetime):
            raise TypeError('timedate should be an instance of the datetime.datetime class.')
        
        self.latitude = latitude
        self.longitude = longitude
        self.timedate = timedate
        self.elevation = elevation

    def __repr__(self):
        if (self.elevation is not None):
            return "RoutePoint({0}, {1}, {2}, {3})".format(\
                self.latitude, self.longitude, self.timedate, self.elevation)
        else:
            return "RoutePoint({0}, {1}, {2})".format(\
                self.latitude, self.longitude, self.timedate)

    def __str__(self):
        if (self.elevation is not None):
            return "lat {0}, lon {1}, elevation {2} at {3}".format(\
                self.latitude, self.longitude, self.elevation, self.timedate)
        else:
            return "lat {0}, lon {1} at {2}".format(\
                self.latitude, self.longitude, self.timedate)

class Activity:
    def __init__(self, routepoints, timedate=None):
        if not isinstance(routepoints, list):
            raise TypeError('routepoints should be a list of instances of the RoutePoint() class.')
        elif (len(routepoints) == 0):
            raise TypeError('routepoints must contain at least one entry.')
        elif not isinstance(routepoints[0], RoutePoint):
            raise TypeError('routepoints should be a list of instances of the RoutePoint() class.')

        self.routepoints = sorted(routepoints, key = lambda rp: rp.timedate)

        if (timedate is None):
            self.timedate = self.routepoints[0].timedate 
        else: 
            if not isinstance(timedate, dt.datetime):
               raise TypeError('timedate should be an instance of the datetime.datetime class.')
            self.timedate = timedate

        


## =============================================================================================================
## END OF PROGRAM
## =============================================================================================================
