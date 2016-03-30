import json,requests
import numpy as np

# Gets SPICE-formated orbital elements from MPC database
#
# desig: MPC number if available, or provisional designation otherwise
# mag: if true, also return absolute magnitude

def get_mpc_elements(desig,mag=False):

    url = 'http://mpc.cfa.harvard.edu/ws/search'
    auth = ('mpc_ws','mpc!!ws')
    d2r = np.pi/180.
    AU = 149597870.7
    day = 24.*3600.
    year = 365.25*day

    # MPC wants numbers to be zero-padded to length 7
    try: desig = '{:07.0f}'.format(int(desig))
    except: pass
    rele='period,semimajor_axis,eccentricity,inclination,argument_of_perihelion,ascending_node,mean_anomaly,epoch_jd,absolute_magnitude'
    params = {'return':rele,'designation':desig,'json':'1'}
    r = json.loads(requests.post(url,params,auth=auth).text)
    if len(r)==0: return None

    T = float(r[0]['period'])
    a = float(r[0]['semimajor_axis'])*AU
    e = float(r[0]['eccentricity'])
    i = float(r[0]['inclination'])*d2r
    O = float(r[0]['ascending_node'])*d2r
    w = float(r[0]['argument_of_perihelion'])*d2r
    M = float(r[0]['mean_anomaly'])*d2r
    jd = float(r[0]['epoch_jd'])
    try: H = float(r[0]['absolute_magnitude'])
    except: H = None
    n = 2.*np.pi/(T*year)
    mu = n**2 * a**3
    rp = a*(1.-e)
    et = (jd-2451544.99925710)*day # Approximate; ignores leap seconds
    ele = np.array([rp,e,i,O,w,M,et,mu])

    if mag: return ele,H
    else: return ele

if __name__=='__main__':

    import argparse
    parser = argparse.ArgumentParser(description='Get an MPC orbit in JPL NAIF SPICE format.')
    parser.add_argument('designation', type=str, help='MPC number or quoted provisional designation')
    parser.add_argument('--mag', action='store_true', help='also output absolute magnitude')
    args = parser.parse_args()

    if args.mag:
        ele,H = get_mpc_elements(args.designation,True)
        print(ele)
        print(H)
    else:
        print(get_mpc_elements(args.designation,False))
