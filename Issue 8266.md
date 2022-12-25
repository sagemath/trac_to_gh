# Issue 8266: Improve documentation for word objects

archive/issues_008266.json:
```json
{
    "body": "Assignee: @seblabbe\n\nCC:  abmasse\n\nDocumentation of words and word objects contains only pickle tests and lacks good examples :\n\n\n```\nsage: words?\n...\nDocstring:\n    \n        A class consisting of constructors for several famous words.\n        \n        TESTS::\n    \n            sage: from sage.combinat.words.word_generators import WordGenerator\n            sage: MyWordBank = WordGenerator()\n            sage: type(loads(dumps(MyWordBank)))\n            <class 'sage.combinat.words.word_generators.WordGenerator'>\n```\n\n    \n        \n\n```\nsage: w = Word(range(5))\nsage: w?\n...\nDocstring:\n    \n        TESTS::\n    \n            sage: w = Word([0,1,1,0])\n            sage: w == loads(dumps(w))\n            True\n```\n\n        \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8266\n\n",
    "created_at": "2010-02-14T22:35:51Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Improve documentation for word objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8266",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

CC:  abmasse

Documentation of words and word objects contains only pickle tests and lacks good examples :


```
sage: words?
...
Docstring:
    
        A class consisting of constructors for several famous words.
        
        TESTS::
    
            sage: from sage.combinat.words.word_generators import WordGenerator
            sage: MyWordBank = WordGenerator()
            sage: type(loads(dumps(MyWordBank)))
            <class 'sage.combinat.words.word_generators.WordGenerator'>
```

    
        

```
sage: w = Word(range(5))
sage: w?
...
Docstring:
    
        TESTS::
    
            sage: w = Word([0,1,1,0])
            sage: w == loads(dumps(w))
            True
```

        



Issue created by migration from https://trac.sagemath.org/ticket/8266





---

archive/issue_comments_073046.json:
```json
{
    "body": "Attachment [trac_8266_word_doc_object-sl.patch](tarball://root/attachments/some-uuid/ticket8266/trac_8266_word_doc_object-sl.patch) by @seblabbe created at 2010-02-14 22:39:15\n\nDepends on #7619.",
    "created_at": "2010-02-14T22:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73046",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8266_word_doc_object-sl.patch](tarball://root/attachments/some-uuid/ticket8266/trac_8266_word_doc_object-sl.patch) by @seblabbe created at 2010-02-14 22:39:15

Depends on #7619.



---

archive/issue_comments_073047.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T22:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73047",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073048.json:
```json
{
    "body": "#7619 now have a positive review... so this patch can now get reviewed",
    "created_at": "2010-03-02T10:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73048",
    "user": "https://github.com/seblabbe"
}
```

#7619 now have a positive review... so this patch can now get reviewed



---

archive/issue_comments_073049.json:
```json
{
    "body": "Looked at the patch. Since it is a documentation-only patch, all tests passed. I made sure that the patch of ticket #7619 was applied first. I still made a few minor changes.\n\n1. I replaced \"pyhon\" by \"Python\" everywhere I found it.\n\n2. I added \":\" after a NOTE block that was not appearing in the documentation.\n\n3. I replaced strange unicode characters by \" at the end of S\u00e9bastien's patch.\n\n4. I replaced the latex output of \"w.\" by a code-font \"w.\"\n\nIf S\u00e9bastien agrees with my changes, I allow him to set the ticket to \"positive review\".",
    "created_at": "2010-03-03T21:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73049",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Looked at the patch. Since it is a documentation-only patch, all tests passed. I made sure that the patch of ticket #7619 was applied first. I still made a few minor changes.

1. I replaced "pyhon" by "Python" everywhere I found it.

2. I added ":" after a NOTE block that was not appearing in the documentation.

3. I replaced strange unicode characters by " at the end of Sébastien's patch.

4. I replaced the latex output of "w." by a code-font "w."

If Sébastien agrees with my changes, I allow him to set the ticket to "positive review".



---

archive/issue_comments_073050.json:
```json
{
    "body": "Attachment [trac_8266_review-abm.patch](tarball://root/attachments/some-uuid/ticket8266/trac_8266_review-abm.patch) by abmasse created at 2010-03-03 21:12:12\n\nDoc fixes -- apply on top of S\u00e9bastien's patch",
    "created_at": "2010-03-03T21:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73050",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Attachment [trac_8266_review-abm.patch](tarball://root/attachments/some-uuid/ticket8266/trac_8266_review-abm.patch) by abmasse created at 2010-03-03 21:12:12

Doc fixes -- apply on top of Sébastien's patch



---

archive/issue_comments_073051.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T23:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73051",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073052.json:
```json
{
    "body": "Thanks for the review Alex. I don't know where those strange characters came from... I added one patch to fix two of those characters (I really wanted ```` not \").\n\nSince I my patch fix only two characters in the doc and because I agree with your changes and because your gave a positive review to my first patch, I think I can change the status of this ticket to positive review.",
    "created_at": "2010-03-03T23:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73052",
    "user": "https://github.com/seblabbe"
}
```

Thanks for the review Alex. I don't know where those strange characters came from... I added one patch to fix two of those characters (I really wanted ```` not ").

Since I my patch fix only two characters in the doc and because I agree with your changes and because your gave a positive review to my first patch, I think I can change the status of this ticket to positive review.



---

archive/issue_comments_073053.json:
```json
{
    "body": "Attachment [trac_8266-review2-sl.patch](tarball://root/attachments/some-uuid/ticket8266/trac_8266-review2-sl.patch) by @seblabbe created at 2010-03-05 16:01:24\n\nApplies over the two precedent patches.",
    "created_at": "2010-03-05T16:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73053",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8266-review2-sl.patch](tarball://root/attachments/some-uuid/ticket8266/trac_8266-review2-sl.patch) by @seblabbe created at 2010-03-05 16:01:24

Applies over the two precedent patches.



---

archive/issue_comments_073054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8266#issuecomment-73054",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
