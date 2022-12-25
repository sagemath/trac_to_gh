# Issue 8892: Many doctests fails since the update of NetworkX !

archive/issues_008892.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nHello everybody !!!\n\nI noticed working on something quite different that many doctests were failing in Sage's graph library because of the recent update of NetworkX... The reason is easy : the default edge label is not \"None\" anymore but {}. Besides, dictionary are not hashable !!!\n\nThis patch fixes it ! \n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8892\n\n",
    "created_at": "2010-05-05T17:44:26Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Many doctests fails since the update of NetworkX !",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8892",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

Hello everybody !!!

I noticed working on something quite different that many doctests were failing in Sage's graph library because of the recent update of NetworkX... The reason is easy : the default edge label is not "None" anymore but {}. Besides, dictionary are not hashable !!!

This patch fixes it ! 

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8892





---

archive/issue_comments_081613.json:
```json
{
    "body": "Apparently now, networkx has moved to having a dictionary of edge attributes, rather than a specific \"label\".  See http://networkx.lanl.gov/reference/api_1.0.html#edge-attributes\n\nI'm not saying we should follow the convention, but it does seem to make sense.  Instead of just storing a single value, store a dict of attributes.\n\nWhy is it important that dictionaries are not hashable?",
    "created_at": "2010-05-05T18:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81613",
    "user": "https://github.com/jasongrout"
}
```

Apparently now, networkx has moved to having a dictionary of edge attributes, rather than a specific "label".  See http://networkx.lanl.gov/reference/api_1.0.html#edge-attributes

I'm not saying we should follow the convention, but it does seem to make sense.  Instead of just storing a single value, store a dict of attributes.

Why is it important that dictionaries are not hashable?



---

archive/issue_comments_081614.json:
```json
{
    "body": "Because I sometimes stored them as keys of dictionaries. It means I will need to forget to store the label, and just the endpoints. The other detail is that in many algorithms, the labels are used as a weight, and I you will see very often in Sage's code :\nweight = lambda label : 1 if label is None else label\n\nSo all these occurrences need to be replaces to label == {} in this case... Does that mean we should assume labels are ALWAYS dictionaries ? This would mean trouble... Where would we store numerical values for edges then.. a default field ?\n\nNathann",
    "created_at": "2010-05-05T18:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81614",
    "user": "https://github.com/nathanncohen"
}
```

Because I sometimes stored them as keys of dictionaries. It means I will need to forget to store the label, and just the endpoints. The other detail is that in many algorithms, the labels are used as a weight, and I you will see very often in Sage's code :
weight = lambda label : 1 if label is None else label

So all these occurrences need to be replaces to label == {} in this case... Does that mean we should assume labels are ALWAYS dictionaries ? This would mean trouble... Where would we store numerical values for edges then.. a default field ?

Nathann



---

archive/issue_comments_081615.json:
```json
{
    "body": "A little farther down the networkx page listed, we find http://networkx.lanl.gov/reference/api_1.0.html#converting-your-existing-code-to-networkx-1-0, which says that now all algorithms (in Networkx) look for the \"weight\" edge attribute.\n\nSounds like that would be a huge change for Sage code, though...",
    "created_at": "2010-05-05T18:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81615",
    "user": "https://github.com/jasongrout"
}
```

A little farther down the networkx page listed, we find http://networkx.lanl.gov/reference/api_1.0.html#converting-your-existing-code-to-networkx-1-0, which says that now all algorithms (in Networkx) look for the "weight" edge attribute.

Sounds like that would be a huge change for Sage code, though...



---

archive/issue_comments_081616.json:
```json
{
    "body": "Hi Nathann,\n\nThanks for uncovering this one.  Not sure right now I have a good idea about what should be done.\n\nHowever, is there a patch to go on this?  I'm not seeing one.\n\nRob",
    "created_at": "2010-05-06T03:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81616",
    "user": "https://github.com/rbeezer"
}
```

Hi Nathann,

Thanks for uncovering this one.  Not sure right now I have a good idea about what should be done.

However, is there a patch to go on this?  I'm not seeing one.

Rob



---

archive/issue_comments_081617.json:
```json
{
    "body": "Not yet. For the moment, my patch is a nasty one : replaces tests \"is None\" by \"is None or == {}\". I thought it may be better to settle on what we want to do with these labels, but I can upload it otherwise (somewhere on another computer at the moment) :-)\n\nNathann",
    "created_at": "2010-05-06T03:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81617",
    "user": "https://github.com/nathanncohen"
}
```

Not yet. For the moment, my patch is a nasty one : replaces tests "is None" by "is None or == {}". I thought it may be better to settle on what we want to do with these labels, but I can upload it otherwise (somewhere on another computer at the moment) :-)

Nathann



---

archive/issue_comments_081618.json:
```json
{
    "body": "Here is a patch that does not make any choice. I replaced the \"is None\" by \"in RR\" :-)\n\nThe failing docstrings come from GraphViz ( at least on my computer ) !\n\nNathann",
    "created_at": "2010-05-08T00:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81618",
    "user": "https://github.com/nathanncohen"
}
```

Here is a patch that does not make any choice. I replaced the "is None" by "in RR" :-)

The failing docstrings come from GraphViz ( at least on my computer ) !

Nathann



---

archive/issue_comments_081619.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-08T00:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81619",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081620.json:
```json
{
    "body": "Now also fixes the edge_coloring function from the graph_coloring module, as reported by Minh in #8781\n\nSorry for that !\n\nNathann",
    "created_at": "2010-05-10T17:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81620",
    "user": "https://github.com/nathanncohen"
}
```

Now also fixes the edge_coloring function from the graph_coloring module, as reported by Minh in #8781

Sorry for that !

Nathann



---

archive/issue_comments_081621.json:
```json
{
    "body": "Attachment [trac_8892.patch](tarball://root/attachments/some-uuid/ticket8892/trac_8892.patch) by @nathanncohen created at 2010-05-10 17:32:00",
    "created_at": "2010-05-10T17:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81621",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_8892.patch](tarball://root/attachments/some-uuid/ticket8892/trac_8892.patch) by @nathanncohen created at 2010-05-10 17:32:00



---

archive/issue_comments_081622.json:
```json
{
    "body": "Attachment [trac_8892-reviewer.patch](tarball://root/attachments/some-uuid/ticket8892/trac_8892-reviewer.patch) by mvngu created at 2010-05-11 06:53:52\n\nI'm mostly happy with [trac_8892.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8892/trac_8892.patch). I have attached a reviewer patch that deals with the part I'm not happy with, i.e. fix some typos introduced by the first patch. Apart from myself, anyone is welcome to give a final sign off on this ticket.",
    "created_at": "2010-05-11T06:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8892-reviewer.patch](tarball://root/attachments/some-uuid/ticket8892/trac_8892-reviewer.patch) by mvngu created at 2010-05-11 06:53:52

I'm mostly happy with [trac_8892.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8892/trac_8892.patch). I have attached a reviewer patch that deals with the part I'm not happy with, i.e. fix some typos introduced by the first patch. Apart from myself, anyone is welcome to give a final sign off on this ticket.



---

archive/issue_comments_081623.json:
```json
{
    "body": "I sign off on your changes.  Are you asking someone else to also sign off on the original patch?",
    "created_at": "2010-05-11T07:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81623",
    "user": "https://github.com/jasongrout"
}
```

I sign off on your changes.  Are you asking someone else to also sign off on the original patch?



---

archive/issue_comments_081624.json:
```json
{
    "body": "Changing assignee from jason, ncohen, rlm to @jasongrout.",
    "created_at": "2010-05-11T07:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81624",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from jason, ncohen, rlm to @jasongrout.



---

archive/issue_comments_081625.json:
```json
{
    "body": "Changing assignee from @jasongrout to @nathanncohen.",
    "created_at": "2010-05-11T07:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81625",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @jasongrout to @nathanncohen.



---

archive/issue_comments_081626.json:
```json
{
    "body": "(I didn't apply your changes, but it is clear that they are cosmetic things.)",
    "created_at": "2010-05-11T07:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81626",
    "user": "https://github.com/jasongrout"
}
```

(I didn't apply your changes, but it is clear that they are cosmetic things.)



---

archive/issue_comments_081627.json:
```json
{
    "body": "Replying to [comment:9 jason]:\n> Are you asking someone else to also sign off on the original patch?\n\nNot really. I'm OK with ncohen's patch.",
    "created_at": "2010-05-11T08:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:9 jason]:
> Are you asking someone else to also sign off on the original patch?

Not really. I'm OK with ncohen's patch.



---

archive/issue_comments_081628.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-11T08:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081629.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-12T22:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8892#issuecomment-81629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
