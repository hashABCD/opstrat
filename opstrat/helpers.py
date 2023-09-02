import yfinance as yf
import numpy as np
from datetime import datetime
from .blackscholes import black_scholes

def check_optype(op_type):
    if (op_type not in ['p','c','s']):
        raise ValueError("Input 'p' for put, 'c' for call, 's' for stock!")

def check_trtype(tr_type):
    if (tr_type not in ['b','s']):
        raise ValueError("Input 'b' for Buy and 's' for Sell!")  

def calculate_days_to_exp(exp_date_str):
    # Convert the future date string to a datetime object
    exp_date = datetime.strptime(exp_date_str, "%d-%b-%y")
        
    # Get today's date as a datetime object
    today_date = datetime.now()
        
    # Calculate the difference in days
    days_to_exp = (exp_date - today_date).days + 1
    
    return days_to_exp

def payoff_calculator(x, op_type, strike, op_pr, tr_type, n, days_to_expiration, r, v):
    y=[]
    
    # If Leg is a Stock - calculate payoff graph for a stock position
    if op_type=='s':
        for i in range(len(x)):
            y.append(x[i]-strike-op_pr)
            
    # If Leg is an Option and Future Expiration, - calculate value of option using Black Scholes Pricing Model
    elif days_to_expiration > 0:
        # Insert Code for Black Scholes Calculation for Option leg
        for i in range(len(x)):
            option_value= black_scholes(K=strike, St=x[i], r=r, t=days_to_expiration, v=v, type=op_type)['value']['option value']
            y.append(option_value-op_pr)
    
    # If Leg is an Option Leg and Expires Today - show expiration payoff leg
    else:
        if op_type=='c':
            for i in range(len(x)):
                y.append(max((x[i]-strike-op_pr),-op_pr))
        else:
            for i in range(len(x)):
                y.append(max(strike-x[i]-op_pr,-op_pr))
        
    y=np.array(y)

    # Invert Payoff Diagram if Option Leg Short Position
    if tr_type=='s':
        y=-y
        
    # Return Option Price List After Multiplying by Number of Contracts
    return y*n

def check_ticker(ticker):
    """
    Check ticker
    """
    try:
        return yf.Ticker('msft').info['currentPrice']
    except KeyError:
        raise ValueError('Ticker not recognized')