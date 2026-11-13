---
permalink: /memlnaut/firmwares/paramsitenisps
title: "MEMLNaut Firmware: Paramsite with NISPS"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true
---

# Overview

Paramsite turns the MEMLNaut into a MIDI controller for any synth, drum machine, effect or DAW, using the [NISPS](../approaches/nisps) approach to ML. It makes no sound of its own: the neural network drives **32 outputs**, each sent as a MIDI CC.

You can set up your own CCs in one of four User slots, or choose a preset with the CC table of a particular synth already filled in.

MIDI arriving at the MEMLNaut is passed through to its outputs, merged with the CCs, so you can play a synth that has no keyboard from a MIDI keyboard or a computer. See [Options](#options).

# MIDI Modes

Choose a mode on the [MIDI Mode](#midi-mode) screen. Each mode has its own CC setup, MIDI channel, focus groups and folder of saved models.

| Mode | Channel | Focus groups | Keyboard thru |
|---|---|---|---|
| User 1–4 | 1 | 1-8, 9-16, 17-24, 25-32 (by output) | no |
| Roland TR-8S | 10 | BD SD LT MT HT RS HC CH OH CC RC FX | no |
| Roland TR-6S | 10 | BD SD LT HC CH OH FX | no |
| Waldorf microQ | 1 | OSC MIX FILT ENV LFO FX | yes |
| Waldorf Blofeld | 1 | OSC MIX FILT FENV AENV MOD FX | yes |
| Novation Supernova II | 1 | OSC MIX FILT ENV LFO FX | yes |
| DSI Mopho | 1 | OSC MIX FILT FENV AENV ENV3 | yes |
| Erica Synths Steampipe | 1 | ENV STEAM PIPE REVERB | yes |
| Erica Synths Resonant Filterbank | 1 | LOW MID HIGH GRP RESO GLOB | no |
| Korg minilogue xd | 1 | OSC MIX FILT ENV LFO FX | yes |
| Novation Bass Station II | 1 | OSC MIX FILT ENV LFO FX | yes |
| Sequential Prophet Rev2 | 1 | OSC MIX FILT FENV AENV ENV3 FX | yes |
| Elektron Digitone | track | FM FMENV FILT AMP LFO | yes |
| Arturia MicroFreak | 1 | OSC FILT ENV CYC LFO | yes |
| Melbourne Instruments Nina | layer | OSC MIX FILT ENV LFO FX | yes |

- **Keyboard thru**: when all the [MIDI thru](#options) routes are off, notes arriving at the MEMLNaut are still passed on to the synth, moved to the mode's MIDI channel. With MIDI thru on, notes go through on the channel they arrive on, so set your keyboard to the synth's channel.
- **Fade**: in every mode, each CC has a *home* value. Knob Y fades between the home values (left) and the neural network (right), so you can start from a patch or kit you've set up and bring in as much of the network as you like. Knob G sets the home value of the CC under the cursor on the [CC Assign](#cc-assign) screen. Homes start at 0, except in the Blofeld and Supernova II presets, which start from a usable patch.

The synth presets were checked against each maker's published CC table. Make sure the synth is set to receive CCs (for example Global → MIDI Param Receive on the Mopho and Rev2, Global → Controller Recv on the microQ). For the Steampipe, check Settings → MIDI CC MAP on the synth, as only some of its CC numbers are published.

# NISPS

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to the set of CC values it's producing. As you indicate preferences, the NISPS system will start to tune the mappings towards your preference. See the [NISPS](../approaches/nisps) documentation for further info.

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
- `Knob Y`: Fade between the home values (left) and the network (right)
- `Knob Z`: Exploration noise (turned off when all the way to the left)
- `Knob G`: Set the home value of a CC (on the CC Assign screen)

# Screens

Navigate between screens using the rotary encoder.

## Neural Net

Info on the neural network: the outputs, the current error rate, the number of datapoints in replay memory, and the most recent command.

## Focus

Selecting one or more groups in the focus menu freezes all *unfocused* outputs at their current value, so that NISPS only changes the *focused* values. In the User modes the groups are blocks of eight outputs; in the synth presets they are sections of the synth, such as oscillators or filter. Most modes also have **HOLD**, which freezes all CC output.

## NN Inputs

Shows the inputs to the neural network.

## Save Model

Tap on a slot to save a model. The model includes the CC assignments. Each mode saves to its own folder on the SD card.

## Load Model

Tap on a slot to load a model.

## Input Source

Choose from
- the joystick that matches your hardware (3D or 4D)
- machine listening analysis of the line input (allows the system to adapt to different sounds)
- various configurations of MIDI controllers

If you use a MIDI controller as the input and the receiving device echoes CCs back (MIDI thru), keep the output CCs off CC 1–8 to avoid a feedback loop.

## CC Assign

Choose up to 32 CCs, and set their home values with knob G. The list is kept sorted, and that is the order of the outputs. Outputs without a CC are left out of training. The User modes offer CC 1–119 and start on CCs that have no standard MIDI meaning, so a DAW or plugin won't treat them as volume, pan or mod wheel; the presets offer their synth's CC list. The assignments are saved when you leave the screen.

## MIDI Learn

For mapping the CCs in a DAW or plugin. Push the encoder, turn to one of the assigned CCs, and push again to start. While the screen has control, every other CC is frozen and the chosen CC sweeps from 0 to 127 every two seconds, so your DAW's MIDI learn picks up that CC alone. Push again, or leave the screen, to stop.

Mapping CCs to a plugin's macros lets one CC drive several parameters.

## MIDI Channel

Choose the MIDI channel, 1–16. Saved separately for each mode.

## MIDI Mode

Choose the [MIDI mode](#midi-modes). Push the encoder, turn to a mode, and push again: the choice is saved and the MEMLNaut restarts into the new mode. To leave without changing mode, choose **Cancel** (at either end of the list) or leave the screen without pushing.

## Options

MIDI thru: copy the MIDI arriving at the MEMLNaut to its outputs, merged with the CCs it sends. Each route can be turned on or off; highlighted routes are on, and all three are on by default.

| Route | From | To |
|---|---|---|
| **HW>HW** | MIDI DIN input | MIDI DIN output |
| **HW>USB** | MIDI DIN input | USB MIDI |
| **USB>HW** | USB MIDI | MIDI DIN output |

USB input is never sent back to USB, so a DAW can't get stuck in a feedback loop. Notes, CCs, program changes, pitch bend and aftertouch are passed through; SysEx and clock are not. The MEMLNaut still responds to the MIDI it receives as usual. The settings are saved, and apply in every MIDI mode.

If something on the input also sends CCs that the MEMLNaut is sending, the receiving synth will get both: turn that route off, or keep the CCs apart.

## Levels

Input and output level meters (In L, In R, Out L, Out R), with the **In Gain** fader beside them. In Gain is the codec's analog input gain, 0 to +22.5 dB in 1.5 dB steps: set it while watching the input meters. It's saved, and applies in every firmware.

## Help

Shows what the various controls do.

## System Info

System information about the MEMLNaut and current firmware.

# MIDI

The CCs are sent on the MIDI DIN output, and also on USB: the MEMLNaut appears on a computer as a USB MIDI port called "MEMLNaut MIDI". Notes and CCs received over USB are handled the same way as on the DIN input. SysEx is DIN only. MIDI received on either input can be passed through to the outputs: see [Options](#options).

# Files

## Code

[https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS)

## Firmware Download

[MEMLNaut-NISPS.Paramsite.1.2.1.uf2](https://github.com/MusicallyEmbodiedML/MEMLNaut-NISPS/releases/download/1.2.1/MEMLNaut-NISPS.Paramsite.1.2.1.uf2)

See the firmware [guide](./guide) for installation instructions.
