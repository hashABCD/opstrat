import numpy as np
from scipy.stats import norm


def black_scholes(t=40, r=4.80, v=32.00, K=60, St=62, type='c'):
    """
    Parameters:
    K : Strike Price
    St: Current Stock Price
    v : Volatility in percentage
    r : Risk free rate in percentage
    t : Time to expiration in days
    type: Type of option 'c' for call 'p' for put
    default: 'c'
    """
    # if type = 'c' or 'C' call option else put option
    try:
        type=type.lower()
        if(type=='c'):
            option_type='call'
        else:
            option_type='put'
    except:
        option_type='put'

    #Check time 
    try:
        #convert time in days to years
        t=t/365
    except:
        raise TypeError("Enter numerical value for time")

    #Check risk free rate 
    try:
        #convert percentage to decimal
        r=r/100
    except:
        raise TypeError("Enter numerical value for risk free rate")
    
    #Check volatility
    try:
        #convert percentage to decimal
        v=v/100
    except:
        raise TypeError("Enter numerical value for volatility")  

    #Check Stock Price
    try:
        St=St+0
    except:
        raise TypeError("Enter numerical value for stock price")
    
    #Check Exercise Price
    try:
        K=K+0
    except:
        raise TypeError("Enter numerical value for Exercise price")    
    
    n1=np.log(St/K)
    n2=(r+(np.power(v,2)/2))*t
    d=v*(np.sqrt(t))

    d1=(n1+n2)/d
    d2=d1-(v*np.sqrt(t))

    if type=='c':
        N_d1=norm.cdf(d1)
        N_d2=norm.cdf(d2)
    else:
        N_d1=norm.cdf(-d1)
        N_d2=norm.cdf(-d2)

    A=(St*N_d1)
    B=(K*N_d2*(np.exp(-r*t)))

    if type=='c':
        val=A-B
        val_int=max(0,St-K)
    else:
        val=B-A
        val_int=max(0,K-St)
    val_time=val-val_int

    # Option values in dictionary
    value={'option value':val, 'intrinsic value':val_int, 'time value':val_time}

    #CALCULATE OPTION GREEKS
    if type=='c':
        delta=N_d1
        theta=(-((St*v*np.exp(-np.power(d1,2)/2))/(np.sqrt(8*np.pi*t)))-(N_d2*r*K*np.exp(-r*t)))/365
        rho=t*K*N_d2*np.exp(-r*t)/100
    else:
        delta=-N_d1
        theta=(-((St*v*np.exp(-np.power(d1,2)/2))/(np.sqrt(8*np.pi*t)))+(N_d2*r*K*np.exp(-r*t)))/365
        rho=-t*K*N_d2*np.exp(-r*t)/100

    gamma=(np.exp(-np.power(d1,2)/2))/(St*v*np.sqrt(2*np.pi*t))
    vega=(St*np.sqrt(t)*np.exp(-np.power(d1,2)/2))/(np.sqrt(2*np.pi)*100)
    
    #Option greeks in Dictionary
    greeks={'delta':delta, 'gamma':gamma, 'theta':theta, 'vega':vega, 'rho':rho}

    return {'value':value, 'greeks':greeks}