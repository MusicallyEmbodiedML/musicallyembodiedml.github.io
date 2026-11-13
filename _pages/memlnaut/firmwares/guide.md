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

Each firmware is downloadable as a ```.uf2``` file.

To install one, you need the ```reset``` and ```boot select``` buttons. They're on the top edge of the MEMLNaut, under the **Reset** and **Boot Sel** labels printed on the panel. From the front, they're between the headphone socket and the SD card, with ```reset``` on the left.

<a href="{{ '/assets/images/memlnaut-boot-buttons.svg' | relative_url }}" class="image-popup" title="Where to find the reset and boot select buttons"><img src="{{ '/assets/images/memlnaut-boot-buttons.svg' | relative_url }}" alt="The MEMLNaut panel with the Reset and Boot Sel labels highlighted on its top edge. A close-up shows the top edge in order: USB, headphones, reset, boot select, SD card. Hold boot select, press and release reset, then let go of boot select. A drive called RP2350 appears on your computer."></a>

To install a firmware:

1. Connect the MEMLNaut to your computer.
2. Put the MEMLNaut into boot select mode: press and release ```reset``` while holding down the ```boot select``` button, then let go of ```boot select```.
3. The microcontroller will now appear as a drive called ```RP2350``` on your computer; drag the ```.uf2``` file onto this drive.
4. The firmware will now upload, and the MEMLNaut will reboot with the new firmware running.

# Firmwares

The current firmwares all use [NISPS](/memlnaut/approaches/nisps). They share one set of controls: like, dislike, drag, scramble and jolt. You can save your models to the SD card. Each firmware's page links to its download.

| Firmware | What it does |
|---|---|
| [MEMLCelium](/memlnaut/firmwares/memlcelium) | Three-voice formant synth with a ratio sequencer |
| [MixMasterMEML](/memlnaut/firmwares/mixmastermeml) | Three drum voices, bassline, arpeggiator and grain delay, with a mixer |
| [VerbFX](/memlnaut/firmwares/verbfxnisps) | Reverb, filterbank and delays for the line input |
| [LiveFX](/memlnaut/firmwares/livefxnisps) | Ten tempo-synced effects for live performance and DJing |
| [VoiceFX](/memlnaut/firmwares/voicefx) | Voice effects: grain delays, delay, reverb, flanger, compressor and vocal EQ |
| [NautLinear](/memlnaut/firmwares/nautlinear) | Waveshaper bank with preamp, damper and feedback, for the line input |
| [Infinibits](/memlnaut/firmwares/infinibitsnisps) | Granular drone synth |
| [Paramsite](/memlnaut/firmwares/paramsitenisps) | MIDI controller for any synth, drum machine, effect or DAW |
| [PAF Synth](/memlnaut/firmwares/pafsynthnisps) | Phase Aligned Formant synth, played over MIDI |

Older firmwares, using the POPR and CARL approaches, are listed under **Legacy** in the sidebar.

# Updating

Models saved to the SD card by an older version of a firmware may not load after you update it. If that happens, train the firmware again and save a new model. Updating doesn't delete the old files from the SD card.
