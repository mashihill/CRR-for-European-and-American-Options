Financial Computing HW2 
=======================
R03246004 陳彥安

--------------------------------------------------
## Environment:
1. python 2.7.9
2. package (module) needed:
    - numpy (1.9.2) 
    - scipy (0.15.1)

## Code Explanation

**Inputs**: 
- `S` : Stock price at time = 0,
- `X` : Strike price
- `s` : Annual volatility in percentage
- `t` : Maturity in years
- `n` : Number of periods
- `r` : Interest rate in percentage

**Outputs**:
- Price of European call and put.
- Price of American call and put.

## How To Run (example):
 - **Entering parameter's value in a file**

Open file `./data` and enter (modify) input values in JSON format

```json
[
    {
        "S": 100,
        "X": 95,
        "s": 25,
        "t": 1,
        "n": 300,
        "r": 3
    }
]
```

It is possible to add multiple test data like:

```json
[
    {
        "S": 100,
        "X": 95,
        "s": 25,
        "t": 1,
        "n": 300,
        "r": 3
    },
    {
        "S": 90,
        "X": 95,
        "s": 40,
        "t": 3,
        "n": 1200,
        "r": 5
    },
    {
        "S": 80,
        "X": 95,
        "s": 50,
        "t": 0.5,
        "n": 200,
        "r": 4
    }
]
```

 - **Execute the program**
Use the command: 
`python <HW2.py|HW2.pyc> <data location>`. 
For example:

```bash
$ python HW2.py ./data
S=100, X=95, s=25%, t=1, n=300, r=3%:
- European Call:   13.9640269239
- European Put :    6.15635261102
- American Call:   13.9640269239
- American Put :    6.3439865473
S=90, X=95, s=40%, t=3, n=1200, r=5%:
- European Call:   27.6049797818
- European Put :   19.3722375422
- American Call:   27.6049797818
- American Put :   21.5349009726
S=80, X=95, s=50%, t=0.5, n=200, r=4%:
- European Call:    6.68719284631
- European Put :   19.8060668105
- American Call:    6.68719284631
- American Put :   20.1465105751
~~ end ~~

$ 
```




Link: [Homework description](http://www.csie.ntu.edu.tw/~lyuu/finance1.html)

