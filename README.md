# Simplified model for the deuteron

## Goal of the code :white_check_mark:

Bfriefly explained, this code is provided to solve specifically the most simplified case of the deuteron equation(s) and get its eigenfunction and eigenvalue.

In order to find the results, a particular model for the potential is implemented. But another option could be applied, making use of the user's preferred election! :smile:

## Theory :books:

With the aim of better understanding what it is done in this code, let us introduce the main theoretical concepts.

### Main idea

The deuteron is the **only bound state of two nucleons** and its bound is weak, therefore it only exists in the ground state. It is formed by one proton and one neutron and the nuclear force between them has the next properties (the most important ones for the goal of this project): attractive (to form the bound state), short range (of order of $\sim 1fm$ ) and non-central (so it has a tensor component). 

All these assumptions have been made through the obtained experimental data. Furthermore, the potential describing the interaction between both particles has been contructed more precisely to fit the actual results. It can be widely analysed and it will show many different components. We instead will focus just on the **main quantity**, avoiding the tentsorial part:
- Central potential $V_C$

This can also be described by different models. One option, the one we will use, is defining it through a **square well potential**:

$$ V(r < r_0)=-V_0, \hspace{0.5cm} V(r \geq r_0)=0.
$$

where $V_0$ and $r_0$ are defined again from experimental data. This will be the exact form of the central potential component $V_C$.

Now, let us derive the form of the Hamiltonian using deuteron's properties. The deuteron has total isospin $T=0$ and spin parity $J^{\pi}=1^+$. Since the spin of both proton and neutron is $s_n=s_p=1/2$, the total spin could in principle be $S=1,0$. Apart from that, in analogy with the Hydrogen atom, it is reasonable to assume that the ground state of the deuteron also has zero orbital angular momentum, so: $L=0$. At this point, due to the asymmetry of the whole wavefunction in a system of two fermions, we have $S=1$ for the total spin.

These results lead us from the total Hamiltonian

$$ H=-\frac{\hbar^2}{2M}\frac{d^2}{dr^2}r+\frac{\hbar^2}{M}\frac{L(L+1)}{r^2}+V_C(r)
$$

to the Schrödinger equation for the deuteron:

$$ -\frac{\hbar^2}{2M}\frac{d^2u_S}{dr^2}r+V_C(r)u_s(r)=Eu_S(r)
$$

This is the equation that this code will solve! So, we will **get the deuteron's wavefunction $u_S$ and energy** (by experimental data we know it is: **$E=-2.225 MeV$**, which is the same as its binding energy but with a negative value).

### Further information

As already said, this is actually the most simplified model for the deuteron. In fact, the potential would have a tensorial part, which generates a mixture between the eigenfunction $u_S$ for the s-wave ($L=0$) and $u_D$ for the d-wave ($L=2$). This could be the next step for this code!

## How to get the results :gear:

## Structure of the project :card_index_dividers:
The code is divided in the next files:
- In [generate_data.py](generate_data.py) we insert the data we want to apply for the potential and for the initial and boundary conditions. This will generate a data file called [values_deuteron.jsonl](values_deuteron.jsonl) in JSON lines format and it will allow us to read the data and work with it on an easy way.
- In [get_values.py](get_values.py) we extract the data saved in [values_deuteron.jsonl](values_deuteron.jsonl) to later insert it easily in the rest of the code.
- In [potential.py](potential.py) we have the function defining the potential which will be applied to model the deuteron interaction. This is my simplified implementation, but it could be replaced by the user's choice taking care of the form of the function, the inputs, outputs and the dimension of the parameters to be implemented.
- In [schro_equation.py](schro_equation.py) we express the system of equations we want to solve through the function **rad_equation**.
- In [find_energy.py](find_energy.py) we take the just explained **rad_equation** function and insert it in the _solve_ivp_ SciPy method. After that, we compare the obtained eigenfunction's value in the last point of the radius and the actual boundary condition we look for. By doing so, we get the difference between those two values as the output of the **error_E** function defined in this file.
- In [run.py](run.py) we finally take the **error_E** function and apply it to a root finding method to obtain the energy value obeying the boundary condition. In this case the chosen method is called 'secant', which is defined inside the _root_scalar_ function of SciPy. After getting the proper eigenvalue, we can solve again our system described in [schro_equation.py](schro_equation.py) but this time with the correct E value. At this point, the code will just show the obtained result for the energy and the eigenfunction in a plot.
- In [tests.py](tests.py) we test that each function of each file of the code works as it should and has the expected outputs.

