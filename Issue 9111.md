# Issue 9111: modular decomposition

archive/issues_009111.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nUsing the C code written by Thierry de Montgolfier and available there :\nhttp://www.liafa.jussieu.fr/~fm/algos/index.html\n\nWe now have a Graph.modular_decomposition function available in Sage !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9111\n\n",
    "created_at": "2010-06-01T21:53:58Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "modular decomposition",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9111",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

Using the C code written by Thierry de Montgolfier and available there :
http://www.liafa.jussieu.fr/~fm/algos/index.html

We now have a Graph.modular_decomposition function available in Sage !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9111





---

archive/issue_comments_084610.json:
```json
{
    "body": "From that webpage, it says that the code is only available for non-commercial use.",
    "created_at": "2010-06-01T23:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84610",
    "user": "https://github.com/mwhansen"
}
```

From that webpage, it says that the code is only available for non-commercial use.



---

archive/issue_comments_084611.json:
```json
{
    "body": "yesyesyes, it should be licensed under the GPL very soon :-)\n\nFabrice de Montgolfer is away for something like a week, and then it should be done :-)\n\nNathann",
    "created_at": "2010-06-01T23:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84611",
    "user": "https://github.com/nathanncohen"
}
```

yesyesyes, it should be licensed under the GPL very soon :-)

Fabrice de Montgolfer is away for something like a week, and then it should be done :-)

Nathann



---

archive/issue_comments_084612.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-02T22:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84612",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084613.json:
```json
{
    "body": "A couple of comments:\n\n1. Why is modular_decomposition.c included in the patch?\n\n2. The comment at the top of modular_decomposition.pyx indicates it is a copy of code, but is it rather a Cython interface to C code?\n\n3. It wouldn't hurt to give a very brief explanation of what a modular decomposition of a graph is in the docstrings",
    "created_at": "2010-06-02T22:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84613",
    "user": "https://github.com/jasongrout"
}
```

A couple of comments:

1. Why is modular_decomposition.c included in the patch?

2. The comment at the top of modular_decomposition.pyx indicates it is a copy of code, but is it rather a Cython interface to C code?

3. It wouldn't hurt to give a very brief explanation of what a modular decomposition of a graph is in the docstrings



---

archive/issue_comments_084614.json:
```json
{
    "body": "And 4. This functionality is cool!",
    "created_at": "2010-06-02T22:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84614",
    "user": "https://github.com/jasongrout"
}
```

And 4. This functionality is cool!



---

archive/issue_comments_084615.json:
```json
{
    "body": "Hello !\n\n1. Because I wasn't paying attention\n\n2. I mean by this that the lines of the code building the graph according to the format used in the .c file, along with the ones reading the decomposition once it is computed, can be found in the .c files too. I copied those and Cythonized them, but the \"real\" code is still contained in the .c file.\n\n3. Indeed.\n\n4. I think so, too ! Especially in C, and in mlog(n) :-)\n\nI will update the patch once the software is \"officially\" GPL2, which could mean next week.\n\nNathann",
    "created_at": "2010-06-03T11:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84615",
    "user": "https://github.com/nathanncohen"
}
```

Hello !

1. Because I wasn't paying attention

2. I mean by this that the lines of the code building the graph according to the format used in the .c file, along with the ones reading the decomposition once it is computed, can be found in the .c files too. I copied those and Cythonized them, but the "real" code is still contained in the .c file.

3. Indeed.

4. I think so, too ! Especially in C, and in mlog(n) :-)

I will update the patch once the software is "officially" GPL2, which could mean next week.

Nathann



---

archive/issue_comments_084616.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-20T19:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84616",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084617.json:
```json
{
    "body": "Here it is ! With a brand-new GPL2 licence, thanks to Fabien de Montgolfier ! :-)\n\nNathann",
    "created_at": "2010-06-20T19:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84617",
    "user": "https://github.com/nathanncohen"
}
```

Here it is ! With a brand-new GPL2 licence, thanks to Fabien de Montgolfier ! :-)

Nathann



---

archive/issue_comments_084618.json:
```json
{
    "body": "Attachment [trac_9111-doc-edits.patch](tarball://root/attachments/some-uuid/ticket9111/trac_9111-doc-edits.patch) by @rlmill created at 2010-06-21 21:27:25",
    "created_at": "2010-06-21T21:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84618",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9111-doc-edits.patch](tarball://root/attachments/some-uuid/ticket9111/trac_9111-doc-edits.patch) by @rlmill created at 2010-06-21 21:27:25



---

archive/issue_comments_084619.json:
```json
{
    "body": "Replying to [comment:5 ncohen]:\n> 2. I mean by this that the lines of the code building the graph according to the format used in the .c file, along with the ones reading the decomposition once it is computed, can be found in the .c files too. I copied those and Cythonized them, but the \"real\" code is still contained in the .c file.\n\nCan you make this a bit more clear in the documentation? (Please, in a new patch on top of attachment:trac_9111-doc-edits.patch to avoid conflict with the other patch.)\n\nIt seems like there should be more thorough documentation of the idea of modular decomposition. Perhaps a chapter, or at least a chunk, for the reference manual, or a guided tour or something? I don't want to block this from getting merged because of this, but maybe in a future ticket?\n\nI'm happy with this patch in that it passes its tests and the docs look good, but I'd be much more comfortable with a second reviewer, since I'm not very familiar with modular decompositions. I can certainly offer half of a positive review, though.",
    "created_at": "2010-06-21T21:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84619",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:5 ncohen]:
> 2. I mean by this that the lines of the code building the graph according to the format used in the .c file, along with the ones reading the decomposition once it is computed, can be found in the .c files too. I copied those and Cythonized them, but the "real" code is still contained in the .c file.

Can you make this a bit more clear in the documentation? (Please, in a new patch on top of attachment:trac_9111-doc-edits.patch to avoid conflict with the other patch.)

It seems like there should be more thorough documentation of the idea of modular decomposition. Perhaps a chapter, or at least a chunk, for the reference manual, or a guided tour or something? I don't want to block this from getting merged because of this, but maybe in a future ticket?

I'm happy with this patch in that it passes its tests and the docs look good, but I'd be much more comfortable with a second reviewer, since I'm not very familiar with modular decompositions. I can certainly offer half of a positive review, though.



---

archive/issue_comments_084620.json:
```json
{
    "body": "Here is a bit more of documentation, if it pleases you :-)\n\nI also added a reference to a freely-downloadable survey, just in case !\n\nNathann",
    "created_at": "2010-06-22T07:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84620",
    "user": "https://github.com/nathanncohen"
}
```

Here is a bit more of documentation, if it pleases you :-)

I also added a reference to a freely-downloadable survey, just in case !

Nathann



---

archive/issue_comments_084621.json:
```json
{
    "body": "Attachment [trac_9111-doc_addition.patch](tarball://root/attachments/some-uuid/ticket9111/trac_9111-doc_addition.patch) by @nathanncohen created at 2010-06-22 07:16:33",
    "created_at": "2010-06-22T07:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84621",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9111-doc_addition.patch](tarball://root/attachments/some-uuid/ticket9111/trac_9111-doc_addition.patch) by @nathanncohen created at 2010-06-22 07:16:33



---

archive/issue_comments_084622.json:
```json
{
    "body": "\n```\nsage -t -long sage/graphs/modular_decomposition/modular_decomposition.pyx\n**********************************************************************\nError: TAB character found.\n\n\t [4.5 s]\n```\n",
    "created_at": "2010-07-18T09:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84622",
    "user": "https://github.com/rlmill"
}
```


```
sage -t -long sage/graphs/modular_decomposition/modular_decomposition.pyx
**********************************************************************
Error: TAB character found.

	 [4.5 s]
```




---

archive/issue_comments_084623.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-18T09:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84623",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084624.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-19T01:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84624",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084625.json:
```json
{
    "body": "Here it is !! The \"tab\" characters were not at the beginning but at the end of some lines... some unlucky copy/paste :-)\n\nNathann",
    "created_at": "2010-07-19T01:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84625",
    "user": "https://github.com/nathanncohen"
}
```

Here it is !! The "tab" characters were not at the beginning but at the end of some lines... some unlucky copy/paste :-)

Nathann



---

archive/issue_comments_084626.json:
```json
{
    "body": "Attachment [trac_9111.patch](tarball://root/attachments/some-uuid/ticket9111/trac_9111.patch) by @nathanncohen created at 2010-07-19 01:54:29",
    "created_at": "2010-07-19T01:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84626",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9111.patch](tarball://root/attachments/some-uuid/ticket9111/trac_9111.patch) by @nathanncohen created at 2010-07-19 01:54:29



---

archive/issue_comments_084627.json:
```json
{
    "body": "Apply in the following order:\n\n```\n\n\ntrac_9111.patch\ntrac_9111-doc-edits.patch\ntrac_9111-doc_addition.patch\n\n```\n",
    "created_at": "2010-07-19T08:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84627",
    "user": "https://github.com/rlmill"
}
```

Apply in the following order:

```


trac_9111.patch
trac_9111-doc-edits.patch
trac_9111-doc_addition.patch

```




---

archive/issue_comments_084628.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-19T08:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84628",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084629.json:
```json
{
    "body": "Great !! Thank youuuuuu ! :-)\n\nNathann",
    "created_at": "2010-07-19T08:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84629",
    "user": "https://github.com/nathanncohen"
}
```

Great !! Thank youuuuuu ! :-)

Nathann



---

archive/issue_comments_084630.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T02:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9111#issuecomment-84630",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009270.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T02:48:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9111",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9111#event-9270"
}
```
