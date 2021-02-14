API Documentation
=================

The dataARC project has implemented a publicly available REST API to aid
researchers in gathering, exploring, and modifying the dataARC information.

Each endpoint is described in detail `here
<https://api.data-arc.org/documentation>`__.  On this page, you'll find a list
of expandable sections that provide endpoint documentation for various classes
of dataARC information. Each endpoint thoroughly documents the parameters,
schema, and possible return values.

Click on "Try it out" under the endpoint heading, then scroll down to click
"Execute". An example JSON response will be populated below.

The standard GET, POST, PUT, and DELETE verbs are available for endpoints under most of
the classes, which include:

* *Category* -- contextual, environmental, and archaeological groupings of datasets
* *Combinators* -- the relationship defined by data specialists that link dataset
  features with concepts
* *Concept* -- the high-level CIDOC CRM concepts that define the dataARC shared ontology
  centered around "changing landscape". May be related to many combinators, and
  may have many concept topics.
* *Dataset* -- a dataset with defined attributes. The dataset will belong to one
  category, but may have many Combinators, Dataset fields, and fieatures
* *Event* -- automatic events logged by the API, such as create, update, delete,
  etc.
* *Features* -- relates to individual data points. Belongs to one dataset, but may
  have many combinators.
* *Search* -- saved searches using the dataARC search tool
* *Unclassified* -- the main endpoints used by the frontend dataARC tool to query
  the API.
* *Combinator-query* -- specific queries that are related to a combinator. For
  example, could return all records where percent avian is greater than 25.
* *Concept-map* -- the defined mapped relationships between all the concepts
* *Concept-topic* -- topics related to a given concept in the concept map
* *Dataset-field* -- definitions of field types and display text. Belongs to one
  dataset.
* *Spatial-coverage* -- predefined spatial areas
* *Temporal-coverage* -- predefined time periods for the timeline.
