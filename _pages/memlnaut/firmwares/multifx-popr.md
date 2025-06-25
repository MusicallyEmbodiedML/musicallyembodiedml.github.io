---
permalink: /memlnaut/firmwares/multifxpopr
title: "MEMLNaut Firmware: Multi FX Processor with POPR"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

# Overview

This firmware offers exploration of multi fx, using the [POPR](../approaches/popr) approach to ML.

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

# POPR

Use the POPR approach to create joystick mappings that interpolate between multifx settings.

# Files

## Code

[https://github.com/MusicallyEmbodiedML/memlnaut-multifx-popr](https://github.com/MusicallyEmbodiedML/memlnaut-multifx-popr)







