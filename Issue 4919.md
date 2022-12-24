# Issue 4919: convert sage.misc.* docstrings to Sphinx

archive/issues_004919.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4919\n\n",
    "created_at": "2009-01-01T22:53:45Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.misc.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4919",
    "user": "@mwhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4919





---

archive/issue_comments_037324.json:
```json
{
    "body": "Attachment [trac_4919.patch](tarball://root/attachments/some-uuid/ticket4919/trac_4919.patch) by @mwhansen created at 2009-01-02 02:23:05",
    "created_at": "2009-01-02T02:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37324",
    "user": "@mwhansen"
}
```

Attachment [trac_4919.patch](tarball://root/attachments/some-uuid/ticket4919/trac_4919.patch) by @mwhansen created at 2009-01-02 02:23:05



---

archive/issue_comments_037325.json:
```json
{
    "body": "I'm not sure why graphs/graph_generators is included in this patch, but the one change there is minor enough that I can give it a positive review...\n\nattach.py isn't part of the reference manual, it seems to me.  Should it be?  The changes to the source code look fine.\n\ndist.py: looks good.\n\nfunc_persist.py: looks good.\n\nfunctional.py: I think lines 428-430 could be deleted, but this is not a big deal.\n\n  lines 943-946: this should be an itemized list (a continuation of the list of inputs)\n\ngetusage.py: looks good.\n\nhg.py: as I mentioned in my review of #4902, methods like `__init__` are missing from the html version of the documentation.\n\n  lines 415-419: this should be an itemized list (it's been garbled in the conversion)\n\n  same thing for lines 454-461, 534-537, 690-693, 921-922, 947-949, 970-972\n\n  line 1035: Sage_ROOT should be SAGE_ROOT\n\nlatex.py: this is not really an appropriate issue for this ticket, but in the conversion to html and/or pdf, can we remove the word \"nodetex\" when it appears as a directive in a docstring?\n\n  lines 744-750: these look okay as is, but might look better with each numbered item starting on a new line\n\nlog.py: looks good.\n\nmisc.py: lines 304-308: should be a list (or two lists, one for input, one for output)\n\n  line 705: need a space between `for` and `\"Sage\"`\n\n  lines 718-720: could be deleted (just produces a break in the EXAMPLES).  same for lines 723-725, 728-730, 733-735, 739-741, 749-751, 756-758, 844-846, 850-852.\n\n  line 1437: it should say \"whether certain integers are >3\", but the \">\" was omitted.\n\n  line 1453: \"positive integer < 100\": the \"<\" was omitted.\n\n  line 1629: \"fail in Sage <= 1.3.7.\": the \"<\" was omitted.\n\n  line 1674: Sage_ROOT should be SAGE_ROOT\n\nmrange.py: looks good.\n\npackage.py: lines 126-128 should be an itemized list.  same with lines 169-171, 212-214, 256-257\n\npersist.py: looks good.\n\nsage_eval.py: looks good.\n\ntrace.py: not part of the reference manual.  looks good anyway.",
    "created_at": "2009-01-07T21:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37325",
    "user": "@jhpalmieri"
}
```

I'm not sure why graphs/graph_generators is included in this patch, but the one change there is minor enough that I can give it a positive review...

attach.py isn't part of the reference manual, it seems to me.  Should it be?  The changes to the source code look fine.

dist.py: looks good.

func_persist.py: looks good.

functional.py: I think lines 428-430 could be deleted, but this is not a big deal.

  lines 943-946: this should be an itemized list (a continuation of the list of inputs)

getusage.py: looks good.

hg.py: as I mentioned in my review of #4902, methods like `__init__` are missing from the html version of the documentation.

  lines 415-419: this should be an itemized list (it's been garbled in the conversion)

  same thing for lines 454-461, 534-537, 690-693, 921-922, 947-949, 970-972

  line 1035: Sage_ROOT should be SAGE_ROOT

latex.py: this is not really an appropriate issue for this ticket, but in the conversion to html and/or pdf, can we remove the word "nodetex" when it appears as a directive in a docstring?

  lines 744-750: these look okay as is, but might look better with each numbered item starting on a new line

log.py: looks good.

misc.py: lines 304-308: should be a list (or two lists, one for input, one for output)

  line 705: need a space between `for` and `"Sage"`

  lines 718-720: could be deleted (just produces a break in the EXAMPLES).  same for lines 723-725, 728-730, 733-735, 739-741, 749-751, 756-758, 844-846, 850-852.

  line 1437: it should say "whether certain integers are >3", but the ">" was omitted.

  line 1453: "positive integer < 100": the "<" was omitted.

  line 1629: "fail in Sage <= 1.3.7.": the "<" was omitted.

  line 1674: Sage_ROOT should be SAGE_ROOT

mrange.py: looks good.

package.py: lines 126-128 should be an itemized list.  same with lines 169-171, 212-214, 256-257

persist.py: looks good.

sage_eval.py: looks good.

trace.py: not part of the reference manual.  looks good anyway.



---

archive/issue_comments_037326.json:
```json
{
    "body": "Attachment [trac_4919-2.patch](tarball://root/attachments/some-uuid/ticket4919/trac_4919-2.patch) by @mwhansen created at 2009-01-11 03:45:12",
    "created_at": "2009-01-11T03:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37326",
    "user": "@mwhansen"
}
```

Attachment [trac_4919-2.patch](tarball://root/attachments/some-uuid/ticket4919/trac_4919-2.patch) by @mwhansen created at 2009-01-11 03:45:12



---

archive/issue_comments_037327.json:
```json
{
    "body": "Great, except you missed (in hg.py):\n\n>   lines 415-419: this should be an itemized list (it's been garbled in the conversion)\n\n(You got the other six instances that I mentioned.)",
    "created_at": "2009-01-11T06:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37327",
    "user": "@jhpalmieri"
}
```

Great, except you missed (in hg.py):

>   lines 415-419: this should be an itemized list (it's been garbled in the conversion)

(You got the other six instances that I mentioned.)



---

archive/issue_comments_037328.json:
```json
{
    "body": "(Oops, I forgot to change the summary when I added my last comment.)",
    "created_at": "2009-01-15T04:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37328",
    "user": "@jhpalmieri"
}
```

(Oops, I forgot to change the summary when I added my last comment.)



---

archive/issue_comments_037329.json:
```json
{
    "body": "Attachment [sage.misc-final.patch](tarball://root/attachments/some-uuid/ticket4919/sage.misc-final.patch) by @jhpalmieri created at 2009-02-21 23:04:09\n\nI still see the problem with lines 415-419 in hg.py: should be an itemized list, not a paragraph.",
    "created_at": "2009-02-21T23:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37329",
    "user": "@jhpalmieri"
}
```

Attachment [sage.misc-final.patch](tarball://root/attachments/some-uuid/ticket4919/sage.misc-final.patch) by @jhpalmieri created at 2009-02-21 23:04:09

I still see the problem with lines 415-419 in hg.py: should be an itemized list, not a paragraph.



---

archive/issue_comments_037330.json:
```json
{
    "body": "I am merging #4919 as is. Please move the remaining issues to a new ticket against 3.4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37330",
    "user": "mabshoff"
}
```

I am merging #4919 as is. Please move the remaining issues to a new ticket against 3.4.

Cheers,

Michael



---

archive/issue_comments_037331.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37331",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037332.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37332",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_037333.json:
```json
{
    "body": "See #5374.",
    "created_at": "2009-02-26T15:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37333",
    "user": "@jhpalmieri"
}
```

See #5374.



---

archive/issue_comments_037334.json:
```json
{
    "body": "Thanks John.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T16:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4919#issuecomment-37334",
    "user": "mabshoff"
}
```

Thanks John.

Cheers,

Michael
