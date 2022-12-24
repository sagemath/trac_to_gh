# Issue 5487: Content function for tableaux

archive/issues_005487.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nKeywords: tableaux content\n\nSimple patch adding a content function for tableaux to tableau.py.\n\n[Mostly just a test to see if I can push a patch to the combinat server.]\n\n---------\n\n```\ndiff -r c6382e76a5e5 sage/combinat/tableau.py\n--- a/sage/combinat/tableau.py  Thu Mar 12 01:07:21 2009 +1100\n+++ b/sage/combinat/tableau.py  Thu Mar 12 01:07:52 2009 +1100\n@@ -480,6 +480,21 @@\n             s += [ (i,j) for j in range(len(self[i])) ]\n         return s\n \n+    def content(self, k):\n+        \"\"\"\n+        Returns the content of <k> in <self>. That is, if <k> appears in\n+        row r and column c of the tableau <self> then we return c-r.\n+\n+        EXAMPLES:\n+            sage: Tableau([[1,2],[3,4]]).content(3)\n+            -1\n+\n+        \"\"\"\n+        for r in range(len(self)):\n+          for c in range(len(self[r])):\n+            if self[r][c]==k: return c-r\n+        return False\n+\n     def k_weight(self, k):\n         \"\"\"\n         Returns the k-weight of self.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5487\n\n",
    "created_at": "2009-03-11T14:12:29Z",
    "labels": [
        "combinatorics",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Content function for tableaux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5487",
    "user": "andrew.mathas"
}
```
Assignee: mhansen

CC:  sage-combinat

Keywords: tableaux content

Simple patch adding a content function for tableaux to tableau.py.

[Mostly just a test to see if I can push a patch to the combinat server.]

---------

```
diff -r c6382e76a5e5 sage/combinat/tableau.py
--- a/sage/combinat/tableau.py  Thu Mar 12 01:07:21 2009 +1100
+++ b/sage/combinat/tableau.py  Thu Mar 12 01:07:52 2009 +1100
@@ -480,6 +480,21 @@
             s += [ (i,j) for j in range(len(self[i])) ]
         return s
 
+    def content(self, k):
+        """
+        Returns the content of <k> in <self>. That is, if <k> appears in
+        row r and column c of the tableau <self> then we return c-r.
+
+        EXAMPLES:
+            sage: Tableau([[1,2],[3,4]]).content(3)
+            -1
+
+        """
+        for r in range(len(self)):
+          for c in range(len(self[r])):
+            if self[r][c]==k: return c-r
+        return False
+
     def k_weight(self, k):
         """
         Returns the k-weight of self.
```


Issue created by migration from https://trac.sagemath.org/ticket/5487





---

archive/issue_comments_042585.json:
```json
{
    "body": "A few comments:\n\n0. Patches should be included as attachments.\n\n1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?\n\n```\nsage: Tableau([[3,3],[3,3]])\n[[3, 3], [3, 3]]\n```\n\n\n2. In case k does not appear in the tableau, perhaps it is better to raise an error?\n\n3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section.",
    "created_at": "2009-03-12T12:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42585",
    "user": "saliola"
}
```

A few comments:

0. Patches should be included as attachments.

1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?

```
sage: Tableau([[3,3],[3,3]])
[[3, 3], [3, 3]]
```


2. In case k does not appear in the tableau, perhaps it is better to raise an error?

3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section.



---

archive/issue_comments_042586.json:
```json
{
    "body": "Replying to [comment:1 saliola]:\n\n> 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?\n> {{{\n> sage: Tableau([[3,3],[3,3]])\n> [[3, 3], [3, 3]]\n> }}}\n\nThis is not exactly a tableau ! :-) I don't know if it's standard but there is a notion of content associated to semi-standard tableau. \n\n> 2. In case k does not appear in the tableau, perhaps it is better to raise an error?\n> \n> 3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section. \n\n4. I think parameters should be written ```n``` (raw sage code) instead of ``n`` (latex code) or `<n>` (no particular meaning in rest) see http://wiki.sagemath.org/combinat/HelpOnTheDoc",
    "created_at": "2009-03-12T23:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42586",
    "user": "hivert"
}
```

Replying to [comment:1 saliola]:

> 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?
> {{{
> sage: Tableau([[3,3],[3,3]])
> [[3, 3], [3, 3]]
> }}}

This is not exactly a tableau ! :-) I don't know if it's standard but there is a notion of content associated to semi-standard tableau. 

> 2. In case k does not appear in the tableau, perhaps it is better to raise an error?
> 
> 3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section. 

4. I think parameters should be written ```n``` (raw sage code) instead of ``n`` (latex code) or `<n>` (no particular meaning in rest) see http://wiki.sagemath.org/combinat/HelpOnTheDoc



---

archive/issue_comments_042587.json:
```json
{
    "body": "Replying to [comment:2 hivert]:\n> Replying to [comment:1 saliola]:\n> \n> > 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?\n\nWhen pushing this patch I described it as a content function on standard tableau and then added it to the Tableau class...I'll move it into the StandardTableau class and then all will be well.\n\nThe obvious \"generalization\" of the definition to semistandard tableau is used in the literature but writing the corresponding function is slightly cumbersome because in the classical case you add up the contents of all of nodes labelled k whereas for the q-analogue you add up the q-contents. Perhaps the nicest solution is to define\n\n```\ndef content(self, k, q=1):\n...\n```\n\nI have never used contents for tableaux which are not (semi)standard.\n\n> > 2. In case k does not appear in the tableau, perhaps it is better to raise an error?\n\nOK\n \n> > 3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section. \n> \n> 4. I think parameters should be written ```n``` (raw sage code) instead of ``n`` (latex code) or `<n>` (no particular meaning in rest) see http://wiki.sagemath.org/combinat/HelpOnTheDoc\n\nThanks.\n\nOne last question: is there an easy way to \"update\" the patch and push it back to the server? Or do I have to somehow delete this patch and then reapply?\n\nCheers,\nAndrew",
    "created_at": "2009-03-13T06:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42587",
    "user": "andrew.mathas"
}
```

Replying to [comment:2 hivert]:
> Replying to [comment:1 saliola]:
> 
> > 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?

When pushing this patch I described it as a content function on standard tableau and then added it to the Tableau class...I'll move it into the StandardTableau class and then all will be well.

The obvious "generalization" of the definition to semistandard tableau is used in the literature but writing the corresponding function is slightly cumbersome because in the classical case you add up the contents of all of nodes labelled k whereas for the q-analogue you add up the q-contents. Perhaps the nicest solution is to define

```
def content(self, k, q=1):
...
```

I have never used contents for tableaux which are not (semi)standard.

> > 2. In case k does not appear in the tableau, perhaps it is better to raise an error?

OK
 
> > 3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section. 
> 
> 4. I think parameters should be written ```n``` (raw sage code) instead of ``n`` (latex code) or `<n>` (no particular meaning in rest) see http://wiki.sagemath.org/combinat/HelpOnTheDoc

Thanks.

One last question: is there an easy way to "update" the patch and push it back to the server? Or do I have to somehow delete this patch and then reapply?

Cheers,
Andrew



---

archive/issue_comments_042588.json:
```json
{
    "body": "Changing assignee from mhansen to andrew.mathas.",
    "created_at": "2009-03-13T06:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42588",
    "user": "andrew.mathas"
}
```

Changing assignee from mhansen to andrew.mathas.



---

archive/issue_comments_042589.json:
```json
{
    "body": "Replying to [comment:3 andrew.mathas]:\n> Replying to [comment:2 hivert]:\n> > Replying to [comment:1 saliola]:\n> > \n> > > 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?\n> \n> When pushing this patch I described it as a content function on standard tableau and then added it to the Tableau class...I'll move it into the StandardTableau class and then all will be well.\n\nOne slight problem: there doesn't seem to be a StandardTableau or SemistandardTableau class, just a Tableau class. So you'll have to create it, which is not a big deal.\n\n> One last question: is there an easy way to \"update\" the patch and push it back to the server? Or do I have to somehow delete this patch and then reapply?\n\nIn you sage-combinat branch, you can type `hg qpop tableau-content-5487-AM.patch`, which will unapply all the patches up until you get to your patch. (Or you might have to qpush instead of qpop above depending on where you are in the stack.) Then you do your modifications. To save your modifications into the top patch (in this case, tableau-content-5487-AM.patch), you do `hg qrefresh`. To see which patch is at the top of your stack, use the command `hg qtop`. Once you are done with your modifications, you proceed as normal. That is: change into the patches directory, commit, then push.",
    "created_at": "2009-03-13T07:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42589",
    "user": "saliola"
}
```

Replying to [comment:3 andrew.mathas]:
> Replying to [comment:2 hivert]:
> > Replying to [comment:1 saliola]:
> > 
> > > 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?
> 
> When pushing this patch I described it as a content function on standard tableau and then added it to the Tableau class...I'll move it into the StandardTableau class and then all will be well.

One slight problem: there doesn't seem to be a StandardTableau or SemistandardTableau class, just a Tableau class. So you'll have to create it, which is not a big deal.

> One last question: is there an easy way to "update" the patch and push it back to the server? Or do I have to somehow delete this patch and then reapply?

In you sage-combinat branch, you can type `hg qpop tableau-content-5487-AM.patch`, which will unapply all the patches up until you get to your patch. (Or you might have to qpush instead of qpop above depending on where you are in the stack.) Then you do your modifications. To save your modifications into the top patch (in this case, tableau-content-5487-AM.patch), you do `hg qrefresh`. To see which patch is at the top of your stack, use the command `hg qtop`. Once you are done with your modifications, you proceed as normal. That is: change into the patches directory, commit, then push.



---

archive/issue_comments_042590.json:
```json
{
    "body": "I have moved the function into the StandardTableaux_n class and fixed the doc string problems.",
    "created_at": "2009-04-10T22:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42590",
    "user": "andrew.mathas"
}
```

I have moved the function into the StandardTableaux_n class and fixed the doc string problems.



---

archive/issue_comments_042591.json:
```json
{
    "body": "Dear Andrew,\n\nSorry for bothering you with this first simple patch but before giving a positive review I'd rather see the following first problem fixed. I leave these to you because I understand that you want test the patch workflow. If you want me to fix these please ask. \n\n1. I agree with Franco's first message: I'd rather raise an error than return False silently. Those `False` or `None` tends to crawl into the programs and to eventually trigger an error at the wrong place. You can always catch the exception if you want. I think `ValueError` is the correct exception (see the similar behavior for list below).\n\n2. I case you don't know, in python, when you have a list `l` the call `l.index(k)` either returns the first position of `k` if it is in the list or raise a\n\n```\nValueError: list.index(x): x not in list\n```\n\nmaybe it's worth using it ? \n\ncheers,\n\nFlorent",
    "created_at": "2009-04-13T10:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42591",
    "user": "hivert"
}
```

Dear Andrew,

Sorry for bothering you with this first simple patch but before giving a positive review I'd rather see the following first problem fixed. I leave these to you because I understand that you want test the patch workflow. If you want me to fix these please ask. 

1. I agree with Franco's first message: I'd rather raise an error than return False silently. Those `False` or `None` tends to crawl into the programs and to eventually trigger an error at the wrong place. You can always catch the exception if you want. I think `ValueError` is the correct exception (see the similar behavior for list below).

2. I case you don't know, in python, when you have a list `l` the call `l.index(k)` either returns the first position of `k` if it is in the list or raise a

```
ValueError: list.index(x): x not in list
```

maybe it's worth using it ? 

cheers,

Florent



---

archive/issue_comments_042592.json:
```json
{
    "body": "Attachment [tableau-content-5487-AM.patch](tarball://root/attachments/some-uuid/ticket5487/tableau-content-5487-AM.patch) by andrew.mathas created at 2009-04-13 15:30:42\n\nDear Florent,\n\nI have changed the function to use index() and added an exception. More importantly, I have also created a StandardTableau_class class and a StandardTableau() function for holding and creating standard tableau...previously I was confused and thought that the StandardTableaux class  did this. I discovered my error when I tested the new version (which I confess I had previously just moved into StandardTableaux and not tested...I promise to test properly in future!).\n\nHopefully the new patch also removes my unintended change to kschur.py.\n\nRegards,\nAndrew",
    "created_at": "2009-04-13T15:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42592",
    "user": "andrew.mathas"
}
```

Attachment [tableau-content-5487-AM.patch](tarball://root/attachments/some-uuid/ticket5487/tableau-content-5487-AM.patch) by andrew.mathas created at 2009-04-13 15:30:42

Dear Florent,

I have changed the function to use index() and added an exception. More importantly, I have also created a StandardTableau_class class and a StandardTableau() function for holding and creating standard tableau...previously I was confused and thought that the StandardTableaux class  did this. I discovered my error when I tested the new version (which I confess I had previously just moved into StandardTableaux and not tested...I promise to test properly in future!).

Hopefully the new patch also removes my unintended change to kschur.py.

Regards,
Andrew



---

archive/issue_comments_042593.json:
```json
{
    "body": "Review patch",
    "created_at": "2009-04-13T21:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42593",
    "user": "hivert"
}
```

Review patch



---

archive/issue_comments_042594.json:
```json
{
    "body": "Attachment [tableau-content-5487-review-fh.patch](tarball://root/attachments/some-uuid/ticket5487/tableau-content-5487-review-fh.patch) by hivert created at 2009-04-13 21:53:51\n\nI Added a review patch which:\n\n- add some more doctests\n\n- correct the ReST syntax for doctests\n\n- Specifies which exception is caught.\n\nI'm giving the positive review though someone should probably reread my trivial review patch... \n\nMichael: please tell me if I should not give the review and ask for a formal review of my patch.   \n\nCheers,\n\nFlorent",
    "created_at": "2009-04-13T21:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42594",
    "user": "hivert"
}
```

Attachment [tableau-content-5487-review-fh.patch](tarball://root/attachments/some-uuid/ticket5487/tableau-content-5487-review-fh.patch) by hivert created at 2009-04-13 21:53:51

I Added a review patch which:

- add some more doctests

- correct the ReST syntax for doctests

- Specifies which exception is caught.

I'm giving the positive review though someone should probably reread my trivial review patch... 

Michael: please tell me if I should not give the review and ask for a formal review of my patch.   

Cheers,

Florent



---

archive/issue_comments_042595.json:
```json
{
    "body": "Replying to [comment:9 hivert]:\n> I Added a review patch which:\n\n<SNIP>\n\n> I'm giving the positive review though someone should probably reread my trivial review patch... \n\nYep. \n\n> Michael: please tell me if I should not give the review and ask for a formal review of my patch.   \n\nI would consider this review patch non-trivial enough to have someone else take a look since it adds more than a doctest. I looked at the patch and it looks good to me, but I will run doctests before mergin.\n\nCheers,\n\nMichael\n\n> Cheers,\n> \n> Florent\n>",
    "created_at": "2009-04-13T22:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42595",
    "user": "mabshoff"
}
```

Replying to [comment:9 hivert]:
> I Added a review patch which:

<SNIP>

> I'm giving the positive review though someone should probably reread my trivial review patch... 

Yep. 

> Michael: please tell me if I should not give the review and ask for a formal review of my patch.   

I would consider this review patch non-trivial enough to have someone else take a look since it adds more than a doctest. I looked at the patch and it looks good to me, but I will run doctests before mergin.

Cheers,

Michael

> Cheers,
> 
> Florent
>



---

archive/issue_comments_042596.json:
```json
{
    "body": "Positive review on Andrew and Florent's patches.",
    "created_at": "2009-04-13T23:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42596",
    "user": "nthiery"
}
```

Positive review on Andrew and Florent's patches.



---

archive/issue_comments_042597.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T00:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42597",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_042598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T00:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42598",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042599.json:
```json
{
    "body": "Attachment [trac_5487_tableau-content-5487-AM.patch](tarball://root/attachments/some-uuid/ticket5487/trac_5487_tableau-content-5487-AM.patch) by mabshoff created at 2009-04-15 00:14:53\n\nThis is the same as the first patch, but instead of a diff it has been commited in Andrew's name",
    "created_at": "2009-04-15T00:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42599",
    "user": "mabshoff"
}
```

Attachment [trac_5487_tableau-content-5487-AM.patch](tarball://root/attachments/some-uuid/ticket5487/trac_5487_tableau-content-5487-AM.patch) by mabshoff created at 2009-04-15 00:14:53

This is the same as the first patch, but instead of a diff it has been commited in Andrew's name



---

archive/issue_comments_042600.json:
```json
{
    "body": "Andrew,\n\nI attached trac_5487_tableau-content-5487-AM.patch which is your patch checked in in your name. You attached a diff, but when you used hg queues you to export the patch after committing so that you get credited properly. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T00:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42600",
    "user": "mabshoff"
}
```

Andrew,

I attached trac_5487_tableau-content-5487-AM.patch which is your patch checked in in your name. You attached a diff, but when you used hg queues you to export the patch after committing so that you get credited properly. 

Cheers,

Michael



---

archive/issue_comments_042601.json:
```json
{
    "body": "Oops, reassign to 3.4.1 since it was merged in that timeframe.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T02:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5487#issuecomment-42601",
    "user": "mabshoff"
}
```

Oops, reassign to 3.4.1 since it was merged in that timeframe.

Cheers,

Michael
