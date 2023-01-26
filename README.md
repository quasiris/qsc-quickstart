# Quickstart Guide Quasiris Search Cloud

## How to use

You have two options to run this example.

### Run locally
This example is written as a Jupyter Notebook. The easiest way to use it locally is to install Jupyter Lab.<br>
- Clone the repository.
- Make sure you have python and pip installed
- Install [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
- Open a terminal and execute "jupyter lab". Your browser should open with jupyter lab. If not open your browser and visit http://localhost:8888
- Use the file browser on the left and navigate to the cloned repository and open "qsc-quickstart.ipynb".
- Use the double arrow (see picture below) to run the notebook and follow the [instructions](qsc-quickstart.ipynb).
![Run Notebook](resources/pictures/qsc_run_notebook.png)

### Run at Google Colab (Recommended)
- Visit this project on [Google Colab](https://colab.research.google.com/github/quasiris/qsc-quickstart/blob/main/qsc-quickstart.ipynb)
- Sign in with your google account.
- Click "Runtime"->"Run All" and follow the [instructions](qsc-quickstart.ipynb).

## (Optional) Additional information

### Connect to Google Drive
If you want to use other data you can upload your files to google drive in order to access them inside Google Colab.

- First click the "Mount Drive" Button as shown in the picture above.
- This will insert a new cell as shown in the picture below. Use the up arrow marked with the orange box to move the cell at the very top.
![](resources/pictures/google_colab_gdrive_cell.png)
- Excecute the cell by clicking the run button marked with the green box and permit access to your Google Drive.
![](resources/pictures/google_colab_permit_access.png)
  - Select your account<br>
  ![](resources/pictures/google_colab_permit_access_1.png)
  - Allow access<br>
  ![](resources/pictures/google_colab_permit_access_2.png)
- If everything worked you should see a message under the cell that your Google Drive is mounted.
- After pressing the refresh button (orange box) you should be able to access your files.
![](resources/pictures/google_colab_mount_success.png)

### Access file
- Make sure the file is uploaded to your Google Drive.
- By hovering over a file in the file browser you get three dots right beside the filename. You can copy the path by
clicking on them and then select "Copy path"

# Convert Google shopping feed to QSC
**This project is still under development. Therefore some features might be missing.**</br></br>
Using [this guide](google_shopping_feed_to_qsc.ipynb) you can convert a given Google shopping feed to the QSC format.

## Run on Google Colab
Visit this project on [Google Colab](https://colab.research.google.com/github/quasiris/qsc-quickstart/blob/main/google_shopping_feed_to_qsc.ipynb)