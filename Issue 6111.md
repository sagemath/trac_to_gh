# Issue 6111: [with patch; needs review] review symbolics in sage-4.0 (switch to pynac)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-05-21 09:44:00

Assignee: burcin

CC:  mhansen

Get sage-4.0.rc0 from 

http://sage.math.washington.edu/home/wstein/build/sage-4.0.rc0/dist/

which is stable and has all the new symbolics code in it. 

You can also do:

./sage -upgrade http://sage.math.washington.edu/home/wstein/build/sage-4.0.rc0/

Note that the code for symbolics is one big flattened patch.  The only way to referee it is is to read straight through all of devel/sage/sage/symbolics, devel/sage/sage/calculus, and also look at the diff outside of those two directories at the patch to see what else was changed. 




---

Comment by was created at 2009-05-21 21:20:24

TODO: This doctest in infinity.py was commented out.  When uncommented we get a total hang:

```
            sage: bool(SR(oo) == sympy.oo)
```


This is what we get:

```
sage:             sage: bool(SR(oo) == sympy.oo)
terminate called after throwing an instance of 'std::runtime_error'
  what():  indeterminate expression: Infinity - Infinity encountered.


^V^C^C^C^C^C^C^Z
```


I'm uncomenting this in my referee patch.


---

Comment by robertwb created at 2009-05-22 02:44:15

I read through the first 2500 lines of expression.pyx earlier today, and it's looking good so far (collecting minor fixes into a patch). I won't be looking at it again until much later tonight.


---

Attachment

Finished reading expression.pyx, it looks good. Should this work:


```
sage: ((x+y)^9).polynomial(None, ring=ZZ['x']['y']).list()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "expression.pyx", line 3616, in sage.symbolic.expression.Expression.polynomial (sage/symbolic/expression.cpp:17320)
  File "/home/robertwb/sage-4.0.rc0-x86_64-Linux/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 975, in polynomial
    converter = PolynomialConverter(ex, base_ring=base_ring, ring=ring)
  File "/home/robertwb/sage-4.0.rc0-x86_64-Linux/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py", line 833, in __init__
    raise TypeError, "%s is not a variable of %s" %(v, ring)
TypeError: y is not a variable of Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Integer Ring
```


Also, there are a lot (too many IMHO) aliases for simplify_radical


```
    radical_simplify = simplify_log = log_simplify = simplify_radical
    simplify_exp = exp_simplify = simplify_radical
```



---

Comment by burcin created at 2009-05-24 15:22:49

Some comments after reading the changesets to pynac after the unreleased 0.1.6 version (numbers next to the bullets refer to changesets in the repository from the pynac-0.1.7.spkg file):


 * 90:fb6582f9bd81 

 isn't this already handled by the first lines of pyExpression_to_ex() in pynac.pyx?
 * 88:25d02eeb427d 

 we should add error checking to py_get_constant() call, we can't guarantee that a constant with the same name will be available between different versions of Sage
 * 84:7b3272f4b4bf  is mine, author field lists Mike
 * 82:da7d7a220723  evalf for constants using a lookup table

 I already commented on this on IRC and the devel list. ginac/pynac already provides a framework to handle this, I would like to revert this in a future version. My previous message:
 http://groups.google.com/group/sage-devel/msg/dc46d9d94dd31b5e (scroll to the paragraph below the bullet items)

I will try to prepare a new package which fixes the version numbers of the library and error handling of py_get_constant().


---

Comment by burcin created at 2009-05-24 19:59:52

New package which adds error handling for py_get_constant() and changes the library version to 0.1.7 is here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.7-r1.spkg

Changing the version numbers of the library might expose some modules in the Sage library which should be rebuilt when the package is updated. The fix is to add a dependency to the pynac header in module_list.py. I didn't try to see which files need this, since my tree wasn't clean and all the relevant files (sage/symbolic/* is more than enough) got rebuilt for me.

Answering my own comments above, I see that the patch I sent Mike for changeset 84 didn't have hg headers, and returning None from eval or derivative methods is a good trick to halt the evaluation. The evalf function for constants is still as it is, I don't think it's a good idea to introduce big changes at this stage.

Thanks everyone for all the work to make the switch, I still can't believe we're almost there.

Cheers,

Burcin


---

Attachment

I like it!  I quickly read through all of sage/symbolic except for expression.pyx, and attached a patch fixing the issues I found.  Technically somebody else should review sage/symbolic/random_tests.py, since I wrote the original version; but if you do, be sure to review rc0+my reviewer patch, since the reviewer patch adds doctests.

So: positive review for sage/symbolic/* except for expression.pyx (which I didn't look at) and random_tests.py (which I can't review since I wrote it).


---

Attachment

I read through most everything outside of symbolics/ and made a few little touchups in my attached patch.  Positive review for this part as well.


---

Attachment


---

Comment by mhansen created at 2009-05-28 02:42:20

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 02:42:20

I looked over the first three patches, and they look good to me.

I added a fourth patch which fixes a segfault that wstein's patch uncovers.


---

Comment by mhansen created at 2009-05-28 02:42:20

Changing assignee from burcin to mhansen.


---

Comment by was created at 2009-05-28 06:26:43

Regarding, `sage: ((x+y)^9).polynomial(None, ring=ZZ['x']['y']).list()` --> boom, none of the above patches address this.  However, this ring option didn't even exist in sage < 4.0, so I'm not going to hold this ticket up for this.


---

Comment by mhansen created at 2009-05-28 06:41:30

Merged in 4.0.rc1.


---

Comment by mhansen created at 2009-05-28 06:41:30

Resolution: fixed
