import geopandas
import matplotlib.pyplot as plt
import pandas as pd

# thailand shape
shape_file = 'THA_Adm1_GISTA_plyg_v5.shp' #downloaded website in readme file
thailand_shape = geopandas.read_file(shape_file)

#tourist data
tourist_file = 'clean_stat.csv'
tourist_df = pd.read_csv(tourist_file)

#join shape and data
joined_df = thailand_shape.set_index('Adm1Name').join(tourist_df.set_index('province'))

#plot map
f, (ax1,ax2,ax3) = plt.subplots(1,3, sharey=True)
joined_df.plot(column = 'total_visitor', cmap = 'Blues',linewidth=0.1, vmin = 500000, vmax = 10000000, edgecolor='0.8',ax = ax1)
joined_df.plot(column = 'thai_visitor', cmap = 'Blues',linewidth=0.1, vmin = 500000, vmax = 10000000, edgecolor='0.8',ax = ax2)
joined_df.plot(column = 'foreign_visitor', cmap = 'Blues',linewidth=0.1, vmin = 500000, vmax = 10000000, edgecolor='0.8',ax = ax3)

ax1.set_title('Total visitors')
ax2.set_title('Thai visitors')
ax3.set_title('Foreign visitors')

ax1.axis('off')
ax2.axis('off')
ax3.axis('off')

sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=500000, vmax=10000000))
sm._A = []
cbaxes = f.add_axes([0.92, 0.22, 0.02, 0.3]) 
plt.colorbar(sm, cax=cbaxes)

f.savefig('map.jpg',dpi=300)
