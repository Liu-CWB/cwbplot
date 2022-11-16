Central Weather Bureau Open Data
=============

This section provides how to process central weather bureau open data


Quick look
-------------

xml file

.. code-block:: python

   from cwbplot import opdata
   out = opdata.read_xml("xmlfile")



json file

.. code-block:: python
   
   from cwbplot import opdata
   out = opdata.read_xml("jsonfile")


api(Only Json)

.. code-block:: python

   from cwbplot import opdata
   out = opdata.json_api("opend dataid","apipath")


grib

.. code-block:: python

   from cwbplot import opdata
   out = opdata.read_grib("grib2 file")



Open data items
--------------------

.. list-table:: 
   :widths:  28 16 12
   :header-rows: 1

   * - 資料名稱
     - 資料id(dataid)
     - 範例連結
   * - 自動氣象站-氣象觀測資料
     - O-A0001-001 
     - `Link <https://cwbplot.readthedocs.io/en/dev/example/O-A0001-001.html>`_
   * - 自動氣象站-雨量觀測資料
     - O-A0002-001
     - `Link <https://cwbplot.readthedocs.io/en/dev/example/O-A0002-001.html>`_
   * - 局屬氣象站-現在天氣觀測報告
     - O-A0003-001
     - `Link <https://cwbplot.readthedocs.io/en/dev/example/O-A0003-001.html>`_
   * - 數值預報模式-區域預報模式(WRF-3公里)
     - M-A0064-???
     - `Link <https://cwbplot.readthedocs.io/en/dev/example/M-A0064.html>`_
