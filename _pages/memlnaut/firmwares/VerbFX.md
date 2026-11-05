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


# Quick start

1. Flash the firmware, connect a sound source to the line input and turn up **G**.
2. Set the wet/dry balance with **knob Y**.
3. Choose a starting character on the **Voice Spaces** screen.
4. Move the joystick, then like, dislike, drag and jolt as described on the [NISPS page](/memlnaut/approaches/nisps#quick-start).

# NISPS

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to the effect sound it's producing. As you indicate preferences for these settings, the NISPS system will start to tune the mappings towards your preference. See the [NISPS](../approaches/nisps) documentation for further info.

# Controls

<a href="{{ '/assets/images/nisps/panel-verbfx.svg' | relative_url }}" class="image-popup" title="MEMLNaut panel with the VerbFX controls"><img src="{{ '/assets/images/nisps/panel-verbfx.svg' | relative_url }}" alt="MEMLNaut panel with the VerbFX controls. Controls that differ from standard NISPS are ringed in gold." class="img-responsive"></a>

*Click the panel to enlarge it. Controls ringed in gold work differently from the standard NISPS controls.*

The controls are the standard [NISPS controls](/memlnaut/approaches/nisps#controls), with this change:

| Control | In VerbFX |
|---|---|
| **Knob Y** | Wet/dry mix (instead of reward scale) |

# Screens

Navigate between screens using the rotary encoder.

## RL 

Info on the neural network - the outputs, the current error rate, the number of datapoints in replay memory, and the most recent command.

## Focus

Selecting one or more items in the focus menu freezes all *unfocused* neural network outputs at their current value, so that NISPS only changed the *focused* values.  This let's you do detailed training, e.g. if you just want to adjust the reverb but not other sounds.

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

## NN Inputs

Shows the inputs to the neural network.

## Save Model

Tap on a slot to save a model and current voice space,

## Load Model

Tap on a slot to load a model.

## Input Source

Choose from 
- the joystick that matches your hardware (3D or 4D) 
- machine listening analysis of the line input (allows the system to adapt to different sounds)
- various configurations of MIDI controllers

## Help

Shows what the various controls do.

## System Info

System information about the MEMLNaut and current firmware.

# Parameters

| Outputs | What they control |
|---|---|
| 0 | Crossfade between filterbank and delays |
| 1–16 | Comb filters: feedback and cutoff for each of the eight |
| 17–20 | Allpass filter feedback |
| 21–28 | Filterbank frequencies |
| 29–36 | Filterbank resonance |
| 37–42 | Delay times and feedback |
| 43–46 | Routing: reverb against delay, delay into reverb, delay morph and blend |

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

[https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS). To build this firmware, define `MODE_VERBFX` in `MEMLNaut-NISPS.ino`.

## Firmware Download

[https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS/releases/tag/VerbFX_1.1.0](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS/releases/tag/VerbFX_1.1.0)

See the firmware [guide](./guide) for installation instructions.
