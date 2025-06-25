---
permalink: /memlnaut/firmwares/multieuclideancarl
title: "MEMLNaut Firmware: Multi-euclidean Sequencer with Reinforement Learning"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---

# Overview

A bank of 8 euclidean sequencers are controlled by a neural network, mapped from 3 axes of the joystick.

# Euclidean Sequencing

Euclidean sequencing describes a process that generates events according to two numbers: ```N``` and ```K```.  ```N``` is the number of divisions within a time period.  ```K``` is the number of events the algorithm tries to fit into these divisions.  If N is divisible by K then a regularly spaced pattern is generated, otherwise the closest fit is chosen, creating varied rhythms.

A good analysis of euclidean rhythms can be found in Godfried Toussaint's paper [The Euclidean Algorithm Generates Traditional Musical Rhythms](https://www-cgrl.cs.mcgill.ca/~godfried/teaching/dm-reading-assignments/Euclidean-Rhythms.pdf)

## Outputs

MIDI notes are output each time a euclidean generator triggers an new event.

# Reinforcement Learning

When you indicate a reward, you are rewarding (negatively or positively) how a particular joystick position is mapped to the sequence it's generating. As you indicate preferences for these settings, the DDPG algorithm will start to tune how the actor reacts to the joystick.

# Files

## Code


