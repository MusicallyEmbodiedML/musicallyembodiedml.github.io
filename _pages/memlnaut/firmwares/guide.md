---
permalink: /memlnaut/firmwares/guide
title: "MEMLNaut Firmware Guide"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true
---

There are several firmwares available, to configure the MEMLNaut in different modes, with varied approaches to signal processing and machine learning.

# Installing a firmware

Each firmware is downloadable as a ```.uf2``` file. To install a firmware:

1. Connect the MEMLNaut to your computer.
2. Put the MEMLNaut into boot select mode: press ```reset``` while holding down the ```boot select``` button.
3. The microcontroller will now appear as a drive on your computer; drag the ```.uf2``` file onto this drive.
4. The firmware will now upload, and the MEMLNaut will reboot with the new firmware running.

# Firmwares

The current firmwares all use [NISPS](/memlnaut/approaches/nisps). They share one set of controls: like, dislike, drag, scramble and jolt. You can save your models to the SD card. Each firmware's page links to its download.

| Firmware | What it does |
|---|---|
| [MEMLCelium](/memlnaut/firmwares/memlcelium) | Three-voice formant synth with a ratio sequencer |
| [MixMasterMEML](/memlnaut/firmwares/mixmastermeml) | Three drum voices, bassline, arpeggiator and grain delay, with a mixer |
| [VerbFX](/memlnaut/firmwares/verbfxnisps) | Reverb, filterbank and delays for the line input |
| [LiveFX](/memlnaut/firmwares/livefxnisps) | Ten tempo-synced effects for live performance and DJing |
| [NautLinear](/memlnaut/firmwares/nautlinear) | Waveshaper bank with feedback and grain delay, for the line input |
| [Infinibits](/memlnaut/firmwares/infinibitsnisps) | Granular drone synth |
| [Paramsite](/memlnaut/firmwares/paramsitenisps) | MIDI controller for any synth, drum machine, effect or DAW |
| [PAF Synth](/memlnaut/firmwares/pafsynthnisps) | Phase Aligned Formant synth, played over MIDI |

Older firmwares, using the POPR and CARL approaches, are listed under **Legacy** in the sidebar.

# Updating

Models saved to the SD card by an older version of a firmware may not load after you update it. If that happens, train the firmware again and save a new model. Updating doesn't delete the old files from the SD card.
