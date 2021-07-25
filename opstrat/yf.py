import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

from helpers import check_ticker, check_optype, check_trtype, payoff_calculator

import warnings
warnings.filterwarnings('ignore')


abb={'c': 'Call',
    'p': 'Put',
    'b': 'Long',
    's': 'Short'}

def yf_plotter(ticker='msft',exp='default',spot_range=10,
               op_list=[{'op_type':'c','strike':250,'tr_type':'b', 'contract':1},
                        {'op_type':'p','strike':225,'tr_type':'b', 'contract':1}], 
                        save=False, file='fig.png'):
    """
    Plots a basic option payoff diagram for a multiple options and resultant payoff diagram
    
    Parameters
    ----------
    ticker: string, default: 'msft' stock ticker for Microsoft.Inc
       Stock Ticker
    exp: string default: next option expiration date
        Option expiration date in 'YYYY-MM-DD' format
       
    spot_range: int, float, optional, default: 10
       Range of spot variation in percentage 
       
    op_list: list of dictionary
       
       Each dictionary must contiain following keys
       'strike': int, float, default: 720
           Strike Price
       'tr_type': kind {'b', 's'} default:'b'
          Transaction Type>> 'b': long, 's': short
       'op_type': kind {'c','p'}, default:'c'
          Opion type>> 'c': call option, 'p':put option 
       'contracts': int default:1, optional
          Number of contracts
    
    save: Boolean, default False
        Save figure
    
    file: String, default: 'fig.png'
        Filename with extension
    
    Example
    -------
    op1={'op_type':'c','strike':250,'tr_type':'b', 'contract':1}
    op2={'op_type':'p','strike':225,'tr_type':'b','contract':3}
    
    import opstrat as op
    op.yf_plotter(ticker='msft',exp='2021-03-26',spot_range=10, op_list=[op1,op2])
    
    #Plots option payoff diagrams for each op1 and op2 and combined payoff 
    
    """
    #Check input and assigns spot price
    spot=check_ticker(ticker)
    #Expiry dates
    exp_list=yf.Ticker(ticker).options
    
    x=spot*np.arange(100-spot_range,101+spot_range,0.01)/100
    y0=np.zeros_like(x)

    
    def check_exp(exp):
        """
        Check expiry date
        """
        if exp not in exp_list:
            raise ValueError('Option for the given date not available!')
    
    if exp=='default':
        exp=yf.Ticker('msft').options[0]
    else:
        check_exp(exp)
               
    def check_strike(df, strike):
        if strike not in df.strike.unique():
            raise ValueError('Option for the given Strike Price not available!')
    
    y_list=[]
    
    for op in op_list:
        op_type=str.lower(op['op_type'])
        tr_type=str.lower(op['tr_type'])
        
        check_optype(op_type)
        check_trtype(tr_type)
    
        if(op_type=='p'):
            df=yf.Ticker(ticker).option_chain(exp).puts
        else:
            df=yf.Ticker(ticker).option_chain(exp).calls
    
        strike=op['strike']
        check_strike(df, strike)
        op_pr=df[df.strike==strike].lastPrice.sum()
        try:
            contract=op['contract']
            print('Setting contract =', contract)
        except:
            contract=1
            print('default')
        
        y_list.append(payoff_calculator(x, op_type, strike, op_pr, tr_type, contract))
    

    def plotter():
        y=0
        plt.figure(figsize=(10,6))
        for i in range (len(op_list)):
            try:
                contract=str(op_list[i]['contract'])  
            except:
                contract='1'
                
            label=contract+' '+str(abb[op_list[i]['tr_type']])+' '+str(abb[op_list[i]['op_type']])+' ST: '+str(op_list[i]['strike'])
            print(label)
            print(len(x))
            print(len(y_list[i]))
            sns.lineplot(x=x, y=y_list[i], label=label, alpha=0.5)
            y+=np.array(y_list[i])
        
        sns.lineplot(x=x, y=y, label='combined', alpha=1, color='k')
        plt.axhline(color='k', linestyle='--')
        plt.axvline(x=spot, color='r', linestyle='--', label='spot price')
        plt.legend()
        plt.legend(loc='upper right')
        title="OPTION STRATEGY ("+str.upper(ticker)+') '+' Exp :'+str(exp)
        plt.fill_between(x, y, 0, alpha=0.2, where=y>y0, facecolor='green', interpolate=True)
        plt.fill_between(x, y, 0, alpha=0.2, where=y<y0, facecolor='red', interpolate=True)
        plt.title(title)
        plt.tight_layout()
        if save==True:
            plt.savefig(file)
        plt.show()

    plotter()           