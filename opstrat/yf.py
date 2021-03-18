import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

abb={'c': 'Call',
    'p': 'Put',
    'b': 'Long',
    's': 'Short'}

def yf_plotter(ticker='msft',exp='default',spot_range=10,
               op_list=[{'op_type':'c','strike':250,'tr_type':'b'},
                        {'op_type':'p','strike':225,'tr_type':'b'}]):
    
    
    def check_ticker(ticker):
        """
        Check ticker
        """
        try:
            spot=yf.Ticker(ticker).info['bid']
        except KeyError:
            raise ValueError('Ticker not recognized')
     
    check_ticker(ticker)
    
    spot=yf.Ticker(ticker).info['bid']
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
    
    def check_optype(op_type):
        if (op_type not in ['p','c']):
            raise ValueError("Input 'p' for put and 'c' for call!")
    def check_trtype(tr_type):
        if (tr_type not in ['b','s']):
            raise ValueError("Input 'b' for Buy and 's' for Sell!")           
    def check_strike(df, strike):
        if strike not in df.strike.unique():
            raise ValueError('Option for the given Strike Price not available!')
    
    def payoff_calculator(op_type, strike, op_pr, tr_type):
        y=[]
        if op_type=='c':
            for i in range(len(x)):
                y.append(max((x[i]-strike-op_pr),-op_pr))
        else:
            for i in range(len(x)):
                y.append(max(strike-x[i]-op_pr,-op_pr))

        if tr_type=='s':
            y=-np.array(y)
        return y
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
        
        y_list.append(payoff_calculator(op_type, strike, op_pr, tr_type))
    

    def plotter():
        y=0
        plt.figure(figsize=(10,6))
        for i in range (len(op_list)):
            label=str(abb[op_list[i]['tr_type']])+' '+str(abb[op_list[i]['op_type']])+' ST: '+str(op_list[i]['strike'])
            sns.lineplot(x=x, y=y_list[i], label=label, alpha=0.5)
            y+=np.array(y_list[i])
        
        sns.lineplot(x=x, y=y, label='combined', alpha=1, color='k')
        plt.axhline(color='k', linestyle='--')
        plt.axvline(x=spot, color='r', linestyle='--', label='spot price')
        plt.legend()
        plt.legend(loc='upper right')
        title="OPTION STRATEGY ("+str.upper(ticker)+') '+' Exp :'+str(exp)
        plt.fill_between(x, y, 0, alpha=0.3, where=y>y0, facecolor='green', interpolate=True)
        plt.fill_between(x, y, 0, alpha=0.3, where=y<y0, facecolor='red', interpolate=True)
        plt.title(title)
        plt.tight_layout()
        plt.show()

    plotter()           