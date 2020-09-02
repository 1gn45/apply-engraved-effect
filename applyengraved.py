import cv2
import numpy as np


def bitwisejoin(img1, img2, mask):
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols ]
    img2gray = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    dst = cv2.add(img1_bg,img2_fg)
    return dst



def changeimageratio(ratiox, imgwidthx, imgheightx, imgx): #####example ratiox=[2, 1] means height=2 width=1
    givenratio=float(ratiox[1])/float(ratiox[0])
    imgratio=float(imgwidthx)/float(imgheightx)##########the higher the ratio the wider the image
    if givenratio>imgratio:
        imagenewheight=imgheightx
        imagenewwidth=int(imgheightx*givenratio)
    elif givenratio<imgratio:
        imagenewwidth=imgwidthx
        imagenewheight=int(imagenewwidth/givenratio)
    else:
        imagenewwidth=imgwidthx
        imagenewheight=imgheightx

    blank_image = np.zeros((imagenewheight, imagenewwidth,3), np.uint8)#new img with new ratio
    blank_image = blank_image+255
    resizedwidth=imgwidthx
    resizedheight=imgheightx
    if givenratio>imgratio:
        whitesides=int((imagenewwidth-resizedwidth)/2)
        blank_image[0:imagenewheight, whitesides:whitesides+resizedwidth]=imgx
        resized_image=blank_image
    elif givenratio<imgratio:
        whiteupsides=int((imagenewheight-resizedheight)/2)
        blank_image[whiteupsides:whiteupsides+resizedheight, 0:imagenewwidth]=imgx
        resized_image=blank_image
    else:
        resized_image = imgx
    return resized_image


#Let's put the effect on photo according to mask
def addengraved(img, texture, mask): #img - the image, on wich we are aplying texture. Mask- the image to be engraved on 'img'
    mask=cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY)
    mask=cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    maskinv=255-mask
    maskinvnp=np.array(maskinv, dtype=np.uint16)
    masknp=np.array(mask, dtype=np.uint16)

    texturenp=np.array(texture, dtype=np.uint16)
    imgnp=np.array(img, dtype=np.uint16)

    maskedtexture=texturenp*maskinvnp/255
    maskedimg=imgnp*masknp/255

    finished=maskedtexture+maskedimg
    return finished


def get4edgesinimage(image):   ######Function used to take 4 edges cordinates from given image with quadrilateral black shape that shows perspective
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 10)

    ############## Getting the corners
    listx=np.ndarray.tolist(corners)  #### turning coordinates in pythonic list
    listnormal=[listx[0][0],listx[1][0],listx[2][0],listx[3][0]]
    listnormal.sort(key=lambda x: x[1])

    ############## Geting corners in list: 0=upper left, 1=upper right 2=lower left 3=lower right
    upperedges=listnormal[0:2]
    loweredges=listnormal[2:]
    upperedges.sort(key=lambda x: x[0])
    loweredges.sort(key=lambda x: x[0])
    li=upperedges+loweredges
    height, width, channels = image.shape
    return li, height, width



def CreateImage(mainimage, putonimagex, edgesimgx, putonratio, texture, filter1):
        # mainimage- the image on which we want to apply engravings
        # putonimagex - the image to be aded on mainimage
        # edgesimgx - white image with quadrilateral black shape that shows perspective field where the engravings will be aplyed
        # putonratio - the real world ratio of the field in perspective
        # texture - the same image as 'mainimage' but photoshoped with needed effect
        # filter1 - Might be same as 'edgesimgx', but can put more white areas where we want to avoid the angravings to be aded
    filter1=cv2.imread(filter1)
    img=cv2.imread(mainimage)
    texture=cv2.imread(texture)
    points4, height, width = get4edgesinimage(cv2.imread(edgesimgx))
    putonimage=cv2.imread(putonimagex)
    height1, width1, channels = putonimage.shape
    putonimage=changeimageratio(putonratio, width1, height1, putonimage)
    height1, width1, channels = putonimage.shape

    # Lets put the image on required perspective
    pts1 = np.float32([[0, 0], [width1, 0], [0, height1], [width1, height1]])
    pts2 = np.float32([points4[0], points4[1], points4[2], points4[3]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(putonimage, matrix, (width, height))     #######result=image aplied on perspective
    result=cv2.add(result, filter1)
    finished=addengraved(img, texture, result)
    cv2.imwrite("result.jpg", finished)
