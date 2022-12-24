# Issue 6903: Function Word currently prevent the inheritance of Words_over_OrderedAlphabet

archive/issues_006903.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @saliola\n\nLet\n\n\n```\nsage: W = Words('ab')\n```\n\n\nIn the state of sage-4.1.1, the function `W.__call__` uses the function `Word`....but it should be the inverse. In fact, the code of the function `Word` contains code like :\n\n\n```\n[...]\n\n    # Construct the word\n    if datatype == 'list':\n        w = FiniteWord_list(parent=parent,data=data)\n    elif datatype == 'str':\n        w = FiniteWord_str(parent=parent,data=data)\n    elif datatype == 'tuple':\n        w = FiniteWord_tuple(parent=parent,data=data)\n    elif datatype == 'callable':\n        if caching:\n            if length is None or length is Infinity:\n                cls = InfiniteWord_callable_with_caching\n            else:\n                cls = FiniteWord_callable_with_caching\n        else:\n            if length is None or length is Infinity:\n                cls = InfiniteWord_callable\n            else:\n                cls = FiniteWord_callable\n        w = cls(parent=parent,callable=data,length=length)\n\n[...]\n```\n\n\nThe problems come when someone wants to inherits the class `Words_over_OrderedAlphabet` to create, let say, a combinatorial classes of all paths (see #5038). Below, we would like the `__call__` function of `WordPaths_all` to creates words paths instances and not the usual words instances. I don't want to rewrite the `__call__` function for `WordPaths_all` since it could be the exact same thing as the one of `Words_over_OrderedAlphabet`.\n\n\n```\nclass WordPaths_all(Words_over_OrderedAlphabet):\n    r\"\"\"\n    The combinatorial class of all paths, i.e of all words over\n    an alphabet where each letter is mapped to a step (a vector).\n    \"\"\"\n    def __init__(self, alphabet, steps):\n        r\"\"\"\n        INPUT:\n\n        - ``alphabet`` - an ordered alphabet \n\n        - ``steps`` - an iterable (of same length as alphabet) of ordered vectors\n\n        EXAMPLES::\n\n[...]\n```\n\n\nOne solution is that the current code of `Word` goes to `Words.__call__` and that the function `Word` simply creates the parent from the input alphabet and delegates the creation to the parent.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6903\n\n",
    "created_at": "2009-09-07T22:44:17Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Function Word currently prevent the inheritance of Words_over_OrderedAlphabet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6903",
    "user": "@seblabbe"
}
```
Assignee: @mwhansen

CC:  @saliola

Let


```
sage: W = Words('ab')
```


In the state of sage-4.1.1, the function `W.__call__` uses the function `Word`....but it should be the inverse. In fact, the code of the function `Word` contains code like :


```
[...]

    # Construct the word
    if datatype == 'list':
        w = FiniteWord_list(parent=parent,data=data)
    elif datatype == 'str':
        w = FiniteWord_str(parent=parent,data=data)
    elif datatype == 'tuple':
        w = FiniteWord_tuple(parent=parent,data=data)
    elif datatype == 'callable':
        if caching:
            if length is None or length is Infinity:
                cls = InfiniteWord_callable_with_caching
            else:
                cls = FiniteWord_callable_with_caching
        else:
            if length is None or length is Infinity:
                cls = InfiniteWord_callable
            else:
                cls = FiniteWord_callable
        w = cls(parent=parent,callable=data,length=length)

[...]
```


The problems come when someone wants to inherits the class `Words_over_OrderedAlphabet` to create, let say, a combinatorial classes of all paths (see #5038). Below, we would like the `__call__` function of `WordPaths_all` to creates words paths instances and not the usual words instances. I don't want to rewrite the `__call__` function for `WordPaths_all` since it could be the exact same thing as the one of `Words_over_OrderedAlphabet`.


```
class WordPaths_all(Words_over_OrderedAlphabet):
    r"""
    The combinatorial class of all paths, i.e of all words over
    an alphabet where each letter is mapped to a step (a vector).
    """
    def __init__(self, alphabet, steps):
        r"""
        INPUT:

        - ``alphabet`` - an ordered alphabet 

        - ``steps`` - an iterable (of same length as alphabet) of ordered vectors

        EXAMPLES::

[...]
```


One solution is that the current code of `Word` goes to `Words.__call__` and that the function `Word` simply creates the parent from the input alphabet and delegates the creation to the parent.

Issue created by migration from https://trac.sagemath.org/ticket/6903





---

archive/issue_comments_057022.json:
```json
{
    "body": "I just posted a patch which corresponds to the work around I recently was using. Something better could be done.\n\nDear Franco, I would like to discuss with you about it, and I could then implement something better.",
    "created_at": "2009-09-07T22:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57022",
    "user": "@seblabbe"
}
```

I just posted a patch which corresponds to the work around I recently was using. Something better could be done.

Dear Franco, I would like to discuss with you about it, and I could then implement something better.



---

archive/issue_comments_057023.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-13T12:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57023",
    "user": "@seblabbe"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057024.json:
```json
{
    "body": "Changing assignee from @mwhansen to @seblabbe.",
    "created_at": "2009-09-13T12:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57024",
    "user": "@seblabbe"
}
```

Changing assignee from @mwhansen to @seblabbe.



---

archive/issue_comments_057025.json:
```json
{
    "body": "Attachment [trac_6903_word_improve_constructor-sl.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_word_improve_constructor-sl.patch) by @seblabbe created at 2009-09-13 12:48:34\n\nI just posted a patch which correspond to something better. All test pass in sage/combinat/words. I also tested the pickle jar using (from http://www.sagemath.org/doc/reference/sage/structure/sage_object.html) :\n\n\n```\nsage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'\nsage: sage.structure.sage_object.unpickle_all(std)\n```\n\n\nI keep the 'needs work' label, because there is still something I want to check. In fact, the code that changes the class of a word from `Word_class` to `FiniteWord_class` when it reaches the end of the word might be updated as well here, but I can't figure out where is that code!!! Franco should remember that.",
    "created_at": "2009-09-13T12:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57025",
    "user": "@seblabbe"
}
```

Attachment [trac_6903_word_improve_constructor-sl.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_word_improve_constructor-sl.patch) by @seblabbe created at 2009-09-13 12:48:34

I just posted a patch which correspond to something better. All test pass in sage/combinat/words. I also tested the pickle jar using (from http://www.sagemath.org/doc/reference/sage/structure/sage_object.html) :


```
sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
```


I keep the 'needs work' label, because there is still something I want to check. In fact, the code that changes the class of a word from `Word_class` to `FiniteWord_class` when it reaches the end of the word might be updated as well here, but I can't figure out where is that code!!! Franco should remember that.



---

archive/issue_comments_057026.json:
```json
{
    "body": "I am including two patches here.\n\nIn `trac_6903_reviewer_patch_1.patch`, I made the following changes:\n\n1. I fixed the code that changes the class of a word `FiniteWord_class` when it reaches the end of the iterator.\n\n2. I changed `_classetype` to `_element_classes` since the method defines the classes of the elements of the parent.\n\n3. I also cleaned up the code for `_element_classes`.\n\n4. Both `Words_all.__call__` and `Words_all._construct_word` run `self._check`, so I am deleting the occurrence in `Words_all._construct_word`.\n\nIn `trac_6903_reviewer_patch_2.patch`, I changed the method `_element_classes` into an attribute (a `lazy_attribute`, actually). So it *is* the dictionary instead of returning the dictionary. I think it is a bad idea to re-create that dictionary every time a word is created.",
    "created_at": "2009-09-16T20:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57026",
    "user": "@saliola"
}
```

I am including two patches here.

In `trac_6903_reviewer_patch_1.patch`, I made the following changes:

1. I fixed the code that changes the class of a word `FiniteWord_class` when it reaches the end of the iterator.

2. I changed `_classetype` to `_element_classes` since the method defines the classes of the elements of the parent.

3. I also cleaned up the code for `_element_classes`.

4. Both `Words_all.__call__` and `Words_all._construct_word` run `self._check`, so I am deleting the occurrence in `Words_all._construct_word`.

In `trac_6903_reviewer_patch_2.patch`, I changed the method `_element_classes` into an attribute (a `lazy_attribute`, actually). So it *is* the dictionary instead of returning the dictionary. I think it is a bad idea to re-create that dictionary every time a word is created.



---

archive/issue_comments_057027.json:
```json
{
    "body": "Apply on top of trac_6903_word_improve_constructor-sl.patch",
    "created_at": "2009-09-16T20:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57027",
    "user": "@saliola"
}
```

Apply on top of trac_6903_word_improve_constructor-sl.patch



---

archive/issue_comments_057028.json:
```json
{
    "body": "Attachment [trac_6903_reviewer_patch_1.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_reviewer_patch_1.patch) by @saliola created at 2009-09-16 20:57:13\n\nApply on top of trac_6903_reviewer_patch_2.patch",
    "created_at": "2009-09-16T20:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57028",
    "user": "@saliola"
}
```

Attachment [trac_6903_reviewer_patch_1.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_reviewer_patch_1.patch) by @saliola created at 2009-09-16 20:57:13

Apply on top of trac_6903_reviewer_patch_2.patch



---

archive/issue_comments_057029.json:
```json
{
    "body": "Attachment [trac_6903_reviewer_patch_2.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_reviewer_patch_2.patch) by @saliola created at 2009-09-16 20:59:40\n\nModulo the changes in the reviewer patches, I give a positive review to S\u00e9bastien's patch.\n\nS\u00e9bastien, can you review my patches?",
    "created_at": "2009-09-16T20:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57029",
    "user": "@saliola"
}
```

Attachment [trac_6903_reviewer_patch_2.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_reviewer_patch_2.patch) by @saliola created at 2009-09-16 20:59:40

Modulo the changes in the reviewer patches, I give a positive review to Sébastien's patch.

Sébastien, can you review my patches?



---

archive/issue_comments_057030.json:
```json
{
    "body": "Attachment [trac_6903_review_3-sl.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_review_3-sl.patch) by @seblabbe created at 2009-09-17 18:03:11\n\nApplies over the precedent 3 patches.",
    "created_at": "2009-09-17T18:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57030",
    "user": "@seblabbe"
}
```

Attachment [trac_6903_review_3-sl.patch](tarball://root/attachments/some-uuid/ticket6903/trac_6903_review_3-sl.patch) by @seblabbe created at 2009-09-17 18:03:11

Applies over the precedent 3 patches.



---

archive/issue_comments_057031.json:
```json
{
    "body": "I just added a patch that removes two lines now useless after Franco's changes.\n\nAll test passed in sage/combinat/words directory. Documentation builds w/o warnings. I am giving a positive review to Franco's changes. I let Franco change the status of the ticket since I posted the last patch.",
    "created_at": "2009-09-17T18:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57031",
    "user": "@seblabbe"
}
```

I just added a patch that removes two lines now useless after Franco's changes.

All test passed in sage/combinat/words directory. Documentation builds w/o warnings. I am giving a positive review to Franco's changes. I let Franco change the status of the ticket since I posted the last patch.



---

archive/issue_comments_057032.json:
```json
{
    "body": "Thanks for catching those two lines S\u00e9bastien. Positive review.",
    "created_at": "2009-09-17T19:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57032",
    "user": "@saliola"
}
```

Thanks for catching those two lines Sébastien. Positive review.



---

archive/issue_comments_057033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-18T02:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57033",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057034.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6903_word_improve_constructor-sl.patch`\n2. `trac_6903_reviewer_patch_1.patch`\n3. `trac_6903_reviewer_patch_2.patch`\n4. `trac_6903_review_3-sl.patch`",
    "created_at": "2009-09-18T02:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6903#issuecomment-57034",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6903_word_improve_constructor-sl.patch`
2. `trac_6903_reviewer_patch_1.patch`
3. `trac_6903_reviewer_patch_2.patch`
4. `trac_6903_review_3-sl.patch`
