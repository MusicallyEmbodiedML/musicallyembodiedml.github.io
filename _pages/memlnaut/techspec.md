---
permalink: /memlnaut/techspec/
title: "MEMLNaut Technical Specification"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

The MEMLNaut pcb is a RP2350B microcontroller with a stereo audio codec, MIDI IO and SD Card storage.  It provides pin headers to break out a wide range of IO from these systems. 

### PCB 

![MEMLNaut Front](/assets/images/MEMLNaut_0_2.jpg){:class="img-responsive"}
![MEMLNaut Back](/assets/images/MEMLNaut_0_2_back.jpg){:class="img-responsive"}

### Microcontroller

- Raspberry Pi RP2350B
- dual ARM M33 or RISCV cores
- 16Mb flash
- pcb footprint for soldering another flash memory or a PSRAM chip
- 8 ADCs
- range of GPIO options including SIO, UART, SPI, i2C, I2S, and custom IO with state machines

### Audio CODEC

- NXP SGTL5000 codec
- stereo line out
- stereo headphone output
- stereo line in
- mono microphone preamp with bias voltage
- variety of sample rates
- I2S

### Power

- runs from 5V USB power (USB-C connector)
- separate 3.3V regulators for analogue and digital power domains
- 5V input for external power (non-USB)

### Breakout Pinheaders

- 5V, 3,3V and 3.3V analog power
- SWD 
- GPIO pins
- ADCs
- line ins and line outs
- microphone input
- SD Card SPI pins
- I2S
- I2C bus (with pull-up resistors)
- vertical mount USB-C connector


### Panels

![MEMLNaut Panel Front](/assets/images/memlnaut_0_3_joystick.jpg){:class="img-responsive"}
![MEMLNaut Panel Back](/assets/images/memlnaut_0_2_backplate.jpg){:class="img-responsive"}


### Schematics

<div id="pdf" style="width:100%; height:800px;"></div>
<script src="https://cdn.jsdelivr.net/npm/pdfobject@2.2.8/pdfobject.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>PDFObject.embed("/assets/pdf/MEMLNaut_0_2.pdf", "#pdf", {height: "100%"});</script>

### Github

[https://github.com/MusicallyEmbodiedML/MEMLNaut](https://github.com/MusicallyEmbodiedML/MEMLNaut)



