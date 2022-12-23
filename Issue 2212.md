# Issue 2212: degree sequence documentation [with bundle, needs review]

archive/issues_002212.json:
```json
{
    "body": "Assignee: rlm\n\nThis corrects some errors/transpositions in the documentation of the various degree sequence functions.  It also removes the \"seed\" variable in DegreeSequence itself, as a main NetworkX developer confirmed what the NetworkX code suggests, that this is unnecessary (they have now removed it in their implementation).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2212\n\n",
    "created_at": "2008-02-19T20:30:40Z",
    "labels": [
        "graph theory",
        "trivial",
        "bug"
    ],
    "title": "degree sequence documentation [with bundle, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2212",
    "user": "kcrisman"
}
```
Assignee: rlm

This corrects some errors/transpositions in the documentation of the various degree sequence functions.  It also removes the "seed" variable in DegreeSequence itself, as a main NetworkX developer confirmed what the NetworkX code suggests, that this is unnecessary (they have now removed it in their implementation).

Issue created by migration from https://trac.sagemath.org/ticket/2212





---

archive/issue_comments_014608.json:
```json
{
    "body": "Changes degree sequence documentation and removes \"seed\" variable from DegreeSequence",
    "created_at": "2008-02-19T20:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14608",
    "user": "kcrisman"
}
```

Changes degree sequence documentation and removes "seed" variable from DegreeSequence



---

archive/issue_comments_014609.json:
```json
{
    "body": "Attachment\n\nUpon looking at the .diff, I see some changes which I did NOT put in there.  I saw them while using hg_sage, but figured it was some artifact, yet here they are.  \nThe only changes I made were very short ones in the documentation for the various DegreeSequence functions and removing \"seed\".  Apologies for not catching this; I assume the other changes were already incorporated in any case.",
    "created_at": "2008-02-19T20:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14609",
    "user": "kcrisman"
}
```

Attachment

Upon looking at the .diff, I see some changes which I did NOT put in there.  I saw them while using hg_sage, but figured it was some artifact, yet here they are.  
The only changes I made were very short ones in the documentation for the various DegreeSequence functions and removing "seed".  Apologies for not catching this; I assume the other changes were already incorporated in any case.



---

archive/issue_comments_014610.json:
```json
{
    "body": "The bundle needs to be rebased against the current release, so do not apply.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T20:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14610",
    "user": "mabshoff"
}
```

The bundle needs to be rebased against the current release, so do not apply.

Cheers,

Michael



---

archive/issue_comments_014611.json:
```json
{
    "body": "New patch correctly based against 2.10.2 release.",
    "created_at": "2008-02-28T01:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14611",
    "user": "kcrisman"
}
```

New patch correctly based against 2.10.2 release.



---

archive/issue_comments_014612.json:
```json
{
    "body": "Newer patch based on 2.10.2",
    "created_at": "2008-02-28T01:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14612",
    "user": "kcrisman"
}
```

Newer patch based on 2.10.2



---

archive/issue_comments_014613.json:
```json
{
    "body": "Attachment\n\nBased on 2.10.3.rc2",
    "created_at": "2008-03-07T02:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14613",
    "user": "kcrisman"
}
```

Attachment

Based on 2.10.3.rc2



---

archive/issue_comments_014614.json:
```json
{
    "body": "Positive review pending a couple of suggestions:\n\n1. In DegreeSequence, in the docs, it says \"connecting vertices of highest to\" and should probably read \"connecting vertices of highest degree to\"\n\n2. DegreeSequenceExpected never does anything with the seed parameter.  Can you modify the call to networkx so that the seed is passed?\n\n3. The docs for DegreeSequenceExpected contain the informational, but distracting, parenthetical remark about quantum graphs.  Can you delete that remark?",
    "created_at": "2008-03-07T23:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14614",
    "user": "jason"
}
```

Positive review pending a couple of suggestions:

1. In DegreeSequence, in the docs, it says "connecting vertices of highest to" and should probably read "connecting vertices of highest degree to"

2. DegreeSequenceExpected never does anything with the seed parameter.  Can you modify the call to networkx so that the seed is passed?

3. The docs for DegreeSequenceExpected contain the informational, but distracting, parenthetical remark about quantum graphs.  Can you delete that remark?



---

archive/issue_comments_014615.json:
```json
{
    "body": "This is probably clear already, but just in case, do NOT apply 8681.patch.\n\n+1 on the positive review",
    "created_at": "2008-03-08T00:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14615",
    "user": "rlm"
}
```

This is probably clear already, but just in case, do NOT apply 8681.patch.

+1 on the positive review



---

archive/issue_comments_014616.json:
```json
{
    "body": "Responding in reverse order:\n\n3. Whoever wrote the original documentation put that in there, so I left it, though I also found it distracting. Was there additional functionality expected?  So I'll remove it there and in another place it occurs, and if we ever support quantum graphs we can put it back in.  (I sheepishly admit I have never heard of quantum graphs.)\n\n2. I didn't notice that, and will add the call, since NetworkX definitely has it.\n\n1. I also left that alone because it was in the original documentation, but with the review I gladly change it.",
    "created_at": "2008-03-08T01:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14616",
    "user": "kcrisman"
}
```

Responding in reverse order:

3. Whoever wrote the original documentation put that in there, so I left it, though I also found it distracting. Was there additional functionality expected?  So I'll remove it there and in another place it occurs, and if we ever support quantum graphs we can put it back in.  (I sheepishly admit I have never heard of quantum graphs.)

2. I didn't notice that, and will add the call, since NetworkX definitely has it.

1. I also left that alone because it was in the original documentation, but with the review I gladly change it.



---

archive/issue_comments_014617.json:
```json
{
    "body": "Attachment\n\nFixes of comments - please apply AFTER 8809 patch.  Confirming to NOT apply 8681 patch or previous bundle.",
    "created_at": "2008-03-08T01:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14617",
    "user": "kcrisman"
}
```

Attachment

Fixes of comments - please apply AFTER 8809 patch.  Confirming to NOT apply 8681 patch or previous bundle.



---

archive/issue_comments_014618.json:
```json
{
    "body": "The changes look good to me.  I say apply.",
    "created_at": "2008-03-10T14:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14618",
    "user": "jason"
}
```

The changes look good to me.  I say apply.



---

archive/issue_comments_014619.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-13T12:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14619",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_014620.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-13T12:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2212#issuecomment-14620",
    "user": "mabshoff"
}
```

Resolution: fixed
