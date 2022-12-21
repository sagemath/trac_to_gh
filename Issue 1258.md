# Issue 1258: additions and changes to linear_codes

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-11-25 04:06:48

Assignee: wdj

The patch
http://sage.math.washington.edu/home/wdj/patches/linear_codes20071124.hg
contains a new functions zeta_polynomial, weight_enumerator, 
chinen_polynomial, is_equivalent (for binary codes); an improved 
best_known_code; many pythonic revisions (suggested by William Stein 
long ago). Also, there are some minor docstring improvements. 
None of these are major improvements but I have a student working
on Duursma zeta functions of self-dual codes and these will be useful 
for her.


---

Comment by rlm created at 2007-12-01 23:19:10

Feedback: The changes all seem good, but I have a suggestion for further improvement. As you are probably well aware, any call like gap.eval(blablahblah) takes a lot of time, because of pseudo-tty. There are several places in the code where you are calling several gap.eval's within an inner loop. It seems like a much better idea to form one large string of GAP code, which includes the loop, and calling gap.eval on the large string exactly once. One example is the loop starting on line 963, linear_codes.py. (I know this will soon be replaced anyway, but it's a good example of unnecessary pseudo-tty lag.)

Also, there are some doctest issues, resulting in a negative review for now.


```
**********************************************************************
File "linear_code.py", line 853:
    sage: C1.is_equivalent(C2)
Exception raised:
    Traceback (most recent call last):
      File "/Volumes/HOME/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_23[5]>", line 1, in <module>
        C1.is_equivalent(C2)###line 853:
    sage: C1.is_equivalent(C2)
      File "/Volumes/HOME/sage/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 881, in is_equivalent
        return C1g.IsEquivalent(C2g) == True
      File "/Volumes/HOME/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 954, in __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args))
      File "/Volumes/HOME/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 901, in function_call
        return self.new("%s(%s)"%(function, ",".join([s.name() for s in args])))
      File "/Volumes/HOME/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 803, in new
        return self(code)
      File "/Volumes/HOME/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 738, in __call__
        return cls(self, x)
      File "/Volumes/HOME/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 989, in __init__
        raise TypeError, x
    TypeError: Gap produced error output
    Error, the command fail is not a name.
    possibly a binary is missing or has not been compiled.

       executing $sage199:=IsEquivalent($sage188,$sage256);;
**********************************************************************
```



```
**********************************************************************
File "linear_code.py", line 1669:
    sage: C.binomial_moment(3)    # long time
Expected:
    4
Got:
    0
**********************************************************************
```



---

Comment by rlm created at 2007-12-03 03:08:38

The first doctest failure seems to be an error in the way GAP is calling Leon's code. The directory mentioned in the documentation is
`SAGEHOME/local/lib/gap*/guava*`
but the guava code is installed in
`SAGEHOME/local/lib/gap*/pkg/guava*`


---

Comment by wdj created at 2007-12-11 00:19:11

1. To the best of my knowledge, the doctest failures are not the result of bad programming in this patch. They are because Leon's code, included with guava, is not compiled. It used to be that one could modify the spkg install file in SAGE's standard GAP package to try to fix this problem. Now the mechanism is different and I don't know why Leon's code is not compiled. 
The docstring typo mentioned above has been fixed.

2. "There are several places in the code where you are calling several gap.eval's within an inner loop." Agreed. I spent even more time trying to remove these calls. I did modify several two functions along these lines but don't know if they are any faster.
(a) I don't see how to without rewriting the GAP code. 
(b) Except for the example above, there were only one or 2 other places where gap.eval 
occurred in a loop. In those two cases, I tried to rewrite the code (I've tried before as well) 
but possibly not entirely successful. I don't see a tremendous savings anyway, since the loops are usually over the dimension and the computation inside the loop is growing exponentially with the dimension anyway...
(c) For the example above, I see not point in trying to speed it up since (a) I think it is buggy, (b) Robert Miller's code is hundreds of times faster and will be replacing it very soon. 
It is good to have for testing purposes though.

3. There was a mistake in the patch with the implementation of Chinen zeta polynomials. That has been fixed. 

The patch is at
http://sage.math.washington.edu/home/wdj/patches/linear-codes20071210.hg
and modified file at
http://sage.math.washington.edu/home/wdj/patches/linear_code.py


---

Attachment


---

Comment by rlm created at 2007-12-11 18:45:47

The bundle at 
http://sage.math.washington.edu/home/rlmill/sage-2.9.alpha5/codes.hg
should apply cleanly to sage-2.9.alpha5


---

Attachment


---

Comment by rlm created at 2007-12-15 23:29:21

From IRC:

```
[2:48pm] was-1258: rlm -- after applying 1258 the doctests for linear_code.py take 93 seconds on sage.math!
[2:48pm] was-1258: unacceptable.
...
[2:48pm] was-1258: line 1062 takes a long time.
...
[2:49pm] was-1258: line 1280
[2:49pm] was-1258: line 1333
[2:49pm] was-1258: 1757
[2:49pm] was-1258: 352 takes very long.
```


Computations taking longer than about 10 seconds or so should be marked # long time, so that the doctester knows to skip them unless you do `./sage -t -long`. Also, computations taking longer than a minute or two are probably not suitable for doctesting.


---

Comment by mabshoff created at 2007-12-16 00:31:18

Resolution: fixed


---

Comment by mabshoff created at 2007-12-16 00:31:18

Merged in 2.9.rc2.
