def _delta(a, b, c):
    return b * b - 4 * a * c 

    
def quadratic(a, b, c): 
    
    delta = _delta(a, b, c)
    sqrt_val = (abs(delta)) **.5
    if delta > 0: 
        print(" two real root ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif delta == 0: 
        print(" one real root") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print("no real root") 
