# Issue 2578: bug in bernoulli_polynomial

Issue created by migration from https://trac.sagemath.org/ticket/2578

Original creator: was

Original creation time: 2008-03-17 23:29:04

Assignee: was

CC:  mhansen


I wanted to verify that Sage could symbolically compute the derivative
of Bn(x), the nth Bernoulli polynomial in (x): Dx[Bn(x)]=n*Bn-1(x).
The following code causes Sage to lockup:

```
Bn = bernoulli_polynomial(x,n)
```


The command "bernpoly(x,n)" in Maxima does not lock up but Maxima
will not compute symbolically.


```
sage: B3 = bernoulli_polynomial(x,3)
sage: B4 = bernoulli_polynomial(x,4)
sage: DxB4 = diff(B4,x)
sage: print expand(DxB4-4*B3)
                                      0
sage: Bn = bernoulli_polynomial(x,n)
Traceback (most recent call last):
...
KeyboardInterrupt
>>>
>>>
```




---

Comment by was created at 2008-03-17 23:45:58

I forgot to define (n) as a variable in the above session.
Now, Sage does not lockup but instead gives the traceback.


```
var('y,x,n')
y = bernoulli_polynomial(x,n)

Exception (click to the left for traceback):
...
NameError: name 'bernpoly' is not defined

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/server2/sage_notebook/worksheets/5463/24/code/18.py",
line 7, in <module>
   y = bernoulli_polynomial(x,n)
 File "/usr/local/sage/local/lib/python2.5/site-packages/sympy/
plotting/", line 1, in <module>

 File "/usr/local/sage/local/lib/python2.5/site-packages/sage/
combinat/combinat.py", line 1806, in bernoulli_polynomial
   return sage_eval(maxima.eval("bernpoly(x,%s)"%n), {'x':x})
 File "/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/
sage_eval.py", line 110, in sage_eval
   return eval(p, sage.all.__dict__, locals)
 File "<string>", line 1, in <module>
NameError: name 'bernpoly' is not defined
```



---

Comment by mabshoff created at 2008-09-14 09:43:32

Since combinat.py is involved I am CCind Mike Hansen :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 09:45:21

Oh, and definitely not invalid.

Cheers,

Michael


---

Comment by craigcitro created at 2009-01-23 09:01:40

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2009-01-23 09:01:40

Changing status from new to assigned.


---

Comment by craigcitro created at 2009-01-23 09:01:40

The attached patch rewrites `bernoulli_polynomial` to avoid Maxima completely. This gives roughly a factor of 10 speedup.

Unfortunately, the originial request doesn't quite make sense -- `bernoulli_polynomial(x,n)` for `n` a symbolic variable would have to return a polynomial of variable degree. As it stands, we don't have any sort of "symbolic sum" to use for that kind of thing. I did add the formula for the `n`th Bernoulli polynomial to the docstring, though.


---

Attachment

positive review;

it could be optimized by using horner's rule


---

Comment by mabshoff created at 2009-01-23 10:46:32

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 10:46:32

Resolution: fixed
