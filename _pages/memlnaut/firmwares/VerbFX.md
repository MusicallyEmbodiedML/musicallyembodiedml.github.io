---
permalink: /memlnaut/firmwares/verbfxnisps
title: "MEMLNaut Firmware: VerbFX with NISPS"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true
---

# Overview

The VerbFX firmware offers exploration of a multi-effects reverb processor, using the [NISPS](../approaches/nisps) approach to ML.

# VerbFX

VerbFX is a multi-effects processor built around a Freeverb-based reverb algorithm with a filterbank and delays. 47 sound processing parameters are controlled by the joystick. Six effect routing options can be individually enabled or disabled via the FX Enable screen.

## Signal Flow

Input → FilterBank → Delays (Short / Medium / Long) → Reverb → Wet/Dry Mix → Output

The FilterBank can receive feedback from the delay outputs. The delay outputs can also be routed into the reverb input.

## Effect Blocks

1. **FilterBank** — 8 bandpass filters in parallel.
2. **Reverb** — Freeverb algorithm (8 low-pass feedback comb filters + 4 allpass filters)
3. **Short Delay** — 512 sample delay buffer
4. **Medium Delay** — 2048 sample delay buffer
5. **Long Delay** — 16384 sample delay buffer
6. **Delay → Reverb** — Routes the delay mix into the reverb input

## Inputs

The processor takes a stereo input. Left and right channels are summed to mono before processing.

## Outputs

Mono processed sound is output to both channels of the line out and headphone sockets.


# NISPS

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to the effect sound it's producing. As you indicate preferences for these settings, the NISPS system will start to tune the mappings towards your preference. See the [NISPS](../approaches/nisps) documentation for further info.

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
- `Knob Y`: Wet/Dry Mix
- `Knob Z`: Exploration noise (turned off when all the way to the left)
- `Knob G`: Volume

# Screens

Navigate between screens using the rotary encoder.

## FX Enable

Toggle each of the six effect blocks on or off: FilterBnk, Reverb, ShortDly, MedDly, LongDly, Dly→Verb.

## Voice Spaces

Choose a voice space by pushing the rotary encoder to focus the selector. Move the encoder to choose a space and then push again to confirm the selection.

Available voice spaces:

1. Default
2. Resonant
3. Soft
4. Cathedral
5. Shimmer
6. Chamber
7. Metallic
8. Granular
9. Diffuse
10. Dark
11. Bright
12. Harmonic

These voice spaces bias the neural network mappings in particular directions.

## NN Output

Shows the live outputs of the neural network.

## RL Stats

Shows the loss of the neural network as it optimises. If this number is high, the network is struggling to train. If it's low the network is training ok (though possibly overfitting).

## NN Inputs

Shows the inputs to the neural network.

## Messages

Various messages logging interactions with the system.

## Save Model

Tap on a slot to save a model (note: this doesn't save the voice space).

## Load Model

Tap on a slot to load a model.

## Help

Shows what the various controls do.

## System Info

System information about the MEMLNaut and current firmware.

# MIDI

The firmware sends out the first 16 neural network outputs as MIDI controllers, so you can use the MEMLNaut to control your hardware synths.

# Files

## Code

[https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS)

## Firmware Download

[https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS/releases/tag/VerbFX](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS/releases/tag/VerbFX)

See the firmware [guide](./guide) for installation instructions.
