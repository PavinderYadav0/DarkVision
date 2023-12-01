
# DarkVision: Detecting Weapons in low light

### Abstract

Currently, weapon detection through video surveillance has been extensively studied using deep learning techniques by researchers. However, limited attention has been given to the detection of weapons in night time or dark scenarios. This paper aims to address this gap by proposing a novel approach for weapon detection specifically modified for low-light conditions. The authors demonstrate accurate and robust detection of weapons in challenging nighttime environments by modifying the deep learning model YOLOv7. The YOLOv7-DarkVision model has been developed by combining a brightening algorithm with the advanced image  processing techniques and architecture of YOLOv7. A dataset of 15,367 images were collected for training of the model, along with five dark videos from various sources for performance evaluation. The derived detection model, which has a precision score of 95.50% and an F1-Score of 93.41%, performs absolutely well as a weapon detector.


## Installation

Install the dependend libraries using

```
pip install -r requirements.txt
```

Requirments

``` 
# Base ----------------------------------------
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.1
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch>=1.7.0,!=1.12.0
torchvision>=0.8.1,!=0.13.0
tqdm>=4.41.0
protobuf<4.21.3

# Logging -------------------------------------
tensorboard>=2.4.1
# wandb

# Plotting ------------------------------------
pandas>=1.1.4
seaborn>=0.11.0

# Export --------------------------------------
# coremltools>=4.1  # CoreML export
# onnx>=1.9.0  # ONNX export
# onnx-simplifier>=0.3.6  # ONNX simplifier
# scikit-learn==0.19.2  # CoreML quantization
# tensorflow>=2.4.1  # TFLite export
# tensorflowjs>=3.9.0  # TF.js export
# openvino-dev  # OpenVINO export

# Extras --------------------------------------
ipython  # interactive notebook
psutil  # system utilization
thop  # FLOPs computation
# albumentations>=1.0.3
# pycocotools>=2.0  # COCO mAP
# roboflow
```



## Architecture - Yolov7-DarkVision

![App Screenshot ](https://i.ibb.co/4sTRsXv/1.png>)
## Deployment

The initial command using ``test.py`` runs the model for testing purposes. 

To test the model run the following command.

```bash
python test.py  --batch-size 8 --device 0 --data data\handgun.yaml --weights results\train\yolov7-handgun\weights\last.pt --conf 0.50 --project results
```
Results will be saved in `runs\test\exp*`  folder.

 ## Inference

Detect –


Dark Video 


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


![](https://github.com/PavinderYadav0/DarkVision/blob/main/ezgif.com-gif-to-mp4.gif)


This GIF showcases a side-by-side comparison between a dark input video and an enhanced bright video with real-time handgun detection. On the left-hand side, the original dark video demonstrates challenging low-light conditions, while the right-hand side displays the same video after enhancement, exhibiting improved brightness and clarity. 
- The video dataset has been sourced from the scholarly work of [Grega et al. (2015)](https://www.mdpi.com/1424-8220/16/1/47)
## Working Pipeline

![App Screenshot](https://i.ibb.co/nnrSRJ3/Screenshot-2023-11-23-170114.png)

In scenarios featuring dark input frames, the YOLOv7-DarkVision model assumes responsibility for the detection process. This specialized model is meticulously crafted to manage dark frames and low-light conditions adeptly. Its initial step involves augmenting the dark input frame utilizing sophisticated image processing techniques, thereby significantly enhancing image visibility and quality. Following the application of this enhancement, the YOLOv7-DarkVision model conducts precise detection by identifying handguns within the improved dark frame.
## Authors

- [**Pavinder Yadav**](https://github.com/PavinderYadav0) 
 
 ```
 Department of Mathematics and Scientific Computing 
 National Institute of Technology, Hamirpur, Himachal Pradesh
 ```
 [Google Scholar](https://scholar.google.com/citations?hl=en&authuser=1&user=p6ZeLMkAAAAJ) , [ResearchGate](https://www.researchgate.net/profile/Pavinder-Yadav) , [Orcid](https://orcid.org/0000-0001-8682-0234)
 

- **Dr. Nidhi Gupta**

 ```
 Department of Computer Applications 
 National Institute of Technology, Kurukshetra, Haryana
 ```


- **Dr. Pawan Kumar Sharma**
 ```
 Department of Mathematics and Scientific Computing 
 National Institute of Technology, Hamirpur, Himachal Pradesh
 ```

## Acknowledgements

 - [Official yolov7](https://github.com/WongKinYiu/yolov7)
  - The video dataset has been sourced from the scholarly work of [Grega et al. (2015)](https://www.mdpi.com/1424-8220/16/1/47)

