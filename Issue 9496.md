# Issue 9496: Crypto lattice basis generator

archive/issues_009496.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: cryptography, lattices\n\nWe introduce a generator for different types of integral lattice bases of row vectors relevant in cryptography.\n\nIt offers more variety and better usability than fplll's generator.\n\nContacts:\nRichard Lindner <rlindner`@`cdc.informatik.tu-darmstadt.de>\nMichael Schneider <mischnei`@`cdc.informatik.tu-darmstadt.de>\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9496\n\n",
    "created_at": "2010-07-14T13:36:13Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "title": "Crypto lattice basis generator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9496",
    "user": "rlindner"
}
```
Assignee: mvngu

Keywords: cryptography, lattices

We introduce a generator for different types of integral lattice bases of row vectors relevant in cryptography.

It offers more variety and better usability than fplll's generator.

Contacts:
Richard Lindner <rlindner`@`cdc.informatik.tu-darmstadt.de>
Michael Schneider <mischnei`@`cdc.informatik.tu-darmstadt.de>


Issue created by migration from https://trac.sagemath.org/ticket/9496





---

archive/issue_comments_091173.json:
```json
{
    "body": "I think overall it looks fine, some small points:\n\n* I think the function is too specialised to be in the main namespace, how about crypto.generate_lattice ?\n* Could you break lines around 80 characters?\n* One shouldn't need to pass a seed, but instead just change the seed with set_random_seed()\n* Id' rename ntl_flag to ntl",
    "created_at": "2010-07-14T20:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91173",
    "user": "malb"
}
```

I think overall it looks fine, some small points:

* I think the function is too specialised to be in the main namespace, how about crypto.generate_lattice ?
* Could you break lines around 80 characters?
* One shouldn't need to pass a seed, but instead just change the seed with set_random_seed()
* Id' rename ntl_flag to ntl



---

archive/issue_comments_091174.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-14T22:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91174",
    "user": "malb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_091175.json:
```json
{
    "body": "Specifically:\n\n* function is now: sage.crypto.gen_lattice()\n* lines are broken at 79 chars\n* set_random_seed() is honored, but option to use seed remains\n* _flag indicator is removed",
    "created_at": "2010-07-15T14:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91175",
    "user": "rlindner"
}
```

Specifically:

* function is now: sage.crypto.gen_lattice()
* lines are broken at 79 chars
* set_random_seed() is honored, but option to use seed remains
* _flag indicator is removed



---

archive/issue_comments_091176.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-15T14:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91176",
    "user": "rlindner"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091177.json:
```json
{
    "body": "Hi, I'm having trouble applying your patch on top of the other, many hunks fail. Did you forget to include an intermediate patch (14533?)? Or can you provide a patch with everything rolled into one patch?",
    "created_at": "2010-07-15T15:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91177",
    "user": "malb"
}
```

Hi, I'm having trouble applying your patch on top of the other, many hunks fail. Did you forget to include an intermediate patch (14533?)? Or can you provide a patch with everything rolled into one patch?



---

archive/issue_comments_091178.json:
```json
{
    "body": "Candidate #2",
    "created_at": "2010-07-15T16:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91178",
    "user": "rlindner"
}
```

Candidate #2



---

archive/issue_comments_091179.json:
```json
{
    "body": "Attachment [14532.patch](tarball://root/attachments/some-uuid/ticket9496/14532.patch) by rlindner created at 2010-07-15 16:28:18\n\nI recreated 14532.patch to include all changes and could not delete the other file, so I did the next best thing.",
    "created_at": "2010-07-15T16:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91179",
    "user": "rlindner"
}
```

Attachment [14532.patch](tarball://root/attachments/some-uuid/ticket9496/14532.patch) by rlindner created at 2010-07-15 16:28:18

I recreated 14532.patch to include all changes and could not delete the other file, so I did the next best thing.



---

archive/issue_comments_091180.json:
```json
{
    "body": "apply after other patch",
    "created_at": "2010-07-15T18:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91180",
    "user": "malb"
}
```

apply after other patch



---

archive/issue_comments_091181.json:
```json
{
    "body": "Attachment [trac_9496_referee.patch](tarball://root/attachments/some-uuid/ticket9496/trac_9496_referee.patch) by malb created at 2010-07-15 18:41:29\n\nI've just uploaded a referee patch which should be applied on top of your patch. It fixes a few formating issues I probably could do quicker than you.\u00a0\n\nNote that this means that I cannot give this ticket a positive review anymore, I cannot referee my own patch. However, since I sign off on your patch iff my patch is applied afterwards, you can review my patch, i.e. accept my changes. Of course, if you have anything to criticise go for it!",
    "created_at": "2010-07-15T18:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91181",
    "user": "malb"
}
```

Attachment [trac_9496_referee.patch](tarball://root/attachments/some-uuid/ticket9496/trac_9496_referee.patch) by malb created at 2010-07-15 18:41:29

I've just uploaded a referee patch which should be applied on top of your patch. It fixes a few formating issues I probably could do quicker than you. 

Note that this means that I cannot give this ticket a positive review anymore, I cannot referee my own patch. However, since I sign off on your patch iff my patch is applied afterwards, you can review my patch, i.e. accept my changes. Of course, if you have anything to criticise go for it!



---

archive/issue_comments_091182.json:
```json
{
    "body": "btw. this is how the result looks like:\n\nhttp://sage.math.washington.edu/home/malb/scratch_sage/sage-4.4/devel/sage/doc/output/html/en/reference/sage/crypto/lattice.html",
    "created_at": "2010-07-15T19:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91182",
    "user": "malb"
}
```

btw. this is how the result looks like:

http://sage.math.washington.edu/home/malb/scratch_sage/sage-4.4/devel/sage/doc/output/html/en/reference/sage/crypto/lattice.html



---

archive/issue_comments_091183.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-15T19:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91183",
    "user": "rlindner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091184.json:
```json
{
    "body": "Looks so much better, thanks!",
    "created_at": "2010-07-15T19:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91184",
    "user": "rlindner"
}
```

Looks so much better, thanks!



---

archive/issue_comments_091185.json:
```json
{
    "body": "I've updated the Author(s) and Reviewer(s) fields with guesses.  Please correct them, if I'm wrong.",
    "created_at": "2010-07-20T10:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91185",
    "user": "mpatel"
}
```

I've updated the Author(s) and Reviewer(s) fields with guesses.  Please correct them, if I'm wrong.



---

archive/issue_comments_091186.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T10:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91186",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_091187.json:
```json
{
    "body": "I didn't do much",
    "created_at": "2010-07-20T10:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91187",
    "user": "malb"
}
```

I didn't do much



---

archive/issue_comments_091188.json:
```json
{
    "body": "Attachment [14604.patch](tarball://root/attachments/some-uuid/ticket9496/14604.patch) by rlindner created at 2010-07-20 15:14:41\n\nAn addtional patch to fix some bugs in the dual lattice generation/ description. Candidate 3",
    "created_at": "2010-07-20T15:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91188",
    "user": "rlindner"
}
```

Attachment [14604.patch](tarball://root/attachments/some-uuid/ticket9496/14604.patch) by rlindner created at 2010-07-20 15:14:41

An addtional patch to fix some bugs in the dual lattice generation/ description. Candidate 3



---

archive/issue_comments_091189.json:
```json
{
    "body": "Please open a new ticket for your bugfix since this ticket is already closed. Btw.:\n\n\n```\nsage: A\n[   1    5   -3    1]\n[-290  -14    1    1]\n[ -13   -6    6   -1]\n[  15   -1    3   62]\n\nsage: A.matrix_from_rows(range(A.nrows())[::-1])\n[  15   -1    3   62]\n[ -13   -6    6   -1]\n[-290  -14    1    1]\n[   1    5   -3    1]\n\n```\n",
    "created_at": "2010-07-21T08:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9496#issuecomment-91189",
    "user": "malb"
}
```

Please open a new ticket for your bugfix since this ticket is already closed. Btw.:


```
sage: A
[   1    5   -3    1]
[-290  -14    1    1]
[ -13   -6    6   -1]
[  15   -1    3   62]

sage: A.matrix_from_rows(range(A.nrows())[::-1])
[  15   -1    3   62]
[ -13   -6    6   -1]
[-290  -14    1    1]
[   1    5   -3    1]

```

