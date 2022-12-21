# Issue 3685: make damned sure that "import sage.all" doesn't import ipython

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-20 14:49:23

Assignee: cwitty

Make sure that doing this does not import ipython:


```
teragon-2:~ was$ sage -python
Python 2.5.2 (r252:60911, Jul 10 2008, 00:31:06) 
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
```



---

Comment by was created at 2008-07-20 14:52:51

Here is how Ondrej Certik verifies that sage.all was importing ipython in sage-3.0.5:

```
I don't want to have anything in common with ipython, but sage invokes
it on import sage.all, as can be checked easily:

ondra`@`fuji:~/ext/sage$ . local/bin/sage-env
ondra`@`fuji:~/ext/sage$ python
Python 2.5.2 (r252:60911, Jul 11 2008, 05:28:36)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
>>>

Then apply this patch:

--- /tmp/genutils.py    2008-07-20 16:33:15.000000000 +0200
+++ local/lib/python2.5/site-packages/IPython/genutils.py       2008-07-20
16:33:26.553433732 +0200
`@``@` -54,6 +54,7 `@``@`
        if not hasattr(stream,'write') or not hasattr(stream,'flush'):
            stream = fallback
        self.stream = stream
+        stop
        self._swrite = stream.write
        self.flush = stream.flush



and:

ondra`@`fuji:~/ext/sage$ python
Python 2.5.2 (r252:60911, Jul 11 2008, 05:28:36)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/all.py",
line 58, in <module>
   from sage.misc.all       import *         # takes a while
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/all.py",
line 15, in <module>
   from sage_timeit_class import timeit
 File "sage_timeit_class.pyx", line 3, in sage.misc.sage_timeit_class
(sage/misc/sage_timeit_class.c:485)
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/sage_timeit.py",
line 12, in <module>
   import timeit as timeit_, time, math, preparser, interpreter
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/interpreter.py",
line 108, in <module>
   from IPython.iplib import InteractiveShell
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/__init__.py",
line 57, in <module>
   __import__(name,glob,loc,[])
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/ipstruct.py",
line 22, in <module>
   from IPython.genutils import list2dict2
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py",
line 95, in <module>
   Term = IOTerm()
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py",
line 90, in __init__
   self.cin  = IOStream(cin,sys.stdin)
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py",
line 57, in __init__
   stop
NameError: global name 'stop' is not defined
```



---

Comment by was created at 2008-07-20 15:49:05

I think this shouldn't go into 3.0.6 since it could introduce bugs, as it touches several files.
That said, it's a smallish patch I made in 30 minutes.  So it's not crazy complicated.  It's just dangerous.


---

Attachment

This patch causes some problems on my machine.

1) Sage segfaults at exit.

2) When doing sage -t, I get the following problem for every file:

```
sage -t  devel/sage-combinat/sage/combinat/root_system/all.pyTraceback (most recent call last):
  File "/opt/sage/tmp/.doctest_all.py", line 2, in <module>
    from sage.all_cmdline import *; 
  File "/opt/sage/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/opt/sage/local/lib/python2.5/site-packages/sage/all.py", line 72, in <module>
    from sage.rings.all      import *
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/all.py", line 94, in <module>
    from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/qqbar.py", line 1163, in <module>
    QQxy = QQ['x', 'y']
  File "ring.pyx", line 146, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:1851)
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 303, in PolynomialRing
    R = _multi_variate(base_ring, names, n, sparse, order)        
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 409, in _multi_variate
    from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
```



---

Comment by was created at 2008-08-13 07:54:15

Mike said:
> 1) Sage segfaults at exit.
> 2) When doing sage -t, I get the following problem for every file: 

Mike, (1) what is your system?  (2) Can you do "sage -ba" and try again?

 -- William


---

Comment by anakha created at 2008-10-23 21:37:34

I just tried it out and got none of the problems described above.  

'import sage.all' doesn't import IPython as desired.  I'm not putting up a positive review because of the problems described above, but I would be nice to have feedback on this

I'm on OS X 10.5 with this patch applied against 3.1.4.


---

Comment by was created at 2009-06-15 23:22:20

If we've released for months and months (8 months!) without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by was created at 2009-06-15 23:22:20

Changing priority from blocker to major.


---

Attachment


---

Comment by mhansen created at 2013-07-22 14:23:58

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2013-07-22 14:23:58

This is much easier now with the new IPython.

Apply trac_3685.patch


---

Comment by chapoton created at 2013-08-21 16:08:57

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2013-08-21 16:08:57

it seems that the doctest fails on 5.12.beta2, so the patch needs work


---

Comment by chapoton created at 2013-08-25 16:14:57

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-08-25 16:14:57

Changing keywords from "" to "startup time and imports".


---

Attachment

I have found the problem, it seems ! Here is the patch solving the issue.

Needs review !


---

Comment by chapoton created at 2013-08-25 19:23:46

arggg, that breaks everything... Back to need work.. :(


---

Comment by chapoton created at 2013-08-25 19:23:46

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2013-08-25 19:53:53

I am not able to sort things out.

It seems that the import of IPython occurs because of the line

```
from IPython.core.formatters import PlainTextFormatter
```

in "sage.misc.displayhook"

Is there a way to avoid this IPython import ?


---

Comment by mkoeppe created at 2021-09-07 08:18:13

#18726 took care of this and also added a doctest for it.

Outdated, should close


---

Comment by mkoeppe created at 2021-09-07 08:18:13

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2021-09-07 08:59:08

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2021-09-07 08:59:08

ok


---

Comment by mkoeppe created at 2021-09-10 04:50:10

Resolution: invalid
