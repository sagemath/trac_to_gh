# Issue 4411: phc breaks on one-variable problems

archive/issues_004411.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: phc, phcpack, numerical, polynomial\n\nphcpack uses a different method and different output for 1-variable problems, which breaks a lot of the assumptions in the interface.  I will ask Jan Verschelde if it is possible to harmonize the output, otherwise I will add some special-casing code to the interface.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4411\n\n",
    "created_at": "2008-10-31T12:54:55Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "phc breaks on one-variable problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4411",
    "user": "mhampton"
}
```
Assignee: mhampton

Keywords: phc, phcpack, numerical, polynomial

phcpack uses a different method and different output for 1-variable problems, which breaks a lot of the assumptions in the interface.  I will ask Jan Verschelde if it is possible to harmonize the output, otherwise I will add some special-casing code to the interface.

Issue created by migration from https://trac.sagemath.org/ticket/4411





---

archive/issue_comments_032425.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-31T12:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32425",
    "user": "mhampton"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032426.json:
```json
{
    "body": "Fixes 1-variable problems with phc",
    "created_at": "2011-01-11T23:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32426",
    "user": "mhampton"
}
```

Fixes 1-variable problems with phc



---

archive/issue_comments_032427.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-11T23:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32427",
    "user": "mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032428.json:
```json
{
    "body": "Attachment [trac_4411_fix_phc_1_variable.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411_fix_phc_1_variable.patch) by mhampton created at 2011-01-11 23:09:22\n\nHere's an example for testing:\n\n```\nR1.<t> = PolynomialRing(QQ)\nstart_sys1 = [t^15-t-1]             \nsol = phc.blackbox(start_sys1, R1, verbose=False)        \nlen(sol.solutions())\n```\n\nshould give 15.",
    "created_at": "2011-01-11T23:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32428",
    "user": "mhampton"
}
```

Attachment [trac_4411_fix_phc_1_variable.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411_fix_phc_1_variable.patch) by mhampton created at 2011-01-11 23:09:22

Here's an example for testing:

```
R1.<t> = PolynomialRing(QQ)
start_sys1 = [t^15-t-1]             
sol = phc.blackbox(start_sys1, R1, verbose=False)        
len(sol.solutions())
```

should give 15.



---

archive/issue_comments_032429.json:
```json
{
    "body": "Oops, for the above snippet you need to first import phc:\n\n```\nfrom sage.interfaces.phc import phc\n```\n\n\nand have the phc optional spkg installed.",
    "created_at": "2011-01-12T00:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32429",
    "user": "mhampton"
}
```

Oops, for the above snippet you need to first import phc:

```
from sage.interfaces.phc import phc
```


and have the phc optional spkg installed.



---

archive/issue_comments_032430.json:
```json
{
    "body": "Changing component from interfaces to optional packages.",
    "created_at": "2011-01-12T00:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32430",
    "user": "mhampton"
}
```

Changing component from interfaces to optional packages.



---

archive/issue_comments_032431.json:
```json
{
    "body": "current spkg does not work on MacOSX 10.6. Will need an update...",
    "created_at": "2011-01-12T20:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32431",
    "user": "dimpase"
}
```

current spkg does not work on MacOSX 10.6. Will need an update...



---

archive/issue_comments_032432.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-13T19:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32432",
    "user": "dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_032433.json:
```json
{
    "body": "Replying to [comment:6 dimpase]:\n> current spkg does not work on MacOSX 10.6. Will need an update...\n\nThe new spkg (Marshall, could you post a link to it?) breaks parts of the current code, as some outputs(?) did change.",
    "created_at": "2011-01-13T19:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32433",
    "user": "dimpase"
}
```

Replying to [comment:6 dimpase]:
> current spkg does not work on MacOSX 10.6. Will need an update...

The new spkg (Marshall, could you post a link to it?) breaks parts of the current code, as some outputs(?) did change.



---

archive/issue_comments_032434.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-26T16:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32434",
    "user": "mhampton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032435.json:
```json
{
    "body": "For this patch, the optional spkg from ticket #10607 should be used.  \n\n[http://sage.math.washington.edu/home/mhampton/phc-2.3.60.spkg](http://sage.math.washington.edu/home/mhampton/phc-2.3.60.spkg)",
    "created_at": "2011-03-26T16:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32435",
    "user": "mhampton"
}
```

For this patch, the optional spkg from ticket #10607 should be used.  

[http://sage.math.washington.edu/home/mhampton/phc-2.3.60.spkg](http://sage.math.washington.edu/home/mhampton/phc-2.3.60.spkg)



---

archive/issue_comments_032436.json:
```json
{
    "body": "Tested so far on OS X 10.6 and linux (64-bit).",
    "created_at": "2011-03-26T16:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32436",
    "user": "mhampton"
}
```

Tested so far on OS X 10.6 and linux (64-bit).



---

archive/issue_comments_032437.json:
```json
{
    "body": "This (and 10607) also work on Solaris (tested on mark on skynet) in addition to OS X 10.6 and linux.",
    "created_at": "2011-03-27T01:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32437",
    "user": "mhampton"
}
```

This (and 10607) also work on Solaris (tested on mark on skynet) in addition to OS X 10.6 and linux.



---

archive/issue_comments_032438.json:
```json
{
    "body": "A few comments: the variable `real_tol` needs to be documented.  Also, the examples should probably be marked \"optional: phc\" instead of just \"optional\".\n\nIn the documentation it says \"A dictionary of lists if dictionaries of solutions, classified by type.\".  Should the word \"if\" be \"of\"?\n\nYou've changed the functions `get_solution_dicts` and `get_classified_solution_dicts`; can you add some doctests to illustrate and test the changes?",
    "created_at": "2011-07-15T02:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32438",
    "user": "jhpalmieri"
}
```

A few comments: the variable `real_tol` needs to be documented.  Also, the examples should probably be marked "optional: phc" instead of just "optional".

In the documentation it says "A dictionary of lists if dictionaries of solutions, classified by type.".  Should the word "if" be "of"?

You've changed the functions `get_solution_dicts` and `get_classified_solution_dicts`; can you add some doctests to illustrate and test the changes?



---

archive/issue_comments_032439.json:
```json
{
    "body": "Attachment [trac_4411_and_10607_phc_fixes.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411_and_10607_phc_fixes.patch) by mhampton created at 2011-08-05 03:02:51\n\nupdated patch for both 4411 and 10607",
    "created_at": "2011-08-05T03:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32439",
    "user": "mhampton"
}
```

Attachment [trac_4411_and_10607_phc_fixes.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411_and_10607_phc_fixes.patch) by mhampton created at 2011-08-05 03:02:51

updated patch for both 4411 and 10607



---

archive/issue_comments_032440.json:
```json
{
    "body": "I think I've addressed all of your comments.  The changes to get_solution_dicts and get_classified_solution_dicts are mostly trivial, just to handle to minor differences in output of phcpack for the 1-variable case.",
    "created_at": "2011-08-05T03:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32440",
    "user": "mhampton"
}
```

I think I've addressed all of your comments.  The changes to get_solution_dicts and get_classified_solution_dicts are mostly trivial, just to handle to minor differences in output of phcpack for the 1-variable case.



---

archive/issue_comments_032441.json:
```json
{
    "body": "patch doesn't apply to sage-5.0, I get a rejected hunk.",
    "created_at": "2012-05-17T22:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32441",
    "user": "vbraun"
}
```

patch doesn't apply to sage-5.0, I get a rejected hunk.



---

archive/issue_comments_032442.json:
```json
{
    "body": "Attachment [trac_4411_and_10607_phc_fixes_5.0.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411_and_10607_phc_fixes_5.0.patch) by mhampton created at 2012-05-28 20:19:45\n\nrebased cumulative patch for #4411 and #10607, for sage-5.0",
    "created_at": "2012-05-28T20:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32442",
    "user": "mhampton"
}
```

Attachment [trac_4411_and_10607_phc_fixes_5.0.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411_and_10607_phc_fixes_5.0.patch) by mhampton created at 2012-05-28 20:19:45

rebased cumulative patch for #4411 and #10607, for sage-5.0



---

archive/issue_comments_032443.json:
```json
{
    "body": "Replying to [comment:16 vbraun]:\n> patch doesn't apply to sage-5.0, I get a rejected hunk.\n\nOkay, I fixed that and updated the description to point to a more recent phcpack spkg.  Please try again!  It would be depressing for this to rot again.",
    "created_at": "2012-05-28T20:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32443",
    "user": "mhampton"
}
```

Replying to [comment:16 vbraun]:
> patch doesn't apply to sage-5.0, I get a rejected hunk.

Okay, I fixed that and updated the description to point to a more recent phcpack spkg.  Please try again!  It would be depressing for this to rot again.



---

archive/issue_comments_032444.json:
```json
{
    "body": "I just posted a new spkg to #10607, since the old one wasn't building on my OS X Lion machine. I don't know what this package is doing, but all optional tests pass for me with the patch here and the spkg from #10607.",
    "created_at": "2012-06-12T21:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32444",
    "user": "jhpalmieri"
}
```

I just posted a new spkg to #10607, since the old one wasn't building on my OS X Lion machine. I don't know what this package is doing, but all optional tests pass for me with the patch here and the spkg from #10607.



---

archive/issue_comments_032445.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2012-10-23T19:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32445",
    "user": "vbraun"
}
```

Looks good to me!



---

archive/issue_comments_032446.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-23T19:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32446",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032447.json:
```json
{
    "body": "I get the following doctest error on Sage-5.4.rc1, perhaps it has something to do with #13579?\n\n```\n[vbraun@volker-desktop hg]$ sage -t -only-optional=phc --verbose devel/sage-main/sage/interfaces/phc.py\nsage -t -only-optional=phc --verbose \"devel/sage-main/sage/interfaces/phc.py\"\nTrying:\n    set_random_seed(0L)\nExpecting nothing\nok\nTrying:\n    change_warning_output(sys.stdout)\nExpecting nothing\nok\nTrying:\n    from sage.interfaces.phc import *         #optional: phc###line 56:_sage_    >>> from sage.interfaces.phc import *         #optional: phc\nExpecting nothing\nok\nTrying:\n    R2 = PolynomialRing(QQ,Integer(2), names=('x1', 'x2',)); (x1, x2,) = R2._first_ngens(2)#optional: phc###line 57:_sage_    >>> R2.<x1,x2> = PolynomialRing(QQ,2)         #optional: phc\nExpecting nothing\nok\nTrying:\n    test_sys = [(x1-Integer(1))**Integer(5)-x2, (x2-Integer(1))**Integer(5)-Integer(1)] #optional: phc###line 58:_sage_    >>> test_sys = [(x1-1)^5-x2, (x2-1)^5-1] #optional: phc\nExpecting nothing\nok\nTrying:\n    sol = phc.blackbox(test_sys, R2)          #optional: phc###line 59:_sage_    >>> sol = phc.blackbox(test_sys, R2)          #optional: phc\nExpecting nothing\n\nThere exists already a file named /home/vbraun/.sage/temp/volker_desktop.stp.dias.ie/21208/tmp_filename-SmhVtI\nDo you want to destroy this file ? (y/n) y\n```\n",
    "created_at": "2012-10-23T19:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32447",
    "user": "vbraun"
}
```

I get the following doctest error on Sage-5.4.rc1, perhaps it has something to do with #13579?

```
[vbraun@volker-desktop hg]$ sage -t -only-optional=phc --verbose devel/sage-main/sage/interfaces/phc.py
sage -t -only-optional=phc --verbose "devel/sage-main/sage/interfaces/phc.py"
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    from sage.interfaces.phc import *         #optional: phc###line 56:_sage_    >>> from sage.interfaces.phc import *         #optional: phc
Expecting nothing
ok
Trying:
    R2 = PolynomialRing(QQ,Integer(2), names=('x1', 'x2',)); (x1, x2,) = R2._first_ngens(2)#optional: phc###line 57:_sage_    >>> R2.<x1,x2> = PolynomialRing(QQ,2)         #optional: phc
Expecting nothing
ok
Trying:
    test_sys = [(x1-Integer(1))**Integer(5)-x2, (x2-Integer(1))**Integer(5)-Integer(1)] #optional: phc###line 58:_sage_    >>> test_sys = [(x1-1)^5-x2, (x2-1)^5-1] #optional: phc
Expecting nothing
ok
Trying:
    sol = phc.blackbox(test_sys, R2)          #optional: phc###line 59:_sage_    >>> sol = phc.blackbox(test_sys, R2)          #optional: phc
Expecting nothing

There exists already a file named /home/vbraun/.sage/temp/volker_desktop.stp.dias.ie/21208/tmp_filename-SmhVtI
Do you want to destroy this file ? (y/n) y
```




---

archive/issue_comments_032448.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-10-23T19:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32448",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032449.json:
```json
{
    "body": "Yes, I guess that since `tmp_filename` now creates the file in addition to returning its path, it causes the problem. Here's a patch. (There are other things which could be cleaned up, for example `log_filename` is never used, but I'm not going to bother.)",
    "created_at": "2012-10-25T20:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32449",
    "user": "jhpalmieri"
}
```

Yes, I guess that since `tmp_filename` now creates the file in addition to returning its path, it causes the problem. Here's a patch. (There are other things which could be cleaned up, for example `log_filename` is never used, but I'm not going to bother.)



---

archive/issue_comments_032450.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-10-25T20:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32450",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032451.json:
```json
{
    "body": "Attachment [trac_4411-tmpfilename.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411-tmpfilename.patch) by jhpalmieri created at 2012-10-25 20:27:29",
    "created_at": "2012-10-25T20:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32451",
    "user": "jhpalmieri"
}
```

Attachment [trac_4411-tmpfilename.patch](tarball://root/attachments/some-uuid/ticket4411/trac_4411-tmpfilename.patch) by jhpalmieri created at 2012-10-25 20:27:29



---

archive/issue_comments_032452.json:
```json
{
    "body": "That does solve this new filename problem. This ticket should have been closed with 10607, but wasn't, so now I guess it can serve this new purpose of fixing the tmp file problem.",
    "created_at": "2012-12-21T14:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32452",
    "user": "mhampton"
}
```

That does solve this new filename problem. This ticket should have been closed with 10607, but wasn't, so now I guess it can serve this new purpose of fixing the tmp file problem.



---

archive/issue_comments_032453.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-12-21T14:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32453",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032454.json:
```json
{
    "body": "Changing component from optional packages to interfaces.",
    "created_at": "2012-12-26T16:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32454",
    "user": "jdemeyer"
}
```

Changing component from optional packages to interfaces.



---

archive/issue_comments_032455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-12-27T10:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4411#issuecomment-32455",
    "user": "jdemeyer"
}
```

Resolution: fixed
