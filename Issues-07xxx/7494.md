# Issue 7494: remove (or clean up) SAGE_ROOT/examples

archive/issues_007494.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @wdjoyner\n\nKeywords: sd32\n\nDid you know there is a directory SAGE_ROOT/examples?   Do you care?  Because if nobody seriously cares, I'm going to *delete it* from future versions of Sage, since it is still a mess, and the last nontrivial commit was 1.5 years ago (!):\n\n```\nchangeset:   158:d18dad210d3b\nuser:        Mike Hansen <mhansen@gmail.com>\ndate:        Mon Apr 14 03:08:48 2008 -0700\nsummary:     Extract sagetex.py and sagetex.sty\n```\nI can put the same directory online somewhere, and move the fortran file that is used in one doctest out.  I'm just really curious if anybody knows about this directory and cares. \n\n**Apply**:\n1. [attachment:trac_7494.patch] to the Sage library repo\n2. [attachment:trac_7494-ref.patch] to the Sage library repo\n3. [attachment:trac_7494-scripts.patch] to the **scripts** repo\n4. [attachment:trac_7494-root-repo.patch] to the **Sage root** repository\n\n**Release Manager:**\n\nDelete `$SAGE_ROOT/examples/` as part of this ticket. \n\n(This should happen automatically, i.e., the directory should vanish, when `sdist`ing.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7494\n\n",
    "closed_at": "2011-10-05T12:19:11Z",
    "created_at": "2009-11-19T22:55:57Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "remove (or clean up) SAGE_ROOT/examples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7494",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @wdjoyner

Keywords: sd32

Did you know there is a directory SAGE_ROOT/examples?   Do you care?  Because if nobody seriously cares, I'm going to *delete it* from future versions of Sage, since it is still a mess, and the last nontrivial commit was 1.5 years ago (!):

```
changeset:   158:d18dad210d3b
user:        Mike Hansen <mhansen@gmail.com>
date:        Mon Apr 14 03:08:48 2008 -0700
summary:     Extract sagetex.py and sagetex.sty
```
I can put the same directory online somewhere, and move the fortran file that is used in one doctest out.  I'm just really curious if anybody knows about this directory and cares. 

**Apply**:
1. [attachment:trac_7494.patch] to the Sage library repo
2. [attachment:trac_7494-ref.patch] to the Sage library repo
3. [attachment:trac_7494-scripts.patch] to the **scripts** repo
4. [attachment:trac_7494-root-repo.patch] to the **Sage root** repository

**Release Manager:**

Delete `$SAGE_ROOT/examples/` as part of this ticket. 

(This should happen automatically, i.e., the directory should vanish, when `sdist`ing.)


Issue created by migration from https://trac.sagemath.org/ticket/7494





---

archive/issue_comments_063188.json:
```json
{
    "body": "#298 would be invalidated by doing this ticket.",
    "created_at": "2009-11-19T23:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63188",
    "user": "https://github.com/williamstein"
}
```

#298 would be invalidated by doing this ticket.



---

archive/issue_comments_063189.json:
```json
{
    "body": "I was wondering about that directory too a few months ago.  So we don't do anything with it currently?  Here are comments.\n\nI think it would be worth linking at least a few of the top-level ones to the wiki, and perhaps put in one of the documentation places, as some of the examples files there are definitely useful for templates.  \n\nI bet some of the programming (Pyrex/SageX/Cython) examples might be useful too.  \n\nI am cc:ing wdj to see if he thinks all his examples/routines from calculus are now in the main Sage library.\n\nThe linalg folder is definitely pointless, as permanents are now in the main library.\n\nThe worksheets folder seems pretty pointless in its current state.\n\nThe tests directory has some things that should be added as random doctests for those things, though.\n\nThe modsym directory stuff likely is already tested in that area, given how important it is to Sage!\n\nThe latex_embed is obviously superfluous at this point.\n\nFortran was has already discussed above.\n\nFinance is *really* pointless.\n\nThe Groebner basis thing seems intriguing - perhaps should be incorporated in doctests for that elsewhere?\n\nIs the Ajax thing now very very superfluous, given how much we use it?  It's not (that) old.\n\nThe GSL folder is quite large compared to the rest and perhaps has some examples which should be combined into one big file which is doctested, if those sorts of tests aren't.  It would seem valuable not to lose this many doctests -does it currently pass?",
    "created_at": "2009-12-30T04:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63189",
    "user": "https://github.com/kcrisman"
}
```

I was wondering about that directory too a few months ago.  So we don't do anything with it currently?  Here are comments.

I think it would be worth linking at least a few of the top-level ones to the wiki, and perhaps put in one of the documentation places, as some of the examples files there are definitely useful for templates.  

I bet some of the programming (Pyrex/SageX/Cython) examples might be useful too.  

I am cc:ing wdj to see if he thinks all his examples/routines from calculus are now in the main Sage library.

The linalg folder is definitely pointless, as permanents are now in the main library.

The worksheets folder seems pretty pointless in its current state.

The tests directory has some things that should be added as random doctests for those things, though.

The modsym directory stuff likely is already tested in that area, given how important it is to Sage!

The latex_embed is obviously superfluous at this point.

Fortran was has already discussed above.

Finance is *really* pointless.

The Groebner basis thing seems intriguing - perhaps should be incorporated in doctests for that elsewhere?

Is the Ajax thing now very very superfluous, given how much we use it?  It's not (that) old.

The GSL folder is quite large compared to the rest and perhaps has some examples which should be combined into one big file which is doctested, if those sorts of tests aren't.  It would seem valuable not to lose this many doctests -does it currently pass?



---

archive/issue_comments_063190.json:
```json
{
    "body": "> \n> I am cc:ing wdj to see if he thinks all his examples/routines from calculus are now in the main Sage library.\n\n\nSee #7936 for this - we can delete this one, at least.",
    "created_at": "2010-04-27T19:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63190",
    "user": "https://github.com/kcrisman"
}
```

> 
> I am cc:ing wdj to see if he thinks all his examples/routines from calculus are now in the main Sage library.


See #7936 for this - we can delete this one, at least.



---

archive/issue_comments_063191.json:
```json
{
    "body": "The last nontrivial commit was 1.5 years before this ticket was created, but now it's been 1.5 years since this ticket was created! Can we get rid of this directory yet?",
    "created_at": "2011-06-14T22:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63191",
    "user": "https://github.com/kini"
}
```

The last nontrivial commit was 1.5 years before this ticket was created, but now it's been 1.5 years since this ticket was created! Can we get rid of this directory yet?



---

archive/issue_comments_063192.json:
```json
{
    "body": "I have asked about this a lot.   In order to give this, it would be really nice to move a few of the examples to other places - wiki, wherever.  \n\n* a few top-level things\n* some of the Cython ones?\n* tests has a few interesting random doctests\n* something fortran is needed somewhere, apparently?  According to the comment in was' original report\n* The GSL examples might be worth moing somewhere\n* Groebner useful in doctests?\n\nAnyway, we shouldn't just completely delete in case there are useful tests.    But I totally agree on the overall strategy.",
    "created_at": "2011-06-14T22:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63192",
    "user": "https://github.com/kcrisman"
}
```

I have asked about this a lot.   In order to give this, it would be really nice to move a few of the examples to other places - wiki, wherever.  

* a few top-level things
* some of the Cython ones?
* tests has a few interesting random doctests
* something fortran is needed somewhere, apparently?  According to the comment in was' original report
* The GSL examples might be worth moing somewhere
* Groebner useful in doctests?

Anyway, we shouldn't just completely delete in case there are useful tests.    But I totally agree on the overall strategy.



---

archive/issue_comments_063193.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-24T06:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63193",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063194.json:
```json
{
    "body": "Delete it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\nI wrote almost everything in there, and it should just go. \n\nI give \"delete the examples directory\" a positive review.  To merge this ticket, do\n\n```\ncd SAGE_ROOT\nrm -rf examples\n```",
    "created_at": "2011-08-24T06:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63194",
    "user": "https://github.com/williamstein"
}
```

Delete it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

I wrote almost everything in there, and it should just go. 

I give "delete the examples directory" a positive review.  To merge this ticket, do

```
cd SAGE_ROOT
rm -rf examples
```



---

archive/issue_comments_063195.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-24T06:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63195",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063196.json:
```json
{
    "body": "For future reference, I've put that directory here:\n\n    http://wstein.org/old_sage_examples/",
    "created_at": "2011-08-24T06:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63196",
    "user": "https://github.com/williamstein"
}
```

For future reference, I've put that directory here:

    http://wstein.org/old_sage_examples/



---

archive/issue_comments_063197.json:
```json
{
    "body": "I just realized that there is one thing that has to be done. Observe:\n\n```\nwstein@ubuntu:~/d/sage$ sage -grep \"examples\"|grep SAGE_ROOT\nfinance/stock.py:            sage: finance.Stock('aapl').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')[:5]\nfinance/stock.py:            sage: finance.Stock('goog').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')[:5]\nfinance/stock.py:            sage: finance.Stock('aapl').load_from_file(SAGE_ROOT + \"/examples/finance/AAPL-minutely.csv\")\nmisc/hg.py:hg_examples = HG('%s/data/examples'%SAGE_ROOT,\nmisc/inline_fortran.py:            sage: s = open(os.environ['SAGE_ROOT'] + '/examples/fortran/FIB1.F').read()\nwstein@ubuntu:~/d/sage$ \n```\n\nSo the stuff in examples that are used in doctests need to be moved to the SAGE_ROOT/data/ directory.  Thus one needs to attach a patch that does this to this ticket, and that patch will need to be reviewed.",
    "created_at": "2011-08-24T06:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63197",
    "user": "https://github.com/williamstein"
}
```

I just realized that there is one thing that has to be done. Observe:

```
wstein@ubuntu:~/d/sage$ sage -grep "examples"|grep SAGE_ROOT
finance/stock.py:            sage: finance.Stock('aapl').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')[:5]
finance/stock.py:            sage: finance.Stock('goog').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')[:5]
finance/stock.py:            sage: finance.Stock('aapl').load_from_file(SAGE_ROOT + "/examples/finance/AAPL-minutely.csv")
misc/hg.py:hg_examples = HG('%s/data/examples'%SAGE_ROOT,
misc/inline_fortran.py:            sage: s = open(os.environ['SAGE_ROOT'] + '/examples/fortran/FIB1.F').read()
wstein@ubuntu:~/d/sage$ 
```

So the stuff in examples that are used in doctests need to be moved to the SAGE_ROOT/data/ directory.  Thus one needs to attach a patch that does this to this ticket, and that patch will need to be reviewed.



---

archive/issue_comments_063198.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-08-24T06:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63198",
    "user": "https://github.com/williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063199.json:
```json
{
    "body": "Attachment [trac_7494.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494.patch) by @williamstein created at 2011-08-24 06:43:53",
    "created_at": "2011-08-24T06:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63199",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7494.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494.patch) by @williamstein created at 2011-08-24 06:43:53



---

archive/issue_comments_063200.json:
```json
{
    "body": "The patch  trac_7494.patch should change the core sage library so it doesn't depend on anything in the SAGE_ROOT/examples directory for testing.  It also does not put anything in the SAGE_ROOT/data directory, since that is not needed.",
    "created_at": "2011-08-24T06:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63200",
    "user": "https://github.com/williamstein"
}
```

The patch  trac_7494.patch should change the core sage library so it doesn't depend on anything in the SAGE_ROOT/examples directory for testing.  It also does not put anything in the SAGE_ROOT/data directory, since that is not needed.



---

archive/issue_comments_063201.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-24T06:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63201",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063202.json:
```json
{
    "body": "So the Groebner, gsl, etc. tests aren't really useful? Ok by me.\n\nNice - thanks for looking at this \"officially\". Since there is a Sage Days going on and today is my first day of classes, I think someone will beat me to the review, but thanks for looking at this a bit more carefully. In some sense, you are the only person who can check it, since you're one of the few who really knows why these things were in in the first place :)",
    "created_at": "2011-08-24T12:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63202",
    "user": "https://github.com/kcrisman"
}
```

So the Groebner, gsl, etc. tests aren't really useful? Ok by me.

Nice - thanks for looking at this "officially". Since there is a Sage Days going on and today is my first day of classes, I think someone will beat me to the review, but thanks for looking at this a bit more carefully. In some sense, you are the only person who can check it, since you're one of the few who really knows why these things were in in the first place :)



---

archive/issue_comments_063203.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63203",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_063204.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-25T06:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63204",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063205.json:
```json
{
    "body": "Trash it.  There's too much old misleading stuff about as is.\n\nI renamed the examples directory, applied the patch, ran tests and got no failures.\n\nI guess we need to alert the release manager somehow to actually delete the directory in the next distribution?  I'll put a note above, edit as necessary.",
    "created_at": "2011-08-25T06:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63205",
    "user": "https://github.com/rbeezer"
}
```

Trash it.  There's too much old misleading stuff about as is.

I renamed the examples directory, applied the patch, ran tests and got no failures.

I guess we need to alert the release manager somehow to actually delete the directory in the next distribution?  I'll put a note above, edit as necessary.



---

archive/issue_comments_063206.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-08-25T21:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63206",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063207.json:
```json
{
    "body": "This also needs a patch to the scripts repo, since `sage-make_devel_packages` tries to create a new examples spkg and fails with a nonzero exit status if it can't do that.  I'm attaching a patch.",
    "created_at": "2011-08-25T21:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63207",
    "user": "https://github.com/jhpalmieri"
}
```

This also needs a patch to the scripts repo, since `sage-make_devel_packages` tries to create a new examples spkg and fails with a nonzero exit status if it can't do that.  I'm attaching a patch.



---

archive/issue_comments_063208.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-25T21:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63208",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063209.json:
```json
{
    "body": "scripts repo",
    "created_at": "2011-08-25T21:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63209",
    "user": "https://github.com/jhpalmieri"
}
```

scripts repo



---

archive/issue_comments_063210.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-27T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63210",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063211.json:
```json
{
    "body": "Attachment [trac_7494-scripts.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494-scripts.patch) by @williamstein created at 2011-09-27 01:23:17\n\nI'm good with jhpalmieri's cleanup of my patch.",
    "created_at": "2011-09-27T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63211",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7494-scripts.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494-scripts.patch) by @williamstein created at 2011-09-27 01:23:17

I'm good with jhpalmieri's cleanup of my patch.



---

archive/issue_comments_063212.json:
```json
{
    "body": "The root repository certainly also has to get patched:\n\n```sh\n$ grep -win examples spkg/install spkg/standard/deps \nspkg/install:184:EXAMPLES=`$newest examples`\nspkg/install:185:export EXAMPLES\nspkg/standard/deps:48:     $(INST)/$(EXAMPLES) \\\nspkg/standard/deps:398:$(INST)/$(EXAMPLES): $(BASE) $(INST)/$(PATCH)\nspkg/standard/deps:399:\t$(INSTALL) \"$(SAGE_SPKG) $(EXAMPLES) 2>&1\" \"tee -a $(SAGE_LOGS)/$(EXAMPLES).log\"\n```",
    "created_at": "2011-09-27T18:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63212",
    "user": "https://github.com/nexttime"
}
```

The root repository certainly also has to get patched:

```sh
$ grep -win examples spkg/install spkg/standard/deps 
spkg/install:184:EXAMPLES=`$newest examples`
spkg/install:185:export EXAMPLES
spkg/standard/deps:48:     $(INST)/$(EXAMPLES) \
spkg/standard/deps:398:$(INST)/$(EXAMPLES): $(BASE) $(INST)/$(PATCH)
spkg/standard/deps:399:	$(INSTALL) "$(SAGE_SPKG) $(EXAMPLES) 2>&1" "tee -a $(SAGE_LOGS)/$(EXAMPLES).log"
```



---

archive/issue_comments_063213.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-09-27T18:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63213",
    "user": "https://github.com/nexttime"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063214.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-27T19:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63214",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063215.json:
```json
{
    "body": "I think this searches through all of the relevant files:\n\n```\n$ grep -win examples `hg manifest`\n```\nI'm attaching a patch for this.  In addition to the two files you found, it also patches libdist_filelist, which looks like it is *completely* out of date, but it doesn't hurt to patch it anyway.",
    "created_at": "2011-09-27T19:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63215",
    "user": "https://github.com/jhpalmieri"
}
```

I think this searches through all of the relevant files:

```
$ grep -win examples `hg manifest`
```
I'm attaching a patch for this.  In addition to the two files you found, it also patches libdist_filelist, which looks like it is *completely* out of date, but it doesn't hurt to patch it anyway.



---

archive/issue_comments_063216.json:
```json
{
    "body": "root repo",
    "created_at": "2011-09-27T19:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63216",
    "user": "https://github.com/jhpalmieri"
}
```

root repo



---

archive/issue_comments_063217.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-29T01:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63217",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063218.json:
```json
{
    "body": "Attachment [trac_7494-root-repo.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494-root-repo.patch) by @nexttime created at 2011-09-29 01:59:00\n\nOk, I've `sdist`ed with a version with the patches applied, built the new Sage distribution from scratch, and all (long) tests pass.\n\nAs expected, I got rid of the `examples/` directory and the spkg in the new distro.\n(Note that also the examples spkg in `spkg/standard/` of the *original* distribution got deleted; not sure whether this is intentional. In contrast, the `examples/` directory there remained.)\n\nUpgrading from a path without an examples spkg *should*<sup>TM</sup> IMHO also work; haven't tried that [yet].\n\n\n\n\nDon't know yet whether Jeroen's merger is \"prepared\" for such an operation, and since Sage 4.7.2.alpha3 is almost out, I don't think I'll attempt to merge this ticket into *this* release. There'll certainly be an alpha4, or we could try with the next release candidate.\n\nUnfortunately we don't win much regarding the size; the current examples spkg is just 2.0 MB, 3.9 MB uncompressed on my disk (i.e., the size of the `examples/` directory), and just 2.6 MB in \"real\" bytes.",
    "created_at": "2011-09-29T01:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63218",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_7494-root-repo.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494-root-repo.patch) by @nexttime created at 2011-09-29 01:59:00

Ok, I've `sdist`ed with a version with the patches applied, built the new Sage distribution from scratch, and all (long) tests pass.

As expected, I got rid of the `examples/` directory and the spkg in the new distro.
(Note that also the examples spkg in `spkg/standard/` of the *original* distribution got deleted; not sure whether this is intentional. In contrast, the `examples/` directory there remained.)

Upgrading from a path without an examples spkg *should*<sup>TM</sup> IMHO also work; haven't tried that [yet].




Don't know yet whether Jeroen's merger is "prepared" for such an operation, and since Sage 4.7.2.alpha3 is almost out, I don't think I'll attempt to merge this ticket into *this* release. There'll certainly be an alpha4, or we could try with the next release candidate.

Unfortunately we don't win much regarding the size; the current examples spkg is just 2.0 MB, 3.9 MB uncompressed on my disk (i.e., the size of the `examples/` directory), and just 2.6 MB in "real" bytes.



---

archive/issue_comments_063219.json:
```json
{
    "body": "Problems while building the documentation:\n\n```\ndochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha4/local/lib/python2.6/site-packages/sage/finance/stock.py:docstring of sage.finance.stock.OHLC:3: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\ndochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha4/local/lib/python2.6/site-packages/sage/finance/stock.py:docstring of sage.finance.stock.OHLC:8: (ERROR/3) Unexpected indentation.\n```",
    "created_at": "2011-10-04T21:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63219",
    "user": "https://github.com/jdemeyer"
}
```

Problems while building the documentation:

```
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha4/local/lib/python2.6/site-packages/sage/finance/stock.py:docstring of sage.finance.stock.OHLC:3: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha4/local/lib/python2.6/site-packages/sage/finance/stock.py:docstring of sage.finance.stock.OHLC:8: (ERROR/3) Unexpected indentation.
```



---

archive/issue_comments_063220.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-10-04T21:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63220",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063221.json:
```json
{
    "body": "I believe this referee patch should fix the documentation problem.",
    "created_at": "2011-10-04T22:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63221",
    "user": "https://github.com/jhpalmieri"
}
```

I believe this referee patch should fix the documentation problem.



---

archive/issue_comments_063222.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-04T22:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63222",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063223.json:
```json
{
    "body": "Attachment [trac_7494-ref.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494-ref.patch) by @jhpalmieri created at 2011-10-04 22:37:15\n\nSage library: fix docbuilding problem",
    "created_at": "2011-10-04T22:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63223",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7494-ref.patch](tarball://root/attachments/some-uuid/ticket7494/trac_7494-ref.patch) by @jhpalmieri created at 2011-10-04 22:37:15

Sage library: fix docbuilding problem



---

archive/issue_comments_063224.json:
```json
{
    "body": "Replying to [comment:22 jhpalmieri]:\n> I believe this referee patch should fix the documentation problem.\n\n\nBelief is not a technical category.\n\nNice patch by the way.",
    "created_at": "2011-10-05T00:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63224",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:22 jhpalmieri]:
> I believe this referee patch should fix the documentation problem.


Belief is not a technical category.

Nice patch by the way.



---

archive/issue_comments_063225.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-05T00:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63225",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063226.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-05T12:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63226",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_017763.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-05T12:19:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7494#event-17763"
}
```



---

archive/issue_comments_063227.json:
```json
{
    "body": "See #11907 for a followup.",
    "created_at": "2011-10-08T17:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7494#issuecomment-63227",
    "user": "https://github.com/jhpalmieri"
}
```

See #11907 for a followup.
