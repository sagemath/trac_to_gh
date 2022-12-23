# Issue 70: WANTED: unsafe pyrex typecasts

Issue created by migration from https://trac.sagemath.org/ticket/70

Original creator: dmharvey

Original creation time: 2006-09-20 20:15:01

Assignee: somebody

Currently pyrex doesn't let you do an unsafe typecast, which is really annoying, and costs us speed in some low-level situations.

For example:

```
cdef SomeType y
if PyObject_TypeCheck(x, SomeType):
   y = x
   [ ... do stuff ... ]
else:
   [ ... do other stuff ... ]
```


In the above code, I have already performed the type check before I get to "y = x". But then when I do "y = x", Pyrex generates more type-checking code, so we check the types twice.

An alternative would be to do:

```
cdef SomeType y
try:
   y = x
   [ ... do stuff ... ]
except TypeError:
   [ ... do other stuff ... ]
```

but this invokes python's exception handling, which is relatively slow. (Also you have to work harder if the first "do stuff" block could raise a TypeError for a different reason.)

What I really want to be able to do is something like:

```
cdef SomeType y
if PyObject_TypeCheck(x, SomeType):
   y = <unsafe> x
   [ ... do stuff ... ]
else:
   [ ... do other stuff ... ]
```


I'm not sure about the best syntax, but I just want a way to assign the underlying pointer without doing a type check. (I can live with the additional reference counting.)



---

Comment by malb created at 2006-10-11 06:37:28

unsafe typecasts are supported in Pyrex:


```
cdef SomeType y
if PyObject_TypeCheck(x, SomeType):
   y = <SomeType> x
   [ ... do stuff ... ]
else:
   [ ... do other stuff ... ]
```



---

Comment by malb created at 2006-10-11 06:37:28

Resolution: invalid
