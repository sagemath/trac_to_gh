# Issue 4988: major easy-to-fix but STUPID bug in gcd

Issue created by migration from https://trac.sagemath.org/ticket/4988

Original creator: was

Original creation time: 2009-01-16 21:12:25

Assignee: was

This is stupid:


```
sage: gcd(3,6,2)
3
```


The problem is that there is an undocumented mysterious and not even used integer third input!

```
File:        /Users/was/s/local/lib/python2.5/site-packages/sage/rings/arith.py
Type:        <type 'function'>
Definition:  gcd(a, b, integer, **kwargs)
Docstring: 

    The greatest common divisor of a and b, or if a is a list and b is
    omitted the greatest common divisor of all elements of a.

    INPUT:
        a,b -- two elements of a ring with gcd
    or
        a -- a list or tuple of elements of a ring with gcd

    Additional keyword arguments are passed to the respectively called
    methods.

    EXAMPLES:
        sage: GCD(97,100)
        1
        sage: GCD(97*10^15, 19^20*97^2)
        97
        sage: GCD(2/3, 4/3)
        2/3
        sage: GCD([2,4,6,8])
        2
        sage: GCD(srange(0,10000,10))  # fast  !!
        10
```


This caused me a ton of confusion just now.  


---

Attachment


---

Comment by cremona created at 2009-01-18 18:40:03

Patch attached.  I deleted the now redundant integer parameter (which once was used to tell the function to use integer-specific code and is now redundant).  I added a relevant doctest and some more so hopefully William's confusion will never again occur (in someone else, I mean ;)).  I discovered some places which still had "integer=True" in gcd calls and fixed those.  I tested all rings/ and used search_src() to find any other places where "integer=True" might have been used, and found that search_src("integer=True") runs for ever while producing no output.


---

Comment by ncalexan created at 2009-01-21 07:30:31

Fine by me.


---

Comment by mabshoff created at 2009-01-23 02:54:36

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 02:54:36

Merged in Sage 3.3.alpha1
