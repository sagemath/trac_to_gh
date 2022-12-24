# Issue 5939: typo in g.automorphism_group documentation, for g a graph; also partition parameter isn't tested anywhere in the docstring

archive/issues_005939.json:
```json
{
    "body": "Assignee: @rlmill\n\nThere is a typo in the docstring for the graph automorphism function:\n\n\n```\n``translation`` - if True, then output includes a a\n           dictionary translating from keys == vertices to entries == elements\n           of 1,2,...,n (since permutation groups can currently only act on\n           positive integers).\n```\n\n\nNotice that it says \"includes a a\" (a appears twice). \n\nAlso, the doctests in that docstring do not test the partition parameter at all, and it seems to me that would be a very important parameter to illustrate, especially given that the docstring starts {{{\n        Returns the largest subgroup of the automorphism group of the\n        (di)graph whose orbit partition is finer than the partition given.\n}}}\nwhich suggests that the most important thing the reader should know is that the automorphism_group computes something associated to a partition.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5939\n\n",
    "created_at": "2009-04-29T16:26:04Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "typo in g.automorphism_group documentation, for g a graph; also partition parameter isn't tested anywhere in the docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5939",
    "user": "@williamstein"
}
```
Assignee: @rlmill

There is a typo in the docstring for the graph automorphism function:


```
``translation`` - if True, then output includes a a
           dictionary translating from keys == vertices to entries == elements
           of 1,2,...,n (since permutation groups can currently only act on
           positive integers).
```


Notice that it says "includes a a" (a appears twice). 

Also, the doctests in that docstring do not test the partition parameter at all, and it seems to me that would be a very important parameter to illustrate, especially given that the docstring starts {{{
        Returns the largest subgroup of the automorphism group of the
        (di)graph whose orbit partition is finer than the partition given.
}}}
which suggests that the most important thing the reader should know is that the automorphism_group computes something associated to a partition.

Issue created by migration from https://trac.sagemath.org/ticket/5939





---

archive/issue_comments_046954.json:
```json
{
    "body": "Attachment [trac_5939.patch](tarball://root/attachments/some-uuid/ticket5939/trac_5939.patch) by ekirkman created at 2009-07-18 23:46:45",
    "created_at": "2009-07-18T23:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5939#issuecomment-46954",
    "user": "ekirkman"
}
```

Attachment [trac_5939.patch](tarball://root/attachments/some-uuid/ticket5939/trac_5939.patch) by ekirkman created at 2009-07-18 23:46:45



---

archive/issue_comments_046955.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T14:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5939#issuecomment-46955",
    "user": "mvngu"
}
```

Resolution: fixed
