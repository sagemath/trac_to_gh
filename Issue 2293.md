# Issue 2293: word_problem error in AbelianGroup

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-02-24 15:33:04

Assignee: joyner


```
sage: sage: A.<a,b,c,d,e> = AbelianGroup(5,[4, 5, 5, 7, 8])
sage: wp = word_problem([a,b,c,d,e],a); wp
[This is the Trac macro *a, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a, 1-macro)
```

is okay but all these are wrong:

```
sage: wp = word_problem([a,b,c,d,e],b); wp
[This is the Trac macro *a, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a, 1-macro)
sage: wp = word_problem([a,b,c,d,e],c); wp
[This is the Trac macro *a, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a, 1-macro)
sage: wp = word_problem([a,b,c,d,e],d); wp
[This is the Trac macro *a, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a, 1-macro)
sage: wp = word_problem([a,b,c,d,e],e); wp
[This is the Trac macro *a, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a, 1-macro)
```




---

Comment by wdj created at 2008-02-24 18:41:42

Please see
http://trac.sagemath.org/sage_trac/ticket/2292
for the patch.


---

Comment by mhansen created at 2008-02-27 22:20:45

The patch for #2292 fixes this.


---

Comment by mabshoff created at 2008-02-27 23:10:18

Fixed due to the patch at #2292 merged in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-27 23:10:18

Resolution: fixed
