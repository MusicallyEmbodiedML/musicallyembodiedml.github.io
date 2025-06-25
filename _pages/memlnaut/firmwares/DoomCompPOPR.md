---
permalink: /memlnaut/firmwares/doomcomppopr
title: "MEMLNaut Firmware: PAF Synth with POPR"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

# Overview

This firmware is inspired by Mick Gordon's extreme compressor.  It generates complex noise and distorted sound in reaction to joystick movement.  Note that this a sound generator rather than an effect.

# Doom Compression

This describes a technique for using extremely high compression ratios.  Six sinewaves are detuned and mixed together with varying amplitudes.  They are put through a delay with variable feedback, and compressed with a 200000:1 ratio and -20db threshold.  The sine oscillators battle for a path through the extreme compression as they intermodulate.

The output is complex, and can be very sensitive to joystick input in some areas and insensitive in others.


## Outputs

Mono sound is output to both channels of the line out and headphone sockets.


# CARL approach

Reinforcement learning helps you to explore the complex soundscape of the doom compressor.

# Files

## Code

[https://github.com/MusicallyEmbodiedML/MEMLNaut-DoomComp](https://github.com/MusicallyEmbodiedML/MEMLNaut-DoomComp)

## Firmware Download

[https://github.com/MusicallyEmbodiedML/MEMLNaut-DoomComp/releases/tag/v1.0](https://github.com/MusicallyEmbodiedML/MEMLNaut-DoomComp/releases/tag/v1.0)



