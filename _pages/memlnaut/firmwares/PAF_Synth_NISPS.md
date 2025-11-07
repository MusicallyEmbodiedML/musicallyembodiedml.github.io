---
permalink: /memlnaut/firmwares/pafsynthnisps
title: "MEMLNaut Firmware: PAF Synth with NISPS"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

# Overview

The PAF-NISPS firmware offers exploration of Phase Aligned Formant synthesis, using the [Neural Interactive Shaping of Parameter Spaces](../approaches/nisps) approach to ML.

# PAF

[Phase Aligned Formant synthesis](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a560464f05a6a0e20e1a9b8e1f5584f83151587a) was developed my Miller Pucklette in the mid 90s.  It offers methods for creating complex spectra that avoid common issues with subtractive and FM.  The synth runs 4 PAF operators along with sine wave shaping, ring modulation, detuning, mixing and a delay effect. 33 sound generation parameters are controlled by the three axes of the joystick.

## Inputs

The PAF synth is controlled by MIDI. It listens for note messages on channel 1.  These control the frequency of the first operator; the other operators are tuned relative to this frequency.  The amplitude is also controlled by these messages.

## Outputs

Mono sound is output to both channels of the line out and headphone sockets.

# Reinforcement Learning

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to a sound. As you indicate preferences for these settings, the NISPS system will start to tune the mappings towards your preference. See the [NISPS](../approaches/nisps) documentation for further info.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9_wnIUFG414?si=ASV7-8gImGS5WuYF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# Physical Controls

- ```Rotary Encoder```: Navigate betwen screens.
- ```Momentary A Up```: Scramble neural network
- ```Momentary A Down```: Jolt neural network
- ```Momentary B Up```: Positive reward
- ```Momentary B Down```: Negative reward
- ```Joystick```: Explore
- ```Joystick button```: Positive reward placement - drag a sound to a different place and release to positively reward it in this position
- ```Toggle A Down```: Clear replay memory
- ```Knob X```: Learning rate 
- ```Knob Y```: Reward scale
- ```Knob Z```: Exploration noise (turned off when all the way to the left)
- ```Knob G```: Volume

# Screens

Navigate between screens using the rotary encoder.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jz2sxsOFroo?si=8-nA4GSPlnBFKj-p" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## NN Output

This shows the live outputs of the neural network.

## RL Stats

Shows the loss of the neural network as it's optimised.  If this number is high, then it's struggling to train. If it's low then the network is training ok (although possibly overfitting).

## Voice Spaces

Choose a voice space by pushing the rotary encooder focus the selector. Move the encoder to choose a space and then push again to keep the selection.

## NN Inputs

Shows the inputs to the neural network

## Messages

Various messages to log interactions with the system.

## Save Model

Tap on a slot to save a model (note: this doesn't save the voice space)

## Load Model

Tap on a slot to load a model

## Play

Tap on the screen to trigger a note. Pitch rises from left to right. Volume rises from bottom to top.

## Help

This shows what the various controls do

## System Info

System information about the MEMLNaut and current firmware.


# Files

## Code

[https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-NISPS](https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-NISPS)

## Firmware Download

[https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-NISPS/releases](https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-NISPS/releases)

See the firmware [guide](./guide) for installation instructions




