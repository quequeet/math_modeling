from lec_3_my_model import earth_mass as em
from lec_3_my_model import gravity_constant as G
from lec_3_my_model import sigma_steff_bolc as sigma

g = 500 * G / 10**2
print(g)

x = em * G * sigma	
print(x)



