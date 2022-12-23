# Issue 5722: fast callable pow

Issue created by migration from https://trac.sagemath.org/ticket/5722

Original creator: robertwb

Original creation time: 2009-04-09 02:15:41

Assignee: somebody

CC:  cwitty

pow(double, double) inconsistent for bad input. See extensive documentation in floatobject.c


---

Comment by mabshoff created at 2009-04-09 02:41:39

Oops, I spoke too soon in person. There are two doctest failures that need fixing:

```
sage -t -long "devel/sage/sage/ext/fast_callable.pyx"       
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/ext/fast_callable.pyx", line 2213:
    sage: fast_callable(sin(x)/x, vars=[x], domain=RDF).get_orig_args()
Expected:
    {'domain': Real Double Field, 'code': [0, 0, 16, 0, 0, 7, 2], 'py_constants': [], 'args': 1, 'stack': 2, 'constants': []}
Got:
    {'domain': Real Double Field, 'code': [0, 0, 16, 0, 0, 8, 2], 'py_constants': [], 'args': 1, 'stack': 2, 'constants': []}
**********************************************************************
1 items had failures:
```

And

```
sage -t -long "devel/sage/sage/ext/gen_interpreters.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/ext/gen_interpreters.py", line 2772:
    sage: print buff.getvalue()
Expected:
        case 7: /* div */
          {
            double i1 = *--stack;
            double i0 = *--stack;
            double o0;
            o0 = i0 / i1;
            *stack++ = o0;
          }
          break;
    <BLANKLINE>
Got:
        case 8: /* div */
          {
            double i1 = *--stack;
            double i0 = *--stack;
            double o0;
            o0 = i0 / i1;
            *stack++ = o0;
          }
          break;
    <BLANKLINE>
<SNIP>
```


I think that just the doctests need to be updated, but I will leave this to you :)

Cheers,

Michael


---

Comment by robertwb created at 2009-04-09 06:29:31

Yes, those are both inconsequential ordering issues.


---

Comment by mabshoff created at 2009-04-09 06:52:07

Hi Robert,

there are actually two more doctest failure that I cut off since the failure message is quite long:

```
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/ext/gen_interpreters.py", line 3592:
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/ext/gen_interpreters.py", line 3608:
```

Sorry for causing confusion ;)

But the other doctest failures are fixed.

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2009-04-09 07:53:22

OK, all doctests in that file pass now.


---

Comment by mabshoff created at 2009-04-09 18:52:19

Positive review. Doctests do pass :). 

I also read the patch and I am happy with it.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 18:52:52

Resolution: fixed


---

Comment by mabshoff created at 2009-04-09 18:52:52

Merged in Sage 3.4.1.rc2.

CCing cwitty so he is aware of this patch. 

Cheers,

Michael
