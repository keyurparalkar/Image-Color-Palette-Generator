import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
from PIL import Image
import base64

def img_to_base64(img_local):
    """
    Function to convert an image read in bytes to base64 format

    Parameters:
    img_bytes = Pillow Image object

    Return:
    base64 encoded image
    """

    img_bytes = img_local.getvalue()
    img_obj64_bytes = base64.b64encode(img_bytes)
    img_obj64_decoded = img_obj64_bytes.decode('ascii')

    return img_obj64_decoded

def RGB2HEX(color: list):
    """
    Converts RGB to HEX values

    Parameters:
    color= List of RGB values

    Returns:
    HEX string values based on RGB values
    """
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def hex_colors(img_obj:Image, n_colors:int):
    """
    Function to return n_colors # of hex values for the given image at img_path
    
    Parameters:
    img_path = Image path
    n_colors = No. of colors to identify

    Returns:
    n_colors # of hex values
    """
    img = Image.open(img_obj)
    img = img.resize((600,400))
    # print(f'IMAGE DATA === {img_obj.__dict__}')
    img_data = np.array(img)
    #   print(f"IMAGE - SHAPE = {img_data.shape}")
    img_data = img_data.reshape(img_data.shape[0]*img_data.shape[1], -1)

    print('Calculating Hex Values....')

    #define KMeans algo with cluster size:
    km = KMeans(n_clusters=n_colors, random_state=0)

    #Get labels for each sample:
    labels = km.fit_predict(img_data)
    counts = Counter(labels)

    #cluster centers:
    center_colors = km.cluster_centers_
    
    print(f'colors = {center_colors}, counts = {counts}')
    hex_vals = [RGB2HEX(center_colors[i]) for i in counts.keys()]
    print('Calculation Complete....')
    
    return hex_vals

