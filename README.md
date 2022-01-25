This document was written by Kaito Masuda (masukai9612kf@gmail.com)

---

# AutoArea-GUI

This **AutoArea-GUI** can calculate something's area in each picture repeatedly by Python 3 (3.8.6) instead of [ImageJ](https://imagej.nih.gov/ij/).
**AutoArea-GUI** is also the GUI version of [AutoArea](https://github.com/masukai/AutoArea).

2021.12.14: On Windows OS, I have received a report that the first line "#! /usr/bin/env python" in all python files can sometimes cause problems. Please remove it and try to run the file.

## Dependencies

- Numpy (1.19.5)
- OpenCV2 (4.5.1)
- (Matplotlib (3.1.1))

## Install

```
git clone https://github.com/masukai/AutoArea-GUI.git
```

If you do not install Python 3, Numpy and OpenCV2, please install them, following below.

- [Python 3](https://www.python.org/downloads/)
- Numpy, OpenCV2 and Matplotlib

```
pip(3) install numpy
pip(3) install opencv-python
pip(3) install matplotlib
```

If you need "(3)" to use Python 3, not Python 2, please add it.

## Usage

### First Step

please set your pictures in which you want to calculate areas in the **photo(YOU CAN CHANGE THE NAME)** folder.
I saved 2 sample pictures. If you want to calculate your data (pictures), please delete my samples.

### Second Step

Move to _AutoArea-GUI_ directory and type below,

```
python(3) gui.py
```

then, the GUI will open.

<img alt="gui_sample" src="https://user-images.githubusercontent.com/37993351/122935809-9b1a6a00-d3ab-11eb-9e58-9b8f350aa3ce.png">

Please refer to [ImageJ](https://imagej.nih.gov/ij/) and enter the appropriate parameters in the GUI.

You can then click on "Calculate" to calculate the area of the object in the image in the **photo (YOU CAN CHANGE THE NAME)** folder.

Finally, you will gain the results in the **photo_calculated_area.csv** file.

The parameters are stored in the **parameter.csv** file and will be quoted when you use **AutoArea-GUI** again.

### Third Step

If you do not want to use the GUI mode, please move to _AutoArea-GUI_ directory and type below.

```
python(3) AutoArea.py
```

The parameters in lines 169 to 177 need to be adjusted in the [AutoArea.py](https://github.com/masukai/AutoArea-GUI/blob/main/AutoArea.py).

## CAUSION

- **An environment of taking pictures is the most important.**
  Please take pictures or images in the almost same environment.

- See [AutoArea](https://github.com/masukai/AutoArea) for the effect of the parameters.

- This program has been checked by MacOS 11.4 (2021.06.23).
  If you find some bugs, please tell me about them.
