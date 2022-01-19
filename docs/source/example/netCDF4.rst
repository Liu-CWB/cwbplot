The example for netCDF4 and wrfpython
-----

The output is from wrf model. 

Data format: netCDF

Data source: CWB

^^^^^

.. code-block:: python

    import netCDF4 as nc4
    import wrf
    
    wrfout1 = nc4.Dataset("wrfout1")

    #Check variables in wrfout1
    varall = wrfout1.variables

    #GET T2 where is already in wrfout1
    T2_netCDF4 = wrfout1["T2"][0] # 0 means the time dims. The shape of wrfout1["T2"] is (1,450,450)

    #There is another way to get T2 (only for wrf output netCDF file).
    T2_wrfpython = wrf.getvar(wrfout1,"T2") #The shape of T2_wrfpython is (450,450)
    
    #Moreover, wrfpython can help do some variable calculation which not include the source wrf output file.
    #For example, 10 m wind speed
    ws10m = wrf.getvar(wrfout1,"wspd10")

