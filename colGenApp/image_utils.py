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