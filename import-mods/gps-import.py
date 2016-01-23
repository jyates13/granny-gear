## =============================================================================================================
## PROGRAM NAME: GPS IMPORT
## CREATED BY: Doug (github = dpfinch)
## CREATED ON: 22/10/2015
##==============================================================================================================
## DESCRIPTION:
##  This program will contain the modules to read in the .gpx file and transform it into a reasonable format
##==============================================================================================================
## USED BY:
##  Name the modules that uses this module
##==============================================================================================================

def get_latitude(data_points):
    '''
        Returns a list of latitude coordinates from the list of instances passed to it.
    '''

    latitude = []
    for dp in data_points:
        latitude.append(dp.latitude)
    
    return latitude

def get_longitude(data_points):
    '''
        Returns a list of longitude coordinates from the list of instances passed to it.
    '''

    longitude = []
    for dp in data_points:
        longitude.append(dp.longitude)
    
    return longitude



def get_data_from_file(filepath):
    '''
        This module parses the data from the .gpx file given to it and returns a list if instances
        Each instance contains lat,lon,elevation,time and a few other parameters. This list of
        instances can be used to extract more readable data (eg. get a list of latitudes)

        The returned list will be a long list (in the 1000's depending on the activity).
        Each element is an instance of gps data.
    '''
    import gpxpy

    f_open = open(filepath,'r')
    gpx = gpxpy.parse(f_open)

    data_list = gpx.tracks[0].segments[0].points
        
    return data_list

## =============================================================================================================
## END OF PROGRAM
## =============================================================================================================
