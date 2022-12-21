# Issue 9233: maxima --> sage conversion error

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-13 23:36:31

Assignee: burcin


```

sage: var('n')
n
sage: sum((4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(16*n+12)-1/(16*n+14)), n, 0,oo)
...

TypeError: unable to make sense of Maxima expression '-(22*log(2)-2*psi[0](7/8)-4*psi[0](5/8)+16*psi[0](1/8)-pi+10*euler_gamma)/32' in Sage
```



---

Comment by burcin created at 2010-06-13 23:43:58

This is probably a duplicate of #9217.


---

Comment by mhansen created at 2010-06-14 00:21:26

Indeed it is.


```

----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: var('n')
n
sage: sum((4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(16*n+12)-1/(16*n+14)), n, 0,oo)
1/32*pi - 5/16*euler_gamma - 1/2*psi(1/8) + 1/8*psi(5/8) + 1/16*psi(7/8) - 11/16*log(2)
```



---

Comment by mhansen created at 2010-06-14 00:21:26

Resolution: duplicate
