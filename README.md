# GUGC Bachelor Project:
<h2> "EXPLORING WEB-BASED MACHINE LEARNING FOR ROTATOR CUFF TEAR DIAGNOSIS IN MAGNETIC RESONANCE IMAGES" </h2>
<img src='img/Logo_Biotech.png' width=300px, height=194px>
<h3> 
  <b> Student: </b> Ju Hyung Lee <br/>
  <b> Supervisor: </b> Prof. Dr. Wesley De Neve <br/>
  <b> Counsellors: </b> Mijung Kim, Homin Park <br/>
</h3>

<h2> Project Description </h2>
<p>
  <b> This project has two main goals: <b>
</p>
<p> 1. Implement Machine Learning to train a model to classify Rotator Cuff Disease from MRI images </p>
<p> 2. Visualize the model above by builing a Graphical User Interface (GUI)</p>

<h2> Pipeline of Machine Learning </h2>
  <img src='img/Pipeline_ML.png'>
  <p>
    ML implementation starts with Data Collection, followed by preprocessing of data including augmentation and normalization of given data. After preprocessing, feature extraction is done with Principal Component Analysis (PCA) to reduce the number of variables. The dataset then is used to train classification models – AdaBoost and KNN – and their performance after training will be evaluated.
  </p>

<h2> Disease: Rotator Cuff Disease </h2>

<style src='css'>
<img src='img/RCT_schematic.png'>
<img src='img/RCT_MRI.jpg'>
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
<pre>
<p> 1. Flip (vertical, horizontal) </p>
<p> 2. Gaussian Noise </p>
<p> 3. Contrast </p> 
<p> 4. Scaling </p> 
<p> 5. Gamma Correction </p>
<p> 6. Gaussian Blur </p> 
<p> 7. Rotation </p>
<p> 8. Shearing </p>
</pre>

 
  



