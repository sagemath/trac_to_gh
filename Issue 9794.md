# Issue 9794: Make sure new plot syntax works with Sage polynomials

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-08-24 15:19:24

Assignee: jason, was

CC:  jason


```
pts = [(1,2),(2,3),(3,2),(4,3),(5,2),(6,3)] 
R.<x>=QQ[] 
f = R.lagrange_polynomial(pts) 
SR(f) 
2. If one has a non-symbolic polynomial currently, it won't plot with 
the new plotting syntax. 
plot(f,0,5) # works, old-school Sage 
plot(f,(x,0,5)) # doesn't work, new-school Sage 
plot(f,x,0,5) # doesn't work, though sort of makes sense it shouldn't 
since x isn't a symbolic variable now... ? 
```

Obviously any polynomial f is what is at issue, not just this particular one.


---

Comment by kcrisman created at 2010-08-24 15:20:13

This would be good to work too, if we can fix the above.

```
pts = [(1,2)] 
R.<x>=QQ[] 
f = R.lagrange_polynomial(pts) 
f.plot(0,7) 
<boom because integers have no .plot() method>
```

