import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
from .helpers import check_optype, check_trtype

warnings.filterwarnings('ignore')

abb={'c': 'Call',
    'p': 'Put',
    'b': 'Long',
    's': 'Short'}

def single_plotter(op_type='c',spot=100, spot_range=10,strike=102,tr_type='b',op_pr=2, save=False, file='fig.png'):
    """
    Plots a basic option payoff diagram for a single option
    Parameters
    ----------
    op_type: kind {'c','p'}, default:'c'
       Opion type>> 'c': call option, 'p':put option 
    
    spot: int, float, default: 100 
       Spot Price
       
    spot_range: int, float, optional, default: 5
       Range of spot variation in percentage 
       
    strike: int, float, default: 102
       Strike Price
    
    tr_type: kind {'b', 's'} default:'b'
       Transaction Type>> 'b': long, 's': short

    op_pr: int, float, default: 10
    Option Price
    
    save: Boolean, default False
        Save figure
    
    file: String, default: 'fig.png'
        Filename with extension
    
    Example
    -------
    import opstrat as op
    op.single_plotter(op_type='p', spot_range=20, spot=1000, strike=950)
    #Plots option payoff diagram for put option with spot price=1000, strike price=950, range=+/-20%
    
    """

    
    op_type=str.lower(op_type)
    tr_type=str.lower(tr_type)
    check_optype(op_type)
    check_trtype(tr_type)
    
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
    y0=np.zeros_like(x)
    
    def plotter(x,y):
        plt.figure(figsize=(10,6))
        sns.lineplot(x=x, y=y)
        plt.axhline(color='k', linestyle='--')
        plt.axvline(x=spot, color='r', linestyle='--')
        title=str(abb[op_type])+' '+str(abb[tr_type])+'\n St price :'+str(strike)
        plt.fill_between(x, y, 0, alpha=0.2, where=y>y0, facecolor='green', interpolate=True)
        plt.fill_between(x, y, 0, alpha=0.2, where=y<y0, facecolor='red', interpolate=True)
        plt.title(title)
        plt.tight_layout()
        if save==True:
            plt.savefig(file)
        plt.show()
    
    plotter(x,y)