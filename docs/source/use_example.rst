How to use
=====

colorbar
-----


example
^^^^^
.. code-block:: python

   import numpy as np
   import cwbplot.cwb_colorbar as cwbcolor #import cwbcolorbar 模組
   import matplotlib.pyplot as plt
   
   rainfall = np.load("/home/c052/work/opendata/21080606/rainfall.npy")
   
   t2m = np.load("/home/c052/work/opendata/21080606/t2m.npy")
   
   ygrids, xgrids = rainfall.shape
   
   xx, yy = np.meshgrid(np.linspace(0, xgrids-1, xgrids),np.linspace(0,ygrids-1, ygrids))
   raincb = cwbcolor.rain() #使用rain()方法，回傳雨量colorbar的物件
   plt.contourf(xx, yy, rainfall, **raincb)

   #設定「直」的colorbar跟tick label
   cbstr = [ str(i) for i in raincb["levels"][1:-1]] 
   cbar = plt.colorbar(ticks=raincb["levels"][1:-1])
   newticks = cbar.ax.set_yticklabels(cbstr)


.. image:: ./image/raincolorbar_cwbrfs.png
 

colormap (default)
^^^^^



