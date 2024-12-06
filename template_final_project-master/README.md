
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Asteroid Shooter Game
## CS110 B1 Final Project Fall 2024

## Team Members

Emma Flores

***

## Project Description

This is a shooter game, most similar to the game asteroids. Shoot as many asteroids as you can for the duration of the game and acheive the highest score. 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. Score tracking and display
3. Moveable ship 
4. Animations for explosions
5. Moving asteroids

### Classes

- Player class: loads img of ship, contains behavior of laser
- Asteroid class: contains sprite, positions, number, and movement
- Laser class: contains laser position

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Press arrow keys     |the ship moves up, down, left, right|
|  2                   | click to fire laser  | laser should release from ship    |
|  3                   |fire laser at asteroid| laser make asteroid explode       |
|  4                   | explode an asteroid  | score display should go up        |
|  5                   |play until end of game| ending screen should pop up       |
etc...
