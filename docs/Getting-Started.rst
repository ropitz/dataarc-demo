Concept Map Overview
=====================

- Dataset overview
    * The full list of current datasets is included in |DEE|.
    * A short summary of the datasets can be found at the |about_dataarc|.
    * Full dataset biographies are included here: TBD.
    * What is important about these datasets to be included here? From the perspective of scientists who work in one discipline, environmental policy makers, data mining folks. Maybe aim for new undergrad level.
    * Use JN1 to see existing connections within DataARC. (JN tells story about how connections exist)

- Concepts overview
    * Become familiar with concepts. 
    * Concepts are taken directly from the CIDOC CRM v 6.0+. For an exploratory examination of these concepts, visit
      the |use_and_learn|.
    * A full set of DataARC concepts with descriptions is available |concepts|.
    * The list of concepts should be treated as static. Try to find concepts that can be linked to your data from those that already exist.

Exploring the existing Knowledge Map
==================================== 
1. Navigate to |DEE|.
2. Click the Launch Binder button. This process may take a couple of minutes to start up.
3. Once the Jupyter Binder loads, click on the `dataarc_pyvis.ipynb` file to open it.
4. Follow directions in the notebook.

.. |DEE| raw:: html

    <a href=https://github.com/aelydens/dataarc-demo<https://github.com/ropitz/experiments/tree/master/data
    target=_blank>DataArc Ecosystem Explorer &#8663;</a>

.. |about_dataarc| raw:: html

    <a href=https://beta.data-arc.org/about target=_blank> DataArc website &#8663;</a>

.. |use_and_learn| raw:: html

    <a href=http://www.cidoc-crm.org/use_and_learn target=_blank>CIDOC Use & Learn Page &#8663;</a>

.. |concepts| raw:: html

    <a href=https://github.com/ropitz/experiments/tree/master/docs/dataarc-concepts target=_blank>on GitHub &#8663;</a>

Including mappings to DataARC
=============================

Below is a list of suggestions to get you started with adding mappings of your dataset to the knowledge map built within DataARC. Any of these items can be visited multiple times in the process, and there is no requirement to go in any specific order. We suggest you come back to this list often to help recenter and reclaim scope.

- Identify the key dataset for mapping in DataARC.
    * See Choosing which data to add later in this document for more guidelines to consider.
- Understand the concepts represented by the knowledge graph.
    * Concepts are taken directly from the CIDOC CRM. For an exploratory examination of these concepts, visit
      |use_and_learn|
- Collect concepts from literature associated with the key dataset. 
    * Recall that the CIDOC CRM is chosen specifically to be consistent in mapping concepts across the ontologies of archaeology.
    * JN3 will be helpful for seeing existing connections between two datasets that have already been mapped.
- Explore existing DataARC connections involving relevant concepts by using JN3. This type of activity should lead to answers for the following questions.
    * Which datasets are connected to a given concept? 
    * Which concepts, datasets, and combinators are associated with a concept?
- Develop the combinators for the concepts that have been identified with your data. More information can be found in Developing a good combinator below.
- Identify the queries of the data that would be needed to satisfy support for a combinator. Consider the time frame, amount (including existence/non-existence), location, and indicators in the various datasets that support a combinator.
    * Test these queries using ???
    * Notebook for building the tests? Arkansas project using MongoDB. Neo4J in Annie’s project.
- Add your mapping to the desired dataset.
- Add your dataset to the concept map.
- Explore new data connections using the |DEE|.

