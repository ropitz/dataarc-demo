Developing a good combinator
============================

A combinator is essentially a label for a query run on your data that will connect elements of your data return by that query with concepts in the dataARC concept map. Examples of combinators can be found in |spreadsheet|. The following key components are required for any new combinator:

* **Combinator (mapping) name.** A short human-readable description of the connection to be made
* **Data query.** A database query string that gathers the appropriate data to support the connection. You will
  construct this using a GUI, so don't worry if you're not familiar with how to code a query.
* **List of connected concepts.** Concepts should be chosen from the list of concepts in the dataARC concept map.
* **Reasoning for connection.** A short description of the relevance of your selected data to human ecodynamic
  research, and reasoning behind the connection between the data returned by the query and the concepts selected.
* **Literature citations.** List of supporting literature used to formulate the combinator. See |pollywillem| for
  guidance on selecting literature.

.. |spreadsheet| raw:: html

    <a href=https://github.com/ropitz/experiments/blob/master/data/dataarc_combinators.csv target=_blank> this spreadsheet </a>

.. |pollywillem| raw:: html

    <a href="" target=_blank> this documentation </a>
