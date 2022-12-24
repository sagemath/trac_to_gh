# Issue 6572: tutorial: put double colon on its own line

archive/issues_006572.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @jhpalmieri @nathanncohen\n\nKeywords: tutorial\n\nSee this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/85929d86accdf94d) thread for some background information. John Palmieri suggests that all doctests in the Sage tutorial be preceded with a double colon on its own line. That way, the doctest script would pick up all doctests in the tutorial.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6572\n\n",
    "created_at": "2009-07-20T20:11:48Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "tutorial: put double colon on its own line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6572",
    "user": "mvngu"
}
```
Assignee: tba

CC:  @jhpalmieri @nathanncohen

Keywords: tutorial

See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/85929d86accdf94d) thread for some background information. John Palmieri suggests that all doctests in the Sage tutorial be preceded with a double colon on its own line. That way, the doctest script would pick up all doctests in the tutorial.

Issue created by migration from https://trac.sagemath.org/ticket/6572





---

archive/issue_comments_053660.json:
```json
{
    "body": "Here are two patches, one for the main repository and one for the scripts repository.  \n\nThe scripts patch does the following: first, previously, doctests had to be preceded by a double colon at the beginning of a line, and now they only need to be preceded by a line which starts with white space then a double colon -- the double colon no longer has to be at the left margin.  This is important for some files (like constructions/algebraic_geometry.rst), in which indentations might break if we had to move the double colons to the left.   The second change is figuring out when the doctest block ends: it looks for text indented no farther than the double colons were.  (Previously, it looked for text which wasn't indented at all, so if a paragraph was indented, then some doctests were indented further, then a paragraph unindented one level, that second paragaph was treated as part of the doctest block.)\n\nAs a result of all of this, some more doctests are found by `sage -t`.  The other patch does two things: it makes the change advertised in the summary for the ticket, moving double colons onto lines of their own where necessary.  It also tries to fix the newly discovered broken doctests.  I don't know how to fix some of these, and so they are being skipped.  These include the one which triggered this whole episode:\n\n```\n     sage: theta = var('theta')\n     sage: solve(cos(theta)==sin(theta))\n     [sin(theta) == cos(theta)]\n```\n\nas well as some doctests involving starting and stopping the Singular console, for example.\n\nFor me, this passes all tests on Mac OS X (both 32-bit and 64-bit), and also on a 32-bit linux box (an old Ubuntu machine) and a 64-bit linux box (sage.math).  It would be best to fix the skipped tests, but that can go in another ticket if no one knows how to do it right now.",
    "created_at": "2009-07-21T03:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53660",
    "user": "@jhpalmieri"
}
```

Here are two patches, one for the main repository and one for the scripts repository.  

The scripts patch does the following: first, previously, doctests had to be preceded by a double colon at the beginning of a line, and now they only need to be preceded by a line which starts with white space then a double colon -- the double colon no longer has to be at the left margin.  This is important for some files (like constructions/algebraic_geometry.rst), in which indentations might break if we had to move the double colons to the left.   The second change is figuring out when the doctest block ends: it looks for text indented no farther than the double colons were.  (Previously, it looked for text which wasn't indented at all, so if a paragraph was indented, then some doctests were indented further, then a paragraph unindented one level, that second paragaph was treated as part of the doctest block.)

As a result of all of this, some more doctests are found by `sage -t`.  The other patch does two things: it makes the change advertised in the summary for the ticket, moving double colons onto lines of their own where necessary.  It also tries to fix the newly discovered broken doctests.  I don't know how to fix some of these, and so they are being skipped.  These include the one which triggered this whole episode:

```
     sage: theta = var('theta')
     sage: solve(cos(theta)==sin(theta))
     [sin(theta) == cos(theta)]
```

as well as some doctests involving starting and stopping the Singular console, for example.

For me, this passes all tests on Mac OS X (both 32-bit and 64-bit), and also on a 32-bit linux box (an old Ubuntu machine) and a 64-bit linux box (sage.math).  It would be best to fix the skipped tests, but that can go in another ticket if no one knows how to do it right now.



---

archive/issue_comments_053661.json:
```json
{
    "body": "Attachment [trac_6572_scripts.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572_scripts.patch) by @jhpalmieri created at 2009-07-27 17:14:26\n\nSee #6642 for the problem with the 'solve' doctest.",
    "created_at": "2009-07-27T17:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53661",
    "user": "@jhpalmieri"
}
```

Attachment [trac_6572_scripts.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572_scripts.patch) by @jhpalmieri created at 2009-07-27 17:14:26

See #6642 for the problem with the 'solve' doctest.



---

archive/issue_comments_053662.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> See #6642 for the problem with the 'solve' doctest.\n\nThis may be fixed now - see #6642.  If so, I guess one could put that back in the tutorial.",
    "created_at": "2009-08-26T21:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53662",
    "user": "@kcrisman"
}
```

Replying to [comment:3 jhpalmieri]:
> See #6642 for the problem with the 'solve' doctest.

This may be fixed now - see #6642.  If so, I guess one could put that back in the tutorial.



---

archive/issue_comments_053663.json:
```json
{
    "body": "Here is a patch against 4.1.2.alpha1; this depends on #6642.",
    "created_at": "2009-09-08T20:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53663",
    "user": "@jhpalmieri"
}
```

Here is a patch against 4.1.2.alpha1; this depends on #6642.



---

archive/issue_comments_053664.json:
```json
{
    "body": "Doesn't it make more sense to detect double colons at the end of a line?\n\nIn restructured text, the two should be equivalent.  It should be the same for the doctests as well.",
    "created_at": "2009-10-05T13:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53664",
    "user": "@mwhansen"
}
```

Doesn't it make more sense to detect double colons at the end of a line?

In restructured text, the two should be equivalent.  It should be the same for the doctests as well.



---

archive/issue_comments_053665.json:
```json
{
    "body": "Attachment [trac_6572-scripts-part2.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572-scripts-part2.patch) by @jhpalmieri created at 2009-10-05 15:06:40\n\napply on top of other scripts patch",
    "created_at": "2009-10-05T15:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53665",
    "user": "@jhpalmieri"
}
```

Attachment [trac_6572-scripts-part2.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572-scripts-part2.patch) by @jhpalmieri created at 2009-10-05 15:06:40

apply on top of other scripts patch



---

archive/issue_comments_053666.json:
```json
{
    "body": "Replying to [comment:6 mhansen]:\n> Doesn't it make more sense to detect double colons at the end of a line?\n> \n> In restructured text, the two should be equivalent.  It should be the same for the doctests as well.\n\nOkay, that makes sense.  The new scripts patch changes the regular expression to fix this, I think.\n\nNow the problem is that the file (added since this ticket was opened) `tour_graphtheory.rst` is a *complete* disaster, with 15 doctest failures.  I can fix lots of the failed doctests by adding \"...\" and \".. link\" in various places, but I don't know what to do about failures like these:\n\n```\n    sage: g.plot(edge_colors=g.edge_coloring(hex_colors=True))\n    AttributeError: 'Graph' object has no attribute 'edge_coloring'\n\n    sage: g.vertex_coloring()\n    AttributeError: 'Graph' object has no attribute 'vertex_coloring'\n\n    sage: print g.max_matching()\n    AttributeError: 'Graph' object has no attribute 'max_matching'\n```\n\nI don't know what was intended and therefore I don't know how to fix it.  I'll post a patch that fixes what I can.",
    "created_at": "2009-10-05T15:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53666",
    "user": "@jhpalmieri"
}
```

Replying to [comment:6 mhansen]:
> Doesn't it make more sense to detect double colons at the end of a line?
> 
> In restructured text, the two should be equivalent.  It should be the same for the doctests as well.

Okay, that makes sense.  The new scripts patch changes the regular expression to fix this, I think.

Now the problem is that the file (added since this ticket was opened) `tour_graphtheory.rst` is a *complete* disaster, with 15 doctest failures.  I can fix lots of the failed doctests by adding "..." and ".. link" in various places, but I don't know what to do about failures like these:

```
    sage: g.plot(edge_colors=g.edge_coloring(hex_colors=True))
    AttributeError: 'Graph' object has no attribute 'edge_coloring'

    sage: g.vertex_coloring()
    AttributeError: 'Graph' object has no attribute 'vertex_coloring'

    sage: print g.max_matching()
    AttributeError: 'Graph' object has no attribute 'max_matching'
```

I don't know what was intended and therefore I don't know how to fix it.  I'll post a patch that fixes what I can.



---

archive/issue_comments_053667.json:
```json
{
    "body": "I'll post a replacement for \"trac_6572-double-colon.patch\" soon.  That patch shouldn't have to be as large, if double colons at the end of lines work right.",
    "created_at": "2009-10-05T15:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53667",
    "user": "@jhpalmieri"
}
```

I'll post a replacement for "trac_6572-double-colon.patch" soon.  That patch shouldn't have to be as large, if double colons at the end of lines work right.



---

archive/issue_comments_053668.json:
```json
{
    "body": "Attachment [trac_6572-double-colon.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572-double-colon.patch) by @jhpalmieri created at 2009-10-06 00:59:39\n\ndepends on #6642",
    "created_at": "2009-10-06T00:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53668",
    "user": "@jhpalmieri"
}
```

Attachment [trac_6572-double-colon.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572-double-colon.patch) by @jhpalmieri created at 2009-10-06 00:59:39

depends on #6642



---

archive/issue_comments_053669.json:
```json
{
    "body": "Here's a new version of \"trac_6572-double-colon.patch\".  This fixes a few more doctest failures uncovered by the script patches.  Apply both script patches, this patch, and the graph theory patch.  Together with the patch at #6642, this means that most doctests pass in the documentation.  `tutorial/tour_graphtheory.rst` is the only problem now.",
    "created_at": "2009-10-06T01:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53669",
    "user": "@jhpalmieri"
}
```

Here's a new version of "trac_6572-double-colon.patch".  This fixes a few more doctest failures uncovered by the script patches.  Apply both script patches, this patch, and the graph theory patch.  Together with the patch at #6642, this means that most doctests pass in the documentation.  `tutorial/tour_graphtheory.rst` is the only problem now.



---

archive/issue_comments_053670.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-08T01:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53670",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053671.json:
```json
{
    "body": "With the patch at #7149, this is now ready for review.  Ignore the graph theory patch, since that is now taken care of by #7149.",
    "created_at": "2009-10-08T01:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53671",
    "user": "@jhpalmieri"
}
```

With the patch at #7149, this is now ready for review.  Ignore the graph theory patch, since that is now taken care of by #7149.



---

archive/issue_comments_053672.json:
```json
{
    "body": "ignore this patch!",
    "created_at": "2009-10-08T01:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53672",
    "user": "@jhpalmieri"
}
```

ignore this patch!



---

archive/issue_comments_053673.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-15T09:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53673",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053674.json:
```json
{
    "body": "Attachment [trac_6572-graphtheory.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572-graphtheory.patch) by @mwhansen created at 2009-10-15 09:17:06\n\nLooks good to me.",
    "created_at": "2009-10-15T09:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53674",
    "user": "@mwhansen"
}
```

Attachment [trac_6572-graphtheory.patch](tarball://root/attachments/some-uuid/ticket6572/trac_6572-graphtheory.patch) by @mwhansen created at 2009-10-15 09:17:06

Looks good to me.



---

archive/issue_comments_053675.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6572#issuecomment-53675",
    "user": "@mwhansen"
}
```

Resolution: fixed
