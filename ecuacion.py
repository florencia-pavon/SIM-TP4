import random
def runge_kutta():
    h = 0.1
    m = 0
    t = 0
    Mcorte = random.uniform(2000,20000)
    print(Mcorte)
        
    while m <= Mcorte:
        k1 = 3*t**2+0.5*m
        k2 = 3*(t+h/2)**2+0.5*(m+h/2*k1)
        k3 = 3*(t+h/2)**2+0.5*(m+h/2*k2)
        k4 = 3*(t+h)**2+0.5*(m+h*k3)
        vector_runge = [t, m, k1, k2, k3, k4]
        m = m + (h/6) *(k1+2*k2+2*k3+k4)
        t += h
        vector_runge.append(t)
        vector_runge.append(m)
        vector_runge = [round(elemento, 4) if isinstance(elemento, float) else elemento for elemento in vector_runge]
        print(vector_runge)
        
            
    return round((t/0.1/60),2)

tiempo_limpieza = runge_kutta()