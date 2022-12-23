# Issue 6287: sage -lisp should run ECL

archive/issues_006287.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  awebb\n\nWhen we upgraded Sage from Clisp to ECL we forgot to make it so\n\n```\nsage -lisp\n```\n \nworks and runs ecl.  Right now it still runs clisp if that happens to be on your system, which is silly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6287\n\n",
    "created_at": "2009-06-14T20:56:44Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "sage -lisp should run ECL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6287",
    "user": "was"
}
```
Assignee: mabshoff

CC:  awebb

When we upgraded Sage from Clisp to ECL we forgot to make it so

```
sage -lisp
```
 
works and runs ecl.  Right now it still runs clisp if that happens to be on your system, which is silly.


Issue created by migration from https://trac.sagemath.org/ticket/6287





---

archive/issue_comments_050197.json:
```json
{
    "body": "Replaced sage -clisp with sage -ecl and pointed sage -lisp at ecl.",
    "created_at": "2009-06-21T13:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50197",
    "user": "awebb"
}
```

Replaced sage -clisp with sage -ecl and pointed sage -lisp at ecl.



---

archive/issue_comments_050198.json:
```json
{
    "body": "Attachment\n\noops, forgot to change clisp to ecl in one line.  ~ Adam",
    "created_at": "2009-08-17T10:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50198",
    "user": "awebb"
}
```

Attachment

oops, forgot to change clisp to ecl in one line.  ~ Adam



---

archive/issue_comments_050199.json:
```json
{
    "body": "Can you post a link to an .spkg I can test. I'll then review this.",
    "created_at": "2009-08-19T13:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50199",
    "user": "drkirkby"
}
```

Can you post a link to an .spkg I can test. I'll then review this.



---

archive/issue_comments_050200.json:
```json
{
    "body": "There is only the patch for the sage-sage script. When I made it I did not know which spkg it was in but I believe it is in sage-scripts. I just applied the patch directly to the mercurial repository in sage/local/bin. ~ Adam",
    "created_at": "2009-08-19T15:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50200",
    "user": "awebb"
}
```

There is only the patch for the sage-sage script. When I made it I did not know which spkg it was in but I believe it is in sage-scripts. I just applied the patch directly to the mercurial repository in sage/local/bin. ~ Adam



---

archive/issue_comments_050201.json:
```json
{
    "body": "I'm not really sure how to check this. I tried to build clisp on my SPARC, but I was unable to get it to build with either gcc or the Sun compiler. I then thought I'd create a dummy executable 'clisp', put that early in my path, and see if sage would run that, rather than ecl. But all I get is an error about a command not being found. \n\n\n```\n[~/sage/sage-4.1.1] $ ./sage -lisp\n/export/home/drkirkby/sage/sage-4.1.1/local/bin/sage-sage: line 297: lisp: command not found\n```\n\n\nDespite having the directory with 'clisp' early in the path, maxima in Sage still pick up 'ecl'. \n\nSorry, but I don't feel able to test this, as I can't build clisp and are not really sure what should happen. \n\nDave",
    "created_at": "2009-08-20T10:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50201",
    "user": "drkirkby"
}
```

I'm not really sure how to check this. I tried to build clisp on my SPARC, but I was unable to get it to build with either gcc or the Sun compiler. I then thought I'd create a dummy executable 'clisp', put that early in my path, and see if sage would run that, rather than ecl. But all I get is an error about a command not being found. 


```
[~/sage/sage-4.1.1] $ ./sage -lisp
/export/home/drkirkby/sage/sage-4.1.1/local/bin/sage-sage: line 297: lisp: command not found
```


Despite having the directory with 'clisp' early in the path, maxima in Sage still pick up 'ecl'. 

Sorry, but I don't feel able to test this, as I can't build clisp and are not really sure what should happen. 

Dave



---

archive/issue_comments_050202.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n\n> Despite having the directory with 'clisp' early in the path, maxima in Sage still pick up 'ecl'. \n> \n> Sorry, but I don't feel able to test this, as I can't build clisp and are not really sure what should happen. \n> \n> Dave \n\nHi,\nThe whole point of the ticket is that clisp is no longer used and that sage should look for ecl instead. The patch tells 'sage -lisp' to use ecl instead of clisp. I also added a 'sage -ecl' which does the same thing. In other words, if either command is used from the shell you get the ecl console. I took out 'sage -clisp' but should it stay for if someone wants it?\n\nAdam",
    "created_at": "2009-08-20T11:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50202",
    "user": "awebb"
}
```

Replying to [comment:7 drkirkby]:

> Despite having the directory with 'clisp' early in the path, maxima in Sage still pick up 'ecl'. 
> 
> Sorry, but I don't feel able to test this, as I can't build clisp and are not really sure what should happen. 
> 
> Dave 

Hi,
The whole point of the ticket is that clisp is no longer used and that sage should look for ecl instead. The patch tells 'sage -lisp' to use ecl instead of clisp. I also added a 'sage -ecl' which does the same thing. In other words, if either command is used from the shell you get the ecl console. I took out 'sage -clisp' but should it stay for if someone wants it?

Adam



---

archive/issue_comments_050203.json:
```json
{
    "body": "Replying to [comment:8 awebb]:\n> The whole point of the ticket is that clisp is no longer used and that sage should look for ecl instead.\n\nCorrect.\n\n> The patch tells 'sage -lisp' to use ecl instead of clisp. I also added a 'sage -ecl' which does the same thing.\n\nGreat.\n\n> I took out 'sage -clisp' but should it stay for if someone wants it?\n\nI agree that it should be removed. All commands of the form `sage -program` run the version of `program` distributed with sage. Since we are no longer distributing clisp, keeping the clisp alias has the potential of causing confusion for a user.\n\n**Positive review**: the patch applies cleanly on top of sage-4.1.1; and `sage -ecl` and `sage -lisp` now work as they should.",
    "created_at": "2009-08-28T14:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50203",
    "user": "saliola"
}
```

Replying to [comment:8 awebb]:
> The whole point of the ticket is that clisp is no longer used and that sage should look for ecl instead.

Correct.

> The patch tells 'sage -lisp' to use ecl instead of clisp. I also added a 'sage -ecl' which does the same thing.

Great.

> I took out 'sage -clisp' but should it stay for if someone wants it?

I agree that it should be removed. All commands of the form `sage -program` run the version of `program` distributed with sage. Since we are no longer distributing clisp, keeping the clisp alias has the potential of causing confusion for a user.

**Positive review**: the patch applies cleanly on top of sage-4.1.1; and `sage -ecl` and `sage -lisp` now work as they should.



---

archive/issue_comments_050204.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T11:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50204",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050205.json:
```json
{
    "body": "Doing any of these \"./sage -ecl\" or \"./sage -lisp\" would run ECL as expected. Also:\n\n```\nsage: !ecl\nECL (Embeddable Common-Lisp) 9.4.1\nCopyright (C) 1984 Taiichi Yuasa and Masami Hagiya\nCopyright (C) 1993 Giuseppe Attardi\nCopyright (C) 2000 Juan J. Garcia-Ripoll\nECL is free software, and you are welcome to redistribute it\nunder certain conditions; see file 'Copyright' for details.\nType :h for Help.  Top level.\n>\n```\n\nAnd if Clisp is installed on your system:\n\n```\nsage: !clisp\n  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo\n  I I I I I I I      8     8   8           8     8     o  8    8\n  I  \\ `+' /  I      8         8           8     8        8    8\n   \\  `-+-'  /       8         8           8      ooooo   8oooo\n    `-__|__-'        8         8           8           8  8\n        |            8     o   8           8     o     8  8\n  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8\n\nWelcome to GNU CLISP 2.42 (2007-10-16) <http://clisp.cons.org/>\n\nCopyright (c) Bruno Haible, Michael Stoll 1992, 1993\nCopyright (c) Bruno Haible, Marcus Daniels 1994-1997\nCopyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998\nCopyright (c) Bruno Haible, Sam Steingold 1999-2000\nCopyright (c) Sam Steingold, Bruno Haible 2001-2007\n\nType :h and hit Enter for context help.\n\n[1]> :h\nYou are in the top-level Read-Eval-Print loop.\nHelp (abbreviated :h) = this list\nUse the usual editing capabilities.\n(quit) or (exit) leaves CLISP.\n[2]> \nBye.\n```\n\nSo one still has the option of running Clisp from within the Sage command line interface.",
    "created_at": "2009-08-30T11:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6287#issuecomment-50205",
    "user": "mvngu"
}
```

Doing any of these "./sage -ecl" or "./sage -lisp" would run ECL as expected. Also:

```
sage: !ecl
ECL (Embeddable Common-Lisp) 9.4.1
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  Top level.
>
```

And if Clisp is installed on your system:

```
sage: !clisp
  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8

Welcome to GNU CLISP 2.42 (2007-10-16) <http://clisp.cons.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2007

Type :h and hit Enter for context help.

[1]> :h
You are in the top-level Read-Eval-Print loop.
Help (abbreviated :h) = this list
Use the usual editing capabilities.
(quit) or (exit) leaves CLISP.
[2]> 
Bye.
```

So one still has the option of running Clisp from within the Sage command line interface.
