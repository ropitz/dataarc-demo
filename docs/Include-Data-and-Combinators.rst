Include your data and mappings
==============================

> Note: This procedure is meant to aid the incorporation of data into the set of Jupyter Notebooks that are supported for mapping ventures. The data included via this procedure will not be uploaded to the main DataARC catalog for dissemination on the AR platform.

To add a dataset to the visualization tool, **you will need to be signed into your GitHub account.**

Procedure
#########

1. Navigate to https://github.com/ropitz/experiments.

2. Fork the repository. Click the :lime:`Fork` button at the top right of the screen

   |fork|

3. You may be prompted to choose a **location for the fork**. You will likely want to choose your favored personal account - work, school, other, etc. If you have only one space available to fork this repository, you may not see the prompt.
4. You will be **redirected** to a new GitHub repository URL in your user space. 

    `https://github.com/[user name here]/experiments>`
 
5. Click on the **data folder**.

   |data_folder|

6. From here, you can choose to add your data set as a whole JSON file, or add mapping(s) to the existing `dataarc_combinators.csv`. Jump to the detailed instructions for these options by following these links:
    1. Upload a JSON file
    2. Add a mapping from the browser
    3. Add a mapping with your favorite CSV editor
    4. Add a mapping in the Jupyter Notebook

.. |fork| raw:: html

    <center>
    <img src="_static/ForkButton.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>

.. |data_folder| raw:: html

    <center>
    <img src="_static/DataFolder.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>


Upload a File
#############

1. Click on **Add file**, then :lime:`Upload files` in the drop down menu.

   |upload|

2. Use the upload interface to drag and drop, or browse your local files.
3. Once files have been chosen, write a commit message. The first small box should contain a short description like “Adding my narwhal data”, while the larger box may contain a more expansive description. 
4. Finish by clicking :violet:`Commit changes` 

   |commit|

Now your data is included in your fork!

.. |upload| raw:: html

    <center>
    <img src="_static/UploadFilesMenu.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>

.. |commit| raw:: html

    <center>
    <img src="_static/CommitChangesButton.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>



Add a mapping from the browser
#################################
These instructions will allow you to directly edit a comma-separated values (CSV) file from the GitHub browser window. **Advantages** of this method include in-place editing of the repository files, no need to download the full repository or upload edited files, no direct knowledge of git repositories required, and the combinator you add is saved and backed up on GitHub. The main **disadvantage** is editing a CSV file in it’s raw text format.

1. From the **data** folder page on your GitHub fork, click on `dataarc_combinators.csv`.
2. The file will open in your browser window.
3. Click the **edit button** at the top right corner of the file contents box.

   |edit|

4. Scroll to the bottom of the file
5. Add a new line with data filled in for each of the fields in the file separated by a comma. The fields are in order as follows:

    **ID** A random numeric identifier for your combinator. Actual number and duplicates do not matter.

    **COMB** A short string naming your combinator

    **User** Your name

    **Data** The name of the data set

    **Descrip** A sentence or two to describe how the data set relates to the concepts used in this combinator.

    **Cite** Any literature citations available as reference to this combination of data and concepts.

    **Query** This section may contain a query string for database querying purposes. It is not used for visualization purposes, so there is no need to include it here.

    **Topics** A comma-separated list of topics 

6. Save your changes. Add a short description as a commit message and (optionally) write a short description of the modification you included to the boxes at the bottom of the screen.
7. Click **Commit changes** to save.

   |commit|

Your combinator is now saved in your fork!

.. |edit| raw:: html

    <center>
    <img src="_static/EditButton.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>


Add a mapping with your favorite CSV editor
###########################################

These instructions will guide you through the process of editing a comma-separated values (CSV) file using your favorite CSV editor (Google Sheets, Microsoft Excel, Numbers, etc.). **Advantages** of this method include no requirements of git repository experience, using a spreadsheet to edit a CSV file, and the combinator you add will be saved and backed up on GitHub. The main **disadvantage** is the additional steps of downloading and uploading a CSV file through GitHub.

1. From the main page of your GitHub fork, click :violet:`Clone or download`.
2. Click :lime:`Download zip`.

   |download|

3. Once your download is complete, **unzip it**. Most computers do this for you when you double click a zipped file to open it.

4. Find the **experiments-master >> data >> dataarc_combinators.csv** file and open it with your favorite CSV editor (Google Sheets, Microsoft Excel, Numbers, or similar).
5. Add a new row(s) of data filled in for each of the columns in the spreadsheet. The columns include:

    **ID** A random numeric identifier for your combinator. Actual number and duplicates do not matter.

    **COMB** A short string naming your combinator

    **User** Your name

    **Data** The name of the data set

    **Descrip** A sentence or two to describe how the data set relates to the concepts used in this combinator.

    **Cite** Any literature citations available as reference to this combination of data and concepts.

    **Query** This section may contain a query string for database querying purposes. It is not used for visualization purposes, so there is no need to include it here.

    **Topics** A comma-separated list of topics 

6. Upload it to your fork following the steps in the Section `Upload a File`_.

.. |download| raw:: html

    <center>
    <img src="_static/CloneDownload.png" alt="drawing" width="250" style="border:5px solid black"/>
    </center>

