# Issue 5132: [with patch, needs review] real numbers don't support __mod__

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-01-30 01:01:03

Assignee: somebody


```
sage: 10.0 % 2r
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/burcin/.sage/temp/karr/24765/_home_burcin__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

TypeError: unsupported operand type(s) for %: 'sage.rings.real_mpfr.RealLiteral' and 'int'
```


A quick look through sage/rings/real_mpfr.pyx reveals that there is no `__mod__` method defined.

MPFR documentation here:

http://www.mpfr.org/mpfr-current/mpfr.html#Integer-Related-Functions

suggests that one of `mpfr_fmod()` or `mpfr_remainder()` should be used, depending on the desired rounding properties. Since I live blissfully in the exact arithmetic world, I have no idea which one is more suitable for Sage.

Nevertheless, a patch that uses `mpfr_remainder()` is attached.


---

Attachment

This is a duplicate of #825.


---

Comment by mhansen created at 2009-02-02 07:14:40

Looks good to me.  This also fixes the broken example reported at #825.


---

Comment by mabshoff created at 2009-02-02 07:27:05

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 07:27:05

Resolution: fixed
