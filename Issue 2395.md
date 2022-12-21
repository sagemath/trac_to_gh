# Issue 2395: [with patch, needs review] New features for number fields (gap interface, matrix groups)

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-03-05 10:28:19

Assignee: SimonKing

CC:  wdj

Keywords: number field, gap interface, matrix group

This ticket replaces #2348 and #2367. The attached patch provides several new features related with number fields.

---------

Firstly, the patch fixes a bug of the gap interface for number fields and their elements. The _gap_init_ method of number fields is now based on gap inline functions (thanks to Nathan Dunfield for that hint!):

```
sage: F=CyclotomicField(8)
sage: gap(QQ).name()
'$sage1'
sage: F._gap_init_()
'CallFuncList(function() local x,E; x:=Indeterminate($sage1,"x"); E:=AlgebraicExtension($sage1,x^4 + 1,"zeta8"); return E; end,[])'
sage: gap(F)
<algebraic extension over the Rationals of degree 4>
```

Note that the variable `$sage1` represents gap(QQ) -- QQ is the base ring of F.

I also learned from Nathan Dunfield that gap(F) is cached. Hence, if p is an element of F then p._gap_init_() may refer to gap(F).name(), which is `$sage2`:

```
sage: p=3*F.gen()^3-F.gen()^2+F.gen()+1
sage: p._gap_init_()
'3*GeneratorsOfField($sage2)[1]^3 - GeneratorsOfField($sage2)[1]^2 + GeneratorsOfField($sage2)[1] + 1'
sage: gap(p)
(1+zeta8-1*zeta8^2+3*zeta8^3)
```

Note that the generator of gap(F) got the same name `'zeta8'` as the generator of F.

Another extension was needed in the _gap_init_ method of matrices. The problem is that `[[elem1,elem2],[elem3,elem4]]` is in general not a matrix; it has to be multiplied with One(field):

```
sage: z=F.gen()
sage: a=z+1/z
sage: b=z^2
sage: MS=MatrixSpace(F,2,2)
sage: g1=MS([[1/a,1/a],[1/a,-1/a]])
sage: g2=MS([[1,0],[0,b]])
sage: g3=MS([[b,0],[0,1]])
sage: g1._gap_init_()
'[[-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1],-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1]],[-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1],1/2*GeneratorsOfField($sage2)[1]^3 - 1/2*GeneratorsOfField($sage2)[1]]]*One($sage2)'

sage: gap(g1)
[ [ (1/2*zeta8-1/2*zeta8^3), (1/2*zeta8-1/2*zeta8^3) ],
  [ (1/2*zeta8-1/2*zeta8^3), (-1/2*zeta8+1/2*zeta8^3) ] ]
sage: gap(g1).IsMatrix()
true

sage: gap('[[GeneratorsOfField($sage2)[1],1],[1,GeneratorsOfField($sage2)[1]]]').IsMatrix()
false
```


Now, one can compute with the gap matrices:

```
sage: (gap(g1)*gap(g2))^12
[ [ !-1, !0 ], [ !0, !-1 ] ]
sage: (g1*g2)^12
[-1  0]
[ 0 -1]
```

Note that `!-1` means that the integer -1 is interpreted as element of a different field, namely of gap(F).

--------

Secondly, the patch extends the method invariant_generators of MatrixGroup to the case of matrix groups over number fields. Fixing the gap interface for number fields suffices for defining matrix groups over number fields; but extending the method invariant_generators requires more effort. Now, the following computation works:

```
sage: G=MatrixGroup([g1,g2,g3])
sage: G.order()
192
sage: G.invariant_generators()
[x1^8 + 14*x1^4*x2^4 + x2^8,
 x1^24 + 10626/1025*x1^20*x2^4 + 735471/1025*x1^16*x2^8 + 2704156/1025*x1^12*x2^12 + 735471/1025*x1^8*x2^16 + 10626/1025*x1^4*x2^20 + x2^24]
```


---------------

The various _gap_init_ methods (in matrix1.pyx, number_field_element.pyx, number_field.py, matrix_group.py and matrix_group_element.py) got doctests. Also, i added more doc tests to invariant_generators, based on examples of David Joyner.




---

Comment by SimonKing created at 2008-03-05 10:29:34

Patch provides extension of the gap interface and of matrix groups to the case of number fields. Should apply to sage-2.10.3.rc1


---

Attachment

Applies and passes tests for me.


---

Comment by mabshoff created at 2008-03-05 14:09:49

Merged in Sage 2.10.3.rc2


---

Comment by mabshoff created at 2008-03-05 14:09:49

Resolution: fixed


---

Comment by wdj created at 2008-03-05 14:51:18

This looks good too. Applies cleanly against 2.10.3.rc1. Passes sage -testall, except for the ones that fail without any patches (rings/polynomial/groebner_fan.py, plot/plot.py).
