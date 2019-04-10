# GUGC Bachelor Project:
<h2> “deep learning for disease symptom  segmentation in medical images” </h2>
<h3> 
  <b> Student: </b> Ju Hyung Lee <br/>
  <b> Promoter: </b> Ph.D. Mijung Kim <br/>
  <b> Supervisor: </b> Prof. Wesley De Neve <br/>
</h3>

<h2> Project Description </h2>
<p>
  This project has two main goals:
</p>
<p> 1. Exploit deep learning to localize certain diseases by taking in MRI images </p>
<p> 2. Visualize the concept above by builing an web-based GUI </p>

<p> [Schematic Image Here] </p>

<h2> Disease: Supraspinatus tendons Tearing </h2>

<p> [Schematic Image of Supraspinatus tendons MRI] </p>
<p> 
  Particularily, I will be examining MRI images of human shoulder. Moreover, from the MRI image, I will only 
  observe the Supraspinatus tendons region. It is one of the group of shoulder muscles/tendons - altogether
  referrring to "Rotator Cuff" - that act to stabilize the shoulder. If the patient suffers from supraspinatus 
  tendons tearing, a white spot will appear in the MRI image.
</p>

<h2> Deep Learning Implementation </h2>

<h3> Samples information </h3>
<p> MRI images were obtained from archive in a hospital: 2643 patients, 16 MRI images of shoulder per patient. </p>

<h3> Image augmentation </h3>
<p> In order to increase sample size, different modifications were done to image: </p>
<p> 
  <pre> 1. Flip (vertical, horizontal) <br />
  <pre> 2. Gaussian Noise
<p>

 
  



