---
title: "Further Experiments in Neural Mapping Design"
date: 2024-11-19
categories:
  - demo
tags:
  - prototype
  - xmos
  - multifx
  - modular
  - sequencing
  - dsp
  - neuralnetwork
  - mapping
author_profile: false
---


In the last month or so we've been doing some more experimentation with hardware instruments and mapping design using neural networks. In October, ahead of a visit to Machina Bristronica, Eric from [Schlappi Engineering](https://schlappiengineering.com/) visited for a week long hack session, and we made a new instrument based on our FM synthesis joystick prototype, converted to use for sequencing in modular synthesis.  


<iframe width="560" height="315" src="https://www.youtube.com/embed/PAwbFgUveCI?si=xEitO005prkhqiG9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


The sequencing engine runs a set of four [euclidean sequencers]( https://erikdemaine.org/papers/DeepRhythms_CGTA/paper.pdf), with four parameters *(n, k, speed, offset)* controlling the rhythm they generate.  This space of 16 parameters is mapped to the three dimensional joystick, via a neural network. Controls on the module allow the player to collect points in the parameter space and train the mappings in the neural network. This results in a joystick controlled techno!


Another experiment we've done is to take a similar system and use it to control a larger parameter space in a multifx engine.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6G7BbbTWlO4?si=pd53CWvXd97U1TPa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

This video shows us trying out the engine, with modular synth drums, e-drums and guitar.  There are four effects (flange, delay, ring mod and filter). These are mixed together through a mixing matrix, which means that each effect takes a mix of itself and other effects as the input, in addition to the live signal from the instrument.  The neural network controls all of the levels in the mixing matrix, in addition to the mix levels of the live input and the parameters of the effects.  This results different in effects fading in and out in different areas of the joystick, and makes some interesting and unexpected surprises.

These different instruments are creating a basis for us to run experiments in different ways to interact with neural networks as we train, modify and evolve them towards musical goals.