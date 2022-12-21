# Issue 6109: Bring documentation for QQbar up to 100% and add to reference manual

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-05-21 08:29:20

Assignee: tbd

CC:  cwitty

Keywords: QQbar documentation

This is not good:

sage/rings/qqbar.py
SCORE sage/rings/qqbar.py: 40% (110 of 272)

and we also need to put this into the reference manual.  It is not totally clear which section, so I'll start out by putting it into number_fields.rst.

I discovered this while trying to actually use the class, of course...so I will have a go but might need to consult Carl.


---

Comment by cremona created at 2009-05-21 08:43:33

I should have said:  there is an excellent block of nearly 500 lines at the beginning of qqbar.py, -- all the more reason to get that into the manual!


---

Attachment

Part 1: applies to 4.0.alpha0


---

Comment by cremona created at 2009-05-21 11:38:50

The first patch converts the docstrings to ReST and put the file into the reference manual, so it looks ok. Still to do:
    1. Reformat the docstrongs which do exist into standard layout (with INPUT/OUTPUT blocks etc)
    2. Add docstrings for 162 functions which do not yet have them (!)
    3. Add doctests to those and the few function which have docstrings but no doctests.

I have taken the liberty of adding "needs review" already despite not having increased the coverage at all yet, since I do actually believe that this should go in already.  there is a huge amount of very useful code here which deserves better publicity (as I think having it in the reference manual will do) and there is already plenty of documentation.  Having been through this file, I can see that I should be using QQbar much more than I have done up to now.

I am not promising to work on tasks 1-3 above i nthe near future, so if anyone else wants to make a start they should go ahead.


---

Comment by cremona created at 2009-05-22 08:36:43

Suggestion for Carl:  I think that the functions norm() and conjugate() on QQbar are not very useful.  I would change the name of conjugate() to complex_conjugate().

I would like to see new functions conjugates(), norm(), trace():

   * a.conjugates()  returns a.minpoly().roots(QQbar,multiplicities=False)
   * a.norm()  returns a.minpoly().constant_coefficient()  (* correct sign)
   * a.trace() returns -a.minpoly().coeffs()[a.degree()-1]

The more I look at qqbar.py the more impressed I am!

John


---

Comment by davidloeffler created at 2009-05-28 10:37:07

The patch applies fine to 4.0.rc1, and qqbar.py passes doctests (unsurprisingly, since the patch doesn't actually change any tests). The key thing is the documentation, which complies fine except for one small glitch:


```
reading sources... sage/rings/qqbar
WARNING: /home/david/sage-4.0.rc1/local/lib/python2.5/site-packages/sage/rings/qqbar.py:docstring of sage.rings.qqbar:81: (ERROR/3) Unexpected indentation.
```


I can't remotely pin down what it is that's upsetting the Sphinx parser. If you delete the entire offending docstring -- the big one at the top of the file -- you get the same "unexpected indentation" error message again, but purporting to be coming from the docstring of some other random function, and if you go through several iterations of deleting docstrings it starts claiming that there is an unexpected indentation at line 0. This sounds rather like a Sphinx bug to me, especially as the finished documentation looks absolutely fine.

I agree with John that the benefits of getting QQbar into the reference manual make it worth merging this patch now -- let's have a new ticket for adding the missing doctests.

David


---

Comment by cremona created at 2009-05-28 11:05:58

Thanks, David -- I spent ages trying to track down that error but without success.  I should have mentioned that when I posted the patch.


---

Attachment

one-line ReST fix


---

Comment by davidloeffler created at 2009-05-28 13:01:58

Found it: here's a one-line patch that adds a missing blank line before a doctest block. (I have found several other similar glitches in the reference manual, which I'm about to open a ticket for.)


---

Comment by cremona created at 2009-05-28 17:32:50

That is amazing -- the line given in the error message is miles away from the actual error.

We can now definitely give thie a +1 and it can rather safely be merged!


---

Comment by mhansen created at 2009-06-01 00:00:26

Merged both patches in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 00:00:26

Resolution: fixed
