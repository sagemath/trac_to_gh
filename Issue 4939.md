# Issue 4939: massive performance regression to primes_first_n

Issue created by migration from https://trac.sagemath.org/ticket/4939

Original creator: was

Original creation time: 2009-01-05 02:16:50

Assignee: was

This is a doctest in arith.py:

```
    This is very fast, because we leave the output as a PARI object:
        sage: v = primes_first_n(10^6, leave_pari=True)
        sage: len(v)
```

In fact, the above is now way way slower than doing leave_pari=False!  So the doctest is blatantly wrong multiple times.   It also says:

```
        leave_pari -- bool (default: False) if True the returned list
                    is a PARI list; this is *vastly* (10 times!)
```


On sage.math it is not very fast, and also uses 1.5GB RAM, which is a major problem for doctesting this on my build farm, where some machines have only 1GB RAM.  Also, I don't think it is reasonable to require 1.5GB RAM for standard doctests.

```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: time v = primes_first_n(10^6,leave_pari=True)
CPU times: user 24.42 s, sys: 0.63 s, total: 25.05 s
Wall time: 25.05 s
sage: get_memory_usage()
1454.27734375
```

| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
For comparison:

```
wstein@sage:~/sage/devel/sage/sage/rings$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: time v = primes_first_n(10^6, leave_pari=False)
CPU times: user 0.42 s, sys: 0.19 s, total: 0.61 s
Wall time: 0.61 s
sage: get_memory_usage()
927.67578125
```

| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
The documentation also says:
{{
However, PARI integers are much different than                                      
SAGE integers.  If you use this option the lower                                   
bound must be 2.         
}}}
which is patently false now.

An easy fix is to get rid entirely of the leave_pari=True option.  It was only ever there because it used to be really fast.  But now it is 50% better. 

The problem is also in prime_range:

```
sage: time w = prime_range(10^6)                                                                                                                     
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s
sage: time w = prime_range(10^6,leave_pari=True)
CPU times: user 0.95 s, sys: 0.02 s, total: 0.97 s
Wall time: 0.97 s
```


The easiest solution is to simply delete all this "leave_pari" stuff.  It's totally useless, bad from an api point of view, and gains only a little speed.  Writing code against this api that uses the option would be particularly stupid, since in the feature we could easily have a native prime_range that is way faster than pari's, hence code that tries to be clever would be slower.


---

Attachment


---

Comment by craigcitro created at 2009-01-05 04:57:50

Yep, looks good.


---

Comment by cremona created at 2009-01-05 09:54:19

Here's what is taking the time when leave_pari=True:

```
sage: time p=pari.prime_list(10^6)
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.09 s
sage: len(p)
1000000
sage: time c=p[0:]
CPU times: user 45.05 s, sys: 0.54 s, total: 45.59 s
Wall time: 46.20 s
sage: time c=p
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07 s
```

If you were to change the line 

```
   if leave_pari:
        return v[m:]
```

to

```
   if leave_pari:
        if m==0: 
              return v
        return v[m:]
}}} 
then it would have been faster.  But as William said, this option seems not to be worth keeping anyway.


---

Comment by was created at 2009-01-05 17:10:59

I have opened #4941 to address the massive performance issue with pari list slicing.


---

Comment by mabshoff created at 2009-01-06 01:53:24

Merged in Sage 3.2.3.post-final

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-06 01:53:24

Resolution: fixed
