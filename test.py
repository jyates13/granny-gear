import datetime
import activity

dts = [datetime.datetime(2016, 01, 23, 19, i, 30) for i in range(59, -1, -1)]
rps = [activity.RoutePoint(56+j/100.0, 0.0, dts[j], j) for j in range(0, 60)]

print dts
print rps

act1 = activity.Activity(rps)

print act1.timedate