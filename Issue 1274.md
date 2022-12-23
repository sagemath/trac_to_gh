# Issue 1274: modify singular interface to allow for verbose output

Issue created by migration from https://trac.sagemath.org/ticket/1274

Original creator: wdj

Original creation time: 2007-11-25 22:21:04

Assignee: malb

Simon King:
 Now, another question on the Singular interface:
In Singular, doing
`matrix P,S,IS = invariant_ring(A,1);`
would make Singular to additionally print information about the
progress of computations (which, in big examples, might be nice to
have).
However, when i use the Singular interface, i can not see such
informations. Where are they gone?

Martin Albrecht:
The information is printed but ignored because pexpect expects
Singular 'output' and ignores the rest. I am no pexpect expert so I don't
know how to fix it. It would very very useful though. Anyone else has any
idea?

William Stein:
I think this would be possible to implement, by modifying
interfaces/singular.py. It's easiest if we just have it print out
the result of all the verbose output, rather than all of it along the way as it is
output by singular, though the latter would also be possible.   With pseudo-tty's it is
possible to do anything you could really imagine doing by hand while physically using
a terminal to interact with singular.  Anything.


---

Attachment


---

Comment by malb created at 2008-01-18 18:23:52

This works now:


```
sage: r = singular.ring(0,'(x,y,z)','dp')
sage: i = singular.ideal(['x^2','y^2','z^2'])
sage: s = i.std()
sage: singular.eval('hilb(%s)'%(s.name()))
'// 1 t^0\n// -3 t^2\n// 3 t^4\n// -1 t^6\n\n// 1 t^0\n//
3 t^1\n// 3 t^2\n// 1 t^3\n// dimension (affine) = 0\n//
degree (affine) = 8'

sage: set_verbose(1)
sage: singular.eval('hilb(%s)'%(s.name()))
//         1 t^0
//        -3 t^2
//         3 t^4
//        -1 t^6
//         1 t^0
//         3 t^1
//         3 t^2
//         1 t^3
// dimension (affine) = 0
// degree (affine)  = 8
''

sage: o = s.hilb()
//         1 t^0
//        -3 t^2
//         3 t^4
//        -1 t^6
//         1 t^0
//         3 t^1
//         3 t^2
//         1 t^3
// dimension (affine) = 0
// degree (affine)  = 8
// ** right side is not a datum, assignment ignored

sage: set_verbose(0)
sage: o = s.hilb()
```



---

Comment by ncalexan created at 2008-01-20 06:42:56

Looks fine to me, should be applied.


---

Comment by mabshoff created at 2008-01-21 05:36:05

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 05:36:05

Resolution: fixed
