# DRI SEM Backscattered Electron Image Analyzer

> Direct Reduced Iron, Phase Identification, Image Processing, Mechanical Properties of DRI

Evaluation of mechanical properties of Direct-Reduced Iron (DRI) by using SEM backscattered-electron images

# Introduction

Direct-Reduced Iron (DRI), also known as sponge iron, is highly porous, much less dense than iron ore and sintered steel, and is used as a raw material in electric furnace steelmaking. DRI is expected to sustain compressive impacts during handling, stockpiling, and shipping, which tend to break down DRI into fines. Fines are undesirable, requiring special handling (briquetting, for example) and potentially causing loss of material. The loss of DRI mostly occurs by cracking; the compression strength measured according to ISO 4700 is generally used to benchmark the physical properties of industrial pellets.

![](Figure%201.jpg)

The strength of DRI can be estimated using the BSE image of DRI cross-section (**Figure 1**). However, processing the SEM backscattered electron image is time-consuming and not automated yet; DRI backscattered electron image analyzer, a new software proposed here, can improve the quality of the image and compute mechanical properties within a few seconds. A metallurgical scientist studying ironmaking and steelmaking, DRI plant operator, DRI technology specialist, DRI process designer and engineer are expected software users


## Detailed Features

*	Improve the input SEM image qualities for better resolution and optimal brightness and contrast
*	Process SEM backscattered electron images to discriminate the phases inside and measure the portions of these phases
*	Process SEM backscattered electron images to calculate porosity, and pore-size distribution
*	Identify the biggest crack and void to determine the critical stress of the sample
*	Compute the physical properties of DRI based on the measured results above

## Tutorial Video

- Youtube Link: https://www.youtube.com/watch?v=03C1qXk-r1I

## Getting Started

Please run ‘**App.py**’ at the interpreter of python 3 including necessary modules. As a dry run, ‘DRI_Image_1.jpg’, ‘DRI_Image_2.jpg’, and ‘DRI_Image_3.jpg’ are attached. Please open these files to operate calculations. Open this file first, then use GUI buttons as follows: [image filtering], [calculate porosity], [calculate portion of iron], [calculate portion of iron oxide], [calculate portion of gangue], and [calculate strength].

## Acknowledged

I would like to acknowledge the use of the Materials Characterization Facility at Carnegie Mellon University under grant # MCF-677785.