# Issue 5460: [with patch, needs review] deprecate 'invert' in matrix_rational_dense

Issue created by migration from https://trac.sagemath.org/ticket/5460

Original creator: jhpalmieri

Original creation time: 2009-03-09 20:17:51

Assignee: jhpalmieri

See [this thread on sage-devel](http://groups.google.com/group/sage-support/browse_frm/thread/215ae58d5a3e900f).



---

Comment by rbeezer created at 2009-03-10 04:17:02

Replying to [ticket:5460 jhpalmieri]:
I get the deprecation warning with a singular matrix, but not with a nonsingular matrix.  Is this the desired/expected behavior?  Otherwise, it looks good, passed tests, etc.



```
sage: a=matrix(QQ, [[1,2],[3,6]])
sage: a.invert()
/opt/sage-dev/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: 'invert' is deprecated; use 'inverse' instead.
  exec code_obj in self.user_global_ns, self.user_ns
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<snip>
```



```
sage: b=matrix(QQ, [[1,2],[3,7]])
sage: b.invert()

[ 7 -2]
[-3  1]
```



```


---

Comment by jhpalmieri created at 2009-03-10 04:26:19

As far as I can tell, the deprecation function produces a warning message the first time you use the deprecated code, but not after that.  If you restart Sage and try the nonsingular matrix, you should get a warning for that one, too.


---

Comment by rbeezer created at 2009-03-10 04:41:26

Replying to [comment:2 jhpalmieri]:
Right.  I tested it twice, with a restart inbetween, but both times in the same order.  ;-)

Looks ready to go.


---

Comment by jason created at 2009-03-10 09:18:25

Good work!

Do the doctests pass for the invert function?  If so, I'm surprised; I thought that the doctest output would have to include the deprecation statement.

Regardless, the documentation for the invert function should include a sentence about the deprecation too.

Positive review (based on rbeezer's positive review) pending the changes to documentation and possibly doctests mentioned above.


---

Comment by rbeezer created at 2009-03-10 14:27:07

Replying to [comment:4 jason]:

> Do the doctests pass for the invert function?  If so, I'm surprised; I thought that the doctest output would have to include the deprecation statement.

I'd have assumed the same.  But doctests on the one source file passed, and  `sage -testall` only gave spurious unrelated errors in one file, and I'd seen those recently, so they should be unrelated.


---

Comment by jhpalmieri created at 2009-03-10 15:02:03

The one doctest involves a Traceback and "...", and I'm guessing that the "..." captures the deprecation error.  I agree, we should add a comment about deprecation to the documentation, and I'll get to that later today.


---

Attachment

Here's a new patch; the only difference is the documentation for 'invert'.


---

Comment by rbeezer created at 2009-03-10 19:15:50

Replying to [comment:7 jhpalmieri]:
> Here's a new patch; the only difference is the documentation for 'invert'.

Looks like its all ready now.


---

Comment by mabshoff created at 2009-03-23 21:26:31

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 21:26:31

Resolution: fixed
