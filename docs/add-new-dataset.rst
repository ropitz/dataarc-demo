Prepare your data
-----------------

By now you should have a better understanding of the basics for preparing your data for dataARC.  You should know how to create combinators in order to map your data to the dataARC concept map and you should have a good sense of what concepts are applicable to your dataset. 

Convert your data to GeoJSON and Validate (The spatial component of your data)
---------------------------------------------------------------------------------

If you have stepped through some of the exercises using the dataARC Ecosystem Explorer, you know that dataARC requires data to be in the GeoJSON format.  GeoJSON is an `open standard format <https://tools.ietf.org/html/rfc7946#section-3.1.2>`__ for representing simple geographic features, in this case point locations, with attribute information.  There are several free tools available online for converting your data to GeoJSON.  `Convert CSV for GeoJSON <https://www.convertcsv.com/csv-to-geojson.htm>`__ is free and is relatively straightforward and easy-to-use.  Feel free to use any GeoJSONconverter available to you. Remember that point locations must be stored as latitude and longitude and in separate columns in your table.

Next it is important to validate your newly created JSON file to ensure that the file is valid before importing it into dataARC.  As with converters, there are a lot of free GeoJSON validators online.  We recommend the following:

.. image:: _static/dataarc.jpg
   :width: 400
   :class: align-left
`JSON Formatter <https://jsonformatter.org/>`__  is one of the easiest yet advanced formatting and validating tools.  It can be used as a JSON validator, editor, and viewer.  While a login isn’t required to save your JSON data, data saved without a login becomes public.  To ensure that your data is private, create an account and login first.  

`GeoJSON IO <https://geojson.io/#map=4/53.57/-39.29>`__ is largely a viewer for GeoJSON data but also offers some conversion options (including CSV).  This interactive viewer allows you to drop your newly created JSON file onto the map and visualize the data quickly. 

A Note about Dates  (The temporal component of your data)
---------------------------------------------------------

How we reference time varies considerably across different disciplines.  Visit the `Time Synthesis section <https://www.data-arc.org/time/>`__ of the dataARC website for a more detailed discussion of this topic.  To ensure compatibility with the temporal filter options in dataARC, dates can be entered as a single discrete value or a date range.  Dates must also be entered in Common Era/Before Common Era (CE/BCE) numerical format where **CE dates are indicated with a positive number and BCE dates are indicated with a negative number.**   
