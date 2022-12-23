# Issue 2054: prun is not preparsed -- potentially very confusing

archive/issues_002054.json:
```json
{
    "body": "Assignee: was\n\nIf one uses the Python profiler through Sage's Ipython command line, the input line is not preparsed, which is potentially very confusing.  E.g., this should print 256:\n\n\n```\nsage: %prun print 2^8\n10\n         2 function calls in 0.000 CPU seconds\n\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.000    0.000 <string>:1(<module>)\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n\nsage: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2054\n\n",
    "created_at": "2008-02-05T14:31:08Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "prun is not preparsed -- potentially very confusing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2054",
    "user": "was"
}
```
Assignee: was

If one uses the Python profiler through Sage's Ipython command line, the input line is not preparsed, which is potentially very confusing.  E.g., this should print 256:


```
sage: %prun print 2^8
10
         2 function calls in 0.000 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

sage: 
```


Issue created by migration from https://trac.sagemath.org/ticket/2054





---

archive/issue_comments_013296.json:
```json
{
    "body": "\n```\nFernando Perez to me\n\t\nshow details 9:15 PM (18 minutes ago)\n\t\n\t\n\t\nReply\n\t\n\t\nHi William,\n\nOn Feb 5, 2008 7:46 AM, William Stein <wstein@gmail.com> wrote:\n> Fernando,\n>\n> Any hints about how I could make the argument to %prun get preparsed?\n\nsorry for the delay, I just wanted to let you know that I don't have a\nquick solution to this right now, and I'm swamped with moving/home\nsale issues, so for a couple of weeks my coding time is reduced to\nexactly zero.\n\nI'll keep this in my inbox, starred, so once I get to Berkeley I can\nfix it.  It's not difficult, I just don't have a spare hour right now\nto code it and test it, sorry.\n\nCheers,\n\nf\n```\n",
    "created_at": "2008-02-08T05:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13296",
    "user": "was"
}
```


```
Fernando Perez to me
	
show details 9:15 PM (18 minutes ago)
	
	
	
Reply
	
	
Hi William,

On Feb 5, 2008 7:46 AM, William Stein <wstein@gmail.com> wrote:
> Fernando,
>
> Any hints about how I could make the argument to %prun get preparsed?

sorry for the delay, I just wanted to let you know that I don't have a
quick solution to this right now, and I'm swamped with moving/home
sale issues, so for a couple of weeks my coding time is reduced to
exactly zero.

I'll keep this in my inbox, starred, so once I get to Berkeley I can
fix it.  It's not difficult, I just don't have a spare hour right now
to code it and test it, sorry.

Cheers,

f
```




---

archive/issue_comments_013297.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-02T19:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13297",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_013298.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-02T19:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13298",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013299.json:
```json
{
    "body": "Is this an error on my part?\n\n\n```\n/scratch/rossk/sage-4.3.2/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/2054/scripts_2054.patch\nadding scripts_2054.patch to series file\n\n/scratch/rossk/sage-4.3.2/devel/sage$ hg qpush\napplying scripts_2054.patch\nunable to find 'ipy_profile_sage.py' for patching\n1 out of 1 hunks FAILED -- saving rejects to file ipy_profile_sage.py.rej\npatch failed, unable to continue (try -v)\nipy_profile_sage.py: No such file or directory\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh scripts_2054.patch\n```\n",
    "created_at": "2010-02-09T10:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13299",
    "user": "rossk"
}
```

Is this an error on my part?


```
/scratch/rossk/sage-4.3.2/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/2054/scripts_2054.patch
adding scripts_2054.patch to series file

/scratch/rossk/sage-4.3.2/devel/sage$ hg qpush
applying scripts_2054.patch
unable to find 'ipy_profile_sage.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file ipy_profile_sage.py.rej
patch failed, unable to continue (try -v)
ipy_profile_sage.py: No such file or directory
patch failed, rejects left in working dir
errors during apply, please fix and refresh scripts_2054.patch
```




---

archive/issue_comments_013300.json:
```json
{
    "body": "Hello,\n\nYou need to be in /scratch/rossk/sage-4.3.2/local/bin in order to be in the repository which the patch applies to.",
    "created_at": "2010-02-09T10:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13300",
    "user": "mhansen"
}
```

Hello,

You need to be in /scratch/rossk/sage-4.3.2/local/bin in order to be in the repository which the patch applies to.



---

archive/issue_comments_013301.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> Hello,\n> \n> You need to be in /scratch/rossk/sage-4.3.2/local/bin in order to be in the repository which the patch applies to.\n\nThanks - it installed and built ok :-) \n\n(I suppose look in the patch next time to know which folder I should be in?) \n\nWill run a few tests, do the doctests and hopefully we'll knock this one over soon.",
    "created_at": "2010-02-09T10:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13301",
    "user": "rossk"
}
```

Replying to [comment:4 mhansen]:
> Hello,
> 
> You need to be in /scratch/rossk/sage-4.3.2/local/bin in order to be in the repository which the patch applies to.

Thanks - it installed and built ok :-) 

(I suppose look in the patch next time to know which folder I should be in?) 

Will run a few tests, do the doctests and hopefully we'll knock this one over soon.



---

archive/issue_comments_013302.json:
```json
{
    "body": "Tested the patch with a few statements that exercised the preparser. e.g.\n\n```\nsage: %prun 123456789123456789123456789123456789123456789123456789.factor()\n\nsage: %prun print integrate(log(x)^(2^3),x)\n```\n\nPre-patch statements like these crashed or gave incorrect answers if prefixed with \"%prun \". \nPost-patch the statements give the same answers with or without \"%prun\" (and all doctests passed).\nPositive review",
    "created_at": "2010-02-09T11:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13302",
    "user": "rossk"
}
```

Tested the patch with a few statements that exercised the preparser. e.g.

```
sage: %prun 123456789123456789123456789123456789123456789123456789.factor()

sage: %prun print integrate(log(x)^(2^3),x)
```

Pre-patch statements like these crashed or gave incorrect answers if prefixed with "%prun ". 
Post-patch the statements give the same answers with or without "%prun" (and all doctests passed).
Positive review



---

archive/issue_comments_013303.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-09T11:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13303",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013304.json:
```json
{
    "body": "For the record: Applying the patch to Sage 4.3.2's scripts repository, I get\n\n```\npatching file ipy_profile_sage.py\nHunk #1 succeeded at 29 with fuzz 2 (offset 0 lines).\nnow at: scripts_2054.patch\n```\n",
    "created_at": "2010-02-10T10:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13304",
    "user": "mpatel"
}
```

For the record: Applying the patch to Sage 4.3.2's scripts repository, I get

```
patching file ipy_profile_sage.py
Hunk #1 succeeded at 29 with fuzz 2 (offset 0 lines).
now at: scripts_2054.patch
```




---

archive/issue_comments_013305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2054#issuecomment-13305",
    "user": "mpatel"
}
```

Resolution: fixed
