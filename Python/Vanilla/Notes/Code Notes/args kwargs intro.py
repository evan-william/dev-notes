def f(*args, **kwargs): #args= arguments, kwargs=keywordarguments (PLACEHOLDER)
    print("Positional:", args)
    print("Named:", kwargs)
    
f(100, 50, 25, 5) # Work even if its 4 beacause use args
f(galleons=100, sickles=50, knuts=25)