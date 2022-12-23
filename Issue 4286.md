# Issue 4286: [with patch, needs review] minor improvements to old integer code

Issue created by migration from https://trac.sagemath.org/ticket/4286

Original creator: robertwb

Original creation time: 2008-10-14 19:49:00

Assignee: somebody

just cleaning up some cruft


---

Comment by GeorgSWeber created at 2008-10-14 22:53:33

Tired as I am, I only write down some remarks from "pure reading":

1. The (new) lines 3636 and 3682 ("return v[0]") should perhaps be:

   return as_Integer(v[0])

i.e. with the explicit (eventual) conversion of v[0] to a Sage integer. Probably that is done by the compiler implicitly. But anyway, the code would display even more visibly its intention what it is doing.

2. I'm unsure whether the macro "PY_TYPE_CHECK" is allowed to be used inside _sig_on / _sig_off. And even if it is for the time being, a future change of that macro using some more pythonics might bombastically break the new code this patch brings --- at runtime. (It's implicitly used in lines 3639, 3641, 3685, 3687 inside "as_Integer".)

3. The line 3523 ("if mpz_cmp_ui(m.value, 1) == 0:"). If I was a puricist, I'd say it should be replaced by the four lines:
   
   _sig_on
   r = mpz_cmp_ui(m.value, 1)
   _sig_off
   if r == 0:

Thus this "external" function call to GMP is wrapped by _sig_on/_sig_off, too.
(The variable r is destroyed in the very next line anyway.)


---

Attachment

Thanks for looking at this. I've attached a new patch that should address your comments. The type checking has been pulled out of the main loop which addresses 1 and 2, which was actually an issue in the old code as well. (Note that isinstance will be a fast typecheck in the next release of Cython). 

As for (3), there is no reason to put _sig_on/_sig_of around mpz_cmp_ui. These signal handlers are used for long-running code (where one wants to be able to intercept control-C) or code that might raise other signals/abort. mpz_cmp_ui is not such a function (in fact, it's a simple macro).


---

Comment by GeorgSWeber created at 2008-10-16 20:19:58

Thanks for cleaning up this old code.

The following very minor issues do certainly not prevent me from giving this patch "as is" a positive review, but I thought I should write them down nevertheless:

4. By the patch file, only "def LCM_list" becomes "cpdef LCM_list". One might also change "def GCD_list" into "cpdef GCD_list", at least for 3.1.3.rc0 (which is the youngest version I currently have and where this is otherwise not the case), if only for consistency. (I do not know enough about the difference between "def" and "cpdef" yet, but I do trust you there.)


5. Again for consistency (or beauty?) only, one could make the two lines 2129/2130

```
cdef Integer z
z = PY_NEW(Integer)
```

into the one line

```
cdef Integer z = <Integer>PY_NEW(Integer)
```

(And again I do not enough about using "<Integer>" or not as a type qualifier, but yet again I trust you there.)


---

Comment by mabshoff created at 2008-10-18 20:32:35

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 20:32:35

Merged in Sage 3.2.alpha0


---

Comment by cremona created at 2008-10-22 12:59:33

Remark: This patch introduced a bug:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |
| Type notebook() for the GUI, and license() for information.        |
sage: sage.rings.integer.GCD_list([2,2,3])
2
```


The problem is in line 3654 of integer.pyx where there is a
missing ==0 so the break occurs immediately where it shouldn't.

This will be fixed in a patch at #3118, so there is no need to reopen this ticket.
