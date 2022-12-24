# Issue 9672: Improve performance of Graph.genus

archive/issues_009672.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  rlm\n\nTwo easy improvements can be made to `Graph.genus`:\n\n* When computing local orbit structure of face map, don't compute the entire orbits.\n* Compute blocks and cut vertices, embed the individual blocks, and reconstruct them if the user wants the embedding.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9672\n\n",
    "created_at": "2010-08-03T01:30:08Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Improve performance of Graph.genus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9672",
    "user": "boothby"
}
```
Assignee: jason, ncohen, rlm

CC:  rlm

Two easy improvements can be made to `Graph.genus`:

* When computing local orbit structure of face map, don't compute the entire orbits.
* Compute blocks and cut vertices, embed the individual blocks, and reconstruct them if the user wants the embedding.

Issue created by migration from https://trac.sagemath.org/ticket/9672





---

archive/issue_comments_093985.json:
```json
{
    "body": "Attachment [9672-genus_improvements.patch](tarball://root/attachments/some-uuid/ticket9672/9672-genus_improvements.patch) by boothby created at 2010-08-05 14:45:52",
    "created_at": "2010-08-05T14:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93985",
    "user": "boothby"
}
```

Attachment [9672-genus_improvements.patch](tarball://root/attachments/some-uuid/ticket9672/9672-genus_improvements.patch) by boothby created at 2010-08-05 14:45:52



---

archive/issue_comments_093986.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-05T14:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93986",
    "user": "boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093987.json:
```json
{
    "body": "Hmmm... I quite agree with the part of the patch distributing the genus computations over 2-connected components, but I know nothing about what happens in the `flip` method. I will try to have a closer look at that, but do you think reading some textbook may help me understand what it does ? I am totally ignorant  about graph embeddings `^^;`. If you have a title in mind, please tell me `:-)`\n\nNathann\n\nP.S. : This shouldn't, of course, prevent any knowledgeable reviewer from reading this patch in the meantime.",
    "created_at": "2010-08-23T03:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93987",
    "user": "ncohen"
}
```

Hmmm... I quite agree with the part of the patch distributing the genus computations over 2-connected components, but I know nothing about what happens in the `flip` method. I will try to have a closer look at that, but do you think reading some textbook may help me understand what it does ? I am totally ignorant  about graph embeddings `^^;`. If you have a title in mind, please tell me `:-)`

Nathann

P.S. : This shouldn't, of course, prevent any knowledgeable reviewer from reading this patch in the meantime.



---

archive/issue_comments_093988.json:
```json
{
    "body": "Nathann,\n\nThere's a forthcoming writeup about how this algorithm works.  Robert Miller understands how it works, though we haven't had a chance to chat about this patch yet.  Either I'll get Robert to review this, or finish the writeup.  I'm more tempted to have Robert review this, since I don't believe the algorithm is novel enough to publish.",
    "created_at": "2010-08-23T19:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93988",
    "user": "boothby"
}
```

Nathann,

There's a forthcoming writeup about how this algorithm works.  Robert Miller understands how it works, though we haven't had a chance to chat about this patch yet.  Either I'll get Robert to review this, or finish the writeup.  I'm more tempted to have Robert review this, since I don't believe the algorithm is novel enough to publish.



---

archive/issue_comments_093989.json:
```json
{
    "body": "Got it ! Waiting for Robert then `:-)`\n\nI don't like to see tickets waiting for review in the Graph Theory section that are not mine `:-D`\n\nNathann",
    "created_at": "2010-08-24T10:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93989",
    "user": "ncohen"
}
```

Got it ! Waiting for Robert then `:-)`

I don't like to see tickets waiting for review in the Graph Theory section that are not mine `:-D`

Nathann



---

archive/issue_comments_093990.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-11T12:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93990",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093991.json:
```json
{
    "body": "Don't let this think you're getting out of writing up the algorithm!",
    "created_at": "2010-11-11T12:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93991",
    "user": "rlm"
}
```

Don't let this think you're getting out of writing up the algorithm!



---

archive/issue_comments_093992.json:
```json
{
    "body": "Or even, a sentence that makes sense!",
    "created_at": "2010-11-11T12:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93992",
    "user": "rlm"
}
```

Or even, a sentence that makes sense!



---

archive/issue_comments_093993.json:
```json
{
    "body": "Should this be merged in Sage 4.6.1? (if yes, please set the Milestone)",
    "created_at": "2010-11-11T16:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93993",
    "user": "jdemeyer"
}
```

Should this be merged in Sage 4.6.1? (if yes, please set the Milestone)



---

archive/issue_comments_093994.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9672#issuecomment-93994",
    "user": "jdemeyer"
}
```

Resolution: fixed
