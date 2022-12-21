# Issue 7194: extended singular functions interface, needs work

Issue created by migration from Trac.

Original creator: PolyBoRi

Original creation time: 2009-10-12 12:23:23

Assignee: malb

CC:  malb burcin hannes@mathematik.uni-kl.de

Keywords: singular

wrapped list, use intvec as input, wrapped ring (RingWrap for return)...
This can wrap a lot more of Singular functions now.

This needs the header file lists.h, which is not installed by default.


---

Attachment


---

Comment by PolyBoRi created at 2009-10-13 09:50:38

I updated the patch. It now supports matrices as well :-).
I also fixes some problem when returning polynomials.
Cheers,
Michael

P.S.: Next targets are intmat and letter place.


---

Comment by PolyBoRi created at 2009-10-13 11:03:46

Hi!
A small demonstration of the copy and paste feature:

Singular:

```
proc content(f)
"USAGE:   content(f); f polynomial/vector
RETURN:  number, the content (greatest common factor of coefficients)
         of the polynomial/vector f
SEE ALSO: cleardenom
EXAMPLE: example content; shows an example
"
{
  if (f==0) { return(number(1)); }
  return(leadcoef(f)/leadcoef(cleardenom(f)));
}
example
{ "EXAMPLE:"; echo = 2;
   ring r=0,(x,y,z),(c,lp);
   content(3x2+18xy-27xyz);
   vector v=[3x2+18xy-27xyz,15x2+12y4,3];
   content(v);
}
```


Sage:

```python

from sage.libs.singular.function import singular_function, lib
leadcoef =  singular_function("leadcoef")
cleardenom = singular_function("cleardenom")

def content(f):
    """
    Examples:
    sage: P.<x,y,z>=PolynomialRing(QQ)
    sage: content(3*x**2+18*x*y-27*x*y*z)
    -3
    """
    if f==0:
        return 1
    return leadcoef(f)/leadcoef(cleardenom(f))

```



---

Attachment


---

Comment by PolyBoRi created at 2009-10-13 13:07:30

How to construct ring with parameters

```python
P.<x,y,z>=PolynomialRing(QQ)
characteristic=0
number_of_variables=1
number_of_parameters=3
l=[
    [0, ['a','b','c'], [['dp', number_of_parameters*(1,)], ['C', (0,)]], P.ideal([0])]
, ['x', 'y', 'z'], [['dp', number_of_parameters*(1,)], ['C', (0,)]], P.ideal([0])]
ring=singular_function("ring")
ring(l, ring=P)
```



---

Comment by PolyBoRi created at 2009-10-13 13:24:21

how to make letter place
sage: from sage.libs.singular.function import lib, singular_function
sage: P.<x,y,z>=QQ[]
sage: lib("freegb.lib")
sage: make_letter_place_ring = singular_function("makeLetterplaceRing")
sage: make_letter_place_ring(10, ring=P)
<RingWrap>


---

Comment by PolyBoRi created at 2009-10-13 13:24:41

sorry:


```python

sage: from sage.libs.singular.function import lib, singular_function
sage: P.<x,y,z>=QQ[]
sage: lib("freegb.lib")
sage: 
sage: make_letter_place_ring = singular_function("makeLetterplaceRing")
sage: make_letter_place_ring(10, ring=P)
<RingWrap>
```



---

Comment by PolyBoRi created at 2009-10-15 11:18:51

Changing status from new to needs_work.


---

Comment by PolyBoRi created at 2009-10-15 11:18:51

the latest patch supports intvec/intmat
Cheers,
Michael


---

Attachment


---

Attachment

the recent version wraps vectors over P**n in both direction.
Now, I am about hunting the modules.


---

Attachment


---

Comment by PolyBoRi created at 2009-10-16 13:06:08

The latest version supports also modules and free resolution objects.

Free resolution objects form some lazy blackbox in Singular, so I just did some basic blackbox. The rest can be accessed via singular functions using this interface.
So, we might extend Resolution object interface at some time, when it is needed.
Cheers,
Michael


---

Attachment


---

Attachment

A new SPKG installing `Singular/lists.h` is available here

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg


---

Attachment

I give Michael's patch a positive review. However, somebody needs to review my documentation/cleanup patch and the SPKG.

How to apply:
 * install http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg
 * apply singular_list.10.patch
 * apply singular_lists_referee.patch


---

Comment by malb created at 2009-11-18 17:45:30

Changing status from needs_work to needs_review.


---

Comment by malb created at 2009-12-01 16:39:04

Michael, Burcin, any takers for looking at my referee patch?


---

Comment by burcin created at 2009-12-01 18:19:20

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2009-12-01 18:19:20

Looks good to me.


---

Comment by mhansen created at 2009-12-02 08:29:21

I get all sorts of Cython errors in function.pyx about cdef functions not being declared.

Did you try this on 4.3.alpha0?


---

Comment by mhansen created at 2009-12-02 08:29:21

Changing status from positive_review to needs_work.


---

Attachment

fixed to work with 4.3


---

Comment by malb created at 2009-12-02 11:13:08

I fixed the compilation failures under 4.3, strange that it compiled with 4.2. The instructions remain the same:

 * install  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg 
 * apply `singular_list.10.patch` (fixed)
 * apply `singular_lists_referee.patch`


---

Comment by mhansen created at 2009-12-02 11:39:21

Resolution: fixed


---

Comment by PolyBoRi created at 2009-12-07 13:27:02

Thanks to all, who helped to get that code into Sage (while I was in holidays).
You made me really happy :-).

Cheers,
Michael
