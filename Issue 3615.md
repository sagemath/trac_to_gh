# Issue 3615: update constructions document for solving linear equations.

Issue created by migration from https://trac.sagemath.org/ticket/3615

Original creator: mhansen

Original creation time: 2008-07-08 18:55:06

Assignee: tba

http://modular.math.washington.edu/sage/doc/html/const/node35.html

Sage can do far better than what's there:


```
<mhansen> sage: matrix(ZZ, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> (-13, 9)
<mhansen> sage: matrix(RR, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> (-13.0000000000000, 9.00000000000000)
<mhansen> sage: matrix(RIF, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> ([-13.000000000000000 .. -13.000000000000000], [9.0000000000000000 .. 9.0000000000000000])
<mhansen> sage: matrix(CDF, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> (-13.0, 9.0)
<mhansen> sage: a,b = var('a,b')
<mhansen> sage: matrix(SR, [[1,2],[3,5]]) \ vector([a,b])
<mhansen> (a - 2*(3*a - b), 3*a - b)
```



---

Comment by wdj created at 2008-07-08 22:36:50

If you are suggesting to add these I'd be happy to create a patch for it. Or are you suggesting to make a replacement?


---

Comment by mvngu created at 2008-09-19 20:52:07

Replying to [ticket:3615 mhansen]:
> http://modular.math.washington.edu/sage/doc/html/const/node35.html
[...]

This URL gave me an "Object not found!" message. But here's a link to the official online version
[http://www.sagemath.org/doc/const/node35.html](http://www.sagemath.org/doc/const/node35.html)
