# Issue 6323: optional doctest failure -- problem in species code (easy to fix)

archive/issues_006323.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/combinat/species/library.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py\", line 55:\n    sage: number, name, sseq = sloane_find(seq)[0]                    #optional\nExpected nothing\nGot:\n    Searching Sloane's online database...\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py\", line 62:\n    sage: number, name, sseq = sloane_find(seq)[0]    #optional\nExpected nothing\nGot:\n    Searching Sloane's online database...\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py\", line 101:\n    sage: number, name, sseq = sloane_find(seq)[0]                    #optional\nExpected nothing\nGot:\n    Searching Sloane's online database...\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py\", line 135:\n    sage: number, name, sseq = sloane_find(seq)[0]                    #optional\nExpected nothing\nGot:\n    Searching Sloane's online database...\n**********************************************************************\n3 items had failures:\n   2 of  12 in __main__.example_1\n   1 of  12 in __main__.example_2\n   1 of   9 in __main__.example_3\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_library.py\n\t [6.9 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6323\n\n",
    "created_at": "2009-06-16T14:53:29Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- problem in species code (easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6323",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/combinat/species/library.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 55:
    sage: number, name, sseq = sloane_find(seq)[0]                    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 62:
    sage: number, name, sseq = sloane_find(seq)[0]    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 101:
    sage: number, name, sseq = sloane_find(seq)[0]                    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 135:
    sage: number, name, sseq = sloane_find(seq)[0]                    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
3 items had failures:
   2 of  12 in __main__.example_1
   1 of  12 in __main__.example_2
   1 of   9 in __main__.example_3
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_library.py
	 [6.9 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6323





---

archive/issue_comments_050370.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-21T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50370",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050371.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2013-06-21T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50371",
    "user": "https://github.com/mwhansen"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_050372.json:
```json
{
    "body": "Changing component from packages: optional to combinatorics.",
    "created_at": "2013-06-21T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50372",
    "user": "https://github.com/mwhansen"
}
```

Changing component from packages: optional to combinatorics.



---

archive/issue_comments_050373.json:
```json
{
    "body": "Attachment [trac_6323.patch](tarball://root/attachments/some-uuid/ticket6323/trac_6323.patch) by @mwhansen created at 2013-06-21 15:29:41",
    "created_at": "2013-06-21T15:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50373",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6323.patch](tarball://root/attachments/some-uuid/ticket6323/trac_6323.patch) by @mwhansen created at 2013-06-21 15:29:41



---

archive/issue_comments_050374.json:
```json
{
    "body": "Helloooooooooo !!!\n\nCould you please change the \"#optional\" tag to \"# optional - internet\" ? It will never be run otherwise `:-)`\n\nNathann",
    "created_at": "2013-06-25T12:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50374",
    "user": "https://github.com/nathanncohen"
}
```

Helloooooooooo !!!

Could you please change the "#optional" tag to "# optional - internet" ? It will never be run otherwise `:-)`

Nathann



---

archive/issue_comments_050375.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-27T17:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50375",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050376.json:
```json
{
    "body": "Attachment [trac_6323-rev.patch](tarball://root/attachments/some-uuid/ticket6323/trac_6323-rev.patch) by @nathanncohen created at 2013-06-27 17:08:20\n\nHmmmmmm... The doctests do not pass because of a bug in Sage's interface with sloane, and #10358 fixes the file anyway !\n\nNathann",
    "created_at": "2013-06-27T17:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50376",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_6323-rev.patch](tarball://root/attachments/some-uuid/ticket6323/trac_6323-rev.patch) by @nathanncohen created at 2013-06-27 17:08:20

Hmmmmmm... The doctests do not pass because of a bug in Sage's interface with sloane, and #10358 fixes the file anyway !

Nathann



---

archive/issue_comments_050377.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-08-13T08:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6323#issuecomment-50377",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_006569.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-08-13T08:46:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6323",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6323#event-6569"
}
```
