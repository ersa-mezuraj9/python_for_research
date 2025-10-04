from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pyproj import transform

birddata = pd.read_csv("C:/Users/User/OneDrive/Desktop/python_for_research/data/bird_tracking.csv")

print(birddata.info())

# Plot Bird Migration Paths by Longitude and Latitude
bird_names = pd.unique(birddata.bird_name)
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x , y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()

# Histogram of Eric's 2D Speed Distribution
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
print(np.sum(np.isnan(speed))) # 85 entries are not numeric
ind = np.isnan(speed)
plt.hist(speed[~ind]) # we took those entries which are not equal to True (nan values). But it is not necessary anymore cause now matplot can deal with nan values and the histogram can be shown.
plt.show()

ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
plt.hist(speed, bins=np.linspace(0,30,20), density=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")
plt.show()

birddata.speed_2d.plot(kind='hist', range=[0,30]) #creating histogram using pandas
plt.xlabel("2D speed (m/s)")
plt.show()

# Visualizing Elapsed Time and Daily Mean Speed of Eric
import datetime
print(datetime.datetime.today())

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata['timestamp'] = pd.Series(timestamps, index = birddata.index)

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)
plt.plot(elapsed_days)
plt.xlabel("Observation")
plt.ylabel("Elapsed time (days)")
plt.show()

data = birddata[birddata.bird_name == "Eric"]
daily_mean_speed = []
next_day = 1
inds = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1 
        inds = []

plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean Speed (m/s)")
plt.show()

# Plot Bird Migration Paths on a Map Using Cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

for name in bird_names:
    ix = birddata['bird_name'] == name
    x , y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)
plt.legend(loc="upper left")
plt.show()