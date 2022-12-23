# Issue 2171: [with patch; needs review] followup to #2169 -- (magma/sage interface) some further optimizations and fixes

archive/issues_002171.json:
```json
{
    "body": "Assignee: was\n\nApply the patches from #2169, then apply both these patches.  To test do\n\n```\nsage -t --optional SAGE_ROOT/devel/sage/sage/interfaces/magma.py\n```\n\n\nConversion of Magma matrices over ZZ back to Sage should also be much faster now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2171\n\n",
    "created_at": "2008-02-15T08:11:04Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] followup to #2169 -- (magma/sage interface) some further optimizations and fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2171",
    "user": "was"
}
```
Assignee: was

Apply the patches from #2169, then apply both these patches.  To test do

```
sage -t --optional SAGE_ROOT/devel/sage/sage/interfaces/magma.py
```


Conversion of Magma matrices over ZZ back to Sage should also be much faster now.

Issue created by migration from https://trac.sagemath.org/ticket/2171





---

archive/issue_comments_014249.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-15T08:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14249",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_014250.json:
```json
{
    "body": "Attachment\n\nApply all the attached files -- the sage- ones to hg_sage and the extcode ones to hg_extcode.",
    "created_at": "2008-02-15T09:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14250",
    "user": "was"
}
```

Attachment

Apply all the attached files -- the sage- ones to hg_sage and the extcode ones to hg_extcode.



---

archive/issue_comments_014251.json:
```json
{
    "body": "I get a reject with http://sagetrac.org/sage_trac/attachment/ticket/2171/sage-trac2171.patch on rc1.  It looks like it is depending on a patch that isn't there.  This is the failure:\n\n\n```\n--- expect.py\n+++ expect.py\n@@ -860,10 +860,15 @@ If this all works, you can then make cal\n         return self.eval(var)\n \n     def get_using_file(self, var):\n-        \"\"\"\n+        r\"\"\"\n         Return the string representation of the variable var in self\n         using a file.  Use this if var has a huge string\n         representation.  It'll be way faster.\n+\n+        WARNING: In fact unless a special derived class implements\n+        this, it will \\emph{not} be any faster.  This is the case for\n+        this class if you're reading it through introspection and\n+        seeing this.\n         \"\"\"\n         return self.get(var)\n```\n\n\nand this is expect.py in rc1:\n\n\n```\n    def get_using_file(self, var):\n        return self.get(var)\n```\n",
    "created_at": "2008-03-05T00:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14251",
    "user": "mhansen"
}
```

I get a reject with http://sagetrac.org/sage_trac/attachment/ticket/2171/sage-trac2171.patch on rc1.  It looks like it is depending on a patch that isn't there.  This is the failure:


```
--- expect.py
+++ expect.py
@@ -860,10 +860,15 @@ If this all works, you can then make cal
         return self.eval(var)
 
     def get_using_file(self, var):
-        """
+        r"""
         Return the string representation of the variable var in self
         using a file.  Use this if var has a huge string
         representation.  It'll be way faster.
+
+        WARNING: In fact unless a special derived class implements
+        this, it will \emph{not} be any faster.  This is the case for
+        this class if you're reading it through introspection and
+        seeing this.
         """
         return self.get(var)
```


and this is expect.py in rc1:


```
    def get_using_file(self, var):
        return self.get(var)
```




---

archive/issue_comments_014252.json:
```json
{
    "body": "The patch that this code depends on is attached to trac #2120. I guess this will have to wait until that patch is ready to go? Or should we pull over that part of the patch to this ticket so we can get it merged? William, what's the status of the Maple ticket?",
    "created_at": "2008-05-10T11:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14252",
    "user": "craigcitro"
}
```

The patch that this code depends on is attached to trac #2120. I guess this will have to wait until that patch is ready to go? Or should we pull over that part of the patch to this ticket so we can get it merged? William, what's the status of the Maple ticket?



---

archive/issue_comments_014253.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14253",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_014254.json:
```json
{
    "body": "Craig, \n\ncan you review this? It has been potentially bitrotting for a long, long time :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T05:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14254",
    "user": "mabshoff"
}
```

Craig, 

can you review this? It has been potentially bitrotting for a long, long time :)

Cheers,

Michael



---

archive/issue_comments_014255.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-24T03:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14255",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_014256.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-24T03:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14256",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_014257.json:
```json
{
    "body": "I rebased these patches against 3.2.alpha0 and got rid of the dependence on #2120.  This should be easy to apply and go into sage-3.2.",
    "created_at": "2008-10-24T03:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14257",
    "user": "was"
}
```

I rebased these patches against 3.2.alpha0 and got rid of the dependence on #2120.  This should be easy to apply and go into sage-3.2.



---

archive/issue_comments_014258.json:
```json
{
    "body": "In sage-trac2171-part1.patch there is still a change to sage/interfaces/maple.py. I will delete that hunk and test the patch. Other than that I expect a positive review assuming the doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T02:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14258",
    "user": "mabshoff"
}
```

In sage-trac2171-part1.patch there is still a change to sage/interfaces/maple.py. I will delete that hunk and test the patch. Other than that I expect a positive review assuming the doctests pass.

Cheers,

Michael



---

archive/issue_comments_014259.json:
```json
{
    "body": "For the patch **extcode-trac2171-part2.patch**, here's a possible documentation fix:\n\n```\n-{Conver the ring of integers to Sage.}\n+{Convert the ring of integers to Sage.}\n```\n",
    "created_at": "2008-10-27T03:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14259",
    "user": "mvngu"
}
```

For the patch **extcode-trac2171-part2.patch**, here's a possible documentation fix:

```
-{Conver the ring of integers to Sage.}
+{Convert the ring of integers to Sage.}
```




---

archive/issue_comments_014260.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T04:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14260",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_014261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T04:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14261",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014262.json:
```json
{
    "body": "Merged sage-trac2171-part1.patch and sage-trac2171-part2.patch in Sage 3.2.alpha1",
    "created_at": "2008-10-27T04:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14262",
    "user": "mabshoff"
}
```

Merged sage-trac2171-part1.patch and sage-trac2171-part2.patch in Sage 3.2.alpha1



---

archive/issue_comments_014263.json:
```json
{
    "body": "Oops, I didn't merge extcode-trac2171.patch and extcode-trac2171-part2.patch. Those two patches have been merged in Sage 3.2.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T23:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2171#issuecomment-14263",
    "user": "mabshoff"
}
```

Oops, I didn't merge extcode-trac2171.patch and extcode-trac2171-part2.patch. Those two patches have been merged in Sage 3.2.alpha2.

Cheers,

Michael
