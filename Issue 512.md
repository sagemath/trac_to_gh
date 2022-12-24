# Issue 512: update gap package

archive/issues_000512.json:
```json
{
    "body": "Assignee: wdj\n\nThe package \nhttp://sage.math.washington.edu/home/wdj/patches/gap-4.4.9.p1.spkg\nhas the latest version of guava (guava 3.0, incorporating work\nof Robert Miller and Tom Boothby). \n\nIssue created by migration from https://trac.sagemath.org/ticket/512\n\n",
    "created_at": "2007-08-29T14:43:30Z",
    "labels": [
        "coding theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "update gap package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/512",
    "user": "wdj"
}
```
Assignee: wdj

The package 
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.9.p1.spkg
has the latest version of guava (guava 3.0, incorporating work
of Robert Miller and Tom Boothby). 

Issue created by migration from https://trac.sagemath.org/ticket/512





---

archive/issue_comments_002588.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T22:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2588",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002589.json:
```json
{
    "body": "done for sage-2.8.3.",
    "created_at": "2007-08-29T22:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2589",
    "user": "was"
}
```

done for sage-2.8.3.



---

archive/issue_comments_002590.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-30T06:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2590",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002591.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-08-30T06:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2591",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002592.json:
```json
{
    "body": "\n```\n\nDavid,\n\nI made some fixes to gap-4.4.9.p1.spkg  to make it suitable for inclusion in SAGE.\nUnfortunately when I did a clean build of SAGE with this gap package there were\nnumerous doctest failures in all the following packages;\n\n        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py\n        sage -t  devel/sage-main/sage/coding/guava.py\n        sage -t  devel/sage-main/sage/coding/linear_code.py\n        sage -t  devel/sage-main/sage/coding/code_constructions.py\n        sage -t  devel/sage-main/sage/coding/code_bounds.py\n\nI'm reverting to the previous gap package until I figure how to get these resolved.\n\nI've put my version of gap-4.4.9.p1.spkg here:\n   http://sage.math.washington.edu/tmp\n\n -- William\n```\n",
    "created_at": "2007-08-30T06:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2592",
    "user": "was"
}
```


```

David,

I made some fixes to gap-4.4.9.p1.spkg  to make it suitable for inclusion in SAGE.
Unfortunately when I did a clean build of SAGE with this gap package there were
numerous doctest failures in all the following packages;

        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t  devel/sage-main/sage/coding/guava.py
        sage -t  devel/sage-main/sage/coding/linear_code.py
        sage -t  devel/sage-main/sage/coding/code_constructions.py
        sage -t  devel/sage-main/sage/coding/code_bounds.py

I'm reverting to the previous gap package until I figure how to get these resolved.

I've put my version of gap-4.4.9.p1.spkg here:
   http://sage.math.washington.edu/tmp

 -- William
```




---

archive/issue_comments_002593.json:
```json
{
    "body": "Changing component from coding theory to packages.",
    "created_at": "2007-10-05T03:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2593",
    "user": "was"
}
```

Changing component from coding theory to packages.



---

archive/issue_comments_002594.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2007-10-05T03:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2594",
    "user": "was"
}
```

Changing priority from minor to major.



---

archive/issue_comments_002595.json:
```json
{
    "body": "From David Joyner\n\n```\n(1) The package\n\nhttp://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.spkg\n\ninstalls okay passes these tests. However, I added a build for Leon's code,\nwhich\n(a) was only tested on one machine,\n(b) is based on my negligable knowledge of how Makefiles/spkg install\nfiles work (so I got lucky that it seemss to have worked even on one\nmachine!).\n\nI think GAP version 4.4.10 will be officially released tomorrow.\n\n(2) This might be way too old, but I wonder if you could at least try\nto apply the patch\n\nhttp://sage.math.washington.edu/home/wdj/patches/maxima-patch-latest-really.hg\n\nwhich I think fixes some old minor bugs in the interface to special\nfunctions. (The file dates from November of last year!) I created a\nclone, viewed it using hg_sage.inspect and noticed it\nseems to only affect special functions. Then I applied the patch and ran\n\n./sage -t \"/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage-maxima/sage/functions/special.py\"\n\n(All tests passed.) I tried to view it again (to see what else it\nmight change, in case I misssed something) but couldn't.\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++\n\n```\n",
    "created_at": "2007-10-05T03:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2595",
    "user": "was"
}
```

From David Joyner

```
(1) The package

http://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.spkg

installs okay passes these tests. However, I added a build for Leon's code,
which
(a) was only tested on one machine,
(b) is based on my negligable knowledge of how Makefiles/spkg install
files work (so I got lucky that it seemss to have worked even on one
machine!).

I think GAP version 4.4.10 will be officially released tomorrow.

(2) This might be way too old, but I wonder if you could at least try
to apply the patch

http://sage.math.washington.edu/home/wdj/patches/maxima-patch-latest-really.hg

which I think fixes some old minor bugs in the interface to special
functions. (The file dates from November of last year!) I created a
clone, viewed it using hg_sage.inspect and noticed it
seems to only affect special functions. Then I applied the patch and ran

./sage -t "/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage-maxima/sage/functions/special.py"

(All tests passed.) I tried to view it again (to see what else it
might change, in case I misssed something) but couldn't.


+++++++++++++++++++++++++++++++++++++++++++++++++++

```




---

archive/issue_comments_002596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T20:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2596",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002597.json:
```json
{
    "body": "I've upgraded everything to gap-4.4.10, and fixed the insanely bloated 4.4.10 spkg that was on David's web page.",
    "created_at": "2007-10-20T20:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/512#issuecomment-2597",
    "user": "was"
}
```

I've upgraded everything to gap-4.4.10, and fixed the insanely bloated 4.4.10 spkg that was on David's web page.
