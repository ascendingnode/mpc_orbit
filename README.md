# mpc_orbit

A simple python function for grabbing orbital elements from the MPC database and formating them in JPL NAIF SPICE format (J2000 ecliptic frame).

```python
from mpc_orbit import get_mpc_elements

ele1,H1 = get_mpc_elements("2014 MU69",True)
ele2 = get_mpc_elements(50000)
```

Can also be used directly on the command line:

```shell
python mpc_orbit.py "2014 MU69" --mag
python mpc_orbit.py 50000
```
