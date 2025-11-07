---
permalink: /memlnaut/approaches/nisps
title: "ML Approaches: Neural Interactive Shaping of Parameter Spaces"
sidebar:
  nav: "memlnaut"
toc: true
toc_sticky: true  
---


# Introduction

NISPS is a method for interactive engagement with the training process of machine learning models, based in reinforcement learning (RL) principles.  NISP merges exploration and optimisation into a continuous experience.  It builds on our [first experiments with RL](./carl), and also brings in exploration features from the [POPR](./popr) approach that give further option for shaping of sound.   The approach is called NISPS because it allows you to creatively refine how the joystick on MEMLNaut controls sound, in a dialog between the musician and the instrument.

# Context

The MEMLNaut system takes an input (usually from the 3D joystick), passes this input into a machine learning (ML) system, and then the ML system outputs a set of parameters which control sound processing. This might be the sounds of a synthesiser, or the way in which a set of effects are applied to audio input.  Algorithms on the MEMLNaut allow the musician to tune the ML system; to guide it towards making different sounds in reaction to different inputs.  This allows large and complex sound processes to be controlled in musically meaningful ways from low dimensional inputs, a bit like controlling all the knobs at once of a large synthesiser just by moving a joystick.  This approach to sound control allows musicians to set up expressive and dynamic mappings. However, it can be a challenge to find the right mappings in a *musical* way, which is where the MEML project's experimentation with machine learning approaches offers new solutions.

# Machine Learning Background

NISPS draws on the core idea of reinforcement learning, that an algorithm is rewarded for doing something well, and penalised for doing something that is undesired.  Conventionally, RL systems are comprised of an *agent* and an *environment*; the agent explores the environment and is rewarded (or not) for it's actions. The agent tries to estimate the value of current and future actions based on how it has been rewarded. Through ongoing exploration, the agent is optimised towards achieving a particular task, for example playing a game or controlling a robot.  In the context of the MEMLNaut, we have a different scenario from this traditional RL configuration;  there is no concept of *future* on which to estimate the value of rewards (we call this a *stateless* system), the ML system maps whatever the musician's current input is into sound parameters, which no regard for what might happen next. Secondly, the concept of a penalty is ambiguous. In a typical RL system, the agent receives a penalty because if made an error or exhibited undesirable behaviour.  In a creative musical system, there's no explicit wrong action, but instead there are actions that the musician has an aesthetic preference for or against (e.g. i don't like the sound that happens when the joystick is in this position). Bearing these differences in mind, NISPS draws on the core concepts of RL, and adapts them to work within an interactive, stateless environment. NISPS aims to provide the musicians with controls over the machine learning process so that it can become a creative component of musical practice.


# Elements of NISPS

## Control Inputs

These are what the musician uses to play the system and influence how sound is generated or processed.  It might be a combination of the following:

1. The MEMLNaut joystick
2. MIDI Inputs
3. Machine listening obserations of audio input

## Sound System

This might be a synthesiser, an effects processor, or a combination of the two. The sound system will have a set of parameters available that determine its behaviour, the equivelant of the knobs and sliders on a synthesiser.

## Voice Spaces

A voice space is a hand-designed translation layer that sits between the outputs of the neural network and the controls of the sound system.  It biases the controls in certain ways, for example it might make a synthesis more likely to produce bass sounds, or it might make an effects unit more likely to produce distorted sounds.  It constrains the neural network to exploring certain areas of what the sound system is capable of making.

## The Neural Network

The neural network takes input, and transforms this into parameters for controlling sound.  The net is malleable, and can continually change in use.  Everytime the input changes, the sound control parameters will change.  If the system is not being optimised, the neural network will behave consistently, i.e. the same input will always produce the same output.  If the system is being optimised, then the relationship between input and output can be adjusted.

## Rewards

Rewards tell NISPS when the musician has a preference (positive or negative) for how the neural network behaves. i.e. how it takes input and translates it into parameters for sound control.  A positive reward tells NISPS that you like the sound that is being made for a particular input. A negative reward signifies the opposite.

## Replay Memory

This is a collection of the most recent rewards, along with a snapshop of the inputs and neural network outputs at the moment the reward was given.  The replay memory is finite, and when it is full, older memories are forgotten.

## Optimisation

This is a process that continually runs in the background.  As soon as NISPS has enough memories to work with, it begins to adjust the neural network to match the musicians preferences.

## Controls for NISPS

These govern how the neural network changes during optimisation.

### Positive and negative rewards

These place an item into the replay memory

### Scramble the neural network

This randomises the neural network, which in effect gives a completely new mapping from input to sound control.  If there are items in replay memory, then the optimisation system will adjust the randomised network towards the musicians preferences following randomisation.

### Jolt the neural network

This adds a small amount of randomness to the neural network.  It can be useful if the optimisation process is stuck, or if you just want to try a slightly different mapping.

### Reward scaling

You can change the scaling of rewards, i.e. how much you dislike or like a certain mapping.  You can tell the system, for example, that you *really like* something, or that you have a *slight preference* for something else.

### Learning Rate

This is a speed at which the system is optimised according to your rewards.  If you're happy with how the system is behaving, then you can turn this all the way down to ```0``` and the system will not change. A high learning rate might mean that the system has less precision about how it learns, but will learn quickly.  With a medium learning rate, there might be more precision but the system will adjust more slowly. Learning rates which are too fast or two slow might mean the system can either *overshoot* the optimal solution or *undershoot* and get stuck in a suboptimal solution.  In NISPS and creative machine learning, the concept of an optimal solution is often ambiguous or unknown. Optimisation of neural networks is not an exact science, which is why NISPS offers these interactive controls to the musician who can develop an intuitive feel for steering this process. 

### Exploration Noise

The exploration noise control adds incresing amounts of slow moving noise to the outputs of the neural network.  This is a method, taking from reinforcement learning, that allows exploration of the sound space.  E.g. if you want to find a different sound for a particular place on the joystick, then turn up the exploration noise and wait until you like the sound, then reward the system for that sound and turn the noise off. You'll find that the system now adjusts towards that sound.  *Note:* check that you don't leave this control on when not needed, as it will mask the true behaviour of the neural network.

### Positive Reward Placement

This is where you can not just reward the combination of input and sound, but move that rewarded input to somewhere else in the space of possible inputs. For example, using the joystick, you might take the input-sound combination for the joystick in the up position, but place the reward instead in the down position. NISPS will then adjust the neural network so that sound tends to appear in the down position.   This is a way of organised and editing the mappings of the neural network.  You can be creative with this system.  For example, you might place several input-sound combinations in the same position, and then the neural network will tend towards a sound that's somewhere in between these sounds.

### Forgetting

You might need a fresh start, in which case you can clear the replay memory of all the rewards you have collected, and collect new ones. If you forget the memory and then ramdomise the network, you are starting from a completely new place.




