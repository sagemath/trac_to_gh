# Issue 2348: MatrixGroup over CyclotomicField is broken

Issue created by migration from https://trac.sagemath.org/ticket/2348

Original creator: SimonKing

Original creation time: 2008-02-28 18:36:58

Assignee: wdj

CC:  was wdj

Keywords: matrix group, cyclotomic field

Define the following:

```
sage: F = CyclotomicField(8)
sage: z = F.gen()
sage: a = z+1/z
sage: MS = MatrixSpace(F, 2, 2)
sage: g1 = MS([[1/a,1/a],[1/a,-1/a]])
sage: b = z^2
sage: g2 = MS([[1,0],[0,b]])
sage: g3 = MS([[b,0],[0,1]])
sage: G = MatrixGroup([g1,g2,g3])
```


Then, one obtains a traceback by the attempt to see G:

```
sage: G
<traceback removed>
<type 'exceptions.TypeError'>: Gap produced error output
Variable: 'zeta8' must have a value


   executing Read("/home/king/.sage//temp/mpc739/6870//interface//tmp");
```


Note that in fact `zeta8` is known:

```
sage: G.base_ring().gen()
zeta8
```




---

Comment by SimonKing created at 2008-02-28 19:16:26

Searching in `sage/groups/matrix_gps/matrix_group.py`, i found that `MatrixGroup([g1,g2,g3])` calls `MatrixGroup_gens.__init__`, which in turn calls `MatrixGroup_gap.__init__`. The latter has signature `(self, n, R, var='a')`. 

In the above example, i guess `var` is supposed to be `'zeta8'`, and by consequence `G._var` should be `'zeta8'`. But it isn't, `G._var` will never be initialised with a value different from `'a'`.

I thought this might be a source of trouble. But unfortunately, it doesn't help to change `MatrixGroup_gens.__init__` accordingly. 

By the way, it seems that the attribute `_var` is not used somewhere.


---

Comment by wdj created at 2008-02-28 19:47:37

This is my guess:
The problem is buried in _gap_init_, which behaves incorrectly for cyclotomics:

sage: F = GF(8,"z"); a = F.gen(); a._gap_init_()
'Z(8)^1'
sage: F = CyclotomicField(8); a = F.gen(); a._gap_init_()
'zeta8'

I don't know if fixing that will fix the problem though.


---

Comment by wdj created at 2008-02-28 19:55:29

I should have added that in the last line of 


```
sage: F = GF(8,"z"); a = F.gen(); a._gap_init_() 
'Z(8)1'
sage: F = CyclotomicField?(8); a = F.gen(); a._gap_init_()
'zeta8'
```

the output should be 'E(8)', or possibly 'E(8)^1', since this
is the GAP notation for a primitive 8th root of unity.


---

Comment by SimonKing created at 2008-02-28 19:59:03

Replying to [comment:2 wdj]:
> This is my guess:
> The problem is buried in _gap_init_, which behaves incorrectly for cyclotomics:

It seems to me that you are right that it is the gap interface. Therefore i change Summary, Component, and Keywords of the ticket, and send Cc to William.

In the above example, `G._repr_()` refers to `G.gens()`, and that is calling the gap interface for the matrices that have been used to define `G`.

While the following works,

```
sage: F=CyclotomicField(8)
sage: N=Matrix(F,[[1,0],[0,1]])
sage: gap(N)
[ [ 1, 0 ], [ 0, 1 ] ]
```

the following crashes,

```
sage: M=Matrix(F,[[F.gen(),0],[0,F.gen()]])
sage: M
[zeta8     0]
[    0 zeta8]
sage: gap(M)
```

Again, `gap` complains that `'zeta8'` has no value.

For solving the problem with `MatrixGroup` i would appreciate if someone could explain to me 
 * how one can introduce `zeta8` to `gap`
or
 * how `F.gen()` should be called in order to be understood by `gap`


---

Comment by SimonKing created at 2008-02-28 19:59:03

Changing keywords from "matrix group, cyclotomic field" to "gap interface, matrix group, cyclotomic field".


---

Comment by SimonKing created at 2008-02-28 19:59:03

Changing component from group_theory to interfaces.


---

Comment by SimonKing created at 2008-02-29 08:36:27

More and more it seems to me that the troubles come from gaps in the gap interface. So i think this ticket should really be focused on the interface.

In the above example, one has to tell `gap` that it shall create a field extension, namely the cyclotomic field. The following crashes:

```
sage: F=CyclotomicField(8)
sage: gap(F)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
 ...
Syntax error: ; expected
$sage7:=Cyclotomic Field of order 8 and degree 4;;
                       ^
Variable: 'of' must have a value

Variable: 'degree' must have a value

   executing $sage7:=Cyclotomic Field of order 8 and degree 4;;
```

Apparently, `gap(F)` is equivalent to `gap(str(F))`, which of course yields nonsense.

Instead, the `gap` related methods of the class `NumberField` and related classes should do something like that:

```
sage: PR=PolynomialRing(F.base_field(),F.gen())
sage: pr=gap(PR)
sage: bf=gap(F.base_field())
sage: mp=gap(F.polynomial())
sage: f=bf.AlgebraicExtension(mp)
sage: f
<algebraic extension over the Rationals of degree 4>
```

Now `f` is the `gap` version of `F`.


---

Comment by SimonKing created at 2008-02-29 08:36:27

Changing keywords from "gap interface, matrix group, cyclotomic field" to "gap, field extension".


---

Comment by wdj created at 2008-02-29 11:51:38

I agree this needs fixing but, based on my reading of sage/interfaces/gap.py, I'm not sure how to do this. Do you have a suggestion William?


---

Comment by SimonKing created at 2008-02-29 23:26:49

I tried to figure out how the interfaces are used, and it seems to me that there will be much work to do.

Am i right that, if `X` is some Sage object, `gap(X)` sends the value of `X._gap_init_()` (which is a string) through the gap interface; and similarly `singular(X)` sends `X._singular_init_()`?

The problem is that `_gap_init_` and `_singular_init_` often can not be interpreted by gap or by Singular. Examples:


```
sage: QQ._singular_init_()
'Rationals'
```

This is ok, since `gap` knows what Rationals means. But:

```
sage: QQ._singular_init_()
'Rational Field'
```

This is something that Singular does not understand! In fact, for Singular the rationals do not exist, except as the base field of a polynomial ring. So i believe there should be a `NotImplementedError` in that case.


```
sage: CyclotomicField(8)._gap_init_()
'Cyclotomic Field of order 8 and degree 4'
sage: CyclotomicField(8)._singular_init_()
'Cyclotomic Field of order 8 and degree 4'
```

Neither gap nor Singular can interprete that string.

Something that seems inconsistent to me: the method `_singular_init_` is not always returning a string:

```
sage: QQ[x]._gap_init_()
'PolynomialRing(Rationals, ["x"])'
sage: QQ[x]._singular_init_()

//   characteristic : 0
//   number of vars : 1
//        block   1 : ordering lp
//                  : names    x
//        block   2 : ordering C
sage: type(QQ[x]._gap_init_())
<type 'str'>
sage: type(QQ[x]._singular_init_())
<class 'sage.interfaces.singular.SingularElement'>
```


I found that in `sage/rings/number_field/number_field.py` there is no method `_singular_init_` or `_gap_init_`. Do you think it would solve the problem if one implements such methods?


---

Attachment

This solves only a part of the problem


---

Comment by SimonKing created at 2008-03-01 10:50:02

I was just attaching a patch (relative to 2.10.3.rc0) that adds a `_gap_init_` method to `NumberField_generic` and may be part of a solution. 

Sometimes `_singular_init_` does not return a string but a SingularElement. I don't know whether it is possible to define a number field in gap in a single line (i.e., by a single string). So, it seemed reasonable to me to return a GapElement rather than a string.

However, this would require many changes in other parts of the code. E.g., I also need a change in 
`/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py`.
This seems not to be part of the mercurial repository, so i have no patch for it.
However, the method `_gap_init_` of the class `PolynomialRing_general` should be like that:

```
    def _gap_init_(self):
        br=self.base_ring()._gap_init_()
        if isinstance(br,str):
            return 'PolynomialRing(%s, ["%s"])'%(br, self.variable_name())
        return br.PolynomialRing('["%s"]'%(self.variable_name()))
```


With these patches, the initial problem is almost solved:


```
sage: F = CyclotomicField(8)
sage: gap(F)
<algebraic extension over the Rationals of degree 4>
sage: z = F.gen()
sage: a = z+1/z
sage: MS = MatrixSpace(F, 2, 2)
sage: g1 = MS([[1/a,1/a],[1/a,-1/a]])
sage: b = z^2
sage: g2 = MS([[1,0],[0,b]])
sage: g3 = MS([[b,0],[0,1]])
sage: gap(g1)
[ [ -1/2*zeta8^3+1/2*zeta8, -1/2*zeta8^3+1/2*zeta8 ],
  [ -1/2*zeta8^3+1/2*zeta8, 1/2*zeta8^3-1/2*zeta8 ] ]
sage: G = MatrixGroup([g1,g2,g3])
sage: G
Matrix group over Cyclotomic Field of order 8 and degree 4 with 3 generators:
 [[[-1/2*zeta8^3 + 1/2*zeta8, -1/2*zeta8^3 + 1/2*zeta8], [-1/2*zeta8^3 + 1/2*zeta8, 1/2*zeta8^3 - 1/2*zeta8]], [[1, 0], [0, zeta8^2]], [[zeta8^2, 0], [0, 1]]]
```


Why is that only *almost* a solution? 
Since the line `sage: gap(F)` is necessary; otherwise `zeta8` would not be defined in gap. Hence, it would be needed to change the `_gap_init_` method of MatrixSpace, and so on and so on.

_Conclusion_
 * What i do in the patch can't be a definite solution. 
 * Is there a way to find a string s so that `gap(s)` returns a gap version of `F`, with the variable name `zeta8`? Having this would probably solve the problem.


---

Attachment

This may be close to a solution


---

Comment by SimonKing created at 2008-03-01 14:55:49

The second patch (again relative to rc0-version) may be close to a solution. The following now works:

```
sage: F=CyclotomicField(8)
sage: z=F.gen()
sage: a=z+1/z
sage: b=z^2
sage: MS=MatrixSpace(F,2,2)
sage: g1=MS([[1/a,1/a],[1/a,-1/a]])
sage: g2=MS([[1,0],[0,b]])
sage: g3=MS([[b,0],[0,1]])
sage: G = MatrixGroup([g1,g2,g3])
sage: gap(g1)
[ [ -1/2*zeta8^3+1/2*zeta8, -1/2*zeta8^3+1/2*zeta8 ],
  [ -1/2*zeta8^3+1/2*zeta8, 1/2*zeta8^3-1/2*zeta8 ] ]
sage: G
Matrix group over Cyclotomic Field of order 8 and degree 4 with 3 generators:
 [[[-1/2*zeta8^3 + 1/2*zeta8, -1/2*zeta8^3 + 1/2*zeta8], [-1/2*zeta8^3 + 1/2*zeta8, 1/2*zeta8^3 - 1/2*zeta8]], [[1, 0], [0, zeta8^2]], [[zeta8^2, 0], [0, 1]]]
```


The suggested solution works as follows.
 * F._gap_init_() returns the _name_ of a gap object corresponding to F. That name is stored in the dictionary of F. If it does not exist in the dictionary, then the gap object is created first; so, that happens only once.
 * If g is an element of F, then `g._gap_init_()` first checks whether there is already a gap version of `g.parent()` (which is F). If there isn't, `F._gap_init_()` is called and creates that object. In either case, `g.__repr__()` is returned.
 * If M is a matrix with coefficients in F then the existing methods can remain unchanged.

Do you think that approach makes sense? And by the way: I raise a NotImplementedError if F.is_absolute()==False, because gap can not deal with non-simple extensions.

I still see some problems:
 * gap(G) does not work in the above example. So, the `_gap_init_` method for matrix groups needs being fixed.
 * In my suggested solution, it is not possible to work with non-standard gap interfaces: F._gap_init_() returns a name that is defined in the standard gap interface. Do you have an idea how this can be fixed?


---

Attachment

The patch is relative to sage-2.10.3.rc0 and replaces the previous patches. I think it provides a solution of the problem


---

Comment by SimonKing created at 2008-03-02 00:06:40

I think that the last patch provides a solution. Now, simple algebraic extensions of the rationals and matrices over such extensions can by send through the gap interface. By consequence, Matrix Groups over such extensions work.

Examples:

```
sage: F=CyclotomicField(8)
sage: z=F.gen()
sage: a=z+1/z
sage: MS=MatrixSpace(F,2,2)
sage: g1=MS([[1/a,1/a],[1/a,-1/a]])
sage: b=z^2
sage: g2=MS([[1,0],[0,b]])
sage: g3=MS([[b,0],[0,1]])
sage: gap(g1)*gap(g2)
[ [ (1/2*a-1/2*a^3), (1/2*a+1/2*a^3) ], [ (1/2*a-1/2*a^3), (-1/2*a-1/2*a^3) ] ]
```

Remark: So far, the generator of the gap-version of F is alway displayed as 'a'. I did not learn yet how to make it being displayed by gap as 'zeta8', which is how sage displays the generator of F.

```
sage: (gap(g1)*gap(g2))^12
[ [ !-1, !0 ], [ !0, !-1 ] ]
```

Remark: '!-1' is the integer -1 interpreted in the gap number field.

```
sage: G = MatrixGroup([g1,g2,g3])
sage: G
Matrix group over Cyclotomic Field of order 8 and degree 4 with 3 generators:
 [[[-1/2*zeta8^3 + 1/2*zeta8, -1/2*zeta8^3 + 1/2*zeta8], [-1/2*zeta8^3 + 1/2*zeta8, 1/2*zeta8^3 - 1/2*zeta8]], [[1, 0], [0, zeta8^2]], [[zeta8^2, 0], [0, 1]]]
sage: G.order()
192
```


The last line is based on applying a gap method to G. So, it seems to me that everything works. Making the generator of gap(F) appear as 'a' would probably be a trivial change.


---

Comment by wdj created at 2008-03-02 11:45:57

Applies cleanly and fixes the problem. Great job Simon!
Recommend acceptance.


---

Comment by SimonKing created at 2008-03-02 14:14:03

Replying to [comment:11 wdj]:
> Applies cleanly and fixes the problem. Great job Simon!
> Recommend acceptance.

There is one caveat: I had to fix the _gap_init_ method of matrices, since in gap an expression of the form [[field elements,...],[...]] is not a matrix. That expression becomes a matrix in gap only when multiplied with One(field).

By consequence, the doc test of the _gap_init_ method of MatrixGroup has to be modified. That modification is part of the patch provided in ticket #2367.


---

Comment by SimonKing created at 2008-03-02 14:56:25

Replying to [comment:11 wdj]:
> Recommend acceptance.

I still think it may be premature to include the patch. Nathan Dunfield gave me a hint on sage-support http://groups.google.com/group/sage-support/browse_thread/thread/ee3c23ea1b86cfe9?hl=en

I think it would be better to change _gap_init_() for number fields according to Nathan's hint. But i think the rest of the patch can stay as it is.

I hope tomorrow i will be able to submit a "cleaner" patch.


---

Comment by SimonKing created at 2008-03-02 17:33:51

Replying to [comment:13 SimonKing]:
> I still think it may be premature to include the patch. Nathan Dunfield gave me a hint on sage-support http://groups.google.com/group/sage-support/browse_thread/thread/ee3c23ea1b86cfe9?hl=en
> 
> I think it would be better to change _gap_init_() for number fields according to Nathan's hint. 

No, it doesn't work. If field elements are created using inline functions, they belong to different (but isomorphic) fields in gap and thus can not be added. Note that in the following example, x1 and x2 have the same definition, but can't be added to each other.

```
sage: x1=gap('GeneratorsOfField(CallFuncList(function() local x,E; x:=Indeterminate(Rationals,"x"); E:=AlgebraicExtension(Rationals,x^4 + 1); return E; end, []))[1]')
sage: x2=gap('GeneratorsOfField(CallFuncList(function() local x,E; x:=Indeterminate(Rationals,"x"); E:=AlgebraicExtension(Rationals,x^4 + 1); return E; end, []))[1]')
sage: x2+x2
(2*a)
sage: x1+x2
  <Traceback>
```


So, i will return to my previous approach, but taking more care about the doc tests.


---

Comment by SimonKing created at 2008-03-02 22:05:35

First apply the previous patch, then this patch. It fixes and extends doc tests related with the gap interface of number fields


---

Attachment

The patch fix_doctests_gap_numberfield.patch should be applied after final_numberfields_gap.patch. 

The new patch fixes some problems with doc tests. Also, it adds more doc tests. Moreover, now the generator of a number field gets the same name in gap and in sage, which may be convenient for the users.

The following doctests related with and extended by the patch pass:
matrix_group.py,
number_field.py,
number_field_element.pyx,
matrix1.pyx

`@`wdj: Could you please see if your positive review still holds when adding the new patch?


---

Comment by wdj created at 2008-03-02 23:37:23

This applied cleanly against 2.10.3.rc0 and passed sage -testall.
Positive review (again).


---

Comment by SimonKing created at 2008-03-05 10:47:22

This ticket, together with #2367, is now ticket #2395. First reason is that we got a new sage pre-release. 

Second reason is that my suggestions in this ticket for fixing the gap interface ought to be changed: By hints of Nathan Dunfield, i learned that _gap_init_ is in fact called only once, and the objects in the gap interface are cached. Hence, using gap inline functions work. This different approach is in ticket #2395.

Third reason is that #2367 and this ticket belong closely together, hence, they should be worked on in one ticket.


---

Comment by SimonKing created at 2008-03-05 10:47:22

Resolution: invalid
