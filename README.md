
# DarkVision: Detecting Weapons in low light

### Abstract

Currently, weapon detection through video surveillance has been extensively studied using deep learning techniques by researchers. However, limited attention has been given to the detection of weapons in night time or dark scenarios. This paper aims to address this gap by proposing a novel approach for weapon detection specifically modified for low-light conditions. The authors demonstrate accurate and robust detection of weapons in challenging nighttime environments by modifying the deep learning model YOLOv7. The YOLOv7-DarkVision model has been developed by combining a brightening algorithm with the advanced image  processing techniques and architecture of YOLOv7. A dataset of 15,367 images were collected for training of the model, along with five dark videos from various sources for performance evaluation. The derived detection model, which has a precision score of 95.50% and an F1-Score of 93.41%, performs absolutely well as a weapon detector.



Here is the doi to access the paper: https://doi.org/10.1016/j.dsp.2023.104342 


The codes have undergone verification through Code Ocean and are accessible at: https://doi.org/10.24433/CO.2176072.v1

![](https://github.com/PavinderYadav0/DarkVision/blob/main/figures/In_a_disturbing_trend,_V2.mp4)


## Installation

Install the dependend libraries using

```
pip install -r requirements.txt
```


## Architecture - Yolov7-DarkVision

![](https://github.com/PavinderYadav0/DarkVision/blob/main/figures/architecture.png)


## Deployment

For model testing, start by acquiring the validation data from [here](https://drive.google.com/file/d/1SfC_b2F9CIqFXxh23doKV_RkJGHjCwV5/view?usp=sharing). After downloading, unzip the file named ``val.zip`` into the ``data`` folder within the project repository. This action is essential to prepare the data for subsequent model evaluation.

Download the [last.pt](https://drive.google.com/file/d/1LknsYGbqUUGKUUP5KIeP05SpWVsVV0A3/view?usp=sharing) and [best.pt](https://drive.google.com/file/d/1sj6F6xwl0Q9FK-Nsxwzq0QnlgXzVsddI/view?usp=sharing) files and subsequently relocate them to the ``results\train\yolov7-handgun\weights`` folder within the project directory.


The initial command using ``test.py`` runs the model for testing purposes.

To test the model run the following command.

```bash
python test.py  --batch-size 8 --device 0 --data data\handgun.yaml --weights results\train\yolov7-handgun\weights\last.pt --conf 0.50
```
Results will be saved in `runs\test\exp*`  folder.

OR

The viability of the results can be examined on the CodeOcean platform via the following link: https://doi.org/10.24433/CO.2176072.v1. Access the "Reproducible Run" by clicking on the provided link

 ## Inference

### Detect –

Download the [best.pt](https://drive.google.com/file/d/1sj6F6xwl0Q9FK-Nsxwzq0QnlgXzVsddI/view?usp=sharing) files and subsequently relocate them to the ``results\train\yolov7-handgun\weights`` folder within the project directory.

To conduct model testing on both dark and bright videos, begin by downloading the video files from the following sources: [Dark Video](https://drive.google.com/file/d/1GM9FXvSJRAWtWAUw4Uj1IkFMIJLf58Qg/view?usp=sharing) and [Bright Video](https://drive.google.com/file/d/1GQcBSce8SbWcYlPWXPAvz2B6jL8xyf8u/view?usp=sharing). Subsequently, store these downloaded files within the designated 'data' folder for seamless access during the testing phase.


**Dark Videos** 

#### 1.	**Automatic**  -
Automatic Detection: Utilizes ``detect_auto.py`` to perform automatic handgun detection on a dark video. This command uses a specific set of weights, sets the confidence threshold, defines the image size, video source, and enables the view of images during detection. The resulting detections are saved in a designated folder.

On videos -
```
python detect_auto.py --weights  results\train\yolov7-handgun\weights\best.pt --conf 0.50 --img-size 640 --source data\dark.mp4 --view-img
```

On images -
```
python detect_auto.py --weights  results\train\yolov7-handgun\weights\best.pt --conf 0.50 --img-size 640 --source data\images --view-img
```

Replace the argument ``--source data\dark.mp4`` with ``--source video_path`` to conduct detections on your custom videos or images.

Results will be saved in `runs\detect\exp*`  folder.



#### 2.	**Manual**
Executes the ``detect_get.py`` script to manually adjust contrast, brightness, and gamma values for the purpose of detecting handguns in a dark video.

```
python detect_get.py --weights  results\train\yolov7-handgun\weights\best.pt --conf 0.50 --img-size 640 --source data\dark.mp4 --view-img
```

Replace the argument ``--source data\dark.mp4`` with ``--source video_path`` to conduct detections on your custom videos.

Results will be saved in `runs\detect\exp*`  folder.


**Bright Videos**

To execute the detections on a bright or daylight video, use the following command.

```
python detect.py --weights  results\train\yolov7-handgun\weights\best.pt --conf 0.50 --img-size 640 --source data\bright.mp4 --view-img

```

Replace the argument ``--source data\bright.mp4`` with ``--source video_path`` to conduct detections on your custom videos.

Results will be saved in `runs\detect\exp*`  folder.

### Gamma Test
 
 To test the brighning algoritham on images run the command

```
python Gamma_test.py data\dark.jpg
```
Replace the argument ``data\dark.jpg``  with ``Path\to\image`` to conduct detections on your custom image.

Results will be saved in `result` folder.
## Demo


![](https://github.com/PavinderYadav0/DarkVision/blob/main/figures/demo.gif)


This GIF showcases a side-by-side comparison between a dark input video and an enhanced bright video with real-time handgun detection. On the left-hand side, the original dark video demonstrates challenging low-light conditions, while the right-hand side displays the same video after enhancement, exhibiting improved brightness and clarity. 
- The video dataset has been sourced from the scholarly work of [Grega et al. (2015)](https://www.mdpi.com/1424-8220/16/1/47)
## Working Pipeline

![](https://github.com/PavinderYadav0/DarkVision/blob/main/figures/PIPELINE.png)

In scenarios featuring dark input frames, the YOLOv7-DarkVision model assumes responsibility for the detection process. This specialized model is meticulously crafted to manage dark frames and low-light conditions adeptly. Its initial step involves augmenting the dark input frame utilizing sophisticated image processing techniques, thereby significantly enhancing image visibility and quality. Following the application of this enhancement, the YOLOv7-DarkVision model conducts precise detection by identifying handguns within the improved dark frame.
## Authors

- [**Pavinder Yadav**](https://github.com/PavinderYadav0) 
 
 ```
 Department of Mathematics and Scientific Computing 
 National Institute of Technology, Hamirpur, Himachal Pradesh
 ```
 [Google Scholar](https://scholar.google.com/citations?hl=en&authuser=1&user=p6ZeLMkAAAAJ) , [ResearchGate](https://www.researchgate.net/profile/Pavinder-Yadav) , [Orcid](https://orcid.org/0000-0001-8682-0234)
 

If you intend to utilize the code or findings from this study, we kindly request proper citation as follows:

```
@article{YADAV2024104342,
title = {Robust weapon detection in dark environments using Yolov7-DarkVision},
journal = {Digital Signal Processing},
volume = {145},
pages = {104342},
year = {2024},
issn = {1051-2004},
doi = {https://doi.org/10.1016/j.dsp.2023.104342},
url = {https://www.sciencedirect.com/science/article/pii/S1051200423004372},
author = {Pavinder Yadav and Nidhi Gupta and Pawan Kumar Sharma}
}
```
Cite the code by CodeOcean at : https://doi.org/10.24433/CO.2176072.v1
## Acknowledgements

 - [Official yolov7](https://github.com/WongKinYiu/yolov7)
  - The video dataset has been sourced from the scholarly work of [Grega et al. (2015)](https://www.mdpi.com/1424-8220/16/1/47)

