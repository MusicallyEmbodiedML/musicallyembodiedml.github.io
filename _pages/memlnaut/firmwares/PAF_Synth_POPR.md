---
permalink: /memlnaut/firmwares/pafsynthpopr
title: "MEMLNaut Firmware: PAF Synth with POPR"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

# Overview

The PAF-POPR firmware offers exploration of Phase Aligned Formant synthesis, using the [POPR](../approaches/popr) approach to ML.

# PAF

[Phase Aligned Formant synthesis](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a560464f05a6a0e20e1a9b8e1f5584f83151587a) was developed my Miller Pucklette in the mid 90s.  It offers methods for creating complex spectra that avoid common issues with subtractive and FM.  The synth runs 3 PAF operators and a delay effect. 19 sound generation parameters are controlled by the three axes of the joystick.

## Inputs

The PAF synth is controlled by MIDI. It listens for ```note on``` messages on channel 1.  These control the frequency of the first operator; the other two operators are detuned from this frequency.  The amplitude is also controlled by these messages.

## Outputs

Mono sound is output to both channels of the line out and headphone sockets.



# POPR approach

Use the POPR controls to try and build a new instrument: a joystick that controls sound by interpolating between the position-sound pairs that are contained in the training data.

# Files

## Code

[https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-POPR](https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-POPR)

## Firmware Download

[https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-POPR/releases/tag/V1.0](https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-POPR/releases/tag/V1.0)




