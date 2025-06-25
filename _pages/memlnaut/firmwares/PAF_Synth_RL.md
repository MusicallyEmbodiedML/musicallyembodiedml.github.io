---
permalink: /memlnaut/firmwares/pafsynthrl
title: "MEMLNaut Firmware: PAF Synth with Reinforement Learning"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

# Overview

The PAF-CARL firmware offers exploration of Phase Aligned Formant synthesis, using the [CARL](../approaches/carl) approach to ML.

# PAF

[Phase Aligned Formant synthesis](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a560464f05a6a0e20e1a9b8e1f5584f83151587a) was developed my Miller Pucklette in the mid 90s.  It offers methods for creating complex spectra that avoid common issues with subtractive and FM.  The synth runs 3 PAF operators and a delay effect. 19 sound generation parameters are controlled by the three axes of the joystick.

## Inputs

The PAF synth is controlled by MIDI. It listens for ```note on``` messages on channel 1.  These control the frequency of the first operator; the other two operators are detuned from this frequency.  The amplitude is also controlled ny these mnessages.

## Outputs

Mono sound is output to both channels of the line out and headphone sockets.

# Reinforcement Learning

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to the sound it's making. As you indicate preferences for these settings, the DDPG algorithm will start to tune how the actor reacts to the joystick.

# Files

## Code

[https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-CARL](https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-CARL)

## Firmware Download

[https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-CARL/releases/tag/v1.0](https://github.com/MusicallyEmbodiedML/MEMLNaut-PAF-CARL/releases/tag/v1.0)





