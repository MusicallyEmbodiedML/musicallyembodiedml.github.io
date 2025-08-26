---
permalink: /memlnaut/approaches/popr
title: "ML Approaches: Perform-Optimise-Play-Repeat"
sidebar:
  nav: "memlnaut"
---


This approach to ML is conventionally refered to as Interactive Machine Learning, but we call it POPR instead to differentiate it from reinforcement learning approaches.  POPR describes an interactive, data-centric approach to machine learning, much like you would use in Fiebrink's software *Wekinator*.  The musician works in a cycle of collecting data, editing the data into a training set (*Perform*), using this data to *optimise* or train a machine learing model, and then *playing* to evaluate the model in inference mode.  This loop might continue until a satisfying result has been achieved, or it may be an ongoing process.  At various points, the player might reset or cut the dataset, and may also reset (i.e. randomise) the model.

## Quick-start guide

1. Plug the unit in, turn the joystick (or move the input sensors),
hear the untrained model in action.

<video controls loop width="100%">
  <source src="/assets/video/memlnaut/01-explore.webm" type="video/webm">
  <source src="/assets/video/memlnaut/01-explore.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

2. Flick **Toggle B1** switch up to *training mode*.
3. Flick **Momentary B1** switch up to *randomise* the network.
Repeat as many times as desired.
4. When you find a sound that you want to keep, press the **head button of the
joystick**, and keep it pressed. Move the joystick (or the input sensors) to
a position where you would like the sound. Release the head of the joystick.
You have *created a data point* in the dataset.
5. Repeat step 4 as many times as desired.
6. Flick **Toggle B1** down to *inference mode* (centre position). Your
network is now trained.

# Controls

### Momentary switches

**Momentary B1** (up): *randomise* the weights of the network. In training mode, this helps to explore the parameter space and collect training points. In inference mode, it resets or adds noise to the network weights.

**Momentary B2** (down): *clear dataset*. Wipes all data points in training mode. Disabled in inference mode.

### Toggle switches

**Toggle B1** (up): switch to *training mode*.

**Toggle B2** (centre or down): switch to *inference mode*.

**Toggle A1** (up): *zoom in* - takes the current sound and put it at the centre of the space, for finer exploration. Only in training mode, disabled in inference mode.

**Toggle A2** (centre or down): *zoom out* - restores the full set of coordinates if previously in zoomed-in mode. Disabled in inference mode.



### Pots

**X potentiometer**: Sets the scaling for randomisation. In training mode, a large scaling will increase the probability of jumping to a new sound in the parameter space. A small value will make a random modification to the existing sound, creating variations.

**Z potentiometer**: Sets the maximum number of iterations the network will be trained for.

**Y potentiometer**: Sets the zoom-in factor. Lower numbers make the zoom-in mode finer, higher number make it coarser (similar to the zoom-out mode).
POPR.md
3 KB

# Screens

### Messages

Messages from the synthesiser about training and inference

### Save Model

Choose a numbered slot to save the current model to.  SD card required.

### Load Model

Choose a numbered slot to load a current model from.  SD card required.

### Help

Quick info about the controls

### System Info

Various info about the hardware and software.


