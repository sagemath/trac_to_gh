# Issue 3131: README.txt: update recommendations for dev work with binaries

archive/issues_003131.json:
```json
{
    "body": "Assignee: tba\n\n\n```\nAside from all the other issues: You should *always* rebuild the Sage\nlibrary of a binary build before running clone. Otherwise each clone\nrequires a complete rebuild. Aside from that it is *highly*\nrecommended to build from source if you are developing since mixing\nand matching different compiler releases [even on OSX] can lead to odd\nresults, i.e. Heisenbugs and segfaults.\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3131\n\n",
    "created_at": "2008-05-08T12:47:56Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "README.txt: update recommendations for dev work with binaries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3131",
    "user": "mabshoff"
}
```
Assignee: tba


```
Aside from all the other issues: You should *always* rebuild the Sage
library of a binary build before running clone. Otherwise each clone
requires a complete rebuild. Aside from that it is *highly*
recommended to build from source if you are developing since mixing
and matching different compiler releases [even on OSX] can lead to odd
results, i.e. Heisenbugs and segfaults.
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3131





---

archive/issue_comments_021720.json:
```json
{
    "body": "Changing assignee from tba to mabshoff.",
    "created_at": "2008-05-08T12:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21720",
    "user": "mabshoff"
}
```

Changing assignee from tba to mabshoff.



---

archive/issue_comments_021721.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-08T12:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21721",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021722.json:
```json
{
    "body": "Maybe this should go into \"Section 7.1 of the Sage Programming Guide\" instead.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-08T12:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21722",
    "user": "mabshoff"
}
```

Maybe this should go into "Section 7.1 of the Sage Programming Guide" instead.

Cheers,

Michael



---

archive/issue_comments_021723.json:
```json
{
    "body": "This became invalid when we switched to git.",
    "created_at": "2014-08-13T22:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21723",
    "user": "@a-andre"
}
```

This became invalid when we switched to git.



---

archive/issue_comments_021724.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-13T22:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21724",
    "user": "@a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_021725.json:
```json
{
    "body": "Hmm, good point!  I just saw this too.  Are there any instructions we need to give people about how to develop with binaries?  (Such as, you really need to build from scratch.)  Maybe this is already in the much-underused installation guide...",
    "created_at": "2014-08-14T13:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21725",
    "user": "@kcrisman"
}
```

Hmm, good point!  I just saw this too.  Are there any instructions we need to give people about how to develop with binaries?  (Such as, you really need to build from scratch.)  Maybe this is already in the much-underused installation guide...



---

archive/issue_comments_021726.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-08-14T13:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21726",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_021727.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> Are there any instructions we need to give people about how to develop with binaries?  (Such as, you really need to build from scratch.)\nExactly: \"don't do it\" is the best advice you can give.",
    "created_at": "2014-08-14T13:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21727",
    "user": "@jdemeyer"
}
```

Replying to [comment:7 kcrisman]:
> Are there any instructions we need to give people about how to develop with binaries?  (Such as, you really need to build from scratch.)
Exactly: "don't do it" is the best advice you can give.



---

archive/issue_comments_021728.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2014-08-15T05:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21728",
    "user": "@kcrisman"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_021729.json:
```json
{
    "body": "Then what I would say is to make this really loud somewhere correct.  The problem is that some stuff in the install guide should really be in the developer guide, as there isn't much about `sage -b` anywhere in there as far as I can tell (maybe in the git sections?).",
    "created_at": "2014-08-15T05:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21729",
    "user": "@kcrisman"
}
```

Then what I would say is to make this really loud somewhere correct.  The problem is that some stuff in the install guide should really be in the developer guide, as there isn't much about `sage -b` anywhere in there as far as I can tell (maybe in the git sections?).



---

archive/issue_comments_021730.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2014-11-20T15:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21730",
    "user": "@kcrisman"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_021731.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-01-28T15:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21731",
    "user": "@mezzarobba"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_021732.json:
```json
{
    "body": "Why would this be wontfix?  Have we already said very loudly \"don't do it\"?",
    "created_at": "2015-01-28T17:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21732",
    "user": "@kcrisman"
}
```

Why would this be wontfix?  Have we already said very loudly "don't do it"?



---

archive/issue_comments_021733.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2015-01-28T17:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21733",
    "user": "@kcrisman"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_021734.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-01-28T18:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21734",
    "user": "@mezzarobba"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_021735.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> Why would this be wontfix?  Have we already said very loudly \"don't do it\"?\n\nOops, sorry, I had the same reaction as you about this becoming meaningless with the switch to git, and I did not notice the recent discussion.",
    "created_at": "2015-01-28T18:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21735",
    "user": "@mezzarobba"
}
```

Replying to [comment:12 kcrisman]:
> Why would this be wontfix?  Have we already said very loudly "don't do it"?

Oops, sorry, I had the same reaction as you about this becoming meaningless with the switch to git, and I did not notice the recent discussion.



---

archive/issue_comments_021736.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> Have we already said very loudly \"don't do it\"?\nIs there a reason why people shouldn't do it? Since when did we stop supporting developing with binaries?",
    "created_at": "2015-01-28T19:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21736",
    "user": "@jdemeyer"
}
```

Replying to [comment:12 kcrisman]:
> Have we already said very loudly "don't do it"?
Is there a reason why people shouldn't do it? Since when did we stop supporting developing with binaries?



---

archive/issue_comments_021737.json:
```json
{
    "body": "**You** said it!  comment:8\n> Exactly: \"don't do it\" is the best advice you can give.\nIf not, then we should say just what prereqs and problems might be necessary/arise.",
    "created_at": "2015-01-28T19:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21737",
    "user": "@kcrisman"
}
```

**You** said it!  comment:8
> Exactly: "don't do it" is the best advice you can give.
If not, then we should say just what prereqs and problems might be necessary/arise.



---

archive/issue_comments_021738.json:
```json
{
    "body": "Funny :-)\n\nMaybe there is a good reason that I currently cannot think of.",
    "created_at": "2015-01-28T19:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21738",
    "user": "@jdemeyer"
}
```

Funny :-)

Maybe there is a good reason that I currently cannot think of.



---

archive/issue_comments_021739.json:
```json
{
    "body": "Well, the obvious reason is that people keep trying to do it and then failing because they don't have gcc or some other prereq, or because of some hard-coded paths that screw things up from the buildbot.  However, maybe saying that people need to be extra-special careful in that event is enough...?",
    "created_at": "2015-01-28T19:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21739",
    "user": "@kcrisman"
}
```

Well, the obvious reason is that people keep trying to do it and then failing because they don't have gcc or some other prereq, or because of some hard-coded paths that screw things up from the buildbot.  However, maybe saying that people need to be extra-special careful in that event is enough...?



---

archive/issue_comments_021740.json:
```json
{
    "body": "So, where do we say \"don't do this\", if at all?",
    "created_at": "2016-02-25T03:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21740",
    "user": "@kcrisman"
}
```

So, where do we say "don't do this", if at all?



---

archive/issue_comments_021741.json:
```json
{
    "body": "On the index of the Developer's Guide (http://doc.sagemath.org/html/en/developer/index.html) it mentions needing the source code which implies that you can't develop from only a binary.\n\nI think that should be sufficient but maybe we need to **direct users in README.md to \"read the Developer's Guide\"** if they would like to contribute. This is already the advice given in the \"Development\" link on the main website (http://www.sagemath.org/development.html) as well as the contributing FAQ (http://doc.sagemath.org/html/en/faq/faq-contribute.html) where it also says to \"...grab a copy of the Sage source...\".\n\nSo, if anything, we can **change the wording in the Developer's Guide to be less suggestive** since that's where all roads to getting started in development should lead.",
    "created_at": "2016-06-25T23:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21741",
    "user": "btdhall"
}
```

On the index of the Developer's Guide (http://doc.sagemath.org/html/en/developer/index.html) it mentions needing the source code which implies that you can't develop from only a binary.

I think that should be sufficient but maybe we need to **direct users in README.md to "read the Developer's Guide"** if they would like to contribute. This is already the advice given in the "Development" link on the main website (http://www.sagemath.org/development.html) as well as the contributing FAQ (http://doc.sagemath.org/html/en/faq/faq-contribute.html) where it also says to "...grab a copy of the Sage source...".

So, if anything, we can **change the wording in the Developer's Guide to be less suggestive** since that's where all roads to getting started in development should lead.



---

archive/issue_comments_021742.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2016-06-26T00:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21742",
    "user": "btdhall"
}
```

Changing priority from major to minor.



---

archive/issue_comments_021743.json:
```json
{
    "body": "Changing assignee from mabshoff to btdhall.",
    "created_at": "2016-06-26T00:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21743",
    "user": "btdhall"
}
```

Changing assignee from mabshoff to btdhall.



---

archive/issue_comments_021744.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-07-02T15:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21744",
    "user": "btdhall"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_021745.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-07-02T15:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21745",
    "user": "btdhall"
}
```

New commits:



---

archive/issue_comments_021746.json:
```json
{
    "body": "`@`btdhall while you're touching this file, there are two occurrences of `sagemath.org/doc/` and two occurrences of `www.sagemath.org/doc/` that should all be changed to `doc.sagemath.org/html/en/`.\n\nI've been trying to help Harald Schilly to get Google to stop indexing the old documentation location and it doesn't help if it's there on the default [GitHub](GitHub) page.",
    "created_at": "2016-07-07T01:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21746",
    "user": "@paulmasson"
}
```

`@`btdhall while you're touching this file, there are two occurrences of `sagemath.org/doc/` and two occurrences of `www.sagemath.org/doc/` that should all be changed to `doc.sagemath.org/html/en/`.

I've been trying to help Harald Schilly to get Google to stop indexing the old documentation location and it doesn't help if it's there on the default [GitHub](GitHub) page.



---

archive/issue_comments_021747.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-07T03:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21747",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_021748.json:
```json
{
    "body": "Looks good. Thanks!",
    "created_at": "2016-07-07T03:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21748",
    "user": "@paulmasson"
}
```

Looks good. Thanks!



---

archive/issue_comments_021749.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-07-07T03:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21749",
    "user": "@paulmasson"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021750.json:
```json
{
    "body": "Replying to [comment:26 paulmasson]:\n> Looks good. Thanks!\nNo problem.\n\nWhile we're on the topic, the errata ([http://wiki.sagemath.org/errata](http://wiki.sagemath.org/errata)) links to an empty wiki page but I couldn't find the proper location. Let me know if you have a suggestion for fixing it.",
    "created_at": "2016-07-07T03:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21750",
    "user": "btdhall"
}
```

Replying to [comment:26 paulmasson]:
> Looks good. Thanks!
No problem.

While we're on the topic, the errata ([http://wiki.sagemath.org/errata](http://wiki.sagemath.org/errata)) links to an empty wiki page but I couldn't find the proper location. Let me know if you have a suggestion for fixing it.



---

archive/issue_comments_021751.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-07-08T07:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3131#issuecomment-21751",
    "user": "@vbraun"
}
```

Resolution: fixed
