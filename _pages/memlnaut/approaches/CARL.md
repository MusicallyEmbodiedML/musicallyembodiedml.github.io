---
permalink: /memlnaut/approaches/carl
title: "ML Approaches: Continuous Active Reinforcement Learning"
sidebar:
  nav: "memlnaut"
---


# Introduction

CARL describes an interactive approach to reinforcement learning, where the player works in dialog with the machine, by indicating their preference for how the machine is acting.  This can be as simple as indicating 'likes' and 'dislikes' for how the machine responds to inputs in a particular way, or can expand to more complex approches where the player can engage in more depth with the interactive opportunities presented by the reinforcement learning algorithm.  

## CARL

- *Continuous*, as in the process is an ongoing realtime negotiation between player and machine
- *Active*, describing that the player is an active participant in guiding the reinforement learning machine.
- *Reinforcement*
- *Learning* decribing the machine learning approach 

# Reinforcement Learning Approach

## DDPG: Actors and Critics

We follow an approach called *Deep Deterministic Policy Gradient* (DDPG).  In DDPG, there are two types of neural network interacting with each other, the *actor* and the *critic*.  The Actor network performs actions, such as mapping from the MEMLNaut joystick to synthesis parameters.  The Critic network estimates the value of the Actor's actions.  The player provides feedback into this system by rewarding the Actor's behaviour, both negatively and positvely.  DDPG optimises these networks so that the Actor moves towards the behaviours indicated by the player's rewards, and the Critic increases the quality of its estimates of the Actor's actions.

## Replay Memory

Central to this system is the *experience replay memory*.  This is a store of snapshots in time when the player indicated a reward (positive or negative).  The replay memory is limited in size, and when it's full the systemn will forget previous experiences.  As the system runs, minibatches of experiences are randomly selected from the replay memory and used to optimise the Actor and the Critic.

## Interacting with DDPG

When we run DDPG in realtime with active guideance from the player (as opposed to e.g. offline in a simulator),  there are some interesting possibilities that open up for the player.  Beyond providing rewards, the player can also

1. Randomise the weights of the Actor network. 
2. Randomise the weights of the Critic network. 
3. Forget some or all of the experience replay memory
4. Vary the scaling of rewards

## Quick-start guide

1. Plug the unit in, turn the joystick (or move the input sensors),
hear the model make the first sounds.
2. Keep trying different positions. The model will slowly drift towards different sounds.
3. Start flicking **Momentary A1** switch up or down. A flick up will give the model a *positive* reward, a flick downwards a *negative* one.
4. Keep experimenting with the inputs and keep giving feedback to the model.
5. If you feel like the model got stuck, flick **Momentary B1** switch up
to *reset the actor*.

# Controls


### Momentary switches

**Momentary A1** (up): *reset the actor* - the actor restarts from a random position.

**Momentary A2** (down): *reset the critic* - the critic forgets how to anticipate your taste.

**Momentary B1** (up): *positive reward* for the model.

**Momentary B2** (down): *negative reward* for the model.

### Toggle switches

**Toggle B1** (down): clear the *replay memory* (the "dataset" of the RL algorithm's experiences).

### Pots

**X potentiometer**: sets the *frequency of optimisation* - how often the critic affects the actor.

**Y potentiometer**: EXPERIMENTAL: *reward scaling* - associates a measure of how much you like-dislike an experience.










