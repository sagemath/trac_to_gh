# Issue 1300: Customize the output of Singular matrices

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2007-11-28 16:43:37

Assignee: Martin Albrecht

CC:  malb

Keywords: Singular matrix

When Singular prints a matrix M then it tries to keep the row-column structure of M visible on screen. If this is impossible (for large polynomials), the entries are abbreviated:

```
> ring r = 7,(x(1..2)),dp;
> matrix M[1][3] = x(1)^7*x(2)-x(1)*x(2)^7, x(1)^12-2*x(1)^9*x(2)^3-x(1)^6*x(2)^6+2*x(1)^3*x(2)^9+x(2)^12, x(1)^18+2*x(1)^15*x(2)^3+3*x(1)^12*x(2)^6+3*x(1)^6*x(2)^12-2*x(1)^3*x(2)^15+x(2)^18;
> print(M);
x(1)^7*x(2)-x(1)*x(2)^7,M[1,2],M[1,3]
```


The Singular developers have good reasons for it and wouldn't like to change it.

Unfortunate consequence for Sage: Creating this matrix via the Singular interface, it is assigned an automatically generated name; printing it, Singular uses that name, that the user probably is not aware of:

```
sage: R=singular.ring(7,'(x(1..2))','dp')
sage: M=singular.matrix(1,3,'x(1)^7*x(2)-x(1)*x(2)^7,x(1)^12-2*x(1)^9*x(2)^3-x(1)^6*x(2)^6+2*x(1)^3*x(2)^9+x(2)^12,x(1)^18+2*x(1)^15*x(2)^3+3*x(1)^12*x(2)^6+3*x(1)^6*x(2)^12-2*x(1)^3*x(2)^15+x(2)^18')
sage: M
x(1)^7*x(2)-x(1)*x(2)^7,sage1[1,2],sage1[1,3]
sage: print M
x(1)^7*x(2)-x(1)*x(2)^7,sage1[1,2],sage1[1,3]
```


I believe it is confusing for the user to be confronted with variable names that he/she has not defined him/herself. Therefore i think the printing of Singular-matrices in Sage should be customized.

*Remarks*
 * Singular's reason for abbreviation is obvious: When printing a matrix, its shape should be apparent. This problem should also be addressed in some way by a new version of `SingularElement.__str__`.
 * One *solution mimicking Singular's behaviour* is to replace the automatically generated name (`sage1` in the example above) by the user-defined name (`M` in the example above). In that way, one has an output that preserves the shape of the matrix but reduces confusion of the user by cryptic variable names.
 * Singular provides several other ways to show a matrix; perhaps you'll find one of them nicer. 

-----
In the following, i show several ways to continue the Singular-example above, which may provide a nicer printing.

```
> LIB "inout.lib";
// ** loaded /usr/local/lib/Singular/3-0-3/LIB/inout.lib (1.28,2006/07/20)
> pmat(M);
x(1)^7*x(2)-x(1)*x(2)^7,
x(1)^12-2*x(1)^9*x(2)^3-x(1)^6*x(2)^6+2*x(1)^3*x(2)^9+x(2)^12,
x(1)^18+2*x(1)^15*x(2)^3+3*x(1)^12*x(2)^6+3*x(1)^6*x(2)^12-2*x(1)^3*x(2)^15+x(2)^18
> pmat(M,14);
x(1)^7*x(2)-x( x(1)^12-2*x(1) x(1)^18+2*x(1)
```

The first shows everything without abbreviation, even though this destroys the visible matrix shape. The latter shows at most the leading 15 letters of each column, which is another form of abbreviation. However, for the last two polynomials, it is impossible to guess whether they are abbreviated or not!

*I think this is a solution that could almost be adopted by Sage.* However, IMHO, the user __must__ be alerted about the presence of an abbreviation, e.g., by appending '`...`' if there has been an abbreviation. So, the following output would be clearer:

```
x(1)^7*x(2)-x(... x(1)^12-2*x(1)... x(1)^18+2*x(1)...
```

-----

```
> M;
M[1,1]=x(1)^7*x(2)-x(1)*x(2)^7
M[1,2]=x(1)^12-2*x(1)^9*x(2)^3-x(1)^6*x(2)^6+2*x(1)^3*x(2)^9+x(2)^12
M[1,3]=x(1)^18+2*x(1)^15*x(2)^3+3*x(1)^12*x(2)^6+3*x(1)^6*x(2)^12-2*x(1)^3*x(2)^15+x(2)^18
```

This is not good, since this doesn't show the shape of the matrix and, called via the interface, would again show the automatically generated variable name.
-----

```
> print(M,"%l");
matrix(ideal(x(1)^7*x(2)-x(1)*x(2)^7,x(1)^12-2*x(1)^9*x(2)^3-x(1)^6*x(2)^6+2*x(1)^3*x(2)^9+x(2)^12,x(1)^18+2*x(1)^15*x(2)^3+3*x(1)^12*x(2)^6+3*x(1)^6*x(2)^12-2*x(1)^3*x(2)^15+x(2)^18),1,3)
```

This shows a definition of the matrix, but the shape is invisible

Sorry for such long description of a minor problem.


---

Comment by mabshoff created at 2007-11-28 16:46:10

Changing assignee from Martin Albrecht to malb.


---

Comment by mabshoff created at 2007-11-28 16:46:10

Changing priority from minor to major.


---

Comment by mabshoff created at 2007-11-28 16:46:10

Changing component from interfaces to commutative algebra.


---

Comment by SimonKing created at 2007-11-29 14:07:15

As i mentioned, `pmat` (in Singular's `inout.lib`) may help. However, up to now, this function did only display a matrix on screen (it had no return value!), and if a polynomial was truncated, the user hasn't been notified.

I just changed `pmat` in Singular's cvs repository. Now, it returns a string, truncations are made visible, and the column separator now is ", " (before, it was sometimes " " and sometimes ",").

I don't know if the rest of the Singular team accepts this change (after all, a change from "no return" to "return a string" is non-trivial). If this is the case, i think using `pmat` in the method `__str__` (and perhaps `__repr__`) for `SingularElement`s of type `matrix`, choosing the parameter so that the matrix fits on screen, may help to close this ticket.

Examples using the new pmat:

```
sage: singular.LIB("inout.lib")
sage: R=singular.ring(0,'(x,y,z)','dp')
sage: I=singular.ideal('x','z+3y','x+y','z')
sage: M=(I^2).matrix(3,3)
sage: M

x^2,      3*x*y+x*z,      x^2+x*y,
x*z,      9*y^2+6*y*z+z^2,3*x*y+3*y^2+x*z+y*z,
3*y*z+z^2,x^2+2*x*y+y^2,  x*z+y*z
sage: M.pmat()

x^2,       3*x*y+x*z,       x^2+x*y,
x*z,       9*y^2+6*y*z+z^2, 3*x*y+3*y^2+x*z+y*z,
3*y*z+z^2, x^2+2*x*y+y^2,   x*z+y*z
# note the additional blanc space; i find it nicer this way.
sage: M.pmat(7)

x^2,     3*x*y.., x^2+x*y,
x*z,     9*y^2.., 3*x*y..,
3*y*z.., x^2+2.., x*z+y*z
# Now it is clear which polynomials are truncated and which are not!
```



---

Comment by malb created at 2008-06-12 23:03:52

Is the change in the newest Singular upstream? If so, we can make use of it. If not, we should wait for it to hit the official Singular release.


---

Comment by SimonKing created at 2008-08-14 10:52:50

Replying to [comment:4 malb]:
> Is the change in the newest Singular upstream? If so, we can make use of it. If not, we should wait for it to hit the official Singular release.

I realize that we still didn't finish to work on it. 

Yes, it is in the official release, and the above example 

```
sage: M.pmat(7)
x^2,     3*x*y.., x^2+x*y,
x*z,     9*y^2.., 3*x*y..,
3*y*z.., x^2+2.., x*z+y*z
```

is now the standard behaviour.


---

Attachment

Try to avoid autogenerated names when printing pexpect objects


---

Comment by SimonKing created at 2008-08-14 11:22:46

Printing Singular matrices relies on some `__repr__` method from `expect.py`. I changed it as follows:
 1. Get the output suggested by self.parent()
 2. If this output contains self._name then we need to do something, because the appearance of an autogenerated name may confuse the user:
   * If self has a customized name, then use it!
   * Otherwise, if self is a `SingularElement` of type matrix then try `pmat`
   * Otherwise, return the output suggested by self.parent() (even though it contains an autogenerated name).

Hence, my patch changes the usual behaviour only if either the object has a custom name, or it happens to be a singular matrix, in which case the polynomials will be cut by default after 20 characters.

Hence, the example is like this, which i think is an improvement:

```
sage: R=singular.ring(7,'(x(1..2))','dp')
sage: M=singular.matrix(1,3,'x(1)^7*x(2)-x(1)*x(2)^7,x(1)^12-2*x(1)^9*x(2)^3-x(1)^6*x(2)^6+2*x(1)^3*x(2)^9+x(2)^12,x(1)^18+2*x(1)^15*x(2)^3+3*x(1)^12*x(2)^6+3*x(1)^6*x(2)^12-2*x(1)^3*x(2)^15+x(2)^18')
sage: M
x(1)^7*x(2)-x(1)*x.., x(1)^12-2*x(1)^9*x.., x(1)^18+2*x(1)^15*..
sage: M.rename('T')
sage: M
x(1)^7*x(2)-x(1)*x(2)^7,T[1,2],T[1,3]
```


Certainly the "cut point" (now 20 characters) could be customized. Any suggestions how this should be done?


---

Comment by malb created at 2008-08-18 11:31:26

fixes issues found in review


---

Attachment

*Review*
 * no doctest was added to demonstrate the new behavior (added in attached patch)
 * `expect.py` is not the right place for Singular specific interface issue, thus it should be moved code to `singular.py` (done in attached patch).

I'll give Simon's patch a positive review if my patch is applied afterwards. So my patch needs a review.


---

Comment by SimonKing created at 2008-08-18 22:42:18

Replying to [comment:8 malb]:
> *Review*
>  * no doctest was added to demonstrate the new behavior (added in attached patch)
>  * `expect.py` is not the right place for Singular specific interface issue, thus it should be moved code to `singular.py` (done in attached patch).
> 
> I'll give Simon's patch a positive review if my patch is applied afterwards. So my patch needs a review.

I agree with you that the `__repr__` method in `expect.py` should be overwritten with a method in `singular.py`. The doc test shows one the new feature for Singular matrices. Also, doc tests pass.

So, up to here, i give Martin's patch a positive review.

However, one new feature for the `__repr__` method (custom names) is not in the doc tests. Therefore i'll create another patch, with an additional doc test.


---

Attachment

slight layout fixups


---

Comment by malb created at 2008-08-19 10:50:30

I edited Simon's patch to match Sage's undocumented docstring style. Positive review.


---

Comment by mabshoff created at 2008-08-21 21:22:43

Resolution: fixed


---

Comment by mabshoff created at 2008-08-21 21:22:43

Merged SingularMatrix.patch, trac_1300_fixup.patch and SingularMatrixMoreTest.patch in Sage 3.1.2.alpha0
