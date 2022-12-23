# Issue 4556: [with patch, needs review] nth_root for finite fields: document the fact that 'extend' is not implemented

Issue created by migration from https://trac.sagemath.org/ticket/4556

Original creator: jhpalmieri

Original creation time: 2008-11-19 22:21:10

Assignee: somebody

Keywords: finite field, nth_root

From a discussion on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/a01375b02a8a65a0):

The documentation for the nth_root method for finite fields (repeated
in each of the files sage/structure/element.pyx, sage/rings/
finite_field_element.py, and sage/rings/finite_field_givaro.pyx) says
this:

```
        INPUT:
            n -- integer >= 1 (must fit in C int type)
            extend -- bool (default: True); if True, return a square
                 root in an extension ring, if necessary. Otherwise,
                 raise a ValueError if the square is not in the base
                 ring.
            all -- bool (default: False); if True, return all square
                 roots of self, instead of just one.

        OUTPUT:
           If self has an nth root, returns one (if all == False) or a list of
           all of them (if all == True).  Otherwise, raises a ValueError (if
           extend = False) or a NotImplementedError (if extend = True).
```

The entirety of the code dealing with 'extend' is this:

```
        if extend:
            raise NotImplementedError
```

The non-implementation of the 'extend' option needs to be documented.  I've changed the docstrings to reflect this.  Also, "square root" needs to be changed to "nth root" several times.

(The 'extend' issue also applies to the square_root method in finite_field_element.py.
The code for the sqrt method in finite_field_givaro.pyx is similar,
but the extend option, while present, isn't documented.)

I'm attaching a patch to deal with these issues.



---

Attachment


---

Comment by robertwb created at 2008-11-20 01:30:50

Just glancing at it it looks good.


---

Comment by robertwb created at 2008-11-21 06:55:22

Got a chance to look at it more. Thanks.


---

Comment by mabshoff created at 2008-11-21 09:37:47

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 09:37:47

Merged in Sage 3.2.1.alpha0
