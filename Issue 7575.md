# Issue 7575: EllipticCurve.gens: height bounds not handled well in two_descent

archive/issues_007575.json:
```json
{
    "body": "Assignee: cremona\n\nThe documentation for `EllipticCurve.gens` says:\n\n```\nHINT: If you would like to control the height bounds used in the\n2-descent, first call the two_descent function with those height\nbounds. However that function, while it displays a lot of output,\nreturns no values.\n```\n\n\nHowever, this doesn't work, because `EllipticCurve.gens` doesn't know about it:\n\n\n```\nsage: x,y=var('x,y')\nsage: E = EllipticCurve(y^2 + x*y + y == x^3 - 10525529*x - 21714803524)\nsage: E.two_descent(second_limit=11, verbose=False)\nsage: E.gens()\n*BOOM*\n```\n\n\nDespite:\n\n\n```\nsage: A = E.mwrank_curve()\nsage: A.gens()\n[[1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L]]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7575\n\n",
    "created_at": "2009-12-01T21:56:26Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "title": "EllipticCurve.gens: height bounds not handled well in two_descent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7575",
    "user": "rlm"
}
```
Assignee: cremona

The documentation for `EllipticCurve.gens` says:

```
HINT: If you would like to control the height bounds used in the
2-descent, first call the two_descent function with those height
bounds. However that function, while it displays a lot of output,
returns no values.
```


However, this doesn't work, because `EllipticCurve.gens` doesn't know about it:


```
sage: x,y=var('x,y')
sage: E = EllipticCurve(y^2 + x*y + y == x^3 - 10525529*x - 21714803524)
sage: E.two_descent(second_limit=11, verbose=False)
sage: E.gens()
*BOOM*
```


Despite:


```
sage: A = E.mwrank_curve()
sage: A.gens()
[[1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L]]
```


Issue created by migration from https://trac.sagemath.org/ticket/7575





---

archive/issue_comments_064478.json:
```json
{
    "body": "With the patch `trac_7575-heegner_index_example.patch` applied on top of (sage-4.3 plus) #7576 and #7819, I get the following:\n\n\n```\nsage: E = EllipticCurve('123a1')\nsage: E.prove_BSD(verbosity=2)\np = 2: true by 2-descent\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n...<SNIP>...\n/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/libs/mwrank/interface.pyc in gens(self)\n    310         \"\"\"\n    311         self.saturate()\n--> 312         return eval(self.__two_descent_data().getbasis().replace(\":\",\",\"))\n    313 \n    314     def certain(self):\n\nRuntimeError: \n```\n",
    "created_at": "2010-01-02T15:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64478",
    "user": "rlm"
}
```

With the patch `trac_7575-heegner_index_example.patch` applied on top of (sage-4.3 plus) #7576 and #7819, I get the following:


```
sage: E = EllipticCurve('123a1')
sage: E.prove_BSD(verbosity=2)
p = 2: true by 2-descent
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...<SNIP>...
/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/libs/mwrank/interface.pyc in gens(self)
    310         """
    311         self.saturate()
--> 312         return eval(self.__two_descent_data().getbasis().replace(":",","))
    313 
    314     def certain(self):

RuntimeError: 
```




---

archive/issue_comments_064479.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-01-02T15:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64479",
    "user": "rlm"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_064480.json:
```json
{
    "body": "In the original example (in this ticket's description), note that calling E.two_descent() produces output to the screen but returns nothing and stores nothing in E which was not there before.  E.gens() by default uses mwrank_shell, which does not allow any passing of parameters (see the TODO block in the docstring), not because it cannot be done but because we have not implemented it.  The non-default option mwrank_lib goes via creation of the associated mwrank_curve which also does not allow changing of the parameters.\n\nWhat I suggest is that we use mwrank_lib by default;  that we allow passing of all the parameters which the two_descent function of an mwrank elliptic curve allows from all higher level functions which call mwrank (e.g. gens()) and that we use the enquiry functions provided by mwrank to find out how successful it has been:  it can give you a lower and upper bound for the rank, so all is well if they are equal and in any case can give you a number of gens equal to the lower bound.  The only difficulty would be with caching rank and gens -- probably best not to do so at all unless we have certainly found them.\n\nDoes this all make sense?  I think it would be much more helpful to have sample curves where things do not work well and sample code which does not go via a call to the (presumably complicated) function prove_BSD()!",
    "created_at": "2010-01-03T18:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64480",
    "user": "cremona"
}
```

In the original example (in this ticket's description), note that calling E.two_descent() produces output to the screen but returns nothing and stores nothing in E which was not there before.  E.gens() by default uses mwrank_shell, which does not allow any passing of parameters (see the TODO block in the docstring), not because it cannot be done but because we have not implemented it.  The non-default option mwrank_lib goes via creation of the associated mwrank_curve which also does not allow changing of the parameters.

What I suggest is that we use mwrank_lib by default;  that we allow passing of all the parameters which the two_descent function of an mwrank elliptic curve allows from all higher level functions which call mwrank (e.g. gens()) and that we use the enquiry functions provided by mwrank to find out how successful it has been:  it can give you a lower and upper bound for the rank, so all is well if they are equal and in any case can give you a number of gens equal to the lower bound.  The only difficulty would be with caching rank and gens -- probably best not to do so at all unless we have certainly found them.

Does this all make sense?  I think it would be much more helpful to have sample curves where things do not work well and sample code which does not go via a call to the (presumably complicated) function prove_BSD()!



---

archive/issue_comments_064481.json:
```json
{
    "body": "Another thought:  perhaps we should have a class to hold a list of all mwrank-options.",
    "created_at": "2010-01-03T18:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64481",
    "user": "cremona"
}
```

Another thought:  perhaps we should have a class to hold a list of all mwrank-options.



---

archive/issue_comments_064482.json:
```json
{
    "body": "Here is another part where using the library would help:\n\n```\nsage: EllipticCurve([1, 1, 1, -9718914979, 370891890941633]).mwrank()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (47, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (362, 0))\n\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/Users/rlmill/sage-4.3.1.rc1/devel/sage-main/<ipython console> in <module>()\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in mwrank(self, options)\n    484             from sage.interfaces.all import Mwrank\n    485             mwrank = Mwrank(options=options)\n--> 486         return mwrank(list(self.a_invariants()))\n    487 \n    488     def conductor(self, algorithm=\"pari\"):\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/mwrank.pyc in __call__(self, cmd)\n     75 \n     76     def __call__(self, cmd):\n---> 77         return self.eval(str(cmd))\n     78 \n     79     def eval(self, *args, **kwds):\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/mwrank.pyc in eval(self, *args, **kwds)\n     95             # Doing _start again fixes that always. See trac #5157.\n     96             self._start()\n---> 97         return Expect.eval(self, *args, **kwds)\n     98 \n     99     def console(self):\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)\n    981         try:\n    982             with gc_disabled():\n--> 983                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    984         except KeyboardInterrupt:\n    985             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    666                         # we expect to get an EOF if we're quitting.\n    667                         return ''\n--> 668                     raise RuntimeError, \"%s\\n%s crashed executing %s\"%(msg,self, line)\n    669                 out = E.before\n    670             else:\n\nRuntimeError: End Of File (EOF) in read_nonblocking(). Empty string style platform.\n<pexpect.spawn instance at 0xebec738>\nversion: 2.0 ($Revision: 1.151 $)\ncommand: /Users/rlmill/sage-4.3.1.rc1/local/bin/mwrank\nargs: ['/Users/rlmill/sage-4.3.1.rc1/local/bin/mwrank']\npatterns:\n    Enter curve: \nbuffer (last 100 chars): \nbefore (last 100 chars): up to 232549 (square a first...)\nAttempt to round -9608958007.0937 to a long int fails, aborting!\n\nafter: <class 'pexpect.EOF'>\nmatch: None\nmatch_index: None\nexitstatus: None\nflag_eof: 1\npid: 90387\nchild_fd: 7\ntimeout: None\ndelimiter: <class 'pexpect.EOF'>\nlogfile: None\nmaxread: 10000\nsearchwindowsize: None\ndelaybeforesend: 0\nMwrank crashed executing [1, 1, 1, -9718914979, 370891890941633]\n```\n",
    "created_at": "2010-01-19T21:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64482",
    "user": "rlm"
}
```

Here is another part where using the library would help:

```
sage: EllipticCurve([1, 1, 1, -9718914979, 370891890941633]).mwrank()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (47, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (362, 0))

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/rlmill/sage-4.3.1.rc1/devel/sage-main/<ipython console> in <module>()

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in mwrank(self, options)
    484             from sage.interfaces.all import Mwrank
    485             mwrank = Mwrank(options=options)
--> 486         return mwrank(list(self.a_invariants()))
    487 
    488     def conductor(self, algorithm="pari"):

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/mwrank.pyc in __call__(self, cmd)
     75 
     76     def __call__(self, cmd):
---> 77         return self.eval(str(cmd))
     78 
     79     def eval(self, *args, **kwds):

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/mwrank.pyc in eval(self, *args, **kwds)
     95             # Doing _start again fixes that always. See trac #5157.
     96             self._start()
---> 97         return Expect.eval(self, *args, **kwds)
     98 
     99     def console(self):

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)
    981         try:
    982             with gc_disabled():
--> 983                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    984         except KeyboardInterrupt:
    985             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)
    666                         # we expect to get an EOF if we're quitting.
    667                         return ''
--> 668                     raise RuntimeError, "%s\n%s crashed executing %s"%(msg,self, line)
    669                 out = E.before
    670             else:

RuntimeError: End Of File (EOF) in read_nonblocking(). Empty string style platform.
<pexpect.spawn instance at 0xebec738>
version: 2.0 ($Revision: 1.151 $)
command: /Users/rlmill/sage-4.3.1.rc1/local/bin/mwrank
args: ['/Users/rlmill/sage-4.3.1.rc1/local/bin/mwrank']
patterns:
    Enter curve: 
buffer (last 100 chars): 
before (last 100 chars): up to 232549 (square a first...)
Attempt to round -9608958007.0937 to a long int fails, aborting!

after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: None
flag_eof: 1
pid: 90387
child_fd: 7
timeout: None
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 10000
searchwindowsize: None
delaybeforesend: 0
Mwrank crashed executing [1, 1, 1, -9718914979, 370891890941633]
```




---

archive/issue_comments_064483.json:
```json
{
    "body": "This behaviour is supposed to be caught by mwrank C++ code, so that this can be detected gracefully by using the ok() function.\n\nAs we are planning to replace the pexpect interface entirely this will be dealt with.  (There is absolutely no reason to use the interactive interface when everything can be found from the library interface.)",
    "created_at": "2010-01-19T21:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64483",
    "user": "cremona"
}
```

This behaviour is supposed to be caught by mwrank C++ code, so that this can be detected gracefully by using the ok() function.

As we are planning to replace the pexpect interface entirely this will be dealt with.  (There is absolutely no reason to use the interactive interface when everything can be found from the library interface.)



---

archive/issue_comments_064484.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\n> This behaviour is supposed to be caught by mwrank C++ code, so that this can be detected gracefully by using the ok() function.\n\nOn looking into it, I see that this will need a patch to the file src/qrank/mrank1.cc, since I just call abort() when I try to round to a long int and it overflows.  Instead I need to catch that properly.  (Pity C++ does not have the try/except functionality of python).\n\nSo this particular bug / behaviour needs to be flagged as \"report upstream (done) and wait for a patch from upstream (on my todo list)\".\n\n\n> \n> As we are planning to replace the pexpect interface entirely this will be dealt with.  (There is absolutely no reason to use the interactive interface when everything can be found from the library interface.)",
    "created_at": "2010-01-19T22:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64484",
    "user": "cremona"
}
```

Replying to [comment:5 cremona]:
> This behaviour is supposed to be caught by mwrank C++ code, so that this can be detected gracefully by using the ok() function.

On looking into it, I see that this will need a patch to the file src/qrank/mrank1.cc, since I just call abort() when I try to round to a long int and it overflows.  Instead I need to catch that properly.  (Pity C++ does not have the try/except functionality of python).

So this particular bug / behaviour needs to be flagged as "report upstream (done) and wait for a patch from upstream (on my todo list)".


> 
> As we are planning to replace the pexpect interface entirely this will be dealt with.  (There is absolutely no reason to use the interactive interface when everything can be found from the library interface.)



---

archive/issue_comments_064485.json:
```json
{
    "body": "The documentation for `EllipticCurve.gens` says:\n\n```\nHINT: If you would like to control the height bounds used in the\n2-descent, first call the two_descent function with those height\nbounds. However that function, while it displays a lot of output,\nreturns no values.\n```\n\n\nHowever, this doesn't work, because `EllipticCurve.gens` doesn't know about it:\n\n\n```\nsage: x,y=var('x,y')\nsage: E = EllipticCurve(y^2 + x*y + y == x^3 - 10525529*x - 21714803524)\nsage: E.two_descent(second_limit=11, verbose=False)\nsage: E.gens()\n*BOOM*\n```\n\n\nDespite:\n\n\n```\nsage: A = E.mwrank_curve()\nsage: A.gens()\n[[1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L]]\n```\n",
    "created_at": "2010-01-19T22:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64485",
    "user": "rlm"
}
```

The documentation for `EllipticCurve.gens` says:

```
HINT: If you would like to control the height bounds used in the
2-descent, first call the two_descent function with those height
bounds. However that function, while it displays a lot of output,
returns no values.
```


However, this doesn't work, because `EllipticCurve.gens` doesn't know about it:


```
sage: x,y=var('x,y')
sage: E = EllipticCurve(y^2 + x*y + y == x^3 - 10525529*x - 21714803524)
sage: E.two_descent(second_limit=11, verbose=False)
sage: E.gens()
*BOOM*
```


Despite:


```
sage: A = E.mwrank_curve()
sage: A.gens()
[[1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L]]
```




---

archive/issue_comments_064486.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-03T05:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64486",
    "user": "rlm"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_064487.json:
```json
{
    "body": "The 1st and 4th items in the TODO list are implemented in #8184 with a new spkg and subsequent patch,\n\nI think that logically that patch should be reviewed first, and then this one will need so changes (since a lot of the same functions are affected).  I hope others (rlm in particular) will agree!  For that reason (only) I have switched this to \"needs work\".",
    "created_at": "2010-02-04T14:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64487",
    "user": "cremona"
}
```

The 1st and 4th items in the TODO list are implemented in #8184 with a new spkg and subsequent patch,

I think that logically that patch should be reviewed first, and then this one will need so changes (since a lot of the same functions are affected).  I hope others (rlm in particular) will agree!  For that reason (only) I have switched this to "needs work".



---

archive/issue_comments_064488.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-04T14:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64488",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064489.json:
```json
{
    "body": "Attachment\n\ndepends on #8184, #8155 (and possibly #8124)",
    "created_at": "2010-02-04T21:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64489",
    "user": "rlm"
}
```

Attachment

depends on #8184, #8155 (and possibly #8124)



---

archive/issue_comments_064490.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T21:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64490",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064491.json:
```json
{
    "body": "I applied trac_7575.patch successfully to 4.3.2 after first applying everything from \n#8184, #8155 and  #8124 in that order.\n\nThe code looks good.  It's great now that we do not have to make embarrassing excuses for mwrank's incomplete output!\n\nI only spotted one thing:  in a couple of places the docstring says that the default search bound is 16, whereas it is in fact 12.  (Certainly 12 is more sensible!)  That needs changing (trivial).  It might be a good idea to alert the user to how expensive (in time) adding one to the bound is, so that (for example) a bound of 20 could lead to the program never ending.\n\nOne other comment (to rlm):   when doing descent by 2-isogeny, when the second descent is used and the coefficients are large, it is a good idea to increase the decimal precision a lot (to 100 or 200 digits) because then the reduction of the second descent quartics is done much better.  Now, mwrank will not do that for you (though perhaps it should).  I suggest that when mwrank is used on curves with 2-torsion, we first call mwrank_set_precision(200).  This will not slow anything down (in fact the opposite) -- but that is not the case for 2-descent in general (no 2-torsion).  Perhaps we could do that on another ticket.\n\nI tested the whole library with -long after applying this patch and the earlier ones on which it depends (as well as the new eclib spkg at #8184):  all pass!\n\nI really hope that this sequence of 4 tickets can all be merged quickly into 4.3.3.",
    "created_at": "2010-02-06T17:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64491",
    "user": "cremona"
}
```

I applied trac_7575.patch successfully to 4.3.2 after first applying everything from 
#8184, #8155 and  #8124 in that order.

The code looks good.  It's great now that we do not have to make embarrassing excuses for mwrank's incomplete output!

I only spotted one thing:  in a couple of places the docstring says that the default search bound is 16, whereas it is in fact 12.  (Certainly 12 is more sensible!)  That needs changing (trivial).  It might be a good idea to alert the user to how expensive (in time) adding one to the bound is, so that (for example) a bound of 20 could lead to the program never ending.

One other comment (to rlm):   when doing descent by 2-isogeny, when the second descent is used and the coefficients are large, it is a good idea to increase the decimal precision a lot (to 100 or 200 digits) because then the reduction of the second descent quartics is done much better.  Now, mwrank will not do that for you (though perhaps it should).  I suggest that when mwrank is used on curves with 2-torsion, we first call mwrank_set_precision(200).  This will not slow anything down (in fact the opposite) -- but that is not the case for 2-descent in general (no 2-torsion).  Perhaps we could do that on another ticket.

I tested the whole library with -long after applying this patch and the earlier ones on which it depends (as well as the new eclib spkg at #8184):  all pass!

I really hope that this sequence of 4 tickets can all be merged quickly into 4.3.3.



---

archive/issue_comments_064492.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-06T17:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64492",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064493.json:
```json
{
    "body": "PS Robert, please look at those second descent default search limits:  16 is really large, and when I looked again I saw that you really do have 16 as the default.  I would suggest using 12.",
    "created_at": "2010-02-06T17:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64493",
    "user": "cremona"
}
```

PS Robert, please look at those second descent default search limits:  16 is really large, and when I looked again I saw that you really do have 16 as the default.  I would suggest using 12.



---

archive/issue_comments_064494.json:
```json
{
    "body": "Fixes default search bounds",
    "created_at": "2010-02-07T02:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64494",
    "user": "rlm"
}
```

Fixes default search bounds



---

archive/issue_comments_064495.json:
```json
{
    "body": "Attachment\n\nThis last patch sets all defaults (and docstrings) to 12.",
    "created_at": "2010-02-07T02:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64495",
    "user": "rlm"
}
```

Attachment

This last patch sets all defaults (and docstrings) to 12.



---

archive/issue_comments_064496.json:
```json
{
    "body": "With the new version of trac_7575-followup.patch everything is 100% fine.\n\nRecap: apply everything from #8184, #8155 and #8124 in that order and then both patches here in order.  All tests pass, and all looks (very) good!",
    "created_at": "2010-02-07T11:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64496",
    "user": "cremona"
}
```

With the new version of trac_7575-followup.patch everything is 100% fine.

Recap: apply everything from #8184, #8155 and #8124 in that order and then both patches here in order.  All tests pass, and all looks (very) good!



---

archive/issue_comments_064497.json:
```json
{
    "body": "In preparing for 4.3.3.alpha0, I noticed a [minor?] problem : After I run `sage -t ell_rational_field.py`, there's a new untracked file in the repository:\n\n```\n$ hg stat\n? sage/schemes/elliptic_curves/PRIMES\nm\n```\n\nIt contains `16180561` and sometimes `19047851`.  If this is easy to fix, feel free to add another follow-up patch here.",
    "created_at": "2010-02-11T00:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64497",
    "user": "mpatel"
}
```

In preparing for 4.3.3.alpha0, I noticed a [minor?] problem : After I run `sage -t ell_rational_field.py`, there's a new untracked file in the repository:

```
$ hg stat
? sage/schemes/elliptic_curves/PRIMES
m
```

It contains `16180561` and sometimes `19047851`.  If this is easy to fix, feel free to add another follow-up patch here.



---

archive/issue_comments_064498.json:
```json
{
    "body": "Sorry about that.  When eclib programs run they leave behind a file of that name (containing large primes found during the computations, for use in later runs).  And it is left in the working directory.  This is probably leftover from a testrun I did before committing changes.\n\nI think all will be well if you just delete that file.",
    "created_at": "2010-02-11T09:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64498",
    "user": "cremona"
}
```

Sorry about that.  When eclib programs run they leave behind a file of that name (containing large primes found during the computations, for use in later runs).  And it is left in the working directory.  This is probably leftover from a testrun I did before committing changes.

I think all will be well if you just delete that file.



---

archive/issue_comments_064499.json:
```json
{
    "body": "It reappears after `make ptestlong`, or anywhere I run a `sage -t` command that includes `ell_rational_field.py`. \u00a0Is it possible to save the file to a fixed location?\n\nWe could \n\n* Add a line to `.hgignore`.\n* Not add a line to `MANIFEST.in`.\n\nThis should ensure the file is not included in a new `sage-*.spkg`.  But users might complain about the new file appearing elsewhere.",
    "created_at": "2010-02-11T10:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64499",
    "user": "mpatel"
}
```

It reappears after `make ptestlong`, or anywhere I run a `sage -t` command that includes `ell_rational_field.py`.  Is it possible to save the file to a fixed location?

We could 

* Add a line to `.hgignore`.
* Not add a line to `MANIFEST.in`.

This should ensure the file is not included in a new `sage-*.spkg`.  But users might complain about the new file appearing elsewhere.



---

archive/issue_comments_064500.json:
```json
{
    "body": "Add `PRIMES` to `.hgignore`.  Apply in addition to other patches.",
    "created_at": "2010-02-11T10:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64500",
    "user": "mpatel"
}
```

Add `PRIMES` to `.hgignore`.  Apply in addition to other patches.



---

archive/issue_comments_064501.json:
```json
{
    "body": "Attachment\n\nI've attached an \"hgignore\" patch we can use for 4.3.3.alpha0, if it's OK.",
    "created_at": "2010-02-11T10:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64501",
    "user": "mpatel"
}
```

Attachment

I've attached an "hgignore" patch we can use for 4.3.3.alpha0, if it's OK.



---

archive/issue_comments_064502.json:
```json
{
    "body": "I'm not quite sure why this has arisen as an issue now, since mwrank/eclib have always used this file.  Was it just that I forgot to delete it when preparing the spkg?  In which case I could just make a small change to the new eclib spkg at #8184?",
    "created_at": "2010-02-11T11:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64502",
    "user": "cremona"
}
```

I'm not quite sure why this has arisen as an issue now, since mwrank/eclib have always used this file.  Was it just that I forgot to delete it when preparing the spkg?  In which case I could just make a small change to the new eclib spkg at #8184?



---

archive/issue_comments_064503.json:
```json
{
    "body": "Is it a consequence of\n\n```diff\n-             algorithm='mwrank_shell',\n+             algorithm='mwrank_lib',\n```\n\nin `EllipticCurve_rational_field.gens` and/or `EllipticCurve_rational_field.rank`?",
    "created_at": "2010-02-11T11:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64503",
    "user": "mpatel"
}
```

Is it a consequence of

```diff
-             algorithm='mwrank_shell',
+             algorithm='mwrank_lib',
```

in `EllipticCurve_rational_field.gens` and/or `EllipticCurve_rational_field.rank`?



---

archive/issue_comments_064504.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n> Is it a consequence of\n> {{{\n> #!diff\n> -             algorithm='mwrank_shell',\n> +             algorithm='mwrank_lib',\n> }}}\n> in `EllipticCurve_rational_field.gens` and/or `EllipticCurve_rational_field.rank`?\n\nNo, that should not make any difference.",
    "created_at": "2010-02-11T11:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64504",
    "user": "cremona"
}
```

Replying to [comment:20 mpatel]:
> Is it a consequence of
> {{{
> #!diff
> -             algorithm='mwrank_shell',
> +             algorithm='mwrank_lib',
> }}}
> in `EllipticCurve_rational_field.gens` and/or `EllipticCurve_rational_field.rank`?

No, that should not make any difference.



---

archive/issue_comments_064505.json:
```json
{
    "body": "If I replace `algorithm='mwrank_lib'` with `algorithm='mwrank_shell'` in both argspecs and run `sage -b; sage -t ell_rational_field.py`, the `PRIMES` file does not appear. \u00a0Am I missing something?",
    "created_at": "2010-02-11T13:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64505",
    "user": "mpatel"
}
```

If I replace `algorithm='mwrank_lib'` with `algorithm='mwrank_shell'` in both argspecs and run `sage -b; sage -t ell_rational_field.py`, the `PRIMES` file does not appear.  Am I missing something?



---

archive/issue_comments_064506.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64506",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_064507.json:
```json
{
    "body": "For the record: The \"hgignore\" patch is *not* in 4.3.3.alpha0.",
    "created_at": "2010-02-11T14:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64507",
    "user": "mpatel"
}
```

For the record: The "hgignore" patch is *not* in 4.3.3.alpha0.



---

archive/issue_comments_064508.json:
```json
{
    "body": "I have made some progress in tracking this down.   \n1. When the mwrank shell starts up, it looks to see if there is a file in the local directory called PRIMES.  If so, it reads in the contents and uses them (without checking their primality) in a trial division stage of integer factorization.\n2. The function that does that is called initprimes().  This function is wrapped in Sage but as far as I can see is not called when the library is used.  This should possibly be changed.\n3. When integers are factored there is an initial trial division stage.  Primes which are detected this way (e.g. if trial division goes up to their square root) are added to a list which is maintained for the session to help in future trial divisions.\n4. On exit, if there are any primes in the maintained list (which might be there either because they are read at the start or added when found) then that list is output to a file called PRIMES.  In the working directory, and created if it does not already exist, or overwritten if it does.\n\nNow, two of the curves in the doctests for ell_rational_field.rank, namely [1,0,0,0,37455] and [0,0,1,-79,342], have large primes in their discriminants, namely 16180561 and 19047851.  These are added to the maintained list of primes when found, and therefore on exit should be output to the file PRIMES.\n\nI do not know why the output file is only being produced when mwrank_lib is used.  I would expect it to be the other way round!  The writing to file is done by a function called when a global instance of a C++ class has its destructor called.  I know that that happens when a normal binary finishes executing (since the compiler puts in calls to relevant destructors).  But I don't see why those destructors would be called when the library is used.  (Until Sage, I had never used my own C++ code as a library in this way, so my knowledge of C++ runs out here.)\n\nOne solution would be to *only* output to the file PRIMES if it already exists.  That way, users of mwrank can still use the functionality it provides (by creating an empty file at the start) but Sage can ignore it.  This would require a new patch to the eclib code, to be applied after the one recently applied (p9).",
    "created_at": "2010-02-11T17:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64508",
    "user": "cremona"
}
```

I have made some progress in tracking this down.   
1. When the mwrank shell starts up, it looks to see if there is a file in the local directory called PRIMES.  If so, it reads in the contents and uses them (without checking their primality) in a trial division stage of integer factorization.
2. The function that does that is called initprimes().  This function is wrapped in Sage but as far as I can see is not called when the library is used.  This should possibly be changed.
3. When integers are factored there is an initial trial division stage.  Primes which are detected this way (e.g. if trial division goes up to their square root) are added to a list which is maintained for the session to help in future trial divisions.
4. On exit, if there are any primes in the maintained list (which might be there either because they are read at the start or added when found) then that list is output to a file called PRIMES.  In the working directory, and created if it does not already exist, or overwritten if it does.

Now, two of the curves in the doctests for ell_rational_field.rank, namely [1,0,0,0,37455] and [0,0,1,-79,342], have large primes in their discriminants, namely 16180561 and 19047851.  These are added to the maintained list of primes when found, and therefore on exit should be output to the file PRIMES.

I do not know why the output file is only being produced when mwrank_lib is used.  I would expect it to be the other way round!  The writing to file is done by a function called when a global instance of a C++ class has its destructor called.  I know that that happens when a normal binary finishes executing (since the compiler puts in calls to relevant destructors).  But I don't see why those destructors would be called when the library is used.  (Until Sage, I had never used my own C++ code as a library in this way, so my knowledge of C++ runs out here.)

One solution would be to *only* output to the file PRIMES if it already exists.  That way, users of mwrank can still use the functionality it provides (by creating an empty file at the start) but Sage can ignore it.  This would require a new patch to the eclib code, to be applied after the one recently applied (p9).



---

archive/issue_comments_064509.json:
```json
{
    "body": "Replying to [comment:24 cremona]:\n> One solution would be to *only* output to the file PRIMES if it already exists.\n\nWouldn't it be better to simply set the location to something in `DOT_SAGE`, instead of the current directory?",
    "created_at": "2010-02-11T17:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64509",
    "user": "rlm"
}
```

Replying to [comment:24 cremona]:
> One solution would be to *only* output to the file PRIMES if it already exists.

Wouldn't it be better to simply set the location to something in `DOT_SAGE`, instead of the current directory?



---

archive/issue_comments_064510.json:
```json
{
    "body": "Trouble is, eclib currently does not allow this to be changed, it always uses the current dir.  I can change that (as I have changed many other similar hard-wired things specifically for Sage!).  But it also would require another patch to eclib.",
    "created_at": "2010-02-11T19:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64510",
    "user": "cremona"
}
```

Trouble is, eclib currently does not allow this to be changed, it always uses the current dir.  I can change that (as I have changed many other similar hard-wired things specifically for Sage!).  But it also would require another patch to eclib.



---

archive/issue_comments_064511.json:
```json
{
    "body": "I inserted diagnostic \"cout\" statements in `extra_prime_class::~extra_prime_class` and ran a few tests.  It seems the destructor always gets called, but the timing --- and whether `PRIMES` is actually written to the file system, it seems --- depends on whether I use the library or pexpect interface.\n\nThe pexpect interface reads `SAGE_ROOT/data/extcode/mwrank/PRIMES`.  But it doesn't update this file when I quit the Sage command line.  However, if I run\n\n```\nsage -c \"EllipticCurve([1,0,0,0,37455]).rank(proof=False)\"\n```\n\nthen \"hg stat\", for example, confirms the file has changed.\n\nWould it help to call a `exitprimes` method explicitly, near the end of `main`?  This *might* avoid problems related to when the runtime calls the destructor.\n\nDisclaimer:  I'm not at all familiar with eclib.",
    "created_at": "2010-02-15T13:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64511",
    "user": "mpatel"
}
```

I inserted diagnostic "cout" statements in `extra_prime_class::~extra_prime_class` and ran a few tests.  It seems the destructor always gets called, but the timing --- and whether `PRIMES` is actually written to the file system, it seems --- depends on whether I use the library or pexpect interface.

The pexpect interface reads `SAGE_ROOT/data/extcode/mwrank/PRIMES`.  But it doesn't update this file when I quit the Sage command line.  However, if I run

```
sage -c "EllipticCurve([1,0,0,0,37455]).rank(proof=False)"
```

then "hg stat", for example, confirms the file has changed.

Would it help to call a `exitprimes` method explicitly, near the end of `main`?  This *might* avoid problems related to when the runtime calls the destructor.

Disclaimer:  I'm not at all familiar with eclib.



---

archive/issue_comments_064512.json:
```json
{
    "body": "The quickest quick fix would be just to comment out line 372 in src/procs/marith.cc (in eclib).",
    "created_at": "2010-02-25T09:21:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7575#issuecomment-64512",
    "user": "cremona"
}
```

The quickest quick fix would be just to comment out line 372 in src/procs/marith.cc (in eclib).
