# apply-engraved-effect
apply image on another image with correct perspective and effect

Using the script:

from applyengraved import CreateImage<br><br>
Load the image on which we want to apply engravings:<br>
img="box.jpg"              <br>
the image to be aded on 'img':<br>
putonimage="cat.jpg"<br>
white image with quadrilateral black shape that shows perspective field where the engravings will be aplyed:<br>
mask="boxedges.png"      <br>
the real world ratio of the field in perspective:<br>
ratio=[2,3]                <br>
the same image as 'img' but photoshoped with needed effect:<br>
texture="boxengraved.jpg"   <br>
Might be same as 'edgesimgx', but can put more white areas where we want to avoid the angravings to be added. Can be any shapes. Only black areas of 'img' will be affected:<br>
flt="boxfilter.png"         <br><br>

# create engraved image<br>
CreateImage(img, putonimage, mask, ratio, texture, flt)
