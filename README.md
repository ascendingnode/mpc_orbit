# mpc_orbit

A simple python function for grabbing orbital elements from the MPC database and formating them in JPL NAIF SPICE format (J2000 ecliptic frame).

```python
from mpc_orbit import get_mpc_elements
ele,H = get_mpc_elements("2014 MU69",True)
```

Can also be used directly on the command line:

```shell
python mpc_orbit.py "2014 MU69" --mag
```
