# Issue 2472: what parent should floor return?

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-11 20:58:33

Assignee: somebody

CC:  ncalexan

Keywords: floor truncate ceil ceiling parent integer

I think `floor` and `ceil` and `truncate` should return integers.


```
sage: floor(2).parent()
Integer Ring
sage: floor(2.0).parent()
Integer Ring
sage: floor(RIF(2.0)).parent()
Real Interval Field with 53 bits of precision
```



---

Comment by was created at 2008-03-11 21:03:56

> I think floor and ceil and truncate should return integers.

I agree, though this goes against what Python does:


```
sage: math.floor(float(2.3))
2.0    
```


I don't like Python's math.floor behavior, but I bet it agrees with the C library.
Yep:

```
     double
     floor(double x);

     long double
     floorl(long double x);
```


I still vote for making floor always return Integer.


---

Comment by cwitty created at 2008-03-12 01:26:45

But what integer should it return?  In particular, what do you want floor(RIF(1.5, 12345.678)) to return, and why?  

My vote would be that floor and ceiling should not be implemented for RIF at all, because I don't think they have a sensible meaning.

Note that when William first implemented floor and ceiling for RIF, he had them return integers; but he immediately (38 minutes later, according to Mercurial) changed them to return intervals, calling this a '"moral" improvement'.


---

Comment by dmharvey created at 2008-03-13 18:50:35

Perhaps what we need is an `IntegerInterval` class which represents an interval in ZZ.

I think this might even have come up in the context of valuations of p-adic numbers, and I might have even discussed it with David Roe, but I can't remember if anything came out of it.


---

Comment by jdemeyer created at 2014-09-02 08:57:32

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-09-02 08:57:32

We now have `unique_floor()` for `RIF` returning an integer, which solves the problem I guess.


---

Comment by jdemeyer created at 2014-09-02 08:57:37

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-09 14:53:36

Resolution: fixed
