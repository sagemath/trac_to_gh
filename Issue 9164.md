# Issue 9164: cygwin: gap.cputime() does not work

Issue created by migration from https://trac.sagemath.org/ticket/9164

Original creator: was

Original creation time: 2010-06-07 04:02:22

Assignee: tbd

CC:  jpflori dimpase


```

sage: gap.cputime()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/wstein/sage-4.4.3/<ipython console> in <module>()

/home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in cputime(self, t)
    429         else:
    430             self.eval('_r_ := Runtimes();')
--> 431             r = sum(eval(self.eval('[_r_.user_time, _r_.system_time, _r_.user_time_children, _r_.system_time_children]')))
    432             return r/1000.0
    433 

/home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in <module>()

NameError: name 'fail' is not defined
sage: 
```



---

Comment by kcrisman created at 2013-02-27 03:23:37

Hey, is this related to the mysterious comment

```
sage: v, t = qsieve(n, time=True)   # uses the sieve    (optional: time doesn't work on cygwin) 
```

in sage/interfaces/qsieve.py?  And does `time` now work on Cygwin?


---

Comment by jpflori created at 2013-02-27 21:40:30

Changing status from new to needs_review.


---

Comment by jpflori created at 2013-02-27 21:40:30

Dont think so.

gap.cputime() works on both my systems.
It is even so nice it reports twice as much on the 32 bits than on the 64 bits...

So let's close this one.

Nonetheless the other qsieve examples do not work, this should be treated elsewhere.


---

Comment by jpflori created at 2013-02-27 22:02:28

Replying to [comment:2 jpflori]:
> Nonetheless the other qsieve examples do not work, this should be treated elsewhere.
Or not:
http://comments.gmane.org/gmane.os.cygwin/106331
Although the time bash builtin works, there is no time command under Cygwin (nor in any package), so either we should modify the qsieve code (what will have to be done anyway after #12173 gets in and we get rid of qsieve which will then be obsoleted), or live with such code being optional.


---

Comment by jpflori created at 2013-02-27 22:06:08

My bad, I wrongly used cygcheck.
There is http://cygwin.com/packages/time/
So either we make time a prereq which I would not advocate for, or rather test at runtime if the real time executable is available.
But thats for another ticket anyway (unless I get my hand on a Mac, fix #12173 and remove qsieve by that time).


---

Comment by kcrisman created at 2013-02-27 22:07:17

JP, see #14184.  What do you think?


---

Comment by jdemeyer created at 2013-02-28 07:43:18

Replying to [comment:3 jpflori]:
> Although the time bash builtin works, there is no time command under Cygwin (nor in any package)
This has nothing to do with Cygwin. My Gentoo Linux system doesn't have a `time` command either, it does have the `time` keyword (to be pedantic: it's a keyword, not a builtin) in bash.

> so [...] we should modify the qsieve code
Exactly, see #14202.


---

Comment by kcrisman created at 2013-03-08 12:43:30

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-03-08 12:43:30

After a rebase, this works!  Awesome.


---

Comment by jdemeyer created at 2013-03-15 13:02:31

Resolution: worksforme
