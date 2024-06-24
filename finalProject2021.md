---
The pass the course
---

To pass the course:

1. Prepare the project  
2. Pass the exame (you will be asked details concerning your project)


# I. Project

1. The project is an individual task.
2. Tasks included in the project are performed using own functions (for image downloading, preparing for final processing, stretching,  displaying, K-means, etc.). 
3. The functions are stored in modules (`.py` files).
4. Scripts/notebooks import functions from modules.


## 1. Scope of the project

>### 1.1. Script 1: downloading Sentinel-2 images   
>### 1.2. Script 2: conversion of formats - SAFE to TIFF


## 2. Script 1: downloading Sentinel-2 images

Based on laboratories write a script which:

  - read a list of available Sentinel-2 images from the `Copernicus Open Access Hub`   
  - downloads from the `Copernicus Open Access Hub` the indicated image
  
### Script characteristics

1. Launched from the command line of the text console
2. Takes command line arguments:

    - switch: download image or download information about available images   
   - place names identifying the area of interest
   - `UUID` of the image
   - directory address for saving the downloaded image or image information file
   - image date range
   - cloudness

## 3. Script 2: SAFE to TIFF

Based on laboratories write a script which:

 - unpacking the `.zip` archive
 - resampling of selected channels to 10m spatial resolution
 - clip bands limited to the area of interest
 - saving the clipped channels as a new multi-channel raster in `GeoTIFF` format
 
 
### Script characteristics

1. Launched from the command line of the text console
2. Takes command line arguments:

    - path to the downloaded Sentinel-2 image (`.zip`)   
    - path to the directory where the new raster will be saved   
    - name of the new raster


## Notebook: create code creating a land cover map basing on K-means 


---

