# Issue 8430: three doctest failures with Sage 4.3.4.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/8430

Original creator: mvngu

Original creation time: 2010-03-03 18:42:04

Assignee: tbd

CC:  sage-combinat

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/99b72f5f27858b53):

```
* The following tests failed on sage.math:

sage -t  -long local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/notebook/interact.py # 1 doctests failed
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py # 1 doctests failed
sage -t  -long devel/sage/sage/categories/finite_semigroups.py # 2 doctests failed
sage -t  -long devel/sage/sage/categories/examples/finite_semigroups.py # 1 doctests failed 
```



---

Comment by jhpalmieri created at 2010-03-03 22:08:56

I've tried to address the problem with sageinspect.py in ticket #8324.


---

Comment by jhpalmieri created at 2010-03-03 22:29:21

Note that the problem with `sagenb/notebook/interact.py` should be fixed by the sagenb patch at ticket #5601.


---

Comment by hivert created at 2010-03-04 10:14:18

Changing status from new to needs_review.


---

Comment by hivert created at 2010-03-04 10:14:18

> * The following tests failed on sage.math:

```
sage -t  -long devel/sage/sage/categories/finite_semigroups.py # 2 doctests failed
sage -t  -long devel/sage/sage/categories/examples/finite_semigroups.py # 1 doctests failed 
```

Those last two should be fixed by the submitted patch. A better fix together with improvements is being written on sage-combinat but I don't know how long finishing those improvements will take. So please review the patch. 

By the way, should'nt I create a ticket for this patch ? It is certainly orthogonal to the two other one doctest failure.

Cheers,

Florent


---

Comment by mhampton created at 2010-03-04 21:08:26

Since the other issues have there own tickets I don't think another one is necessary.

There is one doctest failure still:

```
File "/Volumes/E/sage-4.3.4.alpha0/devel/sage-t1/sage/categories/finite_semigroups.py", line 229:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
*********************************************
```


which is not covered by the patch.  Seems like maybe the expected string is wrong, unless the sorted function has varying behavior.


---

Comment by mhampton created at 2010-03-04 21:08:46

Changing status from needs_review to needs_work.


---

Attachment

Replying to [comment:5 mhampton]:

> There is one doctest failure still:

```
File "/Volumes/E/sage-4.3.4.alpha0/devel/sage-t1/sage/categories/finite_semigroups.py", line 229:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
*********************************************
}}} 
> which is not covered by the patch.  Seems like maybe the expected string is wrong, unless the sorted function has varying behavior.

I'm not sure to understand:
 - why I missed this one;
 - why the result of sorted changed between 4.3.3 and 4.3.4;
 - why despite of this change it seems to be stable on both version...
Anyway the newly uploaded patch passed the tests 10 times in a raw on the machine sage. Maybe it could be worth checking of it is also stable on other architectures.

Sorry for the mess and please review.


---

Comment by hivert created at 2010-03-04 21:41:49

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-03-04 21:42:10

Changing assignee from tbd to hivert.


---

Comment by mhampton created at 2010-03-04 22:27:10

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-03-04 22:27:10

All tests in categories passed on a 10.6 mac and on 64-bit Ubuntu 9.10, so I think I can give this a positive review.


---

Comment by mpatel created at 2010-03-04 23:28:14

SageNB 0.7.5.2 includes fixes for the first two failures in the description (see #8435).

An important note:  It's best to test SageNB files with `-force_lib`, e.g.,


```sh
sage -t -long -force_lib local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/notebook/interact.py
```


Running `sage -t -sagenb` or `make test` and its friends will set it implicitly.  If the option is set, `SAGE_LOCAL/bin/sage-doctest` will treat the file(s) as Sage library code, even if it does not live under `SAGE_ROOT/devel`.  In particular, `sage-doctest` will not attempt the equivalent of `from filebase import *`, which can raise false errors or cause segfaults.

I suppose I should have called it `-library_code`, instead.

Please remember to fillin


---

Comment by drkirkby created at 2010-03-05 14:00:06

I'm not at home, and can't very easily start applying patches, but I can confirm I get the same results, based on Sage 4.3.4.alpha0 but with a few Solaris-specific patches on Solaris 10 (SPARC)


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/fini
te_semigroups.py", line 232:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/fini
te_semigroups.py", line 198:
    sage: S.j_classes()
Expected:
    [['acb', 'cab', 'bca', 'abc', 'bac', 'cba'], ['ac', 'ca'],
    ['ab', 'ba'], ['bc', 'cb'], ['a'], ['c'], ['b']]
Got:
    [['a'], ['acb', 'cba', 'bca', 'abc', 'bac', 'cab'], ['ac', 'ca'], ['ab', 'ba
'], ['cb', 'bc'], ['c'], ['b']]
**********************************************************************
2 items had failures:
```



So the problem is occuring on more that one architecuture. I hope to try the patch within the next 12 hours.


---

Comment by mhansen created at 2010-03-09 07:44:51

Resolution: fixed
