# Issue 4315: symbolic computing is terribly slow

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-10-17 19:13:23

Assignee: burcin

CC:  zimmerma

Computing the 10th derivative of x<sup>(x</sup>x) in Sage is terribly slow:

```
bash-3.2$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: time a = diff(x^(x^x), x, 10)
CPU times: user 1.71 s, sys: 0.08 s, total: 1.80 s
Wall time: 17.69 s
```

In comparison with Mathemagix I get:

```
bash-3.2$ time ./mmxlight/build/mmx-light 
--------------------------------------------------------------
--------------------------------------------------------------
1] use "symbolix"
2] a = derive (x^x^x, x^^10);
3] quit
|:*)          Welcome to Mathemagix-light 0.4             (*:|
|  This software falls under the GNU General Public License  |
|          It comes without any warranty whatsoever          |
|------------------------------------------------------------|
|                    (c) 2001--2008 by                       |
|           Joris van der Hoeven, Gregoire Lecerf,           |
|        Bernard Mourrain, Olivier Ruatta and others         |
real    0m10.021s
user    0m0.339s
sys     0m0.052s
```



---

Comment by mhansen created at 2008-10-17 21:24:12

Hi Paul,

This is certainly much better with the use of Pynac which will (hopefully) be in 3.2:


```
sage: x = var('x',ns=1)
sage: %time a = (x^(x^x)).diff(x,10)
CPU times: user 0.68 s, sys: 0.00 s, total: 0.68 s
Wall time: 0.71 s
```



---

Comment by jason created at 2008-10-18 07:09:19

For comparison, on sage.math, mathematica gives:


```
In[1]:= Timing[D[x^(x^x), {x, 10}];]

Out[1]= {0.164011, Null}
```


while pynac gives:


```
sage: %timeit a=(x**(x**x)).diff(x,10)
10 loops, best of 3: 609 ms per loop
```



---

Comment by zimmerma created at 2008-10-18 07:53:41

great, Pynac seems indeed much faster. I thus wait for 3.2.


---

Comment by mabshoff created at 2008-10-18 09:03:16

Yep, closed since the main pynac ticket (#3872) has been merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 09:03:16

Resolution: fixed
