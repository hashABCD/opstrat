import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 

warnings.filterwarnings('ignore')

abb={'c': 'Call',
    'p': 'Put',
    'b': 'Long',
    's': 'Short'}

def option_plotter(op_type='c',spot=725, spot_range=5,strike=720,tr_type='b',op_pr=10):

    
    op_type=str.lower(op_type)
    tr_type=str.lower(tr_type)
    

    def check_inputs():
        """
        Check inputs are proper
        """
        if op_type not in ['p','c']:
            raise ValueError("Input 'p' for put and 'c' for call!")
        if tr_type not in ['b','s']:
            raise ValueError("Input 'b' for Buy and 's' for Sell!")
    
    check_inputs()
    
    def payoff_calculator():
        x=spot*np.arange(100-spot_range,101+spot_range,0.01)/100

        y=[]
        if str.lower(op_type)=='c':
            for i in range(len(x)):
                y.append(max((x[i]-strike-op_pr),-op_pr))
        else:
            for i in range(len(x)):
                y.append(max(strike-x[i]-op_pr,-op_pr))

        if str.lower(tr_type)=='s':
            y=-np.array(y)
        return x,y
        
    x,y=payoff_calculator()
    
    def plotter(x,y):
        sns.lineplot(x=x, y=y)
        plt.axhline(color='k', linestyle='--')
        plt.axvline(x=spot, color='r', linestyle='--')
        title=str(abb[op_type])+' '+str(abb[tr_type])+'\n St price :'+str(strike)
        plt.title(title)
        plt.tight_layout()
        plt.show()
    
    plotter(x,y)
    
option_plotter()