Concept Map Overview
=====================

- Dataset overview
    * The full list of current datasets is included in |DEE|.
    * A short summary of the datasets can be found at the |about_dataarc|.
    * Full dataset biographies are included in the data repository under the `data_descriptions` subdirectory.
    * Use the DataArc Ecosystem Explorer, a Jupyter Notebook hosted by Binder, to more fully understand existing connections within DataARC.

- Concepts overview
    * Become familiar with concepts.
    * Concepts that link datasets in DataArc are mapped to the CIDOC CRM v 6.0+. For an exploratory examination of these concepts, visit
      the |use_and_learn|.
    * A full set of DataARC concepts with descriptions is available |concepts|. The diagram below may also be helpful
      for exploring heirarchical relationships between DataArch concepts. 
        - Use zoom, click and drag, and scroll features when exploring the grahic.
        - Darker blue represents mroe general concepts, while more granularity is represented by lighter shades (and
          deeper down the graph).
    * The list of concepts should be treated as static. Try to find concepts that can be linked to your data from those that already exist.

.. raw:: html

   <div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://app.lucidchart.com/documents/embeddedchart/8186e587-133d-47f2-88a6-1040368100d7" id="GKofz3JhU3pp"></iframe></div>




Exploring the existing Knowledge Map
==================================== 
1. Navigate to |DEE|.
2. Click the Launch Binder button. This process may take a couple of minutes to start up.
3. Once the Jupyter Binder loads, click on the `dataarc_pyvis.ipynb` file to open it.
4. Follow directions in the notebook.

.. |DEE| raw:: html

    <a href=https://github.com/aelydens/dataarc-demo target=_blank>DataArc Ecosystem Explorer &#8663;</a>

.. |about_dataarc| raw:: html

    <a href=https://beta.data-arc.org/about target=_blank> DataArc website &#8663;</a>

.. |use_and_learn| raw:: html

    <a href=http://www.cidoc-crm.org/use_and_learn target=_blank>CIDOC Use & Learn Page &#8663;</a>

.. |concepts| raw:: html

    <a href=https://github.com/ropitz/experiments/tree/master/docs/dataarc-concepts target=_blank>on GitHub &#8663;</a>

Mapping your connections
========================

Below is a list of suggestions to get you started with adding mappings of your dataset to the knowledge map built within DataARC. Any of these items can be visited multiple times in the process, and there is no requirement to go in any specific order. We suggest you come back to this list often to help recenter and reclaim scope.

- Identify the key dataset for mapping in DataARC.
    * See Choosing which data to add later in this document for more guidelines to consider.
- Understand the concepts represented by the knowledge graph.
    * Concepts used by DataArc are all mapped to CIDOC CRM concepts. For an exploratory examination of those concepts, visit
      |use_and_learn|
    * The DataArc Team have developed a domain-specific ontology using common concepts that will serve to connect many
      of the contributed datasets. 
    * Note that some of the concepts may be associated with more than one CIDOC CRM concept, e.g., a whale may be both
      an actor and a biological entity.
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

