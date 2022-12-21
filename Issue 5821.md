# Issue 5821: preparser incorrectly handles backslash operator inside strings (sometimes)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-04-19 03:31:24

Assignee: was

CC:  robertwb

Keywords: preparser

When reviewing #5595, I tried typing this:

```
sage: import re
sage: dep_regex = re.compile(r'^ *(?:(?:cimport +([\w\. ,]+))|(?:from +(\w+) +cimport)|(?:include *[\'"]([^\'"]+)[\'"])|(?:cdef *extern *from *[\'"]([^\'"]+)[\'"]))', re.M)
------------------------------------------------------------
   File "<ipython console>", line 1
     dep_regex = re.compile(r'^ *(?:(?:cimport +([\w\. ,]+))|(?:from +(\w+) +cimport)|(?:include *[\'"]([^\'"]+)[ * BackslashOperator() * '"])|(?:cdef *extern *from *[\'"]([^\'"]+)[\'"]))', re.M)
                                                                                                                                                                          ^
SyntaxError: invalid syntax
```


Note that the preparser has turned a backslash from the middle of the regular expression into `" * BackslashOperator() * "`.


---

Comment by robertwb created at 2009-04-19 07:26:54

It appears that even in raw strings the backslash escapes a potential end quote...

http://docs.python.org/reference/lexical_analysis.html


---

Attachment


---

Comment by cwitty created at 2009-04-19 18:31:57

Code looks good (and fixes the problem); doctests pass.

Positive review.


---

Comment by mabshoff created at 2009-04-23 07:58:45

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 07:58:45

Resolution: fixed
