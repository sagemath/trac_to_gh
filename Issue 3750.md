# Issue 3750: Request for a "log" function for Sage integers

Issue created by migration from https://trac.sagemath.org/ticket/3750

Original creator: ljpk

Original creation time: 2008-07-31 17:49:30

Assignee: somebody

The following command


```
sage: N=8
sage: N.log(2)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/ljpk/<ipython console> in <module>()

AttributeError: 'sage.rings.integer.Integer' object has no attribute 'log'
```


returns an error (as does N.exp()). Would it be possible to add a function to the Sage integers class which worked like the ones for the real numbers?


```
sage: N=8.0
sage: N.log(2)
3.00000000000000
sage: N.exp()
2980.95798704173
```




---

Comment by kcrisman created at 2008-10-23 13:40:03

Changing status from new to assigned.


---

Comment by kcrisman created at 2008-10-23 13:40:03

Changing assignee from somebody to kcrisman.


---

Comment by mhansen created at 2008-10-24 03:30:48

I think that log should default to base 'e' as it does with all the other types.  Also both of them should probably take an optional number of bits of precision to use with the default being 53.


---

Comment by was created at 2008-10-24 04:39:56

Somebody should point out the exact_log function in this discussion since it is relevant to the original poster and is superfast:

```
sage: N = 8
sage: N.exact_log(2)
3
```



---

Comment by kcrisman created at 2008-10-25 00:09:02

Replying to [comment:2 mhansen]:
> I think that log should default to base 'e' as it does with all the other types.  Also both of them should probably take an optional number of bits of precision to use with the default being 53.

Know what, I don't think I even realized that m was mandatory the way I wrote it - yes, obviously it should default to natural log.  I like the idea of specifying precision in the function itself as well - good comments.


---

Attachment


---

Comment by kcrisman created at 2008-10-26 00:17:50

The patch now should deal with both of the reviewer's comments.


---

Comment by mhansen created at 2008-10-26 00:24:53

Hmm... there's an issue that before log(3) would just give log(3) since 3 is exact.  After the patch, log(3) will automatically give an approximation which probably isn't desired.


---

Comment by was created at 2008-10-26 22:13:12

Mike, Good point about log(3).  This should be dealt with the same way as with sqrt:

```
sage: 3.sqrt()
sqrt(3)
sage: 3.sqrt(prec=53)
1.73205080756888
```



---

Comment by kcrisman created at 2008-10-30 18:45:58

As long as everyone is okay with 

```
sage: log(1024, 2)
10
```

instead of the previous behavior of 

```
sage: log(1024, 2)
log(1024)/log(2)
```

then the last version of the patch should address all concerns raised above.  Thanks to mhampton for sleuthing down that one must use ** for exponentiation outside the interpreter when I got confused.


---

Attachment

Based on 3.2.alpha0


---

Comment by mhansen created at 2008-11-04 21:42:14

Nice work!  I'm pretty happy with how this turned out.


---

Comment by mabshoff created at 2008-11-05 18:53:07

When I merge integer-log-exp-final.patch I get one doctest failure:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3$  ./sage -t -long devel/sage/sage/coding/linear_code.py
sage -t -long devel/sage/sage/coding/linear_code.py         
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1123:
    sage: Cc = C.galois_closure(GF(2))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[3]>", line 1, in <module>
        Cc = C.galois_closure(GF(Integer(2)))###line 1123:
    sage: Cc = C.galois_closure(GF(2))
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 1141, in galois_closure
        if not(a.integer_part() == a):
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'integer_part'
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1124:
    sage: C; Cc
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[4]>", line 1, in <module>
        C; Cc###line 1124:
    sage: C; Cc
    NameError: name 'Cc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1132:
    sage: c2 in Cc
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[9]>", line 1, in <module>
        c2 in Cc###line 1132:
    sage: c2 in Cc
    NameError: name 'Cc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1541:
    sage: Cc = C.galois_closure(GF(2))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_35[3]>", line 1, in <module>
        Cc = C.galois_closure(GF(Integer(2)))###line 1541:
    sage: Cc = C.galois_closure(GF(2))
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 1141, in galois_closure
        if not(a.integer_part() == a):
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'integer_part'
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1547:
    sage: c2 in Cc
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_35[8]>", line 1, in <module>
        c2 in Cc###line 1547:
    sage: c2 in Cc
    NameError: name 'Cc' is not defined
**********************************************************************
2 items had failures:
   3 of  10 in __main__.example_21
   2 of   9 in __main__.example_35
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/.doctest_linear_code.py
	 [30.6 s]
exit code: 1024
```


Cheers,

Michael


---

Attachment

I've attached a patch which fixes the issue.


---

Comment by kcrisman created at 2008-11-06 14:49:32

This works!  I was going to use q.is_power_of(q0), but as far as I can tell there isn't any meaningful difference between these solutions.  Use integer-log-exp-final.patch and trac_3750-fix.patch.  I assume I can review mhansen's fix; if not, my apologies.

To be honest, how was this working before, when the symbolic logs didn't have an integer_part() method to begin with?


---

Comment by mabshoff created at 2008-11-09 18:18:44

Merged integer-log-exp-final.patch and trac_3750-fix.patch in Sage 3.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-09 18:18:44

Resolution: fixed
