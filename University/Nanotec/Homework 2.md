# Nanotechnologies Homework II

João Barreiros C. Rodrigues
nº99968, MEEC

## Exercise 1 - Microelectrode array for _in vitro_ studies

This is a topic of great personal interest, specifically for the purpose of bio-FPGAs (programming the neuron array through *stimuli* to develop a certain "bio-computer architecture").
Since the specifications do not include the formation of probes this exercise will be treated as if it was refering **only** to the manufacture of a _in vitro_ MEA.

Enumerating the manufacture process:

1. Substrate Preparation
2. Deposition of Aluminium using **Physical Vapour Deposition**
3. Add photoresist coating and bake
4. Photolithography (Mask Aligment, **EUV exposure** and re-baking)
5. Wash exposed photoresist
6. Combination of **chemical (wet) and physical (plasma)** etching to remove the excess aluminium and wash remaining photoresist
7. Deposition of Gold using **Physical Vapour Deposition**
8. Add photoresist coating and bake
9. Photolithography (Mask Aligment, **EUV exposure** and re-baking)
10. Wash exposed photoresist
11. **Chemical** etch of exposed gold using a **Potassium Iodine** (KI) etchant, **DO NOT WASH REMAINING PHOTORESIST**
12. Deposition of Silicon Dioxide using **Physical Vapour Deposition**
13. Lift-off of the remaining photoresist to expose Gold pads

![Schematization of the process described above for the manufacture of a MEA](image_sources/nanotec/process.jpg)

**Advantages:**

* Process only uses two masks (cost-effectiveness)
* Uses Chemical etching of gold and lift-off of Silicon Dioxide in order to not damage the layers beneath

**Problems:**

* Lift-off is traditionally less precise than etching
* Erosion of the gold pads laterals will probably occur during gold etching and the chemical etching of gold is mostly relying on gravity to etch excess gold under the gold pads

**Possible Solutions:**

* Alter gold-pad design (encircle laterals of Aluminium pad) to ease the need to etch excess gold under the gold pad , which has the trade-off of shortening the distance between vias, with the possibility to create parasite capacitances
* Deposite a Silicon Dioxide layer after setting the aluminium and instead use the protective photoresist from the SiO$_2$ lithography process to lift-off gold
* Use a more conventional three mask process

## Exercise 2 
### Part A
Using the formula for the natural frequency of a beam:

$f_{Si}=\frac{C_2}{2 \pi}\sqrt{\frac{I}{AL^4}}\sqrt{\frac{E}{\rho}}$

With the Inertia momentum formula and Area formula for a a beam of a square shaped section:

$I_{beam}=\frac{bh^3}{12}$
$A_{beam}=bh$

And combining with the material properties of Silicon and geometrical dimensions of the beam, and using $C_2$ for the cantliever beam:

$E_{Si}= 190 GPa$

$\rho _{Si}= 2330 kg/m^3$

$L= 1 \mu m$

$b= 100 nm$

$h= 50 nm$

$C_2= 3.52$

We can deduce:

$f_{Si}=\frac{3.52}{2 \pi}\sqrt{\frac{\frac{100n*(50n)^3}{12}}{100n*50n*(1 \mu)^4}}\sqrt{\frac{190G}{2330}}=72MHz$

And for a diamond beam with the same geometrical dimensions:

$E_{Diamond}= 1.2 TPa$

$\rho _{Diamond}= 3500 kg/m^3$

$f_{Diamond}=\frac{3.52}{2 \pi}\sqrt{\frac{\frac{100n*(50n)^3}{12}}{100n*50n*(1 \mu)^4}}\sqrt{\frac{1.2T}{3500}}=151MHz$

### Part B
The formula for the deflection of a cantliever beam due to a uniformly distributed load is:

$\delta= \frac{FL^3}{8EI}$

To determine the number of molecules of BSA absorbed and thereafter the force they apply on the cantliever beam:

$N_{BSA}=\frac{A_{Beam Surface}}{A_{BSA Molecule}}=\frac{b*h}{A_{BSA Molecule}}=\frac{100n * 1 \mu}{(4n)^2}=6250$

$F= N_{BSA}* g * m_{BSA}=6250 * 9.8 * 66.5k * 1.66*10^{-27}=6.76 aPa$

Therefore using the previously calculated Inertia momentum and Young modulus:

$\delta=\frac{6.76a*(1 \mu)^3}{8*190G*0.14q}=4.44 am$

### Part C
To determine the ressonance frequency shift from the BSA monolayer deposition on the cantliever we can use the following formula, and substitute with the previous calculations:

$\frac{f_0 ^2 - f_1 ^2}{f_0 ^2} \approx \frac{\delta m}{m} \Leftrightarrow f_1 \approx$

$\approx f_0 * \sqrt{1-\frac{m_{BSA monolayer}}{m_{beam}}} \Leftrightarrow f_1 \approx f_0 * \sqrt{1-\frac{m_{BSA monolayer}}{L* b * h * \rho_{Silicon}}}=69.768MHz$

### Part D
The micro-cantliever beam has geometrical properties:

$L= 100 \mu m$

$b=10 \mu m$

$h= 5 \mu m$

First to determine the natural frequency of the new beam we re-use the formula in A, adapted:

$f_{microSi}=\frac{3.52}{2 \pi}\sqrt{\frac{\frac{10 \mu *(50 \mu)^3}{12}}{10 \mu * 50 \mu *(100 \mu)^4}}\sqrt{\frac{190G}{2330}}=593.5MHz$


To determine the ressonance frequency shift from the BSA monolayer deposition on the new cantliever we can use the following formula, and substitute with the previous calculations:

$\frac{f_0 ^2 - f_1 ^2}{f_0 ^2} \approx \frac{\delta m}{m} \Leftrightarrow f_1 \approx$

$\approx f_0 * \sqrt{1-\frac{m_{BSA monolayer}}{m_{beam}}} \Leftrightarrow f_1 \approx f_0 * \sqrt{1-\frac{m_{BSA monolayer}}{L* b * h * \rho_{Silicon}}}=593.49MHz$

To determine the ressonance frequency shift from a single BSA molecule deposition on the new cantliever we can use the formula, and substitute with the previous calculations:

$\frac{f_0 ^2 - f_1 ^2}{f_0 ^2} \approx \frac{\delta m}{m} \Leftrightarrow f_1 \approx$

$\approx f_0 * \sqrt{1-\frac{m_{BSA molecule}}{m_{beam}}} \Leftrightarrow f_1 \approx f_0 * \sqrt{1-\frac{m_{BSA molecule}}{L * b * h * \rho_{Silicon}}}=593.5MHz$

As predicted at the micro-scale a solid state sensor based on the physical deformation of a beam is obsolete to detected the depostion of BSA proteins.



