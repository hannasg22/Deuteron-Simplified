# Simplified model for the deuteron

## Goal of the code :white_check_mark:

Briefly explained, this code is provided to solve specifically the most simplified case of the deuteron equation(s) and get its eigenfunction and eigenvalue.

In order to find the results, a particular model for the potential of the interaction is implemented. However, another option could be applied making use of the user's preferred election! :smile: Also, the process could be adjusted to another similar system for which the eigenfunction and eigenvalue want to be reached.

## Theory :books:

With the aim of better understanding what it is done in this project, let us introduce the main theoretical concepts.

### Main idea

The deuteron is the **only bound state of two nucleons** and its bound is weak, therefore it only exists in the ground state. It is formed by one proton and one neutron and the nuclear force between them has the next properties: attractive (to form the bound state), short range (of order of $\sim 1fm$ ) and non-central (so it has a tensor component). 

All these assumptions have been made through the obtained experimental data. Furthermore, the potential describing the interaction between both particles has been contructed more precisely to fit the actual results. It can be widely analysed and it will show many different components. We instead will focus just on the **main quantity**, avoiding the tentsorial part and other constituents. We will then have:
- Central potential $V_C$

This can also be described by different models. One option, the one we will use, is defining it through a **square well potential**:

$$ V(r < r_0)=-V_0, \hspace{0.5cm} V(r \geq r_0)=0.
$$

where $V_0$ and $r_0$ are determined again from experimental data. This will be the exact form of the central potential component $V_C$.

Now, let us derive the form of the Hamiltonian using deuteron's properties. The deuteron has total isospin $T=0$ and spin parity $J^{\pi}=1^+$. Since the spin of both proton and neutron is $s_n=s_p=1/2$, the total spin could in principle be $S=1,0$. Apart from that, in analogy with the Hydrogen atom, it is reasonable to assume that the ground state of the deuteron also has zero orbital angular momentum, so: $L=0$. At this point, due to the asymmetry of the whole wavefunction in a system of two fermions, we have $S=1$ for the total spin.

These results lead us from the total Hamiltonian

$$ H=-\frac{\hbar^2}{2M}\frac{d^2}{dr^2}r+\frac{\hbar^2}{M}\frac{L(L+1)}{r^2}+V_C(r)
$$

to the simplified Schrödinger equation for the deuteron:

$$ -\frac{\hbar^2}{2M}\frac{d^2u_S}{dr^2}r+V_C(r)u_s(r)=Eu_S(r)
$$

This is the equation that the code will solve! Therefore, we will **get the deuteron's wavefunction $u_S$ and energy** (by experimental data we know it is: **$E=-2.225 MeV$**, which is the same as its binding energy but with a negative sign).

### Further information

As already said, this is actually the most simple model for this system. In fact, the potential would have a tensorial part, which generates a mixture between the eigenfunction $u_S$ for the s-wave ($L=0$) and $u_D$ for the d-wave ($L=2$). This could be the next step to improve this code!

## How to get the results :gear:

To use this code properly, the next steps must be followed:
1. Be sure that all libraries needed are installed. For this process the next Python libraries are required:
  - [NumPy](https://numpy.org/install/)
  - [SciPy](https://scipy.org/install/)
  - [Matplotlib](https://matplotlib.org/stable/install/index.html)
  - [JSONLines](https://jsonlines.readthedocs.io)
  - [Seaborn](https://seaborn.pydata.org/installing.html)
2. Check that all the data we want to implement for the deuteron is correct in [generate_data](generate_data.py). :red_circle: In case that any change is made, please run that file so that the new values will be saved in [values_deuteron](values_deuteron.jsonl) and the code will use those new components.
3. If the potential model wants to be changed, look at the file [potential](potential.py) and modify carefully the function. If not, just continue to step 4.
4. We run the [run](run.py) main file and we get the desired eigenfunction $u_s$ and eigenvalue $E$ for deuteron plotted along a specified range of r! :clap:

If the values and models are correctly applied, the execution will show a plot like this:

<img src="images/plot.png" alt="Plot obtained with the actual code." width="600">


## Structure of the project :card_index_dividers:
The code is divided in the next files:
- In [generate_data](generate_data.py) we insert the data we want to apply in the potential and the initial and boundary conditions. This will generate a data file called [values_deuteron](values_deuteron.jsonl) in JSON lines format and it will allow us to read the data and work with it on an easy way.
- In [get_values](get_values.py) we extract the data saved in [values_deuteron](values_deuteron.jsonl) to later insert it straightfordwardly in the rest of the files.
- In [potential](potential.py) we have the function defining the potential which will be put to model the deuteron interaction. This is my simplified implementation, but it could be replaced by the user's choice taking care of the form of the function, the inputs, outputs and the dimension of the parameters to be performed.
- In [schro_equation](schro_equation.py) we express the second order differential equation in a system of two first order differential equations through the function **rad_equation**. This system of 1st order ODEs can be solved with many methods from _scipy.integrate_. 
- In [find_energy](find_energy.py) we take the just explained **rad_equation** function and insert it in the _solve_ivp_ SciPy method. After that, we compare the obtained eigenfunction's value in the last point of the radius and the actual boundary condition we are looking for. By doing so, we get the difference between those two values as the output of the **error_E** function defined in this file.
- In [run](run.py) we finally take the **error_E** function and apply it to a root finding process to obtain the energy value actually obeying the boundary condition. In this case the chosen method is called 'secant', which is defined inside the _root_scalar_ function of SciPy. After getting the proper eigenvalue, we can solve again our system described in [schro_equation](schro_equation.py) but this time with the correct E value. At this point, the code will just show the obtained result for the energy and the eigenfunction in a plot. We achieved the final result!
- In [tests](tests.py) we test that each function of each file of the project works as it should and has the expected outputs.

