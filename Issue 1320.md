# Issue 1320: [graphs] planarity testing

archive/issues_001320.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  bober\n\nKeywords: graphs\n\nFrom Chris Godsil's wishlist.\n\n\n```\n>>> Someone is eventually going to ask for a routine to test for planarity. I\n>>> believe that there are good ones in existence, but it's going to be\n>>> hard to get\n>>> a good one with an open source licence.\n>> The nauty README has this to say about the new planarity testing feature:\n>> \"New program planarg to test for planarity and find planar embeddings:\n>> planarg -help for details. The planarity code was written by Paulette\n>> Lieby for the Magma project and used with permission.\"\n>>\n>> Does anyone know Paulette Lieby? Can we ask about releasing the code\n>> under GPL? It looks like the source has now been released as a part of\n>> nauty.\n> Emily Kirkman understands a linear time algorithm for testing for\n> planarity. There is one in BOOST, which is GPL, and has been nominated\n> for inclusion in Sage several times.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1320\n\n",
    "created_at": "2007-11-28T20:08:11Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[graphs] planarity testing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1320",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

CC:  bober

Keywords: graphs

From Chris Godsil's wishlist.


```
>>> Someone is eventually going to ask for a routine to test for planarity. I
>>> believe that there are good ones in existence, but it's going to be
>>> hard to get
>>> a good one with an open source licence.
>> The nauty README has this to say about the new planarity testing feature:
>> "New program planarg to test for planarity and find planar embeddings:
>> planarg -help for details. The planarity code was written by Paulette
>> Lieby for the Magma project and used with permission."
>>
>> Does anyone know Paulette Lieby? Can we ask about releasing the code
>> under GPL? It looks like the source has now been released as a part of
>> nauty.
> Emily Kirkman understands a linear time algorithm for testing for
> planarity. There is one in BOOST, which is GPL, and has been nominated
> for inclusion in Sage several times.
```



Issue created by migration from https://trac.sagemath.org/ticket/1320





---

archive/issue_comments_008373.json:
```json
{
    "body": "I plan to begin implementing the Boyer-Myrvold linear time planar test/embedding algorithm right after autumn quarter finals.  (Dec 13th).  It should be available in early January.",
    "created_at": "2007-11-30T03:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8373",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

I plan to begin implementing the Boyer-Myrvold linear time planar test/embedding algorithm right after autumn quarter finals.  (Dec 13th).  It should be available in early January.



---

archive/issue_comments_008374.json:
```json
{
    "body": "Changing assignee from @mwhansen to ekirkman.",
    "created_at": "2007-11-30T03:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8374",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Changing assignee from @mwhansen to ekirkman.



---

archive/issue_comments_008375.json:
```json
{
    "body": "Changing keywords from \"graphs\" to \"\".",
    "created_at": "2007-12-17T15:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8375",
    "user": "https://github.com/rlmill"
}
```

Changing keywords from "graphs" to "".



---

archive/issue_comments_008376.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8376",
    "user": "https://github.com/rlmill"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_008377.json:
```json
{
    "body": "Attachment [planarity.hg](tarball://root/attachments/some-uuid/ticket1320/planarity.hg) by @rlmill created at 2008-02-28 02:27:22",
    "created_at": "2008-02-28T02:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8377",
    "user": "https://github.com/rlmill"
}
```

Attachment [planarity.hg](tarball://root/attachments/some-uuid/ticket1320/planarity.hg) by @rlmill created at 2008-02-28 02:27:22



---

archive/issue_comments_008378.json:
```json
{
    "body": "Hi, I had a single, easy to fix merge conflict:\n\n```\n<<<<<<< /scratch/mabshoff/release-cycle/sage-2.10.3.rc0/devel/sage-main/sage/graphs/graph.py.orig.1734827483\nfrom sage.graphs.graph_coloring import chromatic_number, chromatic_polynomial\n=======\nfrom sage.rings.rational import Rational\n```\n\nThe above was caused by the work on the chromatic number and chromatic polynomial by Tom.\n||||||| /tmp/graph.py~base.vsk2R5\nCheers,\n\nMichael",
    "created_at": "2008-02-28T06:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8378",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi, I had a single, easy to fix merge conflict:

```
<<<<<<< /scratch/mabshoff/release-cycle/sage-2.10.3.rc0/devel/sage-main/sage/graphs/graph.py.orig.1734827483
from sage.graphs.graph_coloring import chromatic_number, chromatic_polynomial
=======
from sage.rings.rational import Rational
```

The above was caused by the work on the chromatic number and chromatic polynomial by Tom.
||||||| /tmp/graph.py~base.vsk2R5
Cheers,

Michael



---

archive/issue_comments_008379.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T06:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8379",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_008380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T06:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1320#issuecomment-8380",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
