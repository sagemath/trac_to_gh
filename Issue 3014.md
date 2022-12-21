# Issue 3014: ZZ.random_element -- corrupted docstring (easy to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-24 02:42:40

Assignee: tba


```
sage: ZZ.random_element?
...    
            Return a random integer.
    
                ZZ.random_element() -- return an integer using the default 
                  distribution described below
                ZZ.random_element(n) -- return an integer uniformly 
                  distributed between 0 and n-1, inclusive.
                ZZ.random_element(min, max) -- return an integer uniformly 
                  destributed between min and max-1, inclusive.
    
            The default distribution for ZZ.random_element() is based on
            X = trunc(4/(5R)), where R is a random variable
            uniformly distributed between -1 and 1.  This gives
            Pr(X = 0) = 1/5, and Pr(X = n) =
            2/(5|n|(|n|+1)) for n 
    eq 0.  Most of the samples will be
            small; -1, 0, and 1 occur with probability 1/5 each.  But we
}}

Notice the messed up second t the last line!

This hit me during my demo today. 


---

Comment by mabshoff created at 2008-04-25 06:48:21

With the patch applied we get:

```
            The default distribution for ZZ.random_element() is based on
            X = trunc(4/(5R)), where R is a random variable
            uniformly distributed between -1 and 1.  This gives
            Pr(X = 0) = 1/5, and Pr(X = n) = 2/(5|n|(|n|+1)) for n neq 0.
            Most of the samples will be small; -1, 0, and 1 occur with
            probability 1/5 each.  But we also have a small but
            non-negligible proportion of ``outliers''; Pr(|X| >= n) = 4/(5n),
            so for instance, we expect that |X| >= 1000 on one in
            1250 samples.
```



---

Comment by mabshoff created at 2008-04-25 06:48:21

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-25 06:48:21

Changing assignee from tba to mabshoff.


---

Attachment


---

Comment by gfurnish created at 2008-04-25 06:54:30

applies cleanly and passes doctests


---

Comment by mabshoff created at 2008-04-25 06:55:20

Resolution: fixed


---

Comment by mabshoff created at 2008-04-25 06:55:20

Merged in Sage 3.0.1.alpha0
