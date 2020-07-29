Add Your Own Combinator Tutorial
================================

In this tutorial, we'll work to edit the combinators CSV file in GitHub, then use the updated file to visualize your
new combinator in the DataArc Ecosystem Explorer (Explorer, for short) alongside the existing DataArc mappings.

**You will need to be signed into GitHub for this tutorial.**


Learning Objectives
-------------------

* Use the GitHub web interface to fork a repository.
* Learn where and how to add a combinator to the Explorer
* Visually check your combinator.


Fork the DataArc Repository
---------------------------

.. note::
    You may have already completed this step. If you have a fork, skip ahead to *Add your combintor to your Fork*

1. Navigate to |DataArc|.

2. Fork the repository. Click the :lime:`Fork` button at the top right of the screen

   |fork|

3. You may be prompted to choose a **location for the fork**. You will likely want to choose your favored personal account - work, school, other, etc. If you have only one space available to fork this repository, you may not see the prompt.
4. You will be **redirected** to a new GitHub repository URL in your user space.

    `https://github.com/[user name here]/experiments>`

You now have a fork of the `experiments` repository. This is your own sandbox. You can freely change it without causing
any harm to the main DataArc repository.

.. |DataArc| raw:: html

   <a href=https://github.com/ropitz/experiments target=_blank>the DataArc GitHub</a>

.. |fork| raw:: html

    <center>
    <img src="../_static/ForkButton.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>

.. |data_folder| raw:: html

    <center>
    <img src="../_static/DataFolder.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>

Add your combinator to your Fork
--------------------------------

These instructions will allow you to directly edit a comma-separated values (CSV) file from the GitHub browser window. **Advantages** of this method include in-place editing of the repository files, no need to download the full repository or upload edited files, no direct knowledge of git repositories required, and the combinator you add is saved and backed up on GitHub. The main **disadvantage** is editing a CSV file in it’s raw text format.

1. From the **data** folder page on your GitHub fork, click on `dataarc_combinators.csv`.
2. The file will open in your browser window.
3. Click the **edit button** at the top right corner of the file contents box.

   |edit|

4. Scroll to the bottom of the file
5. Add a new line with data filled in for each of the fields in the file separated by a comma. The fields are in order as follows:

    **ID** A random numeric identifier for your combinator. The actual number you choose does not matter. Duplicates are
    fine.

    **COMB** A short string naming your combinator.

    **User** Your name.

    **Data** The name of the data set.

    **Descrip** A sentence or two to describe how the data set relates to the concepts used in this combinator.

    **Cite** Any literature citations available as reference to this combination of data and concepts.

    **Query** This section may contain a query string for database querying purposes. It is not used for visualization
    purposes, so there is no need to include it here -- just add spaces between the commas.

    **Topics** A comma-separated list of topics. This **must** have a list of topics, separated by commas, and
    surrounded by double quotes.

6. Save your changes. Add a short description as a commit message and (optionally) write a short description of the
   modification you included to the boxes at the bottom of the screen.
7. Click **Commit changes** to save.

   |commit|

Your combinator is now saved in your fork!

.. |edit| raw:: html

    <center>
    <img src="../_static/EditButton.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>

.. |commit| raw:: html

    <center>
    <img src="../_static/CommitChangesButton.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>

Get the raw URL for the CSV file
--------------------------------

Once you have a combinator saved to your fork, you need to find the URL to teh raw CSV file.

1. Navigate to your GitHub fork in your browser.

2. From the **data** folder page on your GitHub fork, click on `dataarc_combinators.csv`.

3. Scroll down to the beginning of the file and click **Raw**.

4. A text-only version of the CSV file will appear in your browser. **Save the URL of this page for later use.** It
   should be something like this:

   ``raw.githubusercontent.com/...``

Visualize your combinator with the DataArc Ecosystem Explorer
-------------------------------------------------------------

1. **Open the Explorer.**

   Recall, that means you need to navigate to the |demo| and click on |launch| if you don't already
   have an active Binder session running.

2. Once the Binder session has started, click on the Jupyter Notebook `dataarc_pyvis.ipynb`.

   The Jupyter Notebook will open in a new window, ready to run!

3. Before running all cells, as prompted at the beginning of the Jupyter Notebook, scroll down to the :jngreen:`Load data
   from GitHub` section. We want the Notebook to point to your newly updated CSV file.

   Change the variable ``url`` in the code block to the URL you saved from the previous section
   (i.e., ``raw.githubusercontent.com/...``).

4. Now, run all the cells in the notebook, as instructed by the DataArc Ecosystem Explorer guidance.


For any of the visualizations in the Explorer, you should now see your combinator and (potentially) new dataset. This
process can be repeated many times for tweaking existing combinators, or adding additional combinators.

.. |demo| raw:: html

  <a href="https://github.com/aelydens/dataarc-demo" target=_blank> DataArc Demo GitHub Repository</a>

.. |launch| raw:: html

  <img src="../_static/launch_binder_button.png" width=120/>



