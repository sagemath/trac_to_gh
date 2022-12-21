# Issue 5442: preparser or magma.eval bug?

Issue created by migration from Trac.

Original creator: kohel

Original creation time: 2009-03-05 16:56:35

Assignee: was

This works:

sage: s = """
x := [
    1,
    2,
    3 ];
x;
"""
sage: magma.eval(s)

However, if one try to type the above interactively 
in the %magma shell, it crashes on the the first line 
'x := ['.

The problem is that either preparse_ipython or 
magma.eval is too naive, inserting a ';' rather 
than waiting for the completion of the expression.

As a start, I think the block:

if interface_name in ['gap', 'magma', 'kash', 'singular']:
    if not line.endswith(';'):
        line += ';'

should be deleted, but I don't know the Expect 
interface well-enough to suggest a complete fix.

Remark: The magma.eval function handles for .. do,
but not if the logical is split over more than one 
line, so maybe this function can be easily fixed 
to not insert a ';' when an expression is incomplete
(e.g. '".."', 'for .. do', '[ .. ]', etc.).

Subtleties arise when a opening to an expression is 
contained in a string.



---

Comment by was created at 2009-03-06 15:45:09

> The problem is that either preparse_ipython or magma.eval is too 
> naive, inserting a ';' rather than waiting for the completion
>  of the expression. 

For the record, this was on purpose and is by design.   The magma
interpreter via magma.eval is a blocking call, and if you send it
a chunk of code without a semicolon it will block forever.   If one
were to do what you suggest above, then typing

magma.eval('2+2')

would lead to a total hang of Sage. 

I'm marking this ticket as invalid unless you see a good reason to totally change the design of the interface to be nonblocking, which I doubt you'll do unless you really understand how they work and what the many negatives of doing that are.


---

Comment by was created at 2009-03-06 15:45:09

Resolution: invalid
