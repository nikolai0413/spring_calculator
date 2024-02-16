# Purdue ME354 Spring Calculator
---

[https://springs.nicolasfransen.com/](https://springs.nicolasfransen.com/)

A website that implements a spring calculator to estimate the mechanical properties of a Helical Compression Spring based on geometric and material inputs.

Formulas taken from Shigley's Mechanical Engineering Design (8th Edition)

## Inputs
- End Type
- Material
- Wire Diameter
- Outer Diameter
- Free length *L_0*
- Solid length *L_s*
- Static Load *F_static*
- Cyclic load *F_max*
- Cyclic load *F_min*

## Outputs

- Pitch *p*
- Total \# of coils *N_t*
- \# of active coils *N_a*
- Spring rate *k*
- Force needed to compress to *L_s*
- Factor of safety *n* when compressed to *L_s*
- Factor of Safety *n_s*
- Factor of Safety *n_f*

# Code Overview

### Frontend
Frontend functionality made with [ReactJS](https://react.dev/)
Layout made with [Bootstrap](https://getbootstrap.com/)
Files in <./src>

Backend calculations performed in Python

