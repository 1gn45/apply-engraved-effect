# apply-engraved-effect
apply image on another image with correct perspective and effect

Using the script:

from applyengraved import CreateImage

img="box.jpg"               # Load the image on which we want to apply engravings<br>
putonimage="result.jpg"     # the image to be aded on 'img'<br>
mask="boxedges.png"         # white image with quadrilateral black shape that shows perspective field where the engravings will be aplyed<br>
ratio=[2,3]                 # the real world ratio of the field in perspective<br>
texture="boxengraved.jpg"   # the same image as 'img' but photoshoped with needed effect<br>
flt="boxfilter.png"         # Might be same as 'edgesimgx', but can put more white areas where we want to avoid the angravings to be added. Can be any shapes. Only black areas of 'img' will be affected<br>
CreateImage(img, putonimage, mask, ratio, texture, flt)
