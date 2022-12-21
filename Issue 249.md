# Issue 249: possible optimization opportunity

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-07 06:39:19

Assignee: somebody


```
print preparse("""
def m(n):
  return [[j%n*n+(j+j-i)%n+1
    for j in range(i+(1-n)/2,i+(n+1)/2)] for i in range(n)]
""")
///
def m(n):
  return [[j%n*n+(j+j-i)%n+Integer(1)
    for j in range(i+(Integer(1)-n)/Integer(2),i+(n+Integer(1))/Integer(2))] for i in range(n)]
```



```
def m(n):
  return [[j%n*n+(j+j-i)%n+1
    for j in range(i+(1-n)/2,i+(n+1)/2)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.63 s,  Wall time: 0.65 s
```



```
def m(n):
  one = 1; two=2
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.60 s,  Wall time: 0.61 s
```



```
def m(n):
  one = 1r; two=2r
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.75 s,  Wall time: 0.79 s
```



```
%python

def m(n):
  one = 1; two=2
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201r)
///
CPU time: 0.03 s,  Wall time: 0.03 s
```



```
def m(n):
  one = 1r; two=2r; n=int(n)
  return [[j%n*n+(j+j-i)%n+one
    for j in range(i+(one-n)/two,i+(n+one)/two)] for i in range(n)]
```



```
time a=m(201)
///
CPU time: 0.02 s,  Wall time: 0.02 s
```



---

Comment by mabshoff created at 2008-03-22 19:20:40

It is unclear to me what the objective of this ticket is besides the fact that python types are potentially faster than certain Sage types like Integers. So: please elaborate or invalidate this ticket.

Cheers,

Michael


---

Comment by was created at 2008-03-22 19:42:49

The examples above very clearly indicate that by factoring preparsed constants out when preparsing chunks of code results in potentially vast speedups.   We should have been doing this since day 1, but just haven't got around to it.  This ticket should definitely *not* be invalidated.  I've reworded it to be much more precise with one clear example.


---

Comment by gfurnish created at 2008-04-07 08:36:42

I have strong concerns about this messing up things with side effects.  It is far from clear for me that this is the correct course of action, and if it is, it must have a flag to disable it for doctests.


---

Comment by robertwb created at 2008-09-23 21:43:10

It makes even more of a difference for real numbers. 

Before 


```
%time
x = 0
while x < 1e5:
    x += 1.5
CPU time: 0.71 s,  Wall time: 0.73 s
```


After


```
%time
x = 0
while x < 1e5:
    x += 1.5
CPU time: 0.06 s,  Wall time: 0.06 s
```



---

Attachment


---

Comment by AlexGhitza created at 2008-09-24 00:45:40

Looks good.  I have tried it with a bunch of different types of constants (reals, complexes, rationals) and I'm satisfied that it works.


---

Comment by mabshoff created at 2008-09-24 02:09:17

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-24 02:09:17

Resolution: fixed
