---
title: "MEML Workshop at CHIME 2024"
date: 2024-12-01
categories:
  - workshop
  - conference
tags:
  - workshop
  - documentation
  - instruments
author_profile: false
toc: true
toc_sticky: true

---

# The Instruments

We have three instruments to use in the workshop, all with a similar interface.  Each instrument has a large-ish parameter space which is controlled by a 3D joystick, supported by other controls for engaging with machine learning models.

The instruments:

- a multi-fx processor
- a sequencer
- an FM synthesiser

# Connecting to the web interfaces

Each instrument is running a small web interface for extended options that control machine learning.


# Documentation

## Quick-start tutorial

1. Make sure you are in Inference mode: the LED on the unit should be Off, and the Web GUI should display the training radio button under the Training section.

2. Wiggle the joystick (and play a note at the same time, if required): you will hear the sound changing as you move the joystick. With the joystick, you can interact with the model and map the joystick’s coordinates to your desired sounds. The joystick moves around in two dimensions and you can twist its top knob too.

3. Switch the toggle on the unit up: the LED lights up, and you will be in Training mode.

4. Press the green button to the LEFT (“Draw”): the sounds mapped to the joystick will change randomly. This is the start of your training session.

5. Explore the new sounds with the joystick. Once you find one that you like, you have two options:
  - Press Draw again: the current sound will be manipulated with further random noise (see “Exploration Modes” in the Web GUI) so you can explore sounds that are similar to it, and fine-tune your base sound. By default, it will put the current sound at the centre of the joystick (“Pre-train” mode). 
  - Press and hold the button on top of the joystick (“Save”): move the joystick to the desired position, and release the Save button. This creates a data point in the Dataset. After training, the selected sound will be in that position when you go back to Inference mode.
6. After a data point is saved into the Dataset, press “Draw” again: the network will be re-randomised, and you can repeat Step 5 to create more data points.
7. If you want to start the acquisition process again, the green button on the RIGHT (“Clear”) will clear the dataset. You can then start again from Step 3.

8. Experiment with populating a dataset with a few data points. Then, flick the toggle switch down to Inference. The Model will train for a few seconds, then display its final loss value on the Web interface.

9. Your Model is trained! Play around with it, find your saved sounds and explore the ones in between that the Model has generated. Then, start creating more than one Dataset and training more than one Model. Use different Exploration Modes too. 

See the GUI guide for a detailed explanation.

## Hardware interface elements

### Joystick

The joystick lets you control the parameters of the instrument, by providing input data to the Model. The joystick operates in three dimensions: X-Y axis movements, and bi-directional twists of its knob. The button on top is the Save button (see below).

### Training/Inference switch
This switch lets you go in and out of Training or Inference mode. In Training mode (green LED ON), you can acquire data and create a dataset. In Inference mode, the Model is trained for the set amount of Iterations, then the joystick guides you through the parameter space using the trained Model.
This switch is equivalent to the Train/Acquire button in the Web GUI.

### Draw button
The Draw button moves the training process by one step. At the start, it draws new random parameters. After that, it lets you “zoom” into the sound that the joystick points to when the Draw button is pressed, according to the selected Exploration mode (see Web GUI elements).

### Clear button
This button clears the current Dataset and re-initialises the training sequence (Step 3 in the Quick Start guide). It is equivalent to the “Clear” button for Datasets in the Web GUI. 
Web GUI elements

### Datasets
Each radio button represents one Dataset. You can change between Datasets in Training mode. Datasets can be cleared at any time with the Clear button below. A Model cannot be trained on an empty dataset.

### Models
Each radio button represents one Model. You can change between Models either in Training or in Inference mode. Models can be reset to random weights with the Reset button below.

## Modes
There are two modes, “Training” and “Inference”. You can switch between them either by flicking the hardware switch on the unit, or by pressing the “Train”/”Acquire” button on the web interface. Every time you switch from Training to Inference mode, the current Model will get trained on the current Dataset.
The green LED on the unit is turned on if you are in Training mode.
If you switch in and out of Inference mode more than once on the same dataset, the network will train for longer on the same dataset.

### Iterations
How long you want the network to train on your data? This slider sets the number of epochs from 1 to 2000. Loosely-trained models may also make inspiring sounds.

### Exploration modes

Exploration modes are different ways to navigate random parameter spaces during training. Each of them is a different way to re-randomise the weights of a Model around a sound that you select with the joystick. The Exploration modes are:

- NN Weights: Gaussian noise is summed to the weights of a neural network. Exploration Range controls the variance of the noise.
- Pre-Train: The network is pre-trained so that a selected sound is moved to the centre of the joystick’s parameter space. Exploration Range controls the range around the centre that the joystick can reach.
- Zoom: This mode “zooms in” around the sound that was selected by the joystick position. The Model’s weights are unaffected. Exploration Range sets the amount of zooming-in: less range means more zoom.

You can change Exploration modes and range at any point as you acquire more data in Training mode.

## Troubleshooting

### The Microsoft way
Unplug the USB-A cable going from the back of the unit to the power supply or USB hub, and plug it back in after a few seconds.

### Web GUI is unresponsive
Have a laptop with a serial terminal ready (e.g. screen). Disconnect the main USB cable from the unit. Connect a MicroUSB cable to the Pi Pico contained in the unit. Open the device /dev/ttyACM0. Disconnect and reconnect the MicroUSB cable into the Pico. Then connect the main USB cable of the unit. Upon boot-up, the Pico should display two things:
- the IP address that it uses for serving the Web GUI
- A message acknowledging that the XMOS board has booted up and has supplied a status message

Check that the webpage refreshes correctly and the browser points at the right IP address, and is connected to the same network. Check that the XMOS board is powered up.
None of the above works

Ask for help from the workshop organisers!