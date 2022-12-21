# Issue 1009: incredibly slow caching of ntl context objects.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-27 03:46:46

Assignee: somebody


```

sage: N = 5^100000
sage: R = Integers(N)
sage: S.<x> = PolynomialRing(R)
sage: v = R(7^100000)
sage: time f = S([v])

I then tracked down the problem which is in the ntl_ZZ_pContext
function in ntl_ZZ_pContext.pyx, where the context is cached.
Unfortunately, the frickin' context is cached as a decimal *string*, so
every single cached access to the context is extremely expensive -- for
more expensive than not even bothing to cache the context would be.
The patch at 

fixes things so that the cache uses the hash of the context, which 
I implemented (along with hash's of ntl_ZZ's).  

Exactly the same mistake is made in ntl_GF2EContext.pyx
```



---

Attachment


---

Comment by cwitty created at 2007-10-27 04:55:36

Resolution: fixed
