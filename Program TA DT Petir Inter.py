import os
os.environ["PROJ_LIB"] = "Anaconda"
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import pylab
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from scipy.interpolate import interp2d


folderdata = 'D:/Fis TA 1/Data & Program TA/Data lightning from TRMM/Dataset/'
files = os.listdir(folderdata)

plt.figure(figsize = (15,4))

file = files[2] 
ds = Dataset(folderdata+file, 'r')

lat = ds.variables['Latitude'][290:330]
lon = ds.variables['Longitude'][2850:2950]

xx,yy= pylab.meshgrid(lon,lat)

petir = ds.variables['VHRFC_LIS_FRD'][290:330,2850:2950]

m=Basemap(projection='cyl',llcrnrlat=-9,urcrnrlat=-5.5,llcrnrlon=105,urcrnrlon=115,resolution='h')

lon1,lat1 = m(xx,yy)

ax = plt.axes(projection = ccrs.PlateCarree())

ax.add_feature(cfeature.OCEAN,zorder=5, color='white')

clevs = pylab.arange(0, 81, 5)

x1 = pylab.arange(lon1.min(), lon1.max(), .1)
y2 = pylab.arange(lat1.min(), lat1.max(), .1)
x1 = np.round(x1,1)
y2 = np.round(y2,1)
xi, yi = np.meshgrid(x1, y2)

f = interp2d(lon, lat, petir, kind = 'cubic')
z2 = f(x1, y2)

print(np.max(z2))
print(np.min(z2))

cs_rain = ax.contourf(xi, yi, z2, clevs, cmap='rainbow', latlon = True)

plt.text(109.5, -7.25, 'Jawa Tengah', fontsize = 10, fontweight = 'demi', fontfamily = 'sans-serif')
plt.text(107.5, -7, 'Jawa Barat', fontsize = 10, fontweight = 'demi', fontfamily = 'sans-serif')
plt.text(111.65, -7.5, 'Jawa Timur', fontsize = 10, fontweight = 'demi', fontfamily = 'sans-serif')
plt.text(106, -6.25, 'Banten', fontsize = 10, fontweight = 'demi', fontfamily = 'sans-serif')
plt.text(106.75, -6.25, 'Jakarta', fontsize = 10, fontweight = 'demi', fontfamily = 'sans-serif')
plt.text(110.25, -7.9, 'Yogyakarta', fontsize = 10, fontweight = 'demi', fontfamily = 'sans-serif')

m.drawmapboundary(color = 'black', linewidth=1.5)
ax.coastlines(linewidth = 3, color = 'black')
cb = plt.colorbar(cs_rain, orientation = 'vertical', pad = 0.01, ticks=[0, 20, 40, 60, 80])
cb.set_label(label= 'sambaran / km$^2$ tahun')

ax.add_feature(cfeature.STATES, edgecolor= 'k', linewidth = 1)
paralles=pylab.arange(-9,-5.5,.5)
meridians=pylab.arange(105.5,115,1)
m.drawparallels(paralles,labels=[1,0,0,0], linewidth=0, fontsize=10)
m.drawmeridians(meridians,labels=[0,0,0,1], linewidth=0, fontsize=10)
plt.xlabel('Longitude', labelpad = 20, fontsize=10)
plt.ylabel('Latitude', labelpad = 40, fontsize=10)


# import matplotlib.patches

# rect1 = matplotlib.patches.Rectangle((106.1,-6.5), 1.5, .5, fill = False, zorder = 5, edgecolor = 'red', linewidth = 3)

# ax.add_patch(rect1)

# rect2 = matplotlib.patches.Rectangle((109,-7.5), 1.5, .5, fill = False, zorder = 5, edgecolor = 'red', linewidth = 3)

# ax.add_patch(rect2)

hasil = 'D:/Fis TA 1/Data & Program TA/Data lightning from TRMM/Hasil/'
plt.savefig(hasil+'Test3.png', dpi = 700)
