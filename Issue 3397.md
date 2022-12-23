# Issue 3397: [with patch, needs review] Steenrod algebra calculations

Issue created by migration from https://trac.sagemath.org/ticket/3397

Original creator: jhpalmieri

Original creation time: 2008-06-11 05:49:59

Assignee: jhpalmieri

Keywords: steenrod algebra

The attached patch adds files to sage.algebras to do Steenrod algebra calculations.  See the files for full documentation.  The only other package for this kind of thing of which I am aware is a Maple package: 

[http://math.scranton.edu/monks/software/Steenrod/steen.html](http://math.scranton.edu/monks/software/Steenrod/steen.html)



---

Comment by jhpalmieri created at 2008-06-11 05:50:40

Steenrod algebra calculations


---

Attachment


---

Comment by craigcitro created at 2008-06-15 21:25:24

Changing keywords from "steenrod algebra" to "steenrod algebra, editor_craigcitro".


---

Attachment

Hi David,

I don't know how far the review has gone, but I have the odd primary Steenrod algebras working now.  This patch replaces the old one.  There are a few other small changes, too, such as adding a 'Sq' method and a 'pst' method to the `SteenrodAlgebra` class, so you can do things like `A = SteenrodAlgebra(2); A.Sq(5,1)` to define elements.  Also, there were minor fixes and some coercion issues which I've more or less straightened out -- see the discussion here:
[http://groups.google.com/group/sage-support/browse_frm/thread/991cc3d21feddcf4/38b6e42d29b0f3d8?lnk=gst&q=coercion#38b6e42d29b0f3d8](http://groups.google.com/group/sage-support/browse_frm/thread/991cc3d21feddcf4/38b6e42d29b0f3d8?lnk=gst&q=coercion#38b6e42d29b0f3d8)

If you've made a lot of progress on changes, etc., then ignore this, and I'll work on incorporating my changes into your version when it's ready.

If I recall our conversation from late June correctly, the main thing still to be done here is to incorporate the default basis into the definition of a Steenrod algebra, so you would say 


```
  A = SteenrodAlgebra(2, 'milnor')
```


and then all elements of A will print in the Milnor basis (and similarly for other choices of basis).  Then the 'basis' method (which right now just prints a string) would be rewritten to coerce the element into a `SteenrodAlgebra` with the chosen basis, hence returning an actual element, not just printing a string. I can work on this, if you don't have the time right now.


---

Comment by jhpalmieri created at 2008-07-18 15:49:10

I had some spare time, so I've made the following changes: from the file 'steenrod_algebra.py', I split off another file: 'steenrod_algebra_element.py' -- this seems to be the style in sage/algebras.  I also now have the bases working as described in the previous comment.

Things still to be done: convert Milnor multiplication to Cython.  There are some minor coercion issues, also, which are minor enough that they don't need to be dealt with.  My previous comment has a thread describing one issue.  The other is with multiplication: if you multiply an element from `SteenrodAlgebra(2, 'milnor')` with an element from `SteenrodAlgebra(2, 'adem')`, it's not clear to me how the parent of the result is determined.  See this thread:
[http://groups.google.com/group/sage-devel/browse_frm/thread/f223018be64680d5](http://groups.google.com/group/sage-devel/browse_frm/thread/f223018be64680d5)

I also have not implemented anything of the form 


```
with steenrod.basis_serre_cartan:
     blah blah blah
```


but I'm not sure how important this is.  Having 


```
A = SteenrodAlgebra(2, 'serre_cartan')
x = Sq(2) * Sq(4)
A(x)   # or A(Sq(2)) * A(Sq(4)),  or A.Sq(2) * A.Sq(4)
```


might be good enough.

I'm wondering if it is worth while defining different methods for defining elements of the Steenrod algebra, depending on the basis.

Other than that, I have some more changes in mind, but they are for some time in the distant future (certainly after this has been reviewed, probably not for a while after that): implementing some other bases at odd primes, maybe implementing sub-Hopf algebras of the Steenrod algebra.


---

Attachment


---

Comment by was created at 2008-07-29 21:41:30

REFEREE REPORT:

It is frickin' awesome that this code is going to be in Sage!!

Here are some comments in order to make sure the code is absolutely the best quality.

STEENROD_ALGEBRA.PY

 * At the top of streenrod_algebra.py you do this:

```
r"""
Defining the mod $p$ Steenrod algebra.

AUTHORS:
    - John H. Palmieri (2008-07-17: version 0.8)

This package defines the mod $p$ Steenrod algebra, some of its
properties, and ways to define elements of it.  In this package,
elements in the Steenrod algebra are represented, by default, using
the Milnor basis.
```


Could you add a brief description here about what the Steenrod algebra is?  E.g., something like in Wikipedia that says "More precisely, for a given prime number p, it is a graded algebra over the field Z/p, the integers modulo p. Briefly, it is the algebra of all stable cohomology operations for mod p singular cohomology. It is generated by the Steenrod reduced pth powers, or Steenrod squares if p=2. The requirements of calculations of homotopy groups mean that homological algebra over the Steenrod algebra must be considered."

 * It would be nice if this returned a NotImplementedError instead of a TypeError, since presumably it will get implemented when there is a more general version of Generators:

```
sage: A5 = SteenrodAlgebra(5); A5
mod 5 Steenrod algebra
sage: A5.gens()
---------------------------------------------------------------------------
TypeError                 
```

 
 * " The following bases have been implemented in this package."  I don't like the passive voice.  Could you change it to: "In this package we implement the following bases:"

 * The line

```
Internal documentation: 
```

in steenrod_algebra.py should be all caps for consistency with REFERENCES, etc. 

 * The references section(s):

```
REFERENCES:
    [Mil] J. W. Milnor, "The Steenrod algebra and its dual," Ann. of Math.
          (2) 67 (1958), 150--171.
    [Mon] K. G. Monks, "Change of basis, monomial relations, and $P^s_t$
          bases for the Steenrod algebra," J. Pure Appl. Algebra 125 (1998),
          no. 1-3, 235--260. 
    [Woo] R. M. W. Wood, "Problems in the Steenrod algebra," Bull. London
          Math. Soc. 30 (1998), no. 5, 449--517. 
```

will get converted by latex to a single nasty line I think.

 * Just fyi you do not have to give me copyright at all if you don't want to.

```
...
#       Copyright (C) 2008 William Stein <wstein@gmail.com>
```


 * This seems like a bug or very bad error message to me:

```
sage: adem = SteenrodAlgebra(2, 'adem')
sage: adem.gen(100)
<type 'long'>
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/was/s/devel/sage-review/sage/algebras/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/algebras/steenrod_algebra.py in gen(self, i)
    381             raise ValueError, "%s is not a non-negative integer" % i
    382         if self.prime == 2:
--> 383             return self.Sq(self.prime**i)
    384         else:
    385             if i == 0:

/Users/was/s/local/lib/python2.5/site-packages/sage/algebras/steenrod_algebra.py in Sq(self, *nums)
    804         if self.prime == 2:
    805             dict = {nums: 1}
--> 806             return SteenrodAlgebraElement(dict, p=2, basis=self._basis_name)
    807         else:
    808             raise ValueError, "Sq is only defined at the prime 2"

/Users/was/s/local/lib/python2.5/site-packages/sage/algebras/steenrod_algebra_element.py in __init__(self, poly, p, basis)
    595                     if p == 2:
    596                         # when p=2, mono is a tuple of integers
--> 597                         trimmed = check_and_trim(mono)
    598                         if new_poly.has_key(trimmed):
    599                             coeff = F(poly[mono] + new_poly[trimmed])

/Users/was/s/local/lib/python2.5/site-packages/sage/algebras/steenrod_algebra_element.py in check_and_trim(nums)
    391         if not (isinstance(nums[i], (Integer, int)) and nums[i] >= 0):
    392             print type(nums[i])
--> 393             raise ValueError, "%s is not a non-negative integer" % nums[i]
    394     return nums[:index]
    395 

ValueError: 1267650600228229401496703205376 is not a non-negative integer
```


  * The doctest coverage is not 100% but needs to be:

```
D-69-91-158-184:algebras was$ sage -coverage .
...
steenrod_algebra.py: 100% (25 of 25)
steenrod_algebra_bases.py: 73% (14 of 19)
steenrod_algebra_element.py: 88% (44 of 50)
steenrod_milnor_multiplication.py: 100% (2 of 2)
steenrod_milnor_multiplication_odd.py: 66% (2 of 3)
```

so there are maybe some missing doctests for steenrod_algebra_bases.py and steenrod_algebra_element.py and steenrod_milnor_multiplication_odd.py.  (That said, GEES, you have an incredibly good number and quality of doctests overall in this package!  Lauditory!)

 * I'm guessing the TeX here is wrong:

```
        The element $Q_n0 Q_n1 ...$, given by specifying the subscripts.
```


 * It seems like you give the full text for the different Steenrod bases twice -- once at the top of the file steenrod_algebra.py and once in the function SteenrodAlgebra.  Choose one place and refer to the other.

 * In the source code in steenrod_algebra.py you have this:

```
"""
These are the recognized basis names.  For the Milnor and Serre-Cartan
bases, give a list of synonyms:
"""

_steenrod_milnor_basis_names = ['milnor']
_steenrod_serre_cartan_basis_names = ['serre_cartan', 'serre-cartan', 'sc',
                                         'adem', 'admissible']

```

I think the """'d part should be replaced by comments.  At least that's what I would do. This isn't really a big deal

```
# These are the recognized basis names.  For the Milnor and Serre-Cartan
# bases, give a list of synonyms:
```




STEENROD_ALGEBRA_BASES.PY

 * Heh, a long list of all the bases seems to be given a third time.

 * Otherwise this file looks good.  Some of the comments about steenrod_algebra.py apply here, e.g., to the list of references.

STEENROD_ALGEBRA_ELEMENT.PY

 * The documentation for Sq says it takes as input a "list", but it doesn't:

```
sage: Sq([4,3])
---------------------------------------------------------------------------
TypeError      
```

In fact, one would have to do

```
sage: Sq(*[4,3])
Sq(4,3)
```

or

```
sage: Sq(4,3)
Sq(4,3)
```

This could cause confusion.  Clear things up in the docs or also allow a list as input.


Overall positive review pending addressing the above issues.


---

Comment by jhpalmieri created at 2008-07-30 01:48:46

Thanks for all of the comments.  Two questions about doctests: if I write the gens() method so that it raises a `NotImplementedError`, how do I write a doctest for that?

Also, if I have one function nested inside another:

```
def outer(x)
    """
    lots of documentation here, including examples
    """
    def inner(y)
        return y^2 + 1

    return inner(x) - 2
```

how do I write doctests for `inner`?  That is, how do I tell sage to call inner?  I don't know how to access that function...


---

Comment by was created at 2008-07-30 12:36:38

> Thanks for all of the comments. Two questions about doctests: if I write the gens() 
> method so that it raises a NotImplementedError, how do I write a doctest for that? 

Here is how to format exceptions for doctests:

```
sage: a = 5
sage: a.gens()
Traceback (most recent call last):
...
AttributeError: 'sage.rings.integer.Integer' object has no attribute 'gens'
```

If you use the notebook and click on "Text" in the upper right, it will do this automatically with exceptions. 

Regarding nested functions, we should remove those from being tested by coverage.  You don't have to doctest them.  It is planned to change the coverage script to address this.


---

Comment by jhpalmieri created at 2008-07-31 03:24:25

Replying to [comment:6 was]:

> Could you add a brief description here about what the Steenrod algebra is?  

I've done this. 

>  * It would be nice if this returned a NotImplementedError instead of a TypeError, since presumably it will get implemented when there is a more general version of Generators:

Done.

>  * " The following bases have been implemented in this package."  I don't like the passive voice.

Changed.

> 
>  * The line "Internal documentation:" in steenrod_algebra.py should be all caps for consistency with REFERENCES, etc. 

Okay.

> 
>  * The references section(s) will get converted by latex to a single nasty line I think.

Fixed.

>  * Just fyi you do not have to give me copyright at all if you don't want to.

Okay, I've take you out.  (I don't care that much, but this way, people are less likely to think you wrote it, so they won't direct any technical questions about the package to you.)

>  * This seems like a bug or very bad error message to me:

Fixed (and included a new doctest verifying this).

>   * The doctest coverage is not 100% but needs to be:

Now the only missing doctests are for nested functions.

>  * I'm guessing the TeX here is wrong:
> {{{
>         The element $Q_n0 Q_n1 ...$, given by specifying the subscripts.
> }}}

Fixed (along with various other little TeX problems).
 
>  * It seems like you give the full text for the different Steenrod bases twice.

Now only one time: in the docs for 'steenrod_algebra_basis', and the other places now just refer to this.

> """
> These are the recognized basis names.  For the Milnor and Serre-Cartan
> bases, give a list of synonyms:
> """

> I think the """'d part should be replaced by comments.  At least that's what I would do. This isn't really a big deal

Done

> STEENROD_ALGEBRA_ELEMENT.PY

>  * The documentation for Sq says it takes as input a "list", but it doesn't:

Fixed the documentation.

> Overall positive review pending addressing the above issues. 


Other changes: miscellaneous rewordings and TeX fixes in the documentation, and I added a few INPUT and OUTPUT blocks where they were missing before. I now have a doc patch which inserts relevant sections into the reference manual, and running this through the reference manual helped me to find various TeX errors.  I found one pretty serious bug in steenrod_algebra_bases.convert_to_milnor_matrix, and fixed that.  (The only other changes in the actual code, as opposed to the documentation: (1)  I found one little function which I had written twice, once in the elements file and once in the bases file, so now I just have one and import it in the other.  (2) In steenrod_algebra_bases, I was using a `@`memoize decorator, but it was messing up my docstrings, so I now do the memoization by hand, by explicitly defining dictionaries in which to cache things.)


---

Comment by jhpalmieri created at 2008-07-31 03:24:58

doc patch: add Steenrod algebra stuff to reference manual


---

Attachment

new version of Steenrod algebra package, incorporating changes suggested by was


---

Attachment


---

Attachment

Excellent.  Positive review.  This is ready to go in!

I added a small patch that changes LaTeX to latex, and fixes a few latex typos. 

Mabshoff, to apply this apply:

 * 3397-2008-07-30-doc.patch 
 * 3397-2008-07-30-main.patch
 * sage-3397-apply_after-3397-2008-07-30-main.patch


---

Comment by mabshoff created at 2008-08-10 08:59:00

Resolution: fixed


---

Comment by mabshoff created at 2008-08-10 08:59:00

Merged the above patches as William suggested in Sage 3.1.alpha1
