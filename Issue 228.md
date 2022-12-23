# Issue 228: bug in sage notebook cell parser and promp stripping.

Issue created by migration from https://trac.sagemath.org/ticket/228

Original creator: was

Original creation time: 2007-01-29 08:10:05

Assignee: boothby


```
On Sun, 28 Jan 2007 15:26:56 -0800, Timothy Clemans <timothy.clemans@gmail.com> wrote:

>
> Just to show that something bad seems to be happening, I looked up the
> source for prime_pi and copied it into a cell and changed the name to
> epi. Well I added print epi(300) and got 0. I also added print "Hello"
> and got nothing. In another cell I typed prime_pi(300) and got 62. So
> I'm sure that there is a bug in SAGE notebook with docstrings in
> personal code.

You're absolutely right.  This is a bug in the SAGE notebook, or rather,
and unforseen "feature".  In the notebook if an input cell line starts
with either "sage:" or ">>>", then the input is viewed as an example
that was likely pasted in, and *only* the lines that begin with sage:
are evaluated.  (The parser that checks for this doesn't take into
account triple-quoted strings!)   Unfortunately this leads to the 
following sort of stupid behavior:
```



```
def foo(x):
    """
    EXAMPLES:
        sage: 2+2
        4
    """ 
    return x
///
4
```



```
foo(5)
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server/sage_notebook/worksheets/_uniqued/code/13.py", line 4, in <module>
    exec compile(ur'foo(Integer(5))' + '\n', '', 'single')
  File "/home/server/", line 1, in <module>
    
NameError: name 'foo' is not defined
```




---

Comment by TimothyClemans created at 2007-04-03 06:16:46

Resolution: fixed


---

Comment by TimothyClemans created at 2007-09-05 16:30:45

Changing status from closed to reopened.


---

Comment by TimothyClemans created at 2007-09-05 16:30:45

Reopen ticket because a patch wasn't created and approved.


---

Comment by TimothyClemans created at 2007-09-05 16:30:45

Resolution changed from fixed to 


---

Attachment

The attached patch addresses this issue by only considering input examples if it starts with a prompt (sage: or >>>).


---

Comment by was created at 2007-09-20 22:24:59

Resolution: fixed
