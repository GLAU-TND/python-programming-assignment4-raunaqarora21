d={
 "key": 3,
 "foo": {
 "a": 5,
 "bar": {
 "baz": 8
 }
 }
}
def apna_fun(dd, separator ='.', prefix =''): 
    return { prefix + separator + k if prefix else k : v 
            
             for kk, vv in dd.items() 
             for k, v in apna_fun(vv, separator, kk).items() 
             } if type(dd)==dict else { prefix : dd } 
              

print ( (apna_fun(d))) 


