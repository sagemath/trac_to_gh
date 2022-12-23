# Issue 1925: unifying [plotobject].show() interface + tests

archive/issues_001925.json:
```json
{
    "body": "Assignee: was\n\nWhile working on #1766 I was not able to save 3d plots in files. There were also some other  questions about printing/saving 3d plots in the discussion groups. I think there is a need for some unification.\n\nFirst, my proposal is to distinguish between notebook-mode and non-interactive-script mode. I think this is a good idea, because in script mode somebody is usually not interested in a java applet or popup graphic, but want's to save the output.\n\nSecond, the .show() command should work the same. In #1766 I was able to save everything created by matplotlib but not the 3d stuff by tachyon. There should be a general design decision to make this possible. Or using another 3d plotting engine.\n\nThird, there should be some kind of doctest to ensure this. e.g. plotting all possible output formats to a TempFile (python's temp files) and testing if the file exists and has size > 0kb.\n\nThere should also be some information (function returning a list of possible values) about the possible output formats. Also, the documentation of \"plot\" does not mention PDF, but PDF works. \n\nThis Issue is quite general, but I think it touches important problems...\n\nIssue created by migration from https://trac.sagemath.org/ticket/1925\n\n",
    "created_at": "2008-01-25T12:48:47Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "unifying [plotobject].show() interface + tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1925",
    "user": "schilly"
}
```
Assignee: was

While working on #1766 I was not able to save 3d plots in files. There were also some other  questions about printing/saving 3d plots in the discussion groups. I think there is a need for some unification.

First, my proposal is to distinguish between notebook-mode and non-interactive-script mode. I think this is a good idea, because in script mode somebody is usually not interested in a java applet or popup graphic, but want's to save the output.

Second, the .show() command should work the same. In #1766 I was able to save everything created by matplotlib but not the 3d stuff by tachyon. There should be a general design decision to make this possible. Or using another 3d plotting engine.

Third, there should be some kind of doctest to ensure this. e.g. plotting all possible output formats to a TempFile (python's temp files) and testing if the file exists and has size > 0kb.

There should also be some information (function returning a list of possible values) about the possible output formats. Also, the documentation of "plot" does not mention PDF, but PDF works. 

This Issue is quite general, but I think it touches important problems...

Issue created by migration from https://trac.sagemath.org/ticket/1925





---

archive/issue_comments_012215.json:
```json
{
    "body": "> This Issue is quite general, but I think it touches important problems...\n\nThis ticket should be marked invalid and replaced by specific tickets each of\nwhich has a very clear do-able description.  Imagine trying to referee something\nthat does everything described in the description above. \n\n> First, my proposal is to distinguish between notebook-mode \n> and non-interactive-script mode. I think this is a good idea,\n>  because in script mode somebody is usually not interested \n> in a java applet or popup graphic, but want's to save the output.\n\nWe already distinguish between:\n* notebook mode\n* doctest mode\n* non-notebook command-line mode\n\nSo far nobody has even requested the functionality of having yet another\nmode.  Before this level of complexity (hence potential confusion) is introduced,\nit needs to be carefully justified.  Some people would find it very confusing\nthat putting a couple commands in a file foo.sage and doing load foo.sage\nsuddenly makes it so the behavior is different.  This is so far not the case\n*anywhere* in Sage --- why should it be the case specifically with graphics?\nWould that go against how things are done in every other program too (e.g.,\nMathematica)?\n\n\n> Second, the .show() command should work the same. In #1766 I was \n> able to save everything created by matplotlib but not the 3d stuff \n> by tachyon. There should be a general design decision to make this \n> possible. Or using another 3d plotting engine.\n\nI'm not sure what this is suggesting actually. \n\n\n> Third, there should be some kind of doctest to ensure this. e.g. \n> plotting all possible output formats to a TempFile? (python's temp \n> files) and testing if the file exists and has size > 0kb.\n\nYes, everything needs doctests.  By the way, when 3d graphics are\ndoctested, every graphic is rendered using tachyon to I think a 10x10\nimage file, just to make sure rendering doesn't blow anything up.\n\n> There should also be some information (function returning a list \n> of possible values) about the possible output formats. Also, the \n> documentation of \"plot\" does not mention PDF, but PDF works.\n\nBy plot, do you actually mean the show or save commands called\non the output of plot?  In any case, they don't mention pdf because\npdf output was really preliminary in matplotlib for a long time.  I\ndon't know if that is still the case.  PDF seems to work well now\nwhen I tried a few random plots with it, so it's probably time to\ndocument this output format.",
    "created_at": "2008-01-25T13:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1925#issuecomment-12215",
    "user": "was"
}
```

> This Issue is quite general, but I think it touches important problems...

This ticket should be marked invalid and replaced by specific tickets each of
which has a very clear do-able description.  Imagine trying to referee something
that does everything described in the description above. 

> First, my proposal is to distinguish between notebook-mode 
> and non-interactive-script mode. I think this is a good idea,
>  because in script mode somebody is usually not interested 
> in a java applet or popup graphic, but want's to save the output.

We already distinguish between:
* notebook mode
* doctest mode
* non-notebook command-line mode

So far nobody has even requested the functionality of having yet another
mode.  Before this level of complexity (hence potential confusion) is introduced,
it needs to be carefully justified.  Some people would find it very confusing
that putting a couple commands in a file foo.sage and doing load foo.sage
suddenly makes it so the behavior is different.  This is so far not the case
*anywhere* in Sage --- why should it be the case specifically with graphics?
Would that go against how things are done in every other program too (e.g.,
Mathematica)?


> Second, the .show() command should work the same. In #1766 I was 
> able to save everything created by matplotlib but not the 3d stuff 
> by tachyon. There should be a general design decision to make this 
> possible. Or using another 3d plotting engine.

I'm not sure what this is suggesting actually. 


> Third, there should be some kind of doctest to ensure this. e.g. 
> plotting all possible output formats to a TempFile? (python's temp 
> files) and testing if the file exists and has size > 0kb.

Yes, everything needs doctests.  By the way, when 3d graphics are
doctested, every graphic is rendered using tachyon to I think a 10x10
image file, just to make sure rendering doesn't blow anything up.

> There should also be some information (function returning a list 
> of possible values) about the possible output formats. Also, the 
> documentation of "plot" does not mention PDF, but PDF works.

By plot, do you actually mean the show or save commands called
on the output of plot?  In any case, they don't mention pdf because
pdf output was really preliminary in matplotlib for a long time.  I
don't know if that is still the case.  PDF seems to work well now
when I tried a few random plots with it, so it's probably time to
document this output format.
