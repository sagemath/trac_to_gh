# Issue 6729: notebook -- bug when input contains uniform leading space

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-10 16:07:47

Assignee: boothby

CC:  timdumol


```


On Mon, Aug 10, 2009 at 8:43 AM, Kiran Kedlaya <kskedl`@`gmail.com> wrote:


    What would you expect from the following input into the notebook?

    CELL 1:
       u = 2+2
       u = 2+3

    CELL 2:
    print u

    If you try something like this at a command line, the first line gives
    an error due to the spaces in front. 


No it doesn't, at least not for me.

flat wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: heckeindex
sage:    u = 2+2
sage:    u = 2+3
sage: print u
5
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
I know it won't give an error, because on the command line all spaces and sage: and >>> prompts are stripped from the left for non-continuation lines.

However, you might have meant the pure python command line, which does give an error:

flat:kamienny wstein$ sage -python
Python 2.6.2 (r262:71600, Jul  8 2009, 17:42:25)
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>    u = 2 + 2
  File "<stdin>", line 1
    u = 2 + 2
    ^
IndentationError: unexpected indent
>>>

 

    But on my notebook server
    (running 4.1), the first cell evaluates without an error, and the
    second one returns 4, not 5. ?!

    Kiran


This must be a bug in the notebook, related to exec compile, which the notebook uses to evaluate cells.   Here's the code that actually gets executed:

----------------------------------------------------------------

flat:code wstein$ pwd
/Users/wstein/.sage/sage_notebook/worksheets/admin/222/code
flat:code wstein$ more 16.py
# -*- coding: utf_8 -*-
from __future__ import with_statement
print "^Ab14"
os.chdir("/Users/wstein/.sage/sage_notebook/worksheets/admin/222/cells/5")
sage.server.notebook.interact.SAGE_CELL_ID=5
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2)
exec compile(ur'u = _sage_const_2 +_sage_const_2\u000a   u = _sage_const_2 +_sage_const_3' + '\n',
 '', 'single')

print "^Ae14"
----------------------------------------------------------------

The code if you get rid of the spaces to the left we get:

flat:code wstein$ more 23.py
...
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2)
u = _sage_const_2 +_sage_const_2
exec compile(ur'u = _sage_const_2 +_sage_const_3' + '\n', '', 'single')

-------------------------

Notice that "exec compile" is supposed to only be used on the *last* line of input.    The reason for this is so that the display print hook is called, e.g., so if you type

  a = 5
  a + 1
  b = 7
  a + b

in a notebook cell, at least you'll see 12 (=a+b) come out.  You will not see 6 from "a+1" though.  So the problem you're seeing is because the code in the notebook to determine "the last line of code" takes account special cases when the last line is indented, so e.g., the following would work:

   for z in range(10):
        z

and print out each of the z's (just like "for z in range(10): z").  In fact, the above is turned into:

_sage_const_5 = Integer(5)
exec compile(ur'for z in range(_sage_const_5 ):\u000a    z' + '\n', '', 'single')

The problem is that when we input
     u = 2 +2
     u = 2 + 3
both indented, then everything is combined into one single exec compile, and surprisingly we have in pure python:

>>> _sage_const_3 =3; _sage_const_2 = 2>>> exec compile(ur'u = _sage_const_2 +_sage_const_2\u000a   u = _sage_const_2 +_sage_const_3' + '\n',
...  '', 'single')>>>
>>> u
4
 
I'm surprised this doesn't set u to 5.  It might have something to do with the "\u000a" which is the unicode character for linefeed.    Basically, I find the following behavior of Python's exec command really weird/broken/surprising.  I would expect an error in the latter two cases:

>>> exec compile(ur'for z in range(5):\u000a   z', '','single')0
1
2
3
4
>>> exec compile(ur'u=2+2\u000a  u=3+3', '','single')
>>> print u
4
>>> exec compile(ur'u=10\u000a  u=3+*fr%Acn `@`#!^2n2azzz3', '','single')
>>> print u
10
 
I hope a Python interpreter expert such as Robert Bradshaw can comment on this.  In the meantime, if I were to spend more time on this now (which I won't), I would read the docs for exec and compile carefully, then probably just find a way to program around this surprising (to me) case in server/notebook/worksheet.py (which generates the exec compile code that is run above).

-- William
```



---

Comment by was created at 2009-08-11 00:11:26

Dorian's remarks:

```
Evaluating Kiran's CELL 1 in a codenode python notebook returns a similar error:

  File "<input>", line 1
    u = 2+3
   ^
IndentationError: unexpected indent

I don't think this is a sign of any bug, it is simply bad Python syntax. It doesn't make sense to exec something with leading white space with no preceding lines.

One interesting clue to add to William's investigation... If you strip the leading white space of the first line, and evaluate in codenode, you get this:

CELL 1:
2+2
   2+3

OUTPUT 1:
4
  File "<input>", line 1
    2+3
   ^
IndentationError: unexpected indent


In the sage notebook, the output of the same input is "4" *without* the IndentationError statement, the same as the result in question (when the first line has 3 initial white spaces).

This must have to do with sage pre-parsing out the white space of the initial line. In codenode, valid command blocks are built up (similar to sage, have look at _runcommands if you want). A cell may contain one or more valid commands. The interpreter processes the input looking for complete commands to compile. Once it has a complete command, it pauses processing the raw input, execs that command, and then resumes processing the raw input until it has all been compiled and exec'd.

So, the experiment I showed in codenode (above, no leading white space on the first line) shows that the first line is a valid and complete command, and the second line is not.
This is consistent with sage pre-parsing out the leading white space of the first line, and then maybe not printing the IndentationError, which shows up in codenode and the regular Python CLI.

What do you all think?
```



---

Attachment


---

Comment by acleone created at 2010-01-20 01:34:33

Strips uniform leading spaces before evaluating sage cells


---

Attachment

Ok, trac_6729-leading_space.patch adds the expected behavior.

```
CELL 1:
    u = 2
    u = 3
CELL 2:
print u  # = 3
```


However, this fails silently (regardless of the patch):

```
CELL 1:
 u = 2
  u = 3
CELL 2:
print u  # = 2
```


With `%python`, it correctly throws an indentation error:

```
CELL 1:
%python
 u = 2
  u = 3
# Identation error
```


So this is a bug in the `%sage` compile system.


---

Comment by acleone created at 2010-01-20 01:47:53

Changing status from new to needs_review.


---

Comment by acleone created at 2010-01-20 02:02:27

See #8006 for the silent Indentation errors


---

Comment by timdumol created at 2010-01-20 07:37:32

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-01-20 07:37:32

The first indent goes away after saving, e.g., this:


```
  print 2
  print 4
  print 6
```


becomes 


```
print 2
  print 4
  print 6
```


upon save & quit and re-opening.


---

Comment by kcrisman created at 2014-12-09 19:37:34

It's pretty likely that this is caused by the same thing as https://github.com/sagemath/sagenb/issues/288


---

Comment by kcrisman created at 2014-12-10 04:00:37

> The first indent goes away after saving, e.g., this:
> 
> {{{
>   print 2
>   print 4
>   print 6
> }}}
> 
> becomes 
> 
> {{{
> print 2
>   print 4
>   print 6
> }}}
> 
> upon save & quit and re-opening.
To be fair, that happens no matter what we do.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid
