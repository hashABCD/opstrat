# opstrat

[![PyPI](https://img.shields.io/pypi/v/opstrat)](https://pypi.org/project/opstrat/)
[![PyPI - License](https://img.shields.io/pypi/l/opstrat)](https://pypi.org/project/opstrat/)
[![GitHub top language](https://img.shields.io/github/languages/top/abhijith-git/opstrat)](https://github.com/abhijith-git/opstrat)
[![GitHub Repo stars](https://img.shields.io/github/stars/abhijith-git/opstrat?style=social)](https://github.com/hashabcd/opstrat)
[![Twitter Follow](https://img.shields.io/twitter/follow/abhijith_abcd?style=social)](https://twitter.com/hashabcd)
[![Youtube](https://img.shields.io/youtube/views/EU3L4ziz3nk?style=social)](https://www.youtube.com/watch?v=EU3L4ziz3nk)

Python library for visualizing options.

## Requirements
pandas, numpy, matplotlib, seaborn, yfinance


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install opstrat.

```bash
pip install opstrat
```

## Usage

## Import opstrat

```python
import opstrat
```
## Version check
```python
op.__version__
```
If you are using an older version upgrade to the latest package using:
```bash
pip install opstrat --upgrade
```

# 1. single_plotter()
Used for plotting payoff diagram involving multiple options.

Parameters
---
op_type: kind {'c','p'}, default:'c'<br>
   &emsp; Opion type>> 'c': call option, 'p':put option 

spot: int, float, default: 100<br>
   &emsp;Spot Price
   
spot_range: int, float, optional, default: 5<br>
   &emsp;Range of spot variation in percentage 
   
strike: int, float, default: 102<br>
   &emsp;Strike Price

tr_type: kind {'b', 's'} default:'b'<br>
   &emsp;Transaction Type>> 'b': long, 's': short

op_pr: int, float, default: 10<br>
    &emsp;Option Price

### 1.a Default plot

Option type : Call<br>
Spot Price : 100<br>
Spot range : +/- 5% <br>
Strike price: 102 <br>
Position : Long<br>
Option Premium: 10 <br>
```python
op.single_plotter()
```
![png](https://raw.githubusercontent.com/abhijith-git/opstrat/main/readme_files/fig1.png)

Green : Profit<br>Red : Loss

### 1.b Input parameters 
Strike Price : 450<br>
Spot price : 460<br>
Option type : Put Option<br> 
Position : Short<br>
Option Premium : 12.5<br>

```python
op.single_plotter(spot=460, strike=460, op_type='p', tr_type='s', op_pr=12.5)
```
![png](https://raw.githubusercontent.com/abhijith-git/opstrat/main/readme_files/fig2.png)

# 2. multi_plotter()

Used for plotting a single option <br>
Parameters
----------
spot: int, float, default: 100<br>&emsp; 
   Spot Price
   
spot_range: int, float, optional, default: 20<br>&emsp; 
   Range of spot variation in percentage 
   
op_list: list of dictionary<br>    
   &emsp;Each dictionary must contiain following keys:
   <br>&emsp; 'strike': int, float, default: 720
       <br>&emsp;&emsp;Strike Price
   <br>&emsp; 'tr_type': kind {'b', 's'} default:'b'
      <br>&emsp;&emsp;Transaction Type>> 'b': long, 's': short
   <br>&emsp; 'op_pr': int, float, default: 10
      <br>&emsp;&emsp;Option Price
   <br>&emsp; 'op_type': kind {'c','p'}, default:'c'
      <br>&emsp;&emsp;Opion type>> 'c': call option, 'p':put option 

### 2.a Default plot : The short strangle 

Options trading that involve: <br>&emsp;(a)selling of a slightly out-of-the-money put and <br>&emsp;(b)a slightly out-of-the-money call of the same underlying stock and expiration date. 
<br>spot_range=+/-20%
<br>    spot=100<br>
    <br>Option 1:Short call at strike price 110<br>&emsp;op_type: 'c','strike': 110 'tr_type': 's', 'op_pr': 2
    <br> Option 2 : Short put at strike price 95<br>&emsp;'op_type': 'p', 'strike': 95, 'tr_type': 's', 'op_pr': 6
    
```python
op.multi_plotter()
```
![png](https://raw.githubusercontent.com/abhijith-git/opstrat/main/readme_files/fig3.png)

### 2.b Example: Iron Condor (Option strategy with 4 options)

An iron condor is an options strategy consisting of two puts (one long and one short) and two calls (one long and one short), and four strike prices, all with the same expiration date. 

stock currently trading at 212.26 (Spot Price)<br>

Option 1: Sell a call with a 215 strike, which gives 7.63 in premium<br>
Option 2: Buy a call with a strike of 220, which costs 5.35. <br>
Option 3: Sell a put with a strike of 210 with premium received 7.20<br>
Option 4: Buy a put with a strike of 205 costing 5.52. 

```python
op1={'op_type': 'c', 'strike': 215, 'tr_type': 's', 'op_pr': 7.63}
op2={'op_type': 'c', 'strike': 220, 'tr_type': 'b', 'op_pr': 5.35}
op3={'op_type': 'p', 'strike': 210, 'tr_type': 's', 'op_pr': 7.20}
op4={'op_type': 'p', 'strike': 205, 'tr_type': 'b', 'op_pr': 5.52}

op_list=[op1, op2, op3, op4]
op.multi_plotter(spot=212.26,spot_range=10, op_list=op_list)
```
![png](https://raw.githubusercontent.com/abhijith-git/opstrat/main/readme_files/fig4.png)

# 3. yf_plotter()

Parameters
----------
ticker: string, default: 'msft' stock ticker for Microsoft.Inc<br>
&emsp;   Stock Ticker<br>
exp: string default: next option expiration date<br>
&emsp;    Option expiration date in 'YYYY-MM-DD' format<br>
   
spot_range: int, float, optional, default: 10<br>
&emsp;   Range of spot variation in percentage <br>
   
op_list: list of dictionary<br>
   
&emsp;   Each dictionary must contiain following keys<br>
&emsp;   'strike': int, float, default: 720<br>
&emsp;&emsp;       Strike Price<br>
&emsp;   'tr_type': kind {'b', 's'} default:'b'<br>
&emsp;&emsp;      Transaction Type>> 'b': long, 's': short<br>
&emsp;   'op_type': kind {'c','p'}, default:'c'<br>
&emsp;&emsp;      Opion type>> 'c': call option, 'p':put option<br> 

### 3.a Default plot

<b>Strangle on Microsoft stock</b><br>
Stock ticker : msft(Microsoft Inc.)<br> &emsp;
Option 1: Buy Call at Strike Price 250<br>&emsp;
Option 2: Buy Put option at Strike price 225

```python
op.yf_plotter()
```
![png](https://raw.githubusercontent.com/abhijith-git/opstrat/main/readme_files/fig5.png)

### 3.b Example: Strangle on Amazon 

Strangle:<br>
A simultaneous purchase of options to buy and to sell a security or commodity at a fixed price, allowing the purchaser to make a profit whether the price of the security or commodity goes up or down.

Stock ticker : AMZN(Amazon Inc.)<br> &emsp;
Option 1: Buy Call at Strike Price 3070<br>&emsp;
Option 2: Buy Put option at Strike price 3070

```python
op_1={'op_type': 'c', 'strike':3070, 'tr_type': 'b'}
op_2={'op_type': 'p', 'strike':3070, 'tr_type': 'b'}
op.yf_plotter(ticker='amzn', 
              exp='default', 
              op_list=[op_1, op_2])
```
![png](https://raw.githubusercontent.com/abhijith-git/opstrat/main/readme_files/fig6.png)

## 4. Save figure

Figure can be saved in the current directory setting <i>save=True</i><br>
Filename with extension has to be provided as <i>file</i>.<br>
If no filename is provided, the figure will be saved as fig in png format.
```python
op.single_plotter(save=True,file='simple_option.jpeg')
```
![png](https://raw.githubusercontent.com/abhijith-git/opstrat/main/readme_files/simple_option.jpeg)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Content License
[MIT](https://choosealicense.com/licenses/mit/)

### Thanks to 
[Stackoverflow Community](https://stackoverflow.com/)<br>
[Ran Aroussi](https://github.com/ranaroussi) : [yfinance](https://pypi.org/project/yfinance/)<br> 
[Daniel Goldfarb](https://github.com/DanielGoldfarb) : [mplfinance](https://pypi.org/project/mplfinance/)


### Tutorial in Video Format
[![Watch the video](https://img.youtube.com/vi/EU3L4ziz3nk/maxresdefault.jpg)](https://youtu.be/EU3L4ziz3nk)
