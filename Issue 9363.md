# Issue 9363: load bug when last line of file begins with #

Issue created by migration from Trac.

Original creator: mariah

Original creation time: 2010-06-28 19:38:07

Assignee: somebody


```
Consider the following files and what sage
does with each when they are loaded:

---- foo1.sage ------
def add(a,b):
 return a+b
------------------------

--- foo2.py---
def add(a,b):
 return a+b
# this is a comment
---------------------

--- foo3.sage---
def add(a,b):
 return a+b
# this is a comment
---------------------

eno% ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: load "foo1.sage"
sage: load "foo2.py"
sage: load "foo3.sage"
------------------------------------------------------------
  File "<string>", line 3
    # this is a comment
                      ^
SyntaxError: invalid syntax
| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |
sage:

Is the inability to load foo3.sage a bug or a feature?

According to William Stein: 

> It's a bug.   Please make a trac ticket for this. 
> Note that adding a newline to the end of the file is enough to 
> fix the problem... 
```



---

Comment by wjp created at 2011-01-07 23:08:19

One line reproduction recipe:


```
exec("if True:\n pass\n#")
```



---

Comment by wjp created at 2011-01-07 23:20:09

The reason for this is likely this note from the python docs:


```
When compiling a string with multi-line code in
'single' or 'eval' mode, input must be terminated
by at least one newline character. This is to
facilitate detection of incomplete and complete
statements in the code module.
```


(Also note:

```
Changed in version 2.7: Allowed use of Windows and
Mac newlines. Also input in 'exec' mode does not
have to end in a newline anymore.
```

)

The obvious patch would be to add a newline automatically before passing the input to `exec`. I'll create a patch for this.


---

Attachment


---

Comment by wjp created at 2011-01-07 23:25:45

Changing status from new to needs_review.


---

Comment by aly.deines created at 2011-01-07 23:49:46

Changing status from needs_review to needs_work.


---

Comment by aly.deines created at 2011-01-07 23:49:46

The patch won't apply:

applying 9363_exec_newline.patch
patching file sage/misc/preparser.py
Hunk #1 FAILED at 1588
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 9363_exec_newline.patch


---

Comment by wjp created at 2011-01-07 23:53:14

Which version of sage are you using? Unless I messed something up, it's a patch against 4.6.1.rc0, which I should have mentioned, sorry.


---

Comment by aly.deines created at 2011-01-08 00:00:58

Replying to [comment:5 wjp]:
> Which version of sage are you using? Unless I messed something up, it's a patch against 4.6.1.rc0, which I should have mentioned, sorry.

Okay!  I was just using 4.6.


---

Comment by wjp created at 2011-01-08 00:05:49

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2011-01-08 20:09:28

On sage-4.6.rc0 the following tests failed:

	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
	sage -t  "devel/sage/sage/interfaces/r.py"
	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"

I'll try again on sage-4.6.rc1 and see what happens there.


---

Comment by aly.deines created at 2011-01-08 20:12:23

Replying to [comment:8 aly.deines]:
> On sage-4.6.rc0 the following tests failed:
> 
> 	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
> 	sage -t  "devel/sage/sage/interfaces/r.py"
> 	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
> 
> I'll try again on sage-4.6.rc1 and see what happens there.

Better formatting:


```

	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
	sage -t  "devel/sage/sage/interfaces/r.py"
	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
```



---

Comment by wjp created at 2011-01-08 23:51:12

Strange, but those shouldn't be related to this patch (or so I hope). Do they also happen if you run these three tests manually? And without this patch?


---

Comment by aly.deines created at 2011-01-08 23:55:48

Replying to [comment:10 wjp]:
> Strange, but those shouldn't be related to this patch (or so I hope). Do they also happen if you run these three tests manually? And without this patch?

I get the same thing when the three tests are run manually, and these tests pass when the patch is not applied.


---

Comment by wjp created at 2011-01-08 23:58:03

Can you show the full output of the failing tests? (I can't get them to fail myself on my PC.)


---

Comment by gbe created at 2011-01-09 00:19:19

Replying to [comment:9 aly.deines]:
> Replying to [comment:8 aly.deines]:
> > On sage-4.6.rc0 the following tests failed:
> > 
> > 	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
> > 	sage -t  "devel/sage/sage/interfaces/r.py"
> > 	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
> > 
> > I'll try again on sage-4.6.rc1 and see what happens there.
> 
> Better formatting:
> 
> {{{
> 
> 	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
> 	sage -t  "devel/sage/sage/interfaces/r.py"
> 	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
> }}}

I'll unapply the patch and retry these three doctests, but earlier this afternoon they failed both before and after the patch was applied.


However, the test


```
      sage -t  "devel/sage/sage/misc/preparser.py"
```


Passes both before and after applying the patch.


---

Comment by jthurber created at 2011-01-09 00:24:52

passed all tests for me this afternoon (4.6.4.rc1), but checking coverage yielded: 


```

devel/sage/sage/misc/preparser.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage/sage/misc/preparser.py: 88% (23 of 26)

Missing documentation:
	 * isalphadigit_(s):
	 * for lambda try """.split() in_single_quote = False in_double_quote = False in_triple_quote = False def in_quote():
	 * re_no_keyword(pattern, code):
```



---

Comment by aly.deines created at 2011-01-09 00:37:28

Replying to [comment:14 jthurber]:
> passed all tests for me this afternoon (4.6.4.rc1), but checking coverage yielded: 
> 
> {{{
> 
> devel/sage/sage/misc/preparser.py
> ERROR: Please add a `TestSuite(s).run()` doctest.
> SCORE devel/sage/sage/misc/preparser.py: 88% (23 of 26)
> 
> Missing documentation:
> 	 * isalphadigit_(s):
> 	 * for lambda try """.split() in_single_quote = False in_double_quote = False in_triple_quote = False def in_quote():
> 	 * re_no_keyword(pattern, code):
> }}}

So two things, first, I think I ran the tests on a different version of sage, as now I am getting that those three tests fail both with and without the patch applied.  
Second, the add 'TestSuit(s).run()' doctest and the missing doctest are not related to this ticket (though completing the coverage could be another ticket.)


---

Comment by aly.deines created at 2011-01-09 00:37:28

Changing status from needs_review to positive_review.


---

Comment by gbe created at 2011-01-09 01:05:32

Replying to [comment:15 aly.deines]:
> So two things, first, I think I ran the tests on a different version of sage, as now I am getting that those three tests fail both with and without the patch applied.  
> Second, the add 'TestSuit(s).run()' doctest and the missing doctest are not related to this ticket (though completing the coverage could be another ticket.)

It looks to me like those doctest failures were fixed some time between 4.6 and 4.6.1rc0.


---

Comment by kcrisman created at 2011-01-14 17:37:25

I've noticed this before but hadn't diagnosed it - thanks!  Will this also fix the analogous thing for `attach` instead of `load`?


---

Comment by wjp created at 2011-01-17 16:44:45

I haven't actually tried that, but looking at the code `attach` should be following the same code path.


---

Comment by jdemeyer created at 2011-01-19 22:20:55

Resolution: fixed
