# Issue 8230: strange behaviour

Issue created by migration from https://trac.sagemath.org/ticket/8230

Original creator: zimmerma

Original creation time: 2010-02-10 15:17:22

Assignee: robertwb

Hi, I found the following strange behaviour of the addition
<int> + 1/2. I have a file `MurphyE.sage` which contains:

```
load E.sage

foo(2)
```

where `E.sage` contains:

```
def foo(K):
    for i in range(K):
       print i, i+1/2, type(i), type(i+1/2)
```

Then I get:

```
sage: load MurphyE.sage
0 0 <type 'int'> <type 'int'>
1 1 <type 'int'> <type 'int'>
```

Now if instead I replace `load E.sage` in my file by the
content of the procedure `foo`, i.e.:

```
def foo(K):
    for i in range(K):
       print i, i+1/2, type(i), type(i+1/2)

foo(2)
```

then I get:

```
sage: load MurphyE.sage
0 1/2 <type 'int'> <type 'sage.rings.rational.Rational'>
1 3/2 <type 'int'> <type 'sage.rings.rational.Rational'>
```

which is the expected behaviour. Please can someone explain to me
the first result? I forgot to say it is with Sage 4.3.


---

Comment by robertwb created at 2010-02-10 19:55:46

Dupe of #6345


---

Comment by ylchapuy created at 2010-08-15 18:01:15

it seems to be fixed now.


---

Comment by ylchapuy created at 2010-08-15 18:01:15

Resolution: fixed


---

Comment by mpatel created at 2010-08-15 21:32:49

I'm closing this as a "duplicate" of #6345.


---

Comment by mpatel created at 2010-08-15 21:32:49

Resolution changed from fixed to duplicate
