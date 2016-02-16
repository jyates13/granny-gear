
# Just a quite program to test how to use gpxpy to get data out of files and how to use
# geopy to get distance between points.
# This is very rough and not pretty but its only a test

def get_speed():

	import gpxpy # To get data out of file
	from geopy.distance import vincenty # Use Vicenty method to find distance between two points
	import numpy as np


	test_fi = 'activities/20150426-104720-Ride.gpx'
	gpx_fi = open(test_fi)
	gpx = gpxpy.parse(gpx_fi) # parse the data from the file

	tracks = gpx.tracks[0] # Not sure the structure of the file but need to extract tracks then segments (each with a lenght of one)
	segments = tracks.segments[0]

	points = segments.points # These are all the data points with the useful data
	# points.latitude -> latitude coord
	# points.longitude -> longitude coord
	# points.time -> time of point

	initial_coords = (points[0].latitude,points[0].longitude)
	initial_time = points[0].time

	distance = list() # Create empty lists to append the distance between points and time 
	time_diff = list()

	# Loop through all the points and get distance between them and difference in time
	for p in range(1,len(points)):
		new_coords = (points[p].latitude,points[p].longitude)
		dist_difference = vincenty(initial_coords,new_coords).meters
		distance.append(dist_difference)
		initial_coords = new_coords

		time_diff.append((points[p].time - initial_time).seconds)
		initial_time = points[p].time

	
	speed = np.asarray(distance) / np.asarray(time_diff) # Speed = distance/time -> m/s
	return distance, time_diff, speed


# Quick comparison with strava for this activity:
# Total distance: 53.17 km,   Strava: 52.7 km
# Ave speed:      24.86 km/h, Strava: 24.3 km/h
# Max speed:      87.16 km/h, Strava: 51.8 km/h
# Total time:     2.85 hrs,   Strava: 2.5 hrs
	
	 



