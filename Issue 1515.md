# Issue 1515: ParametricSurface bug

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-12-15 01:59:55

Assignee: was


```
def f(x,y): return cos(x)*sin(y), sin(x)*sin(y), cos(y)+log(tan(y/2))+0.2*x
show(ParametricSurface(f, (srange(0,12.4,0.1), srange(0.1,2,0.1))))
```

doesn't render. Also


```
[08:48am] williamstein: This should work but doesn't:
[08:48am] williamstein: S = ParametricSurface(lambda (x,y):(cos(x),
sin(x), y), domain=(range(10),range(10)))
```



---

Attachment


---

Comment by robertwb created at 2007-12-15 02:04:17

Now the first example works. Also, the second example almost does


```
S = ParametricSurface(lambda x,y:(cos(x),sin(x), y), domain=(range(10),range(10)))
```


(Note the missing ()'s, it expects to arguments, not a tuple).


---

Comment by robertwb created at 2007-12-15 02:04:17

Changing status from new to assigned.


---

Comment by robertwb created at 2007-12-15 02:04:17

Changing assignee from was to robertwb.


---

Comment by mabshoff created at 2007-12-15 14:03:19

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 14:03:19

Resolution: fixed
