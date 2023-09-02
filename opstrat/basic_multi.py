#multiplotter
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from .helpers import payoff_calculator, check_optype, check_trtype, calculate_days_to_exp

abb={'c': 'Call',
    'p': 'Put',
    'b': 'Long',
    's': 'Short'}

def multi_plotter(spot_range=20, spot=100,  
                op_list=[{'op_type':'c','strike':110,'tr_type':'s','op_pr':2,'contract':1},
                {'op_type':'p','strike':95,'tr_type':'s','op_pr':6,'contract':1,'exp_date':'01-Jan-2025'}], 
                  save=False, file='fig.png', v=20, r=5.3):
    """
    Plots a basic option payoff diagram for a multiple options and resultant payoff diagram
    
    Parameters
    ----------
    spot: int, float, default: 100 
       Spot Price
       
    spot_range: int, float, optional, default: 20
       Range of spot variation in percentage 
       
    op_list: list of dictionary
       
       Each dictionary must contiain following keys
       'strike': int, float, default: 720
           Strike Price
       'tr_type': kind {'b', 's'} default:'b'
          Transaction Type>> 'b': long, 's': short
       'op_pr': int, float, default: 10
          Option Price
       'op_type': kind {'c','p','s'}, default:'c'
          Opion type>> 'c': call option, 'p':put option, 's':stock
       'contracts': int default:1, optional
           Number of contracts
        'exp_date': str, default '01-Jan-2023'
            Expiration date for contract
    
    save: Boolean, default False
        Save figure
    
    file: String, default: 'fig.png'
        Filename with extension
        
    v: int, float, default 20%
        Option Volatility
    
    r: int, float, default 5.3
        Risk Free Rate
    Example
    -------
    op1={'op_type':'c','strike':110,'tr_type':'s','op_pr':2,'contract':1}
    op2={'op_type':'p','strike':95,'tr_type':'s','op_pr':6,'contract':1}
    
    import opstrat  as op
    op.multi_plotter(spot_range=20, spot=100, op_list=[op1,op2])
    
    #Plots option payoff diagrams for each op1 and op2 and combined payoff
    
    """
    x=spot*np.arange(100-spot_range,101+spot_range,0.01)/100
    y0=np.zeros_like(x)         
    
    y_list=[]
    for op in op_list:
        op_type=str.lower(op['op_type'])
        tr_type=str.lower(op['tr_type'])
        check_optype(op_type)
        check_trtype(tr_type)
        
        strike=op['strike']
        op_pr=op['op_pr']
        try:
            if op_type == 's':
                contract=op['contract']/100
            else:
                contract=op['contract']
            
        except:
            contract=1
        
        try:
            if op_type == 's':
                days_to_expiration = 0
            else:
                days_to_expiration = calculate_days_to_exp(op['exp_date'])
        except:
            days_to_expiration = 0 
            
        y_list.append(payoff_calculator(x, op_type, strike, op_pr, tr_type, contract, days_to_expiration, r, v))
    

    def plotter():
        y=0
        plt.figure(figsize=(10,6))
        for i in range (len(op_list)):
            try:
                contract=str(op_list[i]['contract'])  
            except:
                contract='1'
                
            label=contract+' '+str(abb[op_list[i]['tr_type']])+' '+str(abb[op_list[i]['op_type']])+' ST: '+str(op_list[i]['strike'])
            sns.lineplot(x=x, y=y_list[i], label=label, alpha=0.5)
            y+=np.array(y_list[i])
        
        sns.lineplot(x=x, y=y, label='combined', alpha=1, color='k')
        plt.axhline(color='k', linestyle='--')
        plt.axvline(x=spot, color='r', linestyle='--', label='spot price')
        plt.legend()
        plt.legend(loc='upper right')
        title="Multiple Options Plotter"
        plt.title(title)
        plt.fill_between(x, y, 0, alpha=0.2, where=y>y0, facecolor='green', interpolate=True)
        plt.fill_between(x, y, 0, alpha=0.2, where=y<y0, facecolor='red', interpolate=True)
        plt.tight_layout()
        if save==True:
            plt.savefig(file)
        plt.show()

    plotter()      