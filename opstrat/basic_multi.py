#basic_multi
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

abb={'c': 'Call',
    'p': 'Put',
    'b': 'Long',
    's': 'Short'}

def option_plotter(spot_range=20, spot=100,
                op_list=[{'op_type':'c','strike':110,'tr_type':'s','op_pr':2},
                {'op_type':'p','strike':95,'tr_type':'s','op_pr':6}]):
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
       'op_type': kind {'c','p'}, default:'c'
          Opion type>> 'c': call option, 'p':put option 
    
    Example
    -------
    op1={'op_type':'c','strike':110,'tr_type':'s','op_pr':2}
    op2={'op_type':'p','strike':95,'tr_type':'s','op_pr':6}
    
    from opstrat.basic_multi import option_plotter
    option_plotter(spot_range=20, spot=100, op_list=[op1,op2])
    
    #Plots option payoff diagrams for each op1 and op2 and combined payoff
    
    """
    x=spot*np.arange(100-spot_range,101+spot_range,0.01)/100
    
    def check_optype(op_type):
        if (op_type not in ['p','c']):
            raise ValueError("Input 'p' for put and 'c' for call!")
    def check_trtype(tr_type):
        if (tr_type not in ['b','s']):
            raise ValueError("Input 'b' for Buy and 's' for Sell!")           
    
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
        
        strike=op['strike']
        op_pr=op['op_pr']
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
        title="Multiple Options Plotter"
        plt.title(title)
        plt.tight_layout()
        plt.show()

    plotter()      