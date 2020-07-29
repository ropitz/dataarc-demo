# dataarc-demo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aelydens/dataarc-demo/master)

# User Guide

Check out the detailed user information at [Read the Docs](https://dataarc-demo.readthedocs.io/en/latest/).

# Technical Notes

At the time of this project, the GML file that stored nodes and edges was not a valid GML file. It contained edges that pointed to nodes that were not in the file.

To address this, we've added a series of scripts to generate topic nodes and edges from a GML file.

**Note: You will only need to do the following if you are a project maintainer and the knowledge graph has changed, requiring you to add new topic nodes to the DataArc Explorer.**

## Topic Nodes (Knowledge Graph) Data Cleaning Steps

### Step 1

The dataarc_gml.gml file is the file that will be converted. If you have a new GML file to import, save that file in the project directory as dataarc_gml.gml.

Convert the GML file to JSON using the convert.py script by running the following in the command line:

```python
python scripts/convert.py scripts/dataarc_gml.gml > scripts/converted_gml.json
```

Check to make sure the resulting JSON in `scripts/converted_gml.json` is valid. Occasionally the regex won't properly account for certain labels or you'll see a trailing comma you'll need to delete before moving to step 2.

### Step 2

Generate node ids. This will be used to check which edges are valid in the provided GML file.

Once you've checked to make sure `scripts/converted_gml.json` contains valid JSON, run the following in the command line to generate the node ids:

```python
python scripts/generate_node_ids.py scripts/converted_gml.json > scripts/node_ids.json
```

### Step 3

Run the `cleanup.py` script, which will do some formatting of labels and generate the final JSON file we will use to power the knowledge graph display in the notebook.

This script requires a `converted_gml.json` file and a `node_ids.json` file. You generated these files in steps 1 and 2 above.

```python
python scripts/cleanup.py > scripts/topic_nodes.json
```

Double-check to make sure that the JSON in `scripts/topic_nodes.json` is valid before moving onto step 4.

### Step 4

Generate node mappings for labels. This script requires that `scripts/topic_nodes.json` has been updated, which you did in step 3.

```python
python scripts/generate_node_mapping.py > scripts/node-mapping.json
```

After following these four steps in order, you should now have topic nodes loaded in a format that works with the Data Explorer Jupyter notebook!


## Read the Docs

The documentation published on readthedocs.org is contained entirely in the `docs/` directory of this repository and is
built with Sphinx using restructured text files. Building the documentation locally requires a few Python packages that
can be installed in a conda environment using the included `environment.yml` file.


### Building locally

To install the environment "dataarc" environment on your local machine (assuming conda is already installed):

```
conda env create -f environment.yml
```

Active the environment and make the Sphinx documentation by navigating to the `docs/` directory and running these
commands:

```
conda activate dataarc
make html
```

You can then open the local `docs/_build/html/index.html` file in your browser to check your edits as they will appear
on the website.

### Publishing your documentation

- Commit any changes to the documentation to the repository, and push the commits to GitHub.
- Navigate to readthedocs.org and sign in. There you should find the a list of "My Projects".
- Click on the dataarc-demo project.
- Click "Build version" 
- Once the build is complete, click "View Docs"
