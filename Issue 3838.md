# Issue 3838: Element access for RElement

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-08-13 17:27:21

Assignee: SimonKing

CC:  alexghitza

Keywords: r interface, element access

On [http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en](http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en), Alexandr Batalshikov pointed out that

```
> v = c(3,5,9,1)
> v[c(2,3)]
[1] 5 9 
```

works in R, but the corresponding statement in Sage does not:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 3
```


I believe this is a defect. With the attached patch, the following works:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 5 9
sage: v[-2]
[1] 3 9 1
sage: v['c(2,3)']
[1] 5 9
sage: v[2,4,3]
[1] 5 1 9
sage: v[2]
[1] 5
```




---

Comment by SimonKing created at 2008-08-13 17:27:53

Patch relative to 3.1.alpha0


---

Attachment


---

Attachment

Correction for the first patch


---

Comment by SimonKing created at 2008-08-13 20:02:04

I just realized that it is not a good idea to make `v[2,3]` return a vector, because if `v` is an array, `v[2,3]` should return a single entry of the array.

The new patch (that should be applied after the first one) takes this into account. Now we have:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 5 9
sage: v[-n]
[1] 3 1
```

as above, and

```
sage: m = r.array('1:3', r.c(2,4))
sage: m
     [,1] [,2] [,3] [,4]
[1,]    1    3    2    1
[2,]    2    1    3    2
sage: m[1,2]
[1] 3
sage: m[n]
[1] 2 3
```


I think this is better than the first approach, but still allows to use an RElement as index.


---

Comment by schilly created at 2008-08-13 22:58:36

hi, I like the second approach, but just for the sake of completeness and with the future in mind: could you add a doctest for accessing elements of a three dimensional array? I know they can happen and i think it would be good to cover them.


---

Attachment

To be applied after the two previous patches


---

Comment by SimonKing created at 2008-08-14 07:04:14

Replying to [comment:3 schilly]:
> hi, I like the second approach, but just for the sake of completeness and with the future in mind: could you add a doctest for accessing elements of a three dimensional array? I know they can happen and i think it would be good to cover them.

No problem, that works already with the previous version:

```
sage: m = r.array('1:3', r.c(2,4,2))
sage: m
, , 1
     [,1] [,2] [,3] [,4]
[1,]    1    3    2    1
[2,]    2    1    3    2

, , 2
     [,1] [,2] [,3] [,4]
[1,]    3    2    1    3
[2,]    1    3    2    1

sage: m[1,2,2]
[1] 2
sage: m[1,3,2]
[1] 1
```


I changed the doc-tests accordingly (by the third patch).

However, i just realize that mixing integer and r.c does not work:

```
sage: m = r.array('1:3', r.c(2,4,2))
sage: r(m.name()+'[1,c(1,2),1]')
[1] 1 3    # the output how it should be
sage: m[1,r.c(1,2),1]
[1] 2      # wrong output
```


I'll work on this problem.


---

Attachment

Replaces all previous patches


---

Comment by SimonKing created at 2008-08-14 07:24:01

Replying to [comment:4 SimonKing]:
> I'll work on this problem.

The most recent patch replaces all previous patches and should apply to 3.1.alpha0. Here is the new feature:

```
sage: m = r.array('1:3', r.c(2,4,2))
sage: m
, , 1
     [,1] [,2] [,3] [,4]
[1,]    1    3    2    1
[2,]    2    1    3    2

, , 2
     [,1] [,2] [,3] [,4]
[1,]    3    2    1    3
[2,]    1    3    2    1
sage: m[1,r.c(1,2),1]
[1] 1 3
sage: m[1,r.c(1,3),r.c(1,2)]
     [,1] [,2]
[1,]    1    3
[2,]    2    1
```


The doctests provide examples for that type of usage.


---

Comment by AlexGhitza created at 2008-09-23 07:57:32

applies to 3.1.3.alpha0


---

Comment by mabshoff created at 2008-09-23 10:24:33

Merged RElementAccessNew.patch in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 10:24:33

Resolution: fixed
