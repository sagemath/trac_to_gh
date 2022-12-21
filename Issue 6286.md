# Issue 6286: Inconsistence typesettings of PrimitiveFunctions

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-06-14 14:29:47

In sage-4.0.1, most of the primitive functions suffer from
inconsistence typsettings. For example:


```
f = arcsin
latex( f ); latex( f(x) ); latex( f(x,1) )

\sin^{-1}
\arcsin\left(x\right)
\mbox{\sin^{-1}}\left(x\right)
```


Note that the same function is being typeset differently. The additional "\mbox" in third case (which has been reported in
#6268) will get resolved by #5711. 

However, second case seems weird to me, given "class Function_arcsin" (sage.functions.trig) clearly defines its 
latex expression to be "\sin^{-1}". So it seems to be a pynac issue.

One can try following to see the issues for other functions


```
# Trigonometric functions
lst = [sin, cos, tan, cot, sec, csc, arcsin, arccos, arctan, arccot, arcsec, arccsc]  

# view
for fn in lst:
    view( fn ); view( fn(x) ); view( fn(x,1) )
    
# latex
for fn in lst:
    latex( fn ); latex( fn(x) ); latex( fn(x,1) )
```

 
and


```
# Hyperbolic functions
lst = [sinh, cosh, tanh, coth, sech, csch, arcsinh, arccosh, arctanh, arccoth, arcsech, arccsch ] 

# view
for fn in lst:
    view( fn ); view( fn(x) ); view( fn(x,1) )
    
# latex
for fn in lst:
    latex( fn ); latex( fn(x) ); latex( fn(x,1) )
```


It seems, out of these 24 functions, 18 functions suffer from inconsistence typesetting.


---

Comment by burcin created at 2009-06-14 15:47:17

I am working on this at the moment, as a part of the changes for #6211. Thanks for providing this comprehensive test data.

I am not sure about using `sin^{-1}` as the latex form of `arcsin` though.


---

Comment by burcin created at 2009-06-14 15:47:17

Changing status from new to assigned.


---

Comment by burcin created at 2009-06-14 15:47:17

Set assignee to burcin.


---

Comment by burcin created at 2009-11-21 11:26:58

The patch at #7490 fixes this. It also includes doctests to check latex typesetting of each of these functions.


---

Comment by burcin created at 2009-11-21 11:26:58

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-04 06:58:35

Fixed by #7490


---

Comment by mhansen created at 2009-12-04 06:58:35

Resolution: fixed
