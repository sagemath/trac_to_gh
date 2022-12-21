# Issue 4405: double/single quotation marks in docstring

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2008-10-30 19:39:30

Assignee: tba

CC:  kcrisman

Keywords: docstring, triple ''', triple """

At this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/1dc6a340db91e7ac) thread, kcrisman reported the following problem with single quotation marks in docstring:

```
I came across some very strange behavior recently regarding docstrings
in functions.  In the notebook in 3.2.alpha0 and 3.0.6, putting an
apostrophe in the docstring causes various bugs.  It doesn't have to
be in any particular spot, as far as I can tell; in fact, it took a
long time to pinpoint this as the source of the problem!

More precisely, it seems to cause the preparser to turn off or
something, because it disallows the following (in the function
definition):
f(x)=x^3
because of the f(x), and
f=x^3
because of the ^ used instead of ** (the error message for the first
is very mysterious at times, but the second one is always clear when
you try to use the function).

I can post a link to a worksheet if it's really necessary, but
hopefully this will be enough for someone to help.  I checked Sage and
Python docs about documentation strings, but couldn't find anything
about it being bad to have apostrophes; in fact, some Sage docstrings
have them (e.g. for declaring variables).  I didn't try this in the
command line, so it is possible it's only a notebook issue.
```

Some basic experimentation reveals that it's likely to be caused by the use of single quotation marks in docstring from within the console and notebook. However, the reported error as described by kcrisman seems to go away when double quotation marks are used instead of single quotation marks:

```
OK, here's my experimentation from within the console sage-3.1.4, x86
machine, Debian 5.0 Lenny (testing):

Yep, I received a similar error as you described:

sage: def foo():
....:     '''
....:     What's up with this? x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)

John's suggestion about replacing the * with r* results in the same error:

sage: def foo():
....:     r'''
....:     What's up with this? x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)

As Simon has said, the error seems to go away when I used triple "
(double quotation mark, not single quotation mark), which I normally
do anyway whenever I write docstring. But using triple ''' with or
without the leading r, and with or without the question mark, resulted
in a siimilar error:

sage: def foo():
....:     '''
....:     What's up with this? x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)

sage: def foo():
....:     r'''
....:     What's up here x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)
```



---

Comment by justin created at 2008-10-31 20:59:29

The following seems to show that Sage parsing is bypassed, in some way, when using single-quote marks for docstrings.


```
sage: def foo(x):
   ....:     """
   ....:     it's a comment.
   ....:     """
   ....:     return x^2
   ....: 
sage: foo(3)
9
sage: def foo(x):
   ....:     '''
   ....:     It's a comment.
   ....:     '''
   ....:     return x^2
   ....: 
sage: foo(3)
1
```

In the first case, "!^" is exponentiation; in the second, XOR.


---

Comment by mhansen created at 2009-01-23 13:13:13

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-01-23 13:13:13

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2009-01-24 02:04:51

Note that this depends on #3752.


---

Comment by malb created at 2009-01-24 07:59:48

patch looks good, doctests pass.


---

Comment by mabshoff created at 2009-01-24 19:54:48

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 19:54:48

Merged in Sage 3.3.alpha2.

Cheers,

Michael
