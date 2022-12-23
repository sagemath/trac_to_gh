# Issue 2367: [with patch, needs review] Extend invariant_generators to the case of Matrix Groups over number fields

Issue created by migration from https://trac.sagemath.org/ticket/2367

Original creator: SimonKing

Original creation time: 2008-03-02 14:06:04

Assignee: joyner

CC:  wdj

Keywords: invariant ring, matrix group

This ticket is strongly related with ticket #2348. I fix here a doc test failure that is introduced by the patch from #2348, and the new functionality that i introduce here relies on the patch from #2348.

Problem: Let G be a finite matrix group. So far, G.invariant_generators() worked only if G was defined over the rationals or over GF(prime). 
Solution: Singular also provides simple algebraic extensions over these fields, so, it just requires a more careful definition of a singular ring inside the function.

After first applying the patch from #2348 and then applying the new patch, the doc tests of matrix_group.py should pass, and the following should work:

```
sage: F=CyclotomicField(8)
sage: z=F.gen()
sage: a=z+1/z
sage: b=z^2
sage: MS=MatrixSpace(F,2,2)
sage: g1=MS([[1/a,1/a],[1/a,-1/a]])
sage: g2=MS([[1,0],[0,b]])
sage: g3=MS([[b,0],[0,1]])
sage: G=MatrixGroup([g1,g2,g3])
sage: G.invariant_generators()
[x1^8 + 14*x1^4*x2^4 + x2^8,
 x1^24 + 10626/1025*x1^20*x2^4 + 735471/1025*x1^16*x2^8 + 2704156/1025*x1^12*x2^12 + 735471/1025*x1^8*x2^16 + 10626/1025*x1^4*x2^20 + x2^24]
```




---

Comment by SimonKing created at 2008-03-02 14:09:30

Changing type from defect to enhancement.


---

Comment by wdj created at 2008-03-02 16:14:16

The patches (first 2348 then this one) applied cleanly and the above code ran. However, sage -testall failed. Here is one failure:


```
wdj@wooster:~/wdj/sagefiles/sage-2.10.3.rc0$ ./sage -t "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py"
sage -t  devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py**********************************************************************
File "matrix_group_element.py", line 122:
    sage: g._gap_init_()
Expected:
    '[[Z(7)^0,0*Z(7)],[0*Z(7),Z(7)^2]]'
Got:
    '[[Z(7)^0,0*Z(7)],[0*Z(7),Z(7)^2]]*One(GF(7))'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_matrix_group_element.py
         [5.2 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py
Total time for all tests: 5.2 seconds
```


This would be easy to fix of course but, for the failure I cannot recommend
acceptance at this time.

There were other failures,


```
        sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py
        sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py
        sage -t  devel/sage-matgp3/sage/plot/plot.py
```

but they may be unrelated since they were already reported by Jaap Spies
on sage-devel for a clean install.


---

Comment by SimonKing created at 2008-03-02 16:58:55

Replying to [comment:2 wdj]:
> The patches (first 2348 then this one) applied cleanly and the above code ran. However, sage -testall failed. Here is one failure: ...

Clearly the doctest failure in matrix_group_element.py has a trivial fix: The doctest expects output that is incorrect as soon as one switches to an algebraic extension of the rationals:

> Expected:
>     `'[[Z(7)<sup>0,0*Z(7)],[0*Z(7),Z(7)</sup>2]]'`
> Got:
>     `'[[Z(7)<sup>0,0*Z(7)],[0*Z(7),Z(7)</sup>2]]*One(GF(7))'`

In gap:

```
gap> x:=Indeterminate(Rationals,"x");;
gap> p:=x^4+3*x^2+1;;
gap> e:=AlgebraicExtension(Rationals,p);
<algebraic extension over the Rationals of degree 4>
gap> M:=[[1,GeneratorsOfField(e)[1]^2]];
[ [ 1, (a^2) ] ]
gap> IsMatrix(M);
false
gap> IsMatrix(M*One(e));
true
```

Hence, in general the modified output is needed.

> There were other failures,
> 
> {{{
>         sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py
>         sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py
>         sage -t  devel/sage-matgp3/sage/plot/plot.py
> }}}
> but they may be unrelated since they were already reported by Jaap Spies
> on sage-devel for a clean install.

I think so, too. I am about to provide new patches for this ticket and for #2348.


---

Comment by SimonKing created at 2008-03-02 22:47:49

First apply the patches from #2348, then apply this patch. It extends the method invariant_generators to the case of finite matrix groups over number fields


---

Attachment

Replying to [comment:2 wdj]:
> The patches (first 2348 then this one) applied cleanly and the above code ran. 

Now i changed the patches of #2348 and of this ticket. So, a re-check is needed.

> However, sage -testall failed. Here is one failure:
>  ...
> ----------------------------------------------------------------------
> The following tests failed:
> ...
>         sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py
>         sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py
>         sage -t  devel/sage-matgp3/sage/plot/plot.py

These three tests fail on my system as well - with and without the patches. So, it doesn't seem to be related.

But with the patches (that partially add further doc tests), the following clearly related tests pass:
 * matrix_group.py
 * matrix_group_element.py
 * number_field.py
 * number_field_element.pyx
 * matrix1.pyx


---

Comment by wdj created at 2008-03-03 00:45:02

This applies cleanly (first 2348 then this one) to 2.10.3.rc0. It also passes sage -testall (except for the usual 3 that fail, as reported first by Jaap).
Excellent patch. Recommend acceptance.


---

Comment by SimonKing created at 2008-03-05 10:43:58

This ticket, together with #2348, is now ticket #2395. First reason is that we got a new sage pre-release. Second reason is that my suggestions for fixing the gap interface (#2348) changed. Third reason is that #2348 and this ticket belong closely together, hence, they should be worked on in _one_ ticket.


---

Comment by SimonKing created at 2008-03-05 10:43:58

Resolution: invalid
