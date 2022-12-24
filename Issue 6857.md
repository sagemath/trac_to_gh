# Issue 6857: [with patch, needs review] in automorphism_group, orbits=True does not translate vertices back

archive/issues_006857.json:
```json
{
    "body": "Assignee: @rlmill\n\nReported by Chris Godsil\n\nIssue created by migration from https://trac.sagemath.org/ticket/6857\n\n",
    "created_at": "2009-09-02T01:00:23Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] in automorphism_group, orbits=True does not translate vertices back",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6857",
    "user": "@rlmill"
}
```
Assignee: @rlmill

Reported by Chris Godsil

Issue created by migration from https://trac.sagemath.org/ticket/6857





---

archive/issue_comments_056552.json:
```json
{
    "body": "Attachment [trac_6857.patch](tarball://root/attachments/some-uuid/ticket6857/trac_6857.patch) by @rlmill created at 2009-09-02 01:02:09",
    "created_at": "2009-09-02T01:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6857#issuecomment-56552",
    "user": "@rlmill"
}
```

Attachment [trac_6857.patch](tarball://root/attachments/some-uuid/ticket6857/trac_6857.patch) by @rlmill created at 2009-09-02 01:02:09



---

archive/issue_comments_056553.json:
```json
{
    "body": "Applies fines, does its job. Positive review !\n\nNot related to this patch, I found out testing things some *really unimportant* error :\n\n\n```\nsage: g.automorphism_group(return_group=False)\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/user/ncohen/home/.sage/temp/rebelote.inria.fr/22721/_user_ncohen_home__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in automorphism_group(self, partition, translation, verbosity, edge_labels, order, return_group, orbits)\n   8462         # A Python switch statement!\n   8463         return { 0: None,\n-> 8464                  1: output[0],\n   8465                  2: tuple(output),\n   8466                  3: tuple(output),\n\nIndexError: list index out of range \n```\n\n\nThis comes from the fact that in this configuration of arguments, the function is expected to ... do nothing ;-)\n\nAt the end of the function, the code already expects this eventuality and reads :\n\n\n```\n        # A Python switch statement!\n        return { 0: None,\n                 1: output[0],\n                 2: tuple(output),\n                 3: tuple(output),\n                 4: tuple(output)\n               }[len(output)]\n```\n\nI knew nothing about such things in Python and I am glad I read it. But the key 0: None does not behave as expected : it behaves as if there was NO key \"0\" in the dictionary and when len(output) equals 0 there is an error because of that... It can be fixed pretty easily this way :\n\n\n```\n        # A Python switch statement!\n        return { 1: output[0],\n                 2: tuple(output),\n                 3: tuple(output),\n                 4: tuple(output)\n               }[len(output)] if len(output)>0 else None\n```\n\n\nCould it be possible to include discreetely it in your patch ? It does not seem necessary to create a ticket just for this ;-)\n\nNathann",
    "created_at": "2009-09-06T14:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6857#issuecomment-56553",
    "user": "@nathanncohen"
}
```

Applies fines, does its job. Positive review !

Not related to this patch, I found out testing things some *really unimportant* error :


```
sage: g.automorphism_group(return_group=False)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/user/ncohen/home/.sage/temp/rebelote.inria.fr/22721/_user_ncohen_home__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in automorphism_group(self, partition, translation, verbosity, edge_labels, order, return_group, orbits)
   8462         # A Python switch statement!
   8463         return { 0: None,
-> 8464                  1: output[0],
   8465                  2: tuple(output),
   8466                  3: tuple(output),

IndexError: list index out of range 
```


This comes from the fact that in this configuration of arguments, the function is expected to ... do nothing ;-)

At the end of the function, the code already expects this eventuality and reads :


```
        # A Python switch statement!
        return { 0: None,
                 1: output[0],
                 2: tuple(output),
                 3: tuple(output),
                 4: tuple(output)
               }[len(output)]
```

I knew nothing about such things in Python and I am glad I read it. But the key 0: None does not behave as expected : it behaves as if there was NO key "0" in the dictionary and when len(output) equals 0 there is an error because of that... It can be fixed pretty easily this way :


```
        # A Python switch statement!
        return { 1: output[0],
                 2: tuple(output),
                 3: tuple(output),
                 4: tuple(output)
               }[len(output)] if len(output)>0 else None
```


Could it be possible to include discreetely it in your patch ? It does not seem necessary to create a ticket just for this ;-)

Nathann



---

archive/issue_comments_056554.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-07T18:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6857#issuecomment-56554",
    "user": "mvngu"
}
```

Resolution: fixed
