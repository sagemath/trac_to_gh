# Issue 1846: maxima looses minus signs in symbolic expression

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2008-01-19 09:43:52

Assignee: was

Consider

```
log(a*e^(-a*x-b)).simplify_exp()
```


This gets expanded correctly, however


```
log(a*e^(-a*x-b)/(1+exp(-a*x-b))^2 ).simplify_exp()
```

appears to lose the minus signs on ax and b.





---

Comment by was created at 2008-01-19 14:42:38

Resolution: invalid


---

Comment by was created at 2008-01-19 14:42:38

Actually Sage is right and you are wrong, because of the identity `log(e^(-a*x - b) + 1) == log(e^(a*x + b) + 1) - a*x - b` which one can derive from Taylor expansions of `log(x+1)` and `log(x^(-1) + 1)`.  See below. 



```
h = log(exp(-a*x-b) + 1)
```



```
h == h.simplify_exp()
///
log(e^(-a*x - b) + 1) == log(e^(a*x + b) + 1) - a*x - b
```



```
log(x+1).taylor(x,0,5)
///
x - x^2/2 + x^3/3 - x^4/4 + x^5/5
```



```
log(x^(-1)+1).taylor(x,0,5)
///
-log(x) + x - x^2/2 + x^3/3 - x^4/4 + x^5/5
```

