# Issue 1267: documentation for piecewise does not show up in notebook

Issue created by migration from https://trac.sagemath.org/ticket/1267

Original creator: cwitty

Original creation time: 2007-11-25 15:09:41

Assignee: boothby

In the public notebook (on www.sagenb.org), when I evaluate a cell with `piecewise?`, I get this:

```
File:        /usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/functions/piecewise.py
Type:        <type 'classobj'>
Definition:  piecewise(x0)
Docstring:
```

with no actual docstring.  (Doing the same thing from the command line does give a useful docstring.)



---

Comment by mabshoff created at 2007-11-25 17:59:42

After some testing it turns out that cwitty is right and it does work in console mode with 2.8.14 So was is wrong and change it back.


---

Comment by was created at 2007-11-25 18:35:07

I can confirm and replicate this problem:

```
[10:09am] was_: It does fail on my ocally-running notebook.
[10:09am] was_: Ipython does the help on the command line.
[10:09am] was_: *I* wrote what does the help in the notebook.
[10:09am] DenisG_: (my locally running notebook)
[10:09am] was_: It's separate code; I think it is is sage/server/support.py or something like that
[10:10am] was_: And there is definitely a bug.
```



---

Comment by mhansen created at 2007-12-06 00:22:44

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-06 00:22:44

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2007-12-06 00:22:44

Actually, I don't think anything wrong with the ? or ?? notation.  What was happening was roughly the following:


```
class PiecewisePolynomial:
    def __init__(self, list_of_pairs):
        """docstring"""

    ...

piecewise = PiecewisePolynomial
```


The result of piecewise? was correct since PiecewisePolynomial didn't have a class docstring.


---

Attachment


---

Comment by mabshoff created at 2007-12-09 12:34:05

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-09 13:13:17

Resolution: fixed


---

Comment by mabshoff created at 2007-12-09 13:13:17

Merged in 2.9.alpha2.
