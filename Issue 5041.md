# Issue 5041: make it so the magma .sig files in extcode don't get written there by magma

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-20 23:34:43

Assignee: was

If one installs sage sytem wide, and a user tries to run any magma commands, and the .sig files aren't written in data/extcode/magma, then BOOM!  This is a total show stopper for any "normal users" to use the sage magma interface for anything serious.  This must be FIXED!

To fix this, when the magma interface is first run, make sure to copy the .m files over to $DOT_SAGE/magma first and load from there.   One will have to do the copy the first time the magma interface is started in any magma session.   alternatively, one could try: except: the magma.load command, and if it fails, then try to copy and load from /tmp/, say or DOT_SAGE/temp/.  Maybe the second idea is cleaner. 


---

Comment by was created at 2009-01-22 11:33:41

The attached patch does the following:

(1) Deletes magma/ell_padic and magma/padic_height which were only there for p-adic height computations before sage got its own much better native code.   Also, deletes the file SAGE_ROOT/devel/sage/sage/schemes/elliptic_curves/ell_padic.py, which was slated for deprecation officially several months ago, and just wraps those files.

AND

(2) The first (and only first) time a Magma interface is started in a given session, it copies over data/extcode/magma to a temp directory.   This directory is only 52 kilobytes, so this is fast and easy.  It will not grow much, since it is all hand written.    This is new code in magma.py.  It's just a few lines.  By doing this, all extcode code for mamga that we ever write can easily be attached without permission issues. 

TO TEST:
(0) Apply all patches

(1) doctest elliptic curves to make sure my removal of deprecated code didn't break anything:

```
$ sage -tp 3 devel/sage/sage/schemes/elliptic_curves/
```


(2) doctest the entire magma interface optional test code to make sure I didn't break anything:

```
$ ./sage -t -only_optional=magma devel/sage/sage/
```


(3) Read the source code modified in my patch to magma.py.


---

Attachment


---

Comment by malb created at 2009-01-22 20:35:52

> (0) Apply all patches

Works.
 
> (1) doctest elliptic curves to make sure my removal of deprecated code didn't break anything:

Works.

> (2) doctest the entire magma interface optional test code to make sure I didn't break anything:

Works. Also no .sig files are created in the extcode directory.

> (3) Read the source code modified in my patch to magma.py.

Looks good.


---

Comment by mabshoff created at 2009-01-23 08:03:42

Merged both patches in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 08:03:42

Resolution: fixed
