# Issue 5140: is_irreducible() reports units as irreducible

Issue created by migration from Trac.

Original creator: lars.fischer

Original creation time: 2009-01-30 21:15:34

Assignee: tbd

Keywords: is_irreducible

# Description of the bug
The following happens with

```
----------------------------------------------------------------------
----------------------------------------------------------------------
```

| SAGE Version 3.1.2, Release Date: 2008-09-19                       |
| Type notebook() for the GUI, and license() for information.        |
*The function is_irreducible returns True on units:*

```
sage: R.<x>=PolynomialRing( IntegerModRing(13),'x')
sage: (x^2-2).is_irreducible()
True
sage: (x^2).is_irreducible()
False
sage: R(1).is_irreducible()
True
```

The last line should say False or raise an exception as R(0).is_irreducible() does. Because irreducibility of B requires B to be not zero and not a unit. 

# Use case where this bug occured to me

If I want to loop over polynomials in R and count irreducible ones, I need a loop like this:

```
for p in R.polynomials(max_degree=3):
     if not p.is_zero() and not p.is_unit() and p.is_irreducible():
         # count p
```

It is easy to forget the check if p is a unit. Then the count would be wrong. 

# Bug-Fix
The bug is in the implementation:

```
e=R(1)
e.is_irreducible??
```

shows as code after the docstring: 

```
if self.is_zero():
            raise ValueError, "self must be nonzero"
if self.degree() == 0:
            return True
```


*I propose to insert a check*

```
if self.is_unit():
            raise ValueError, "self must not be a unit"
```

between the above ifs. I created a file via commit and  bundle with this modification. 



---

Attachment

The mentioned modification.


---

Comment by mabshoff created at 2009-01-30 22:10:43

Lars,

I am not so sure what you attached, but it does bot look like the change you describe. Please extract the commit for the fix and attach it as patch.

Cheers,

Michael


---

Attachment

The same patch via hg_sage.export().


---

Comment by lars.fischer created at 2009-01-31 13:14:24

Hello Michael,

I exported the modification and attached the file as irred_bug_fix.export.patch. 
Sorry for the inconvenience.

With best regards,
Lars


---

Comment by cremona created at 2009-02-01 15:47:13

Review:  I agree entirely that units need to be handled properly here, but I do not think that this patch solves the issue.  

Firstly, I don't think that raising an error is necessary or helpful, and would prefer to return False for units.

Secondly, you have left in the code which (now for non-units) returns True for degree 0 polynomials.  But that is wrong for polynomials over rings which are not fields such as ZZ[x], where 6 has degree 0, is not a unit but is not irreducible.  Instead, for degree 0 polynomials (which have already been handled by the is_unit() test) one should test irreducibility in the base ring.

Example:

```
sage: R.<x>=ZZ[]
sage: R(6).is_irreducible()
True
```

is wrong, and it would be nice if the patch handled this also.

Lastly: Lars, when you make a patch to correct some incorrect behaviour in Sage you should add a doctest to the function which shows that the problem has been solved.


---

Comment by cremona created at 2009-02-01 15:47:13

Changing priority from trivial to minor.


---

Attachment

Replaces earlier patches; based on 3.3.alpha3


---

Attachment

Replaces all previous; based on 3.4


---

Comment by cremona created at 2009-03-18 17:34:28

I have rebased this on 3.4.  Testing revealed a problem: Now that 1 is no longer reported as an irreducible element of ZZ[x] (as it used to be, amazingly), the quotient of ZZ[x] by the ideal (1) is not tagged as an integral domain, and then a doctest which tested the is_finite() function on that quotient failed since is_finite was always NotImplemented for general rings.

To solve this I implemented an is_zero() function for completely general rings (it just tests is the one_element() equals the zero_element(), and some small functions on general rings can now be decided if the ring is zero -- such as is_finite().

I tested everything in sage/rings.


---

Comment by mabshoff created at 2009-04-06 06:02:30

Since John posted an updated patch I am marking this as "needs review". From the history it seems that there are some unresolved issues, so feel free to change it to "needs work".

Cheers,

Michael


---

Comment by cremona created at 2009-04-06 10:26:56

I just checked that my patch trac_5140_rebase.patch still applies fine to 3.4.rc0, and tests still pass.  That patch dealt with all the issues which I came up against when testing, so as far as I am concerned it is ready to go, but I agree that an independent reviewer is needed since I touched quite a few other things.  Anyone familiar with basic ring stuff could do it!


---

Comment by cremona created at 2009-04-09 08:45:56

Replying to [comment:7 AlexGhitza]:  Thanks, Alex!


---

Comment by mabshoff created at 2009-04-09 09:23:47

Resolution: fixed


---

Comment by mabshoff created at 2009-04-09 09:23:47

Merged trac_5140_rebase.patch in Sage 3.4.1.rc2.

Cheers,

Michael
