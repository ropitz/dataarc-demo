The main components of the DataArc Ecosystem
============================================

The DataArc Ecosystem links together data and key concepts related to human environment dynamics and landscape change in
the North Atlantic. To learn to explore how it connects data and concepts together using the knowledge of a diverse
group of domain experts representing subjects from paleoecology through to saga studies, start by understanding the
different parts of the ecosystem. The key components are: 

- A shared community concept map
- Datasets contributed by the community
- "Combinators" which connect data from those datasets to the shared community concept (aka knowledge) map and provide
  expert explanations of the connections.
- Scope notes which describe the concepts in the concept map from the perspectives of different disciplinary experts 

Concept Map Overview
=====================

- A concept or knowledge map describes how various concepts relate to one another to describe a broader concept or a
  knowledge domain.
  * Become familiar with the concepts in the DataArc community's concept map for "changing landscapes" by reading about
    individual concepts, viewing their mappings to the CIDOC CRM, and viewing their connections to one another on the
    concept map.
  * A full set of DataArc concepts with descriptions is available |concepts|. The descriptions of DataArc concepts are
    written in the form of scope notes. A scope note describes how the community intends a term to be understood.
  * The CIDOC CRM is a set of high-level concepts used widely in archaeology and heritage to describe key ideas
    (concepts) in these broad domains. Concepts that link datasets in DataArc are mapped to the CIDOC CRM v 6.0+.
    - When we say that one concept is mapped to another we mean that we have declared a formal relationship between
      these concepts. DataArc concepts can be thought of as specific instances of concepts in the CIDOC CRM. For
      example, "hunting" is a DataArc concept that is mapped to "activities" in the CIDOC CRM because it is a specific
      instance, an example, of a kind of activity that is important for understanding human-environment dynamics and
      landscape change.
    - For an exploratory examination of the CIDOC CRM concepts, visit the |use_and_learn|.
  * DataArc concepts are related to one another and these relationships can be visualized as a graph.
    - There are two main types of relationships between concepts: class-instances and cross-references - Class instances
      are essentially sub-type relationships. For example, a "beached whale" is a sub-type of "whale" and these two
      concepts have a _class-instance_ relationship.
    - Cross-references relate concepts that are regularly understood as meaningfully associated with one another. An
      example of this might be that a "human" actor participates in the activity of "fishing" where "human" and
      "fishing" are the concepts and they are associated by a "participates in" type of cross-referencing relationship.
    - You can visualize the class instance relationships in the diagram below.
      - Use zoom, click and drag, and scroll features when exploring the graphic.
      - Darker blue represents more general concepts, while more granularity is represented by lighter shades (and
        deeper down the graph).
    - You can read through the cross-reference relationships |concept_map|.
  * Note for data contributors: When you think about connecting your own data to this system, the list of concepts
    should be thought about as static.  In other words, try to find concepts that can be linked to your data from those
    that already exist in the concept map If you have a very specific concept in mind, try to identify a more general
    concept under which it might fit. It took a long time to get the whole community to agree to the shared set of
    concepts and extended negotiations are involved in proposing and approving new ones.

.. raw:: html

   <div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0"
   style="width:640px; height:480px"
   src="https://app.lucidchart.com/documents/embeddedchart/8186e587-133d-47f2-88a6-1040368100d7"
   id="GKofz3JhU3pp"></iframe></div>

Datasets Overview
=================

- The full list of current datasets which researchers have contributed to DataArc is included in the |DEE|
- A short summary of these datasets can be found at the |about_dataarc|.
- Full dataset biographies, which provide background information, are included in the data repository under
  the data_descriptions subdirectory.
- You can use the DataArc Ecosystem Explorer, a Jupyter Notebook hosted by Binder, to more fully understand existing
  connections within DataArc between datasets and concepts and between different datasets which are connected via
  concepts.


Exploring the existing Knowledge Map
====================================

1. Navigate to |DEE|.
2. Click the Launch Binder button. This process may take a couple of minutes to start up. Be patient!
3. Once the Jupyter Binder loads, click on the `dataarc_pyvis.ipynb` file to open it.
4. Follow directions in the notebook to explore how datasets and concepts connect in DataArc. These connections are what
   structure the search results you get when you search by concept in the publicly accessible DataArc Search Tool on the
   |web_dataarc|.

.. |DEE| raw:: html

    <a href=https://github.com/aelydens/dataarc-demo target=_blank>DataArc Ecosystem Explorer &#8663;</a>

.. |about_dataarc| raw:: html

    <a href=https://beta.data-arc.org/about target=_blank> DataArc website &#8663;</a>

.. |web_dataarc| raw:: html

    <a href=https://beta.data-arc.org/ target=_blank> DataArc website &#8663;</a>

.. |use_and_learn| raw:: html

    <a href=http://www.cidoc-crm.org/use_and_learn target=_blank>CIDOC Use & Learn Page &#8663;</a>

.. |concepts| raw:: html

    <a href=https://github.com/ropitz/experiments/tree/master/docs/dataarc-concepts target=_blank>on GitHub &#8663;</a>

.. |concept_map| raw:: html

    <a href= https://ropitz.github.io/experiments/concept_map/dataarc-conceptmap.html target=_blank>here &#8663;</a>

Mapping your connections
========================

Below is a set of suggestions to get you started with adding mappings from your dataset to the DataArc community concept
map. Any of the steps in the process described here can be visited multiple times as you develop your mappings, and
there is no requirement to go in any specific order. We suggest you come back to this list often to help re-center
yourself as you work.

- Identify the key datasets and data elements for your mapping task.
    * See Choosing which data to add later in this document for more guidelines to consider.
      - The main dataset you’ll be creating mappings for will probably be your own dataset. Alternatively, you may be
        proposing new mappings for an existing dataset contributed by someone else.
      - You may also wish to focus on another dataset with which you want your own dataset to share concepts in order to
        build connections between them.
      - Within the dataset which you are mapping to the concept map, you need to choose which fields (data elements) or
        combinations of fields to use in your mappings.
          - When you are mapping your dataset, you don’t have to create explicit mappings for every field in your
            dataset, nor do you have to create mappings which provide matches for every row. See `Choosing which data to
            map` later in this document for more guidelines to consider.
          - For example, if you are mapping your zooarchaeological data to the concept map, you might create a mapping
            that uses the fields in a table which hold data on the age at death and the likely sex of each specimen to
            return a search result for older female sheep and you might connect this to the concept ‘animal husbandry’.
            That search will also return the ‘other notes’ field from the matching rows in that same table. You might
            never make a mapping that uses the ‘other notes’ field. That data is still included in the system and
            accessible when a user is looking at your dataset but is not involved in constructing search results.   
- Understand the concepts represented by the concept map.
    * The DataArc Team have developed a domain-specific ontology, a formal description of the concepts used to
      describe a specific knowledge domain and how these concepts relate to one another, to describe the domain of human
      ecodynamics as it is understood in this research community, whose work is focused on the North Atlantic. This
      domain-specific ontology is centered around the concept "changing landscapes". It is built on a set of concepts and
      connections between concepts which has been extensively discussed and agreed by the DataArc research community.
      This concept map connects contributed datasets and provides a formal structure to describe those connections
        - Each concept might be understood in different ways by different members of the community because of their
          specific disciplinary backgrounds. We've attempted to capture some of the complexity of what we mean by each
          concept in the scope notes, available |concepts|.
        - Recall that you can read about the cross-reference relationships between concepts |concept_map|.
    * Concepts used by DataArc are all mapped to CIDOC CRM concepts. The purpose of these mappings is to provide
      compatibility with other datasets in archaeolology and heritage domains which are also mapping to the CIDOC CRM,
      and to provide additional description of how these concepts are understood by the DataArc community. For an
      exploratory examination of the CIDOC CRM, visit |use_and_learn|.
        - Note that some of the concepts may be associated with more than one CIDOC CRM concept, e.g., a whale may be both
          an actor and a biological entity.
- Think of making each mapping as asking: How would I use my dataset to respond to a question about `x`, which is related
  to the concepts of `y`? 
    * An example of this might be: How would I use my dataset of artifacts made of whale bone to respond to a question
      about changing whale hunting patterns, which is related to concepts of ocean conditions, climate, and sea
      temperature? 
- Collect concepts from literature associated with the mapping you are creating.
    * How do you decide which concepts to map your data onto? We recommend you start by considering the keywords you
      find in the literature that is related to the question you are addressing with your mapping. Then search the
      DataArc concept map for these keywords or terms closely related to them.
        - You may find it is useful to explore by starting with relatively broad concepts within the concept map, and to
          then look for narrower, more specific terms.
- Explore existing DataArc connections involving relevant concepts by using the |DEE|. This should lead
  to answers for the following questions.
    * Which datasets are connected to a given concept? 
    * Which concepts, datasets, and combinators (aka mappings) are associated with a concept?
- Describe and provide bibliography for the combinator mapping you are creating to associate your data elements with
  concepts from the community concept map. More information on descriptions and bibliography can be found in Developing
  a good combinator below.
- Identify the queries of the data that would be needed to satisfy support for a combinator. Consider the time frame, amount (including existence/non-existence), location, and indicators in the various datasets that support a combinator.
- Add your mapping to the desired dataset.
- Add your dataset to the concept map.
- Explore new data connections using the |DEE|.

