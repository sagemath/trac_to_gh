# Issue 83: Docstring bug

Issue created by migration from https://trac.sagemath.org/ticket/83

Original creator: burhanud

Original creation time: 2006-09-25 02:47:04

Assignee: was

After typing QQ? followed the enter key, sage command line seems to be in edit mode (Is it expecting more input?) where I can type anything I want. After Control-C the appropriate docstring is displayed. ZZ? has the same behavior.


```
burhanud@sage:~/sha5$ sage
--------------------------------------------------------
--------------------------------------------------------
| SAGE Version 1.3.7.3.3, Build Date: 2006-09-21       |
| Distributed under the GNU General Public License V2. |

sage: QQ?


AHfDslh

Type:           RationalField
Base Class:     <class 'sage.rings.rational_field.RationalField'>
String Form:    Rational Field
Namespace:      Interactive
Docstring:
    The class class{RationalField} represents the field Q of
    rational numbers.

```



---

Comment by was created at 2006-09-25 23:15:46

This is *really* weird!  I initially have no clue what is going on...  This may be an IPython bug, since

```
sha:~/sage/web was$ sage -ipython
Python 2.4.3 (#1, Sep 21 2006, 04:25:45) 
Type "copyright", "credits" or "license" for more information.

IPython 0.7.2 -- An enhanced Interactive Python.
?       -> Introduction to IPython's features.
%magic  -> Information about IPython's 'magic' % functions.
help    -> Python's own help system.
object? -> Details about 'object'. ?object also works, ?? prints more.

In [1]: import sage.all

In [2]: sage.all.QQ?
[[hangs]]
```



---

Comment by was created at 2006-10-06 14:48:36

Resolution: fixed


---

Comment by was created at 2006-10-06 14:48:36

Fixed by Fernando Perez:


```
William Stein wrote:
Fernando,
 You might have a thought about this:
 http://sage.math.washington.edu:9002/sage_trac/ticket/83
 
I can't log in, but the problem is this:
 
sage: len(QQ)
 
 
This never returns, so ipython waits forever, but in this case the bug is in SAGE, since infinite iterators should declare a safe len() implementation to avoid this kind of situation.
 
You can make it safe by defining:
 
    def __len__(self):
        raise TypeError('len() of unsized object')
 
 
in the class sage.rings.rational_field.RationalField.  This is the standard idiom to indicate possibly infinite iterators in the Python library:
 
In [34]: from itertools import count
 
In [35]: count??
Type:           type
Base Class:     <type 'type'>
String Form:    <type 'itertools.count'>
Namespace:      Interactive
File:           /usr/lib/python2.4/lib-dynload/itertools.so
Docstring [source file open failed]:
    count([firstval]) --> count object
 
    Return a count object whose .next() method returns consecutive
    integers starting from zero or, if specified, from firstval.
 
 
In [36]: len(count())
---------------------------------------------------------------------------
exceptions.TypeError                                 Traceback (most recent call last)
 
/home/fperez/<ipython console>
 
TypeError: len() of unsized object
 
 
Sorry I couldn't get to fixing this one before your 1.4 release, I guess it can go into 1.4.1.
 
Regards,
 
f
```

