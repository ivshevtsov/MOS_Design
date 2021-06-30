

unCox = 126e-6
lambda_n = 0.103
Vtn = 0.618

upCox = 49e-6
lambda_p = 0.061
Vtp = 0.601


Cox = 4e-3
L = 500e-9
Veff = 0.2
Idn = 50e-6
Idp = Idn/2

gm_p = 2*Idp/Veff
gm_n = 2*Idn/Veff

Wn = gm_n*L/(unCox*Veff)
Wp = gm_p*L/(upCox*Veff)

Av = 2*181e-6*100e3
print(307/(2*3.14))


print('Wn = ', Wn)
print('Wp = ', Wp)
print(1/181e-6)

