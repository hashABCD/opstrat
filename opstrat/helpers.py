import numpy as np
import yfinance as yf


def check_optype(op_type):
    if (op_type not in ['p','c', 'bc', 'bp']):
        raise ValueError("Input 'p' for put and 'c' for call, or 'bc'/'bp' for binaries!")

def check_trtype(tr_type):
    if (tr_type not in ['b','s']):
        raise ValueError("Input 'b' for Buy and 's' for Sell!")  

def payoff_calculator(x, op_type, strike, op_pr, tr_type, n):
    y=[]
    if op_type=='c':
        for i in range(len(x)):
            y.append(max((x[i]-strike-op_pr),-op_pr))
    elif op_type=='p':
        for i in range(len(x)):
            y.append(max(strike-x[i]-op_pr,-op_pr))
    elif op_type=='bc':
        for i in range(len(x)):
            y.append(1-op_pr if x[i] > strike else 0-op_pr)
    elif op_type=='bp':
        for i in range(len(x)):
            y.append(1-op_pr if strike > x[i] else 0-op_pr)


    y=np.array(y)

    if tr_type=='s':
        y=-y
    return y*n

def check_ticker(ticker):
    """
    Check ticker
    """
    try:
        return yf.Ticker('msft').info['currentPrice']
    except KeyError:
        raise ValueError('Ticker not recognized')