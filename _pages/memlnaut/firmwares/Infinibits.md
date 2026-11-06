---
permalink: /memlnaut/firmwares/infinibitsnisps
title: "MEMLNaut Firmware: Infinibits with NISPS"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true
---

# Overview

The Infinibits firmware is a granular drone synth, using the [NISPS](../approaches/nisps) approach to ML.

# Infinibits

Infinibits feeds a network of three grain delays from two slightly detuned oscillators, fixed at 80 Hz. The oscillators run all the time, so the drone never fades out. 20 sound parameters are controlled by the joystick: grain length, timing, pitch and feedback for each grain delay, how they feed back into each other, and how the oscillators and grains are mixed.

## Signal Flow

Oscillators → Grain Delays 1 and 2 → Grain Delay 3 → back into Grain Delays 1 and 2

The oscillator output and the grain mix are blended, then passed through a DC blocker and a soft saturator.

## Sound Blocks

1. **Oscillators**: two oscillators at 80 Hz, playing one of nine [waveforms](#waveform). The detune between them is controlled by the neural network, from unison up to 50 cents apart, which gives a slow beating.
2. **Grain Delay 1 and Grain Delay 2**: both are fed by the oscillators. Each has its own grain length (10–500 ms), grain start time, feedback, pitch (an octave down to an octave up) and pitch spread. A crossfade blends the two.
3. **Grain Delay 3**: takes the blend of grain delays 1 and 2 and feeds it back into them, with a separate amount for each. With its own pitch and timing, this is where the sound builds up and evolves.

Feedback above unity saturates rather than distorting harshly, so you can push the feedback a long way.

## Inputs

The audio input is not part of the sound, but it can drive the neural network through machine listening (see [Input Source](#input-source)).

## Outputs

Mono, sent to both channels of the line out and headphone sockets.

# NISPS

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to the sound it's producing. As you indicate preferences for these settings, the NISPS system will start to tune the mappings towards your preference. See the [NISPS](../approaches/nisps) documentation for further info.

# Physical Controls

- `Rotary Encoder`: Navigate between screens
- `Momentary A Up`: Scramble neural network
- `Momentary A Down`: Jolt neural network
- `Momentary B Up`: Positive reward
- `Momentary B Down`: Negative reward
- `Joystick`: Explore
- `Joystick button`: Positive reward placement — drag a sound to a different place and release to positively reward it in this position
- `Toggle A Down`: Clear replay memory
- `Knob X`: Learning rate
- `Knob Y`: Feedback amount, scaling all the grain feedback from none (left) to double (right)
- `Knob Z`: Exploration noise (turned off when all the way to the left)
- `Knob G`: Volume

# Screens

Navigate between screens using the rotary encoder.

## RL

Info on the neural network - the outputs, the current error rate, the number of datapoints in replay memory, and the most recent command.

## NN Inputs

Shows the inputs to the neural network.

## Save Model

Tap on a slot to save a model. The current waveform is saved with it.

## Load Model

Tap on a slot to load a model, along with the waveform it was saved with.

## Waveform

Choose the oscillator waveform: Saw, Square, Triangle, Falling Saw, Sine, Half-rect Sine, Trapezoid, Asym Triangle or Staircase.

## Input Source

Choose from
- the joystick that matches your hardware (3D or 4D)
- machine listening analysis of the line input (allows the system to adapt to different sounds)
- various configurations of MIDI controllers

## Help

Shows what the various controls do.

## System Info

System information about the MEMLNaut and current firmware.

# MIDI

This firmware doesn't send the neural network outputs as MIDI. It does listen for MIDI CCs, so you can control NISPS from a footcontroller or similar:

| CC | Action |
|---|---|
| 1 | Positive reward |
| 2 | Negative reward |
| 3 | Scramble neural network |
| 4 | Clear replay memory |
| 5 | Exploration noise |
| 6 | Training speed |

If you choose a MIDI controller on the [Input Source](#input-source) screen, CCs 1-8 become inputs to the neural network instead.

# Files

## Code

[https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS)

## Firmware Download

[MEMLNaut-NISPS.Infinibits.1.2.0.uf2](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS/releases/download/1.2.0/MEMLNaut-NISPS.Infinibits.1.2.0.uf2)

See the firmware [guide](./guide) for installation instructions.
