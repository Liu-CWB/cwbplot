Central Weather Bureau \ Open Data
=============

This section provides how to process central weather bureau open data


Quick look
=============

xml file

.. code-block:: python

   from cwbplot import opdata
   out = opdata.read_xml("xmlfile")



json file

.. code-block:: python
   
   from cwbplot import opdata
   out = opdata.read_xml("jsonfile")



api

.. code-block:: python

   from cwbplot import opdata
   out = opdata.json_api("opend dataid","apipath")



Open data items
================

+-------------------------+------------------+-------------+
|資料名稱                 | 資料id(dataid)   |範例連結     |
+=========================+==================+=============+
|自動氣象站-氣象觀測資料  | O-A0001-001      |`Link <https://cwbplot.readthedocs.io/en/dev/example/O-A0001-001.html>`_  |
+-------------------------+------------------+-------------+
