Project Title : Image Segmentation using Kmeans & DBSCAN Algorithm 

Project Description : 

The project includes segmenting color images using DBSCAN and kmeans. 

Kmeans : Kmeans find the color representatives for the number of classes given and create one cluster for it and include those points in that group.

DBSCAN : DBSCAN stands for density based clustering algorithm which includes grouping similar color points into different clusters based on how dense they are or how closely related
they are with each other.

FILES :

kmeans.py -> It includes code for all including  reading , saving and segmenting image by our kmean algorithm.

DBSCAN.py -> reads image , perform DBSCAN & output vector image.

main.py->reading image, converting it and calling dbscan algorithm.  


DEPENDENCIES :

All the packages/Libaries should be included in python 3.6.8 or above.


LIMITATIONS : 

For the DBSCAN algorithm you must first compressed the image into 100*100 pixels or else it will take longer to run.


How to install and run the project :

You must have python and opencv installed in your system.

Below Python packages are to be downloaded and installed to their default locations :

Python 3.x (3.4+) or Python 2.7.x from here.

Numpy package (for example, using pip install numpy command).

Matplotlib (pip install matplotlib) (Matplotlib is optional, but recommended since we use it a lot in our tutorials).

Install all packages into their default locations. Python will be installed to C:/Python27/ in case of Python 2.7.

After installation, open Python IDLE. Enter import numpy and make sure Numpy is working fine.

Download latest OpenCV release from GitHub or SourceForge site and double-click to extract it.

Goto opencv/build/python/2.7 folder.

Copy cv2.pyd to C:/Python27/lib/site-packages.

Open Python IDLE and type following codes in Python terminal.

>>> import cv2 as cv
>>> print( cv.__version__ )

1. Extract this code into a folder
2. Open this fodler into Spyder or anyother IDE such as Jupyter Notebook or Pycharm.
3. After opening the code succesfully run this code
 






   