---
permalink: /memlnaut/firmwares/multifxrl
title: "MEMLNaut Firmware: Multi FX Processor with Reinforement Learning"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

# Overview

This firmware offers exploration of multi fx, using the [CARL](../approaches/carl) approach to ML.

# Multi Effect Algorithms

The processor has the following effects chain:

Pitch shifter -> Stereo Delay -> Dry/Wet Mix -> Outputs

Output from the neural network controls:

1. The pitch shift frequency (from -12 to +12 semitones)
2. The delay time, feedback and dry/wet mix for delays on each channel
3. The overall dry/wet balance


## Inputs

The processor takes a mono input on the right channel.

## Outputs

Stereo sound is output to the line outs and headphone sockets.

# Reinforcement Learning

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to the sound it's making. As you indicate preferences for these settings, the DDPG algorithm will start to tune how the actor reacts to the joystick.

# Files

## Code

[https://github.com/MusicallyEmbodiedML/memlnaut-multifx-carl](https://github.com/MusicallyEmbodiedML/memlnaut-multifx-carl)





