# Issue 8533: browse thematic tutorials from command line and within notebook

archive/issues_008533.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @wdjoyner @rlmill @nathanncohen @rbeezer sage-combinat @dwbump @jhpalmieri\n\nTicket #8470 adds a collection of thematic tutorials to the Sage standard documentation. We should be able to browse such tutorials from the Sage command line or within the Sage notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8533\n\n",
    "created_at": "2010-03-14T00:01:21Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "browse thematic tutorials from command line and within notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @wdjoyner @rlmill @nathanncohen @rbeezer sage-combinat @dwbump @jhpalmieri

Ticket #8470 adds a collection of thematic tutorials to the Sage standard documentation. We should be able to browse such tutorials from the Sage command line or within the Sage notebook.

Issue created by migration from https://trac.sagemath.org/ticket/8533





---

archive/issue_comments_076983.json:
```json
{
    "body": "Attachment [trac_8533-browse-doc.patch](tarball://root/attachments/some-uuid/ticket8533/trac_8533-browse-doc.patch) by mvngu created at 2010-03-14 00:03:49\n\nbased on Sage 4.3.4.alpha1; depends on #8442",
    "created_at": "2010-03-14T00:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8533-browse-doc.patch](tarball://root/attachments/some-uuid/ticket8533/trac_8533-browse-doc.patch) by mvngu created at 2010-03-14 00:03:49

based on Sage 4.3.4.alpha1; depends on #8442



---

archive/issue_comments_076984.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-14T00:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076985.json:
```json
{
    "body": "The attachment should allow you to do these things from the Sage command line and within the Sage notebook:\n\n1. browse the FAQ\n2. browse the index of thematic tutorials\n3. browse any of the following thematic tutorials at #8465, #8469, #8468, #8442.",
    "created_at": "2010-03-14T00:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76985",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The attachment should allow you to do these things from the Sage command line and within the Sage notebook:

1. browse the FAQ
2. browse the index of thematic tutorials
3. browse any of the following thematic tutorials at #8465, #8469, #8468, #8442.



---

archive/issue_comments_076986.json:
```json
{
    "body": "From IRC:\n\n```\n16:33 < mhansen> I don't think things like group_theory_tutorial should be at \n                 the top-level.\n16:34 < mvngu> mhansen: Another way is: browse_sage_doc(\"group_theory_tutorial\")\n16:34 < mvngu> The original goal was to able to do sage.groups.tutorial()\n16:35 < mvngu> But I can't figure out how to put the group theory tutorial \n               within the Sage library, and to also list it within the thematic \n               tutorials page.\n16:40 < palmieri> Put this in sage/groups/__init__.py:  from sage.misc.sagedoc \n                  import browse_sage_doc\n16:40 < palmieri> tutorial = browse_sage_doc.group_theory_tutorial\n16:40 < mvngu> OK. Let try...\n16:40 < palmieri> Put those two lines in sage/groups/__init__.py\n16:41 < palmieri> Or maybe \"from sage.misc.sagedoc import groups_tutorial as \n                  tutorial\"\n16:41 < mvngu> The last syntax looks better.\n```\n",
    "created_at": "2010-03-14T00:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76986",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

From IRC:

```
16:33 < mhansen> I don't think things like group_theory_tutorial should be at 
                 the top-level.
16:34 < mvngu> mhansen: Another way is: browse_sage_doc("group_theory_tutorial")
16:34 < mvngu> The original goal was to able to do sage.groups.tutorial()
16:35 < mvngu> But I can't figure out how to put the group theory tutorial 
               within the Sage library, and to also list it within the thematic 
               tutorials page.
16:40 < palmieri> Put this in sage/groups/__init__.py:  from sage.misc.sagedoc 
                  import browse_sage_doc
16:40 < palmieri> tutorial = browse_sage_doc.group_theory_tutorial
16:40 < mvngu> OK. Let try...
16:40 < palmieri> Put those two lines in sage/groups/__init__.py
16:41 < palmieri> Or maybe "from sage.misc.sagedoc import groups_tutorial as 
                  tutorial"
16:41 < mvngu> The last syntax looks better.
```




---

archive/issue_comments_076987.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-14T00:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76987",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076988.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-14T01:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076989.json:
```json
{
    "body": "The attachment [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch) is another implementation different from the one in [trac_8533-browse-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc.patch). With [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch), you can do these:\n\n* `sage.groups.tutorial()`\n* `sage.combinat.lie_tutorial()`\n* `sage.crypto.rsa_tutorial()`\n\nThat is, the above three tutorials are no longer available from the global name space. The above is closer to the original goal of being able to do \"sage.groups.tutorial()\" to get the group theory tutorial, etc. However, the FAQ and the index of thematic tutorials are still available in the global name space:\n\n* `faq()`\n* `thematic_tutorials()`\n\nTo see a list of tutorials that you could browse, use \"browse_sage_doc.<tab>\". Nevertheless, we still have the problem of listing thematic tutorials in the index of thematic tutorials. Could the second patch be seen as a compromise?",
    "created_at": "2010-03-14T01:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76989",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The attachment [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch) is another implementation different from the one in [trac_8533-browse-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc.patch). With [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch), you can do these:

* `sage.groups.tutorial()`
* `sage.combinat.lie_tutorial()`
* `sage.crypto.rsa_tutorial()`

That is, the above three tutorials are no longer available from the global name space. The above is closer to the original goal of being able to do "sage.groups.tutorial()" to get the group theory tutorial, etc. However, the FAQ and the index of thematic tutorials are still available in the global name space:

* `faq()`
* `thematic_tutorials()`

To see a list of tutorials that you could browse, use "browse_sage_doc.<tab>". Nevertheless, we still have the problem of listing thematic tutorials in the index of thematic tutorials. Could the second patch be seen as a compromise?



---

archive/issue_comments_076990.json:
```json
{
    "body": "based on Sage 4.3.4.alpha1; depends on #8442",
    "created_at": "2010-03-19T01:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.3.4.alpha1; depends on #8442



---

archive/issue_comments_076991.json:
```json
{
    "body": "Attachment [trac_8533-browse-doc-take2.patch](tarball://root/attachments/some-uuid/ticket8533/trac_8533-browse-doc-take2.patch) by mvngu created at 2010-03-19 01:26:43\n\nThe latest version [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch) now allows you to do these:\n\n* `sage.groups.tutorial()`\n* `sage.combinat.tutorial()`\n* `sage.crypto.tutorial()`\n\nThat is, there is only one tutorial for each Sage top level module.",
    "created_at": "2010-03-19T01:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8533-browse-doc-take2.patch](tarball://root/attachments/some-uuid/ticket8533/trac_8533-browse-doc-take2.patch) by mvngu created at 2010-03-19 01:26:43

The latest version [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch) now allows you to do these:

* `sage.groups.tutorial()`
* `sage.combinat.tutorial()`
* `sage.crypto.tutorial()`

That is, there is only one tutorial for each Sage top level module.



---

archive/issue_comments_076992.json:
```json
{
    "body": "In addition to #8442, does this also depend on #8465 and #8469?  Without those, commands like `browse_sage_doc.funcprogramming_tutorial` (available via tab completion) don't work and give a message \n\n```\nOSError: The document 'thematic_tutorials/functional_programming' does not exist.  Please build it\nwith 'sage -docbuild thematic_tutorials/functional_programming html --jsmath' and try again.\n```\n\nwhich is misleading, since that command won't succeed.\n\nI have no idea if there is any good way to doctest functions like \n\n```\n    def faq(self):\n        \"\"\"\n        The Sage FAQ. A collection of frequently asked questions, together\n        with answers to those questions.\n        \"\"\"\n        self._open(\"faq\")\n```\n\nIt would be nice to not lower our coverage by including functions like this.  Here's an idea: replace the function by\n\n```\nfaq = lambda self: self._open('faq')\n```\n\nOr is that cheating? This belongs on another ticket, in any case.\n\nGiven my understanding of the dependencies, this gets a positive review.",
    "created_at": "2010-06-23T17:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76992",
    "user": "https://github.com/jhpalmieri"
}
```

In addition to #8442, does this also depend on #8465 and #8469?  Without those, commands like `browse_sage_doc.funcprogramming_tutorial` (available via tab completion) don't work and give a message 

```
OSError: The document 'thematic_tutorials/functional_programming' does not exist.  Please build it
with 'sage -docbuild thematic_tutorials/functional_programming html --jsmath' and try again.
```

which is misleading, since that command won't succeed.

I have no idea if there is any good way to doctest functions like 

```
    def faq(self):
        """
        The Sage FAQ. A collection of frequently asked questions, together
        with answers to those questions.
        """
        self._open("faq")
```

It would be nice to not lower our coverage by including functions like this.  Here's an idea: replace the function by

```
faq = lambda self: self._open('faq')
```

Or is that cheating? This belongs on another ticket, in any case.

Given my understanding of the dependencies, this gets a positive review.



---

archive/issue_comments_076993.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T17:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76993",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076994.json:
```json
{
    "body": "Is it possible to move the dependent code here to #8442 and #8469?  Then I could merge this ticket into 4.5.3.x.",
    "created_at": "2010-08-07T05:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76994",
    "user": "https://github.com/qed777"
}
```

Is it possible to move the dependent code here to #8442 and #8469?  Then I could merge this ticket into 4.5.3.x.



---

archive/issue_comments_076995.json:
```json
{
    "body": "based on Sage 4.5.2.rc1",
    "created_at": "2010-08-07T07:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76995",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.5.2.rc1



---

archive/issue_comments_076996.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-07T07:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076997.json:
```json
{
    "body": "Attachment [trac_8533-browse-doc-take3.patch](tarball://root/attachments/some-uuid/ticket8533/trac_8533-browse-doc-take3.patch) by mvngu created at 2010-08-07 07:38:28\n\nThe new patch [attachment:trac_8533-browse-doc-take3.patch] does the same thing as the previous two. But here are the changes in this new patch:\n\n* Remove dependency on #8442 and #8469.\n* Use John's idea of invoking a document using `lambda`.\n* Allow for browsing the following documents from the command line: FAQ and all the thematic tutorials in the standard documentation so far.\n* Doctesting the `lambda` functions that are used for browsing the FAQ and the thematic tutorials.\n \nJohn's idea of invoking a document using `lambda` is not cheating at all. I implemented that for the FAQ and the extant thematic tutorials, and have provided doctests.\n\n\n\nWith [attachment:trac_8533-browse-doc-take3.patch] offering a completely new implementation, it renders John's previous positive review ineffective. Sorry, but I have to move this ticket to \"needs review\" again.",
    "created_at": "2010-08-07T07:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8533-browse-doc-take3.patch](tarball://root/attachments/some-uuid/ticket8533/trac_8533-browse-doc-take3.patch) by mvngu created at 2010-08-07 07:38:28

The new patch [attachment:trac_8533-browse-doc-take3.patch] does the same thing as the previous two. But here are the changes in this new patch:

* Remove dependency on #8442 and #8469.
* Use John's idea of invoking a document using `lambda`.
* Allow for browsing the following documents from the command line: FAQ and all the thematic tutorials in the standard documentation so far.
* Doctesting the `lambda` functions that are used for browsing the FAQ and the thematic tutorials.
 
John's idea of invoking a document using `lambda` is not cheating at all. I implemented that for the FAQ and the extant thematic tutorials, and have provided doctests.



With [attachment:trac_8533-browse-doc-take3.patch] offering a completely new implementation, it renders John's previous positive review ineffective. Sorry, but I have to move this ticket to "needs review" again.



---

archive/issue_comments_076998.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-07T07:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76998",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076999.json:
```json
{
    "body": "On my mac: when I run doctests on sagedoc.py, my browser opens up several different windows.  I don't think this is a good idea.     Maybe the lines\n\n```\n    sage: faq() \n    sage: thematic_tutorials() \n    sage: funcprogramming_tutorial() \n    sage: sage.groups.tutorial() \n```\n\nshould be labeled `# not tested` instead?  Also, do we need to have `funcprogramming_tutorial()` as a top-level command, or is it good enough to have `thematic_tutorials()`?  (This is a genuine question: I don't know which way is better.)",
    "created_at": "2010-08-11T21:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-76999",
    "user": "https://github.com/jhpalmieri"
}
```

On my mac: when I run doctests on sagedoc.py, my browser opens up several different windows.  I don't think this is a good idea.     Maybe the lines

```
    sage: faq() 
    sage: thematic_tutorials() 
    sage: funcprogramming_tutorial() 
    sage: sage.groups.tutorial() 
```

should be labeled `# not tested` instead?  Also, do we need to have `funcprogramming_tutorial()` as a top-level command, or is it good enough to have `thematic_tutorials()`?  (This is a genuine question: I don't know which way is better.)



---

archive/issue_comments_077000.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-11T21:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-77000",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077001.json:
```json
{
    "body": "Replying to [comment:11 jhpalmieri]:\n> Also, do we need to have `funcprogramming_tutorial()` as a top-level command, or is it good enough to have `thematic_tutorials()`?  (This is a genuine question: I don't know which way is better.)\n\nOr `thematic_tutorials.funcprogramming_tutorial()` which would be useful in conjunction with `thematic_tutorials.<tab>`. Only one entry point for all thematic tutorials seem more reasonable.\n\nVincent",
    "created_at": "2014-08-29T18:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-77001",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:11 jhpalmieri]:
> Also, do we need to have `funcprogramming_tutorial()` as a top-level command, or is it good enough to have `thematic_tutorials()`?  (This is a genuine question: I don't know which way is better.)

Or `thematic_tutorials.funcprogramming_tutorial()` which would be useful in conjunction with `thematic_tutorials.<tab>`. Only one entry point for all thematic tutorials seem more reasonable.

Vincent



---

archive/issue_comments_077002.json:
```json
{
    "body": "I think this ticket didn't get enough momentum, perhaps because we don't want to clutter the global namespace with names of not much use.\n\nTime to close?",
    "created_at": "2022-02-09T01:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-77002",
    "user": "https://github.com/kwankyu"
}
```

I think this ticket didn't get enough momentum, perhaps because we don't want to clutter the global namespace with names of not much use.

Time to close?



---

archive/issue_comments_077003.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-02-09T01:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-77003",
    "user": "https://github.com/kwankyu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077004.json:
```json
{
    "body": "Yes, I agree.",
    "created_at": "2022-02-09T06:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-77004",
    "user": "https://github.com/jhpalmieri"
}
```

Yes, I agree.



---

archive/issue_comments_077005.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-02-09T06:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-77005",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008712.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-02-12T18:02:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8533#event-8712"
}
```



---

archive/issue_comments_077006.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-02-12T18:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8533#issuecomment-77006",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
