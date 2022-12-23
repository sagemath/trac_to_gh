# Issue 6305: preparser issue with recurssive loading of .sage files

Issue created by migration from https://trac.sagemath.org/ticket/6305

Original creator: was

Original creation time: 2009-06-15 23:53:40

Assignee: cwitty


```
Hi,
I'm not sure if it's a bug or it's me doing something wrong.

I have two files:

test1.sage containing nothing but
  print numpy.random.normal(0,(2*0.0061*0.33)^(1/2),1)

and

test2.sage containing
  load "test1.sage"


I import numpy
sage: import numpy

Now
sage: load "test1.sage"
returns values always smaller than 1
thats the right distribution, the same i get when using the notebook-
interface

but
sage: load "test2.sage"
very often returns values bigger than 1,
thats a whole different distribution

My system is ubuntu-9.04-amd64 on Pentium Dual Core
sage-4.0.1 from 2009-06-06
```


to which Marshall responds:

```
I'm not sure what is happening but I would guess that at some point
the ^(1/2) gets turned into ^(0), and then your standard deviation
goes from .06... to 1.  I.e., it seems like maybe the preparser
doesn't catch these nested loadings.

-M. Hampton

```



---

Attachment

A simple fix by moving out the code that does the literals (changes 1/2 -> Integer(1)/Integer(2)) into a separate function and made sure its called at each load.

all tests in devel/sage/misc passed.


---

Comment by timdumol created at 2010-01-19 07:19:13

This seems to be fixed now. I'll close this.


---

Comment by timdumol created at 2010-01-19 07:19:13

Resolution: worksforme
