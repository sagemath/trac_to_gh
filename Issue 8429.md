# Issue 8429: Split word.py file into 4 files

archive/issues_008429.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  abmasse\n\nThe file `word.py` is getting very huge and forces one to create new classes inside of it (see below for explanation) which will get the file `word.py` even more huge in the future...\n\nIf a file contains the following :\n\n\n```\n#file1.py\nclass A:\n    #huge class\n    pass\nclass C(A):\n    #huge class\n    pass\n```\n \n\none can not create a new class between A and C in another file (because of loops of import) :\n\n\n```\n#file1.py\nclass A:\n    #huge class\n    pass\nfrom file2 import B\nclass C(B):\n    #huge class\n    pass\n```\n \n\n\n```\n#file2.py\nfrom file1 import A\nclass B(A)\n    #large intermediate class\n    pass\n```\n\n\nSo the solution is either to put everything in the same file or to put everything in different files. In this case, I choose the last solution because `word.py` is getting huge.\n\nThis ticket removes `Word_class`, `FiniteWord_class` and `InfiniteWord_class` from `word.py` and put them in new files called respectively `abstrac_word.py`, `finite_word.py` and `infinite_word.py`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8429\n\n",
    "created_at": "2010-03-03T18:18:23Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Split word.py file into 4 files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8429",
    "user": "@seblabbe"
}
```
Assignee: sage-combinat

CC:  abmasse

The file `word.py` is getting very huge and forces one to create new classes inside of it (see below for explanation) which will get the file `word.py` even more huge in the future...

If a file contains the following :


```
#file1.py
class A:
    #huge class
    pass
class C(A):
    #huge class
    pass
```
 

one can not create a new class between A and C in another file (because of loops of import) :


```
#file1.py
class A:
    #huge class
    pass
from file2 import B
class C(B):
    #huge class
    pass
```
 


```
#file2.py
from file1 import A
class B(A)
    #large intermediate class
    pass
```


So the solution is either to put everything in the same file or to put everything in different files. In this case, I choose the last solution because `word.py` is getting huge.

This ticket removes `Word_class`, `FiniteWord_class` and `InfiniteWord_class` from `word.py` and put them in new files called respectively `abstrac_word.py`, `finite_word.py` and `infinite_word.py`.


Issue created by migration from https://trac.sagemath.org/ticket/8429





---

archive/issue_comments_075567.json:
```json
{
    "body": "I will post a patch as soon as #8418 gets a positive review, because the patch will depend on it.",
    "created_at": "2010-03-03T18:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75567",
    "user": "@seblabbe"
}
```

I will post a patch as soon as #8418 gets a positive review, because the patch will depend on it.



---

archive/issue_comments_075568.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-06T13:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75568",
    "user": "@seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075569.json:
```json
{
    "body": "Attachment [trac_8429_split_word-sl.patch](tarball://root/attachments/some-uuid/ticket8429/trac_8429_split_word-sl.patch) by @seblabbe created at 2010-03-06 14:32:29\n\nDepends on many tickets already merged in 4.3.4.alpha1",
    "created_at": "2010-03-06T14:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75569",
    "user": "@seblabbe"
}
```

Attachment [trac_8429_split_word-sl.patch](tarball://root/attachments/some-uuid/ticket8429/trac_8429_split_word-sl.patch) by @seblabbe created at 2010-03-06 14:32:29

Depends on many tickets already merged in 4.3.4.alpha1



---

archive/issue_comments_075570.json:
```json
{
    "body": "I tested S\u00e9bastien's patch after having applied many tickets of the sage-combinat server. Here is the list\n\n#7420 #7420 #7421 #7976 #7976 #7921 #7921 #7938 #8028 #8001 #8001 #5524 #8095 #8200 #8044 #8093 #8093 #8140 #8140 #8140 #6775 #8186 #8186 #8120 #7978 #8127 #8127 #8215 #8154 #8250 #8250 #8224 #8223 #8232 #8259 #8259 #8187 #8187 #8227 #8227 #8268 #8268 #8289 #8289 #8318 #8313 #7520 #7619 #8294 #8276 #8276 #8276 #8273 #8273 #8367 #8266 #8266 #8266 #8233 #8353 #8353 #8418 #8418 #8418 #8296 #7448 #8475 #8422 #8429\n\nAll tests passed, and the documentation buils correctly.",
    "created_at": "2010-03-08T10:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75570",
    "user": "abmasse"
}
```

I tested Sébastien's patch after having applied many tickets of the sage-combinat server. Here is the list

#7420 #7420 #7421 #7976 #7976 #7921 #7921 #7938 #8028 #8001 #8001 #5524 #8095 #8200 #8044 #8093 #8093 #8140 #8140 #8140 #6775 #8186 #8186 #8120 #7978 #8127 #8127 #8215 #8154 #8250 #8250 #8224 #8223 #8232 #8259 #8259 #8187 #8187 #8227 #8227 #8268 #8268 #8289 #8289 #8318 #8313 #7520 #7619 #8294 #8276 #8276 #8276 #8273 #8273 #8367 #8266 #8266 #8266 #8233 #8353 #8353 #8418 #8418 #8418 #8296 #7448 #8475 #8422 #8429

All tests passed, and the documentation buils correctly.



---

archive/issue_comments_075571.json:
```json
{
    "body": "Changing assignee from sage-combinat to abmasse.",
    "created_at": "2010-03-08T10:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75571",
    "user": "abmasse"
}
```

Changing assignee from sage-combinat to abmasse.



---

archive/issue_comments_075572.json:
```json
{
    "body": "There seems to be three patches that have not been merged to sage-4.3.4 yet, but I don't think they are needed for #8429. Here is the list:\n\n#8475, #8313, #8296.\n\nI shouldn't have included #8429 as it is this current patch. I'll check for the three above patches if they are a problem.",
    "created_at": "2010-03-08T10:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75572",
    "user": "abmasse"
}
```

There seems to be three patches that have not been merged to sage-4.3.4 yet, but I don't think they are needed for #8429. Here is the list:

#8475, #8313, #8296.

I shouldn't have included #8429 as it is this current patch. I'll check for the three above patches if they are a problem.



---

archive/issue_comments_075573.json:
```json
{
    "body": "Sorry, remove #8313 from the list, that was a typo. So the only tickets to look at are #8475 and #8296.",
    "created_at": "2010-03-08T10:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75573",
    "user": "abmasse"
}
```

Sorry, remove #8313 from the list, that was a typo. So the only tickets to look at are #8475 and #8296.



---

archive/issue_comments_075574.json:
```json
{
    "body": "Replying to [comment:5 abmasse]:\n> Sorry, remove #8313 from the list, that was a typo. So the only tickets to look at are #8475 and #8296.\n\nAlexandre, I just moved the patch `trac_8429_split_word-sl.patch` before #8475 and #8296 in the sage-combinat tree. I can confirm that they commute so that this ticket doesn't \"mercurialy\" depend on #8296 and #8475.",
    "created_at": "2010-03-08T11:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75574",
    "user": "@seblabbe"
}
```

Replying to [comment:5 abmasse]:
> Sorry, remove #8313 from the list, that was a typo. So the only tickets to look at are #8475 and #8296.

Alexandre, I just moved the patch `trac_8429_split_word-sl.patch` before #8475 and #8296 in the sage-combinat tree. I can confirm that they commute so that this ticket doesn't "mercurialy" depend on #8296 and #8475.



---

archive/issue_comments_075575.json:
```json
{
    "body": "I restested the patch after having applied all above listed patches except #8296 and #8475 and all tests passed ! The documentation builds fine too, so I give this patch a positive review. It is very unlikely that another patch could be in conflict with this one.",
    "created_at": "2010-03-08T13:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75575",
    "user": "abmasse"
}
```

I restested the patch after having applied all above listed patches except #8296 and #8475 and all tests passed ! The documentation builds fine too, so I give this patch a positive review. It is very unlikely that another patch could be in conflict with this one.



---

archive/issue_comments_075576.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-08T13:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75576",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75577",
    "user": "@jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_075578.json:
```json
{
    "body": "Merged \"trac_8429_split_word-sl.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8429#issuecomment-75578",
    "user": "@jhpalmieri"
}
```

Merged "trac_8429_split_word-sl.patch" into 4.4.alpha0.
