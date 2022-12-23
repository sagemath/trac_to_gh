# Issue 3750: Request for a "log" function for Sage integers

archive/issues_003750.json:
```json
{
    "body": "Assignee: somebody\n\nThe following command\n\n\n```\nsage: N=8\nsage: N.log(2)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/ljpk/<ipython console> in <module>()\n\nAttributeError: 'sage.rings.integer.Integer' object has no attribute 'log'\n```\n\n\nreturns an error (as does N.exp()). Would it be possible to add a function to the Sage integers class which worked like the ones for the real numbers?\n\n\n```\nsage: N=8.0\nsage: N.log(2)\n3.00000000000000\nsage: N.exp()\n2980.95798704173\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3750\n\n",
    "created_at": "2008-07-31T17:49:30Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "Request for a \"log\" function for Sage integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3750",
    "user": "ljpk"
}
```
Assignee: somebody

The following command


```
sage: N=8
sage: N.log(2)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/ljpk/<ipython console> in <module>()

AttributeError: 'sage.rings.integer.Integer' object has no attribute 'log'
```


returns an error (as does N.exp()). Would it be possible to add a function to the Sage integers class which worked like the ones for the real numbers?


```
sage: N=8.0
sage: N.log(2)
3.00000000000000
sage: N.exp()
2980.95798704173
```



Issue created by migration from https://trac.sagemath.org/ticket/3750





---

archive/issue_comments_026639.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-23T13:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26639",
    "user": "kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026640.json:
```json
{
    "body": "Changing assignee from somebody to kcrisman.",
    "created_at": "2008-10-23T13:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26640",
    "user": "kcrisman"
}
```

Changing assignee from somebody to kcrisman.



---

archive/issue_comments_026641.json:
```json
{
    "body": "I think that log should default to base 'e' as it does with all the other types.  Also both of them should probably take an optional number of bits of precision to use with the default being 53.",
    "created_at": "2008-10-24T03:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26641",
    "user": "mhansen"
}
```

I think that log should default to base 'e' as it does with all the other types.  Also both of them should probably take an optional number of bits of precision to use with the default being 53.



---

archive/issue_comments_026642.json:
```json
{
    "body": "Somebody should point out the exact_log function in this discussion since it is relevant to the original poster and is superfast:\n\n```\nsage: N = 8\nsage: N.exact_log(2)\n3\n```\n",
    "created_at": "2008-10-24T04:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26642",
    "user": "was"
}
```

Somebody should point out the exact_log function in this discussion since it is relevant to the original poster and is superfast:

```
sage: N = 8
sage: N.exact_log(2)
3
```




---

archive/issue_comments_026643.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> I think that log should default to base 'e' as it does with all the other types.  Also both of them should probably take an optional number of bits of precision to use with the default being 53.\n\nKnow what, I don't think I even realized that m was mandatory the way I wrote it - yes, obviously it should default to natural log.  I like the idea of specifying precision in the function itself as well - good comments.",
    "created_at": "2008-10-25T00:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26643",
    "user": "kcrisman"
}
```

Replying to [comment:2 mhansen]:
> I think that log should default to base 'e' as it does with all the other types.  Also both of them should probably take an optional number of bits of precision to use with the default being 53.

Know what, I don't think I even realized that m was mandatory the way I wrote it - yes, obviously it should default to natural log.  I like the idea of specifying precision in the function itself as well - good comments.



---

archive/issue_comments_026644.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-26T00:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26644",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_026645.json:
```json
{
    "body": "The patch now should deal with both of the reviewer's comments.",
    "created_at": "2008-10-26T00:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26645",
    "user": "kcrisman"
}
```

The patch now should deal with both of the reviewer's comments.



---

archive/issue_comments_026646.json:
```json
{
    "body": "Hmm... there's an issue that before log(3) would just give log(3) since 3 is exact.  After the patch, log(3) will automatically give an approximation which probably isn't desired.",
    "created_at": "2008-10-26T00:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26646",
    "user": "mhansen"
}
```

Hmm... there's an issue that before log(3) would just give log(3) since 3 is exact.  After the patch, log(3) will automatically give an approximation which probably isn't desired.



---

archive/issue_comments_026647.json:
```json
{
    "body": "Mike, Good point about log(3).  This should be dealt with the same way as with sqrt:\n\n```\nsage: 3.sqrt()\nsqrt(3)\nsage: 3.sqrt(prec=53)\n1.73205080756888\n```\n",
    "created_at": "2008-10-26T22:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26647",
    "user": "was"
}
```

Mike, Good point about log(3).  This should be dealt with the same way as with sqrt:

```
sage: 3.sqrt()
sqrt(3)
sage: 3.sqrt(prec=53)
1.73205080756888
```




---

archive/issue_comments_026648.json:
```json
{
    "body": "As long as everyone is okay with \n\n```\nsage: log(1024, 2)\n10\n```\n\ninstead of the previous behavior of \n\n```\nsage: log(1024, 2)\nlog(1024)/log(2)\n```\n\nthen the last version of the patch should address all concerns raised above.  Thanks to mhampton for sleuthing down that one must use ** for exponentiation outside the interpreter when I got confused.",
    "created_at": "2008-10-30T18:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26648",
    "user": "kcrisman"
}
```

As long as everyone is okay with 

```
sage: log(1024, 2)
10
```

instead of the previous behavior of 

```
sage: log(1024, 2)
log(1024)/log(2)
```

then the last version of the patch should address all concerns raised above.  Thanks to mhampton for sleuthing down that one must use ** for exponentiation outside the interpreter when I got confused.



---

archive/issue_comments_026649.json:
```json
{
    "body": "Attachment\n\nBased on 3.2.alpha0",
    "created_at": "2008-10-30T18:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26649",
    "user": "kcrisman"
}
```

Attachment

Based on 3.2.alpha0



---

archive/issue_comments_026650.json:
```json
{
    "body": "Nice work!  I'm pretty happy with how this turned out.",
    "created_at": "2008-11-04T21:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26650",
    "user": "mhansen"
}
```

Nice work!  I'm pretty happy with how this turned out.



---

archive/issue_comments_026651.json:
```json
{
    "body": "When I merge integer-log-exp-final.patch I get one doctest failure:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3$  ./sage -t -long devel/sage/sage/coding/linear_code.py\nsage -t -long devel/sage/sage/coding/linear_code.py         \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py\", line 1123:\n    sage: Cc = C.galois_closure(GF(2))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[3]>\", line 1, in <module>\n        Cc = C.galois_closure(GF(Integer(2)))###line 1123:\n    sage: Cc = C.galois_closure(GF(2))\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 1141, in galois_closure\n        if not(a.integer_part() == a):\n    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'integer_part'\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py\", line 1124:\n    sage: C; Cc\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[4]>\", line 1, in <module>\n        C; Cc###line 1124:\n    sage: C; Cc\n    NameError: name 'Cc' is not defined\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py\", line 1132:\n    sage: c2 in Cc\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_21[9]>\", line 1, in <module>\n        c2 in Cc###line 1132:\n    sage: c2 in Cc\n    NameError: name 'Cc' is not defined\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py\", line 1541:\n    sage: Cc = C.galois_closure(GF(2))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_35[3]>\", line 1, in <module>\n        Cc = C.galois_closure(GF(Integer(2)))###line 1541:\n    sage: Cc = C.galois_closure(GF(2))\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 1141, in galois_closure\n        if not(a.integer_part() == a):\n    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'integer_part'\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py\", line 1547:\n    sage: c2 in Cc\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_35[8]>\", line 1, in <module>\n        c2 in Cc###line 1547:\n    sage: c2 in Cc\n    NameError: name 'Cc' is not defined\n**********************************************************************\n2 items had failures:\n   3 of  10 in __main__.example_21\n   2 of   9 in __main__.example_35\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/.doctest_linear_code.py\n\t [30.6 s]\nexit code: 1024\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T18:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26651",
    "user": "mabshoff"
}
```

When I merge integer-log-exp-final.patch I get one doctest failure:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3$  ./sage -t -long devel/sage/sage/coding/linear_code.py
sage -t -long devel/sage/sage/coding/linear_code.py         
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1123:
    sage: Cc = C.galois_closure(GF(2))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[3]>", line 1, in <module>
        Cc = C.galois_closure(GF(Integer(2)))###line 1123:
    sage: Cc = C.galois_closure(GF(2))
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 1141, in galois_closure
        if not(a.integer_part() == a):
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'integer_part'
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1124:
    sage: C; Cc
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[4]>", line 1, in <module>
        C; Cc###line 1124:
    sage: C; Cc
    NameError: name 'Cc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1132:
    sage: c2 in Cc
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[9]>", line 1, in <module>
        c2 in Cc###line 1132:
    sage: c2 in Cc
    NameError: name 'Cc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1541:
    sage: Cc = C.galois_closure(GF(2))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_35[3]>", line 1, in <module>
        Cc = C.galois_closure(GF(Integer(2)))###line 1541:
    sage: Cc = C.galois_closure(GF(2))
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 1141, in galois_closure
        if not(a.integer_part() == a):
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'integer_part'
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/linear_code.py", line 1547:
    sage: c2 in Cc
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_35[8]>", line 1, in <module>
        c2 in Cc###line 1547:
    sage: c2 in Cc
    NameError: name 'Cc' is not defined
**********************************************************************
2 items had failures:
   3 of  10 in __main__.example_21
   2 of   9 in __main__.example_35
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.alpha3/tmp/.doctest_linear_code.py
	 [30.6 s]
exit code: 1024
```


Cheers,

Michael



---

archive/issue_comments_026652.json:
```json
{
    "body": "Attachment\n\nI've attached a patch which fixes the issue.",
    "created_at": "2008-11-06T12:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26652",
    "user": "mhansen"
}
```

Attachment

I've attached a patch which fixes the issue.



---

archive/issue_comments_026653.json:
```json
{
    "body": "This works!  I was going to use q.is_power_of(q0), but as far as I can tell there isn't any meaningful difference between these solutions.  Use integer-log-exp-final.patch and trac_3750-fix.patch.  I assume I can review mhansen's fix; if not, my apologies.\n\nTo be honest, how was this working before, when the symbolic logs didn't have an integer_part() method to begin with?",
    "created_at": "2008-11-06T14:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26653",
    "user": "kcrisman"
}
```

This works!  I was going to use q.is_power_of(q0), but as far as I can tell there isn't any meaningful difference between these solutions.  Use integer-log-exp-final.patch and trac_3750-fix.patch.  I assume I can review mhansen's fix; if not, my apologies.

To be honest, how was this working before, when the symbolic logs didn't have an integer_part() method to begin with?



---

archive/issue_comments_026654.json:
```json
{
    "body": "Merged integer-log-exp-final.patch and trac_3750-fix.patch in Sage 3.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T18:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26654",
    "user": "mabshoff"
}
```

Merged integer-log-exp-final.patch and trac_3750-fix.patch in Sage 3.2.rc0.

Cheers,

Michael



---

archive/issue_comments_026655.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-09T18:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3750#issuecomment-26655",
    "user": "mabshoff"
}
```

Resolution: fixed
