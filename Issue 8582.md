# Issue 8582: sum(1/(1+k^2), k, -oo, oo) returns 0

Issue created by migration from https://trac.sagemath.org/ticket/8582

Original creator: mvngu

Original creation time: 2010-03-23 04:13:54

Assignee: burcin

From [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/658b0fe8413b86f8):

```
But I want to make a comment, also from this documentation. It says
sum(1/(1+k^2), k, -oo, oo, algorithm = 'mathematica')     # optional
-- requires mathematica

OK, I understand that sage do not kown how to evaluate
sum(1/(1+k^2), k, -oo, oo)

But it answer     0      , that is wrong!!!
```



---

Comment by kcrisman created at 2010-09-22 14:43:27

This seems to be fixed in Maxima 5.21.1 or so:

```

(%i2) load(simplify_sum);
(%o2) /Users/.../maxima/share/contrib/solve_rec/simplif\
y_sum.mac
(%i5) display2d:false;

(%o5) false
(%i6) simplify_sum(sum(1/(1+k^2),k,-inf,inf));

(%o6) -%i*(psi[0](%i+1)+%gamma)/2-%i*(psi[0](%i)+%gamma)/2
                                 +%i*(psi[0](-%i)+%gamma)/2
                                 +%i*(psi[0](1-%i)+%gamma)/2
```

Which uses the digamma function quite a bit.  We don't get the (perhaps) simpler answer `pi coth(pi)`.


---

Comment by kcrisman created at 2010-09-22 14:45:02

This should hopefully be resolved by #8731.


---

Comment by mvngu created at 2010-12-06 11:56:39

Resolution: fixed


---

Comment by mvngu created at 2010-12-06 11:56:39

This is fixed at ticket #10187 by upgrading to Maxima 5.22.1:


```
[mvngu@sage sage-4.6.1.alpha3]$ ./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: k = var("k") 
sage: sum(1/(1+k^2), k, -oo, oo)
1/2*I*psi(-I) - 1/2*I*psi(I) + 1/2*I*psi(-I + 1) - 1/2*I*psi(I + 1)
sage: %maxima
| Sage Version 4.6.1.alpha3, Release Date: 2010-12-05                |
| Type notebook() for the GUI, and license() for information.        |
  --> Switching to Maxima <-- 

''
maxima: load(simplify_sum);
"/dev/shm/mvngu/sage-4.6.1.alpha3/local/share/maxima/5.22.1/share/contrib/solve_rec/simplify_sum.mac"
maxima: display2d:false;
false
maxima: 
maxima: simplify_sum(sum(1/(1+k^2),k,-inf,inf));
-%i*(psi[0](%i+1)+%gamma)/2-%i*(psi[0](%i)+%gamma)/2+%i*(psi[0](-%i)+%gamma)/2+%i*(psi[0](1-%i)+%gamma)/2
```


So I'm closing this ticket as fixed.


---

Comment by kcrisman created at 2010-12-06 13:15:56

Is that doctested in the patches for #10187?


---

Comment by mvngu created at 2010-12-06 13:34:13

Replying to [comment:4 kcrisman]:
> Is that doctested in the patches for #10187?

No. But it shouldn't be difficult to write a documentation patch with doctests in the current ticket. The Sage 4.6.1 release cycle is now in feature freeze, but I think documentation patches are OK for merging in the upcoming release candidates.


---

Comment by mvngu created at 2010-12-06 13:40:39

See #10434 for a follow-up documentation ticket.
