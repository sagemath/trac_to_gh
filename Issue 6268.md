# Issue 6268: Typesetting of sec(x), csc(x), cot(x) are broken

Issue created by migration from https://trac.sagemath.org/ticket/6268

Original creator: gmhossain

Original creation time: 2009-06-12 15:25:27

Assignee: cwitty

CC:  ncalexan

Typesettings of sec(x), csc(x), cot(x) are broken. It puts an
extra "\mbox" around them. However, typesetting for sin(x), 
cos(x), tan(x) works as expected.


---

Comment by mvngu created at 2009-06-12 19:22:17


```
[mvngu@sage sage-4.0.1]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: # the following work as expected
sage: latex(sec)
\sec
sage: latex(csc)
\csc
sage: latex(cot)
\cot
sage: # but the following have extra "\mbox" around the trig function name
sage: latex(sec(x))
\mbox{\sec}\left(x\right)
sage: latex(csc(x))
\mbox{\csc}\left(x\right)
sage: latex(cot(x))
\mbox{\cot}\left(x\right)
```



---

Comment by jhpalmieri created at 2009-06-12 20:32:11

Is this a bug in ginac/pynac?  Look at this:

```
sage: SR
Symbolic Ring
sage: SR._latex_element_(sin(x))
'\\sin\\left(x\\right)'
sage: SR._latex_element_(sec(x))
'\\mbox{\\sec}\\left(x\\right)'
```

The method `_latex_element_` is a one-liner:

```
        return GEx_to_str_latex(&x._gobj)
```

and I think GEx_to_str_latex is a ginac/pynac thing.  At least, I found it in sage/libs/ginac/decl.pxi.

It's possible to work around it, I think, with a patch like the attached, but I'm not at all convinced that this is the right way to fix it.  If you think it's okay, feel free to review it, but since I'm not sure, I've labeled it as "not read for review".


---

Attachment

The rebased patch for the ticket

http://trac.sagemath.org/sage_trac/ticket/5711

will resolve this issue as an un-intended consequence.


---

Comment by burcin created at 2009-06-14 22:16:04

new patch, apply only this one


---

Comment by burcin created at 2009-06-14 22:17:42

Changing status from new to assigned.


---

Comment by burcin created at 2009-06-14 22:17:42

Changing assignee from cwitty to burcin.


---

Comment by burcin created at 2009-06-14 22:17:42

Changing component from misc to symbolics.


---

Attachment

attachment:trac_6268-py_print_latex.patch fixes the reported problem. Apply only this patch.


---

Comment by ncalexan created at 2009-06-14 22:21:33

Resolution: fixed
