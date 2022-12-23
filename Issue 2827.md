# Issue 2827: sage -notebook does not handle options passed to it correctly

Issue created by migration from https://trac.sagemath.org/ticket/2827

Original creator: mhansen

Original creation time: 2008-04-06 10:05:02

Assignee: boothby

The code suspect code is the following (which doesn't isn't flexible enough:


```
if len(sys.argv) > 1:
    notebook(*sys.argv[1:])
```



---

Comment by was created at 2008-05-27 01:12:43

Maybe we should change sage -notebook so that it works like this:


```
sage -notebook "(secure=True, address='sage.math.washington.edu', accounts=False)"
```


where anything in quotes is valid Python.  What do you think?


---

Comment by mabshoff created at 2009-02-12 08:01:58

Some recent work went in in this area? Can someone still reproduce this or is this ticket invalid?

Cheers,

Michael


---

Comment by timdumol created at 2010-01-19 22:32:52

Replying to [comment:2 was]:
> Maybe we should change sage -notebook so that it works like this:
> 
> {{{
> sage -notebook "(secure=True, address='sage.math.washington.edu', accounts=False)"
> }}}
> 
> where anything in quotes is valid Python.  What do you think?

This seems quite reasonable to me. I also remember Dr. Kirkby's problem with specifying server_pool using `sage -n`.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid
