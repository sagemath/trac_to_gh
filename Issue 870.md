# Issue 870: singular.spkg requires bison to build

archive/issues_000870.json:
```json
{
    "body": "Assignee: malb\n\nSee http://groups.google.com/group/sage-forum/browse_thread/thread/6f56a3cc9f4a1598\n\nTo quote malb:\n\n```\nHi,\n\nSAGE 2.8.5 shipped a version of Singular where we got rid of the dependency of\nbison/flex ourselves. SAGE 2.8.6 removes this workaround because Singular\n3-0-3-1 handles this itself.\n\nHowever, it seems the Singular team forgot to take care of the factory\nlibrary. There are three ways to solve this issue for you:\n\n(a) Install bison for now\n\n(b) replace\n\n$(srcdir)/readcf.cc: readcf.y\n        $(BISON) $< -o $@; \\\n\nwith\n\n$(srcdir)/readcf.cc: readcf.y\n                @if test -r $@; then \\\n                        touch $@ ;\\\n                else \\\n                if test \"${BISON}\" = where-is-your-bison; then \\\n                        echo Error: no bison given, could not rebuilt\ngrammar.cc; \\\n                        exit 1; \\\n                fi; \\\n                $(BISON) $< -o $@; \\\n                fi\n\nin the singular spkg / factory/GNUmakefile.in or drop in the attached file.\nThis requires that you know a little about SAGE SPKGs.\n\n(c) wait until I got confirmation from the Singular team and provide an\nupdated SPKG. (I am BCC'ing Hans Sch\u00f6nemann from the Singular team with this\ne-mail)\n\nCheers,\nMartin \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/870\n\n",
    "created_at": "2007-10-13T02:11:40Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "singular.spkg requires bison to build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/870",
    "user": "mabshoff"
}
```
Assignee: malb

See http://groups.google.com/group/sage-forum/browse_thread/thread/6f56a3cc9f4a1598

To quote malb:

```
Hi,

SAGE 2.8.5 shipped a version of Singular where we got rid of the dependency of
bison/flex ourselves. SAGE 2.8.6 removes this workaround because Singular
3-0-3-1 handles this itself.

However, it seems the Singular team forgot to take care of the factory
library. There are three ways to solve this issue for you:

(a) Install bison for now

(b) replace

$(srcdir)/readcf.cc: readcf.y
        $(BISON) $< -o $@; \

with

$(srcdir)/readcf.cc: readcf.y
                @if test -r $@; then \
                        touch $@ ;\
                else \
                if test "${BISON}" = where-is-your-bison; then \
                        echo Error: no bison given, could not rebuilt
grammar.cc; \
                        exit 1; \
                fi; \
                $(BISON) $< -o $@; \
                fi

in the singular spkg / factory/GNUmakefile.in or drop in the attached file.
This requires that you know a little about SAGE SPKGs.

(c) wait until I got confirmation from the Singular team and provide an
updated SPKG. (I am BCC'ing Hans Schönemann from the Singular team with this
e-mail)

Cheers,
Martin 
```


Issue created by migration from https://trac.sagemath.org/ticket/870





---

archive/issue_comments_005364.json:
```json
{
    "body": "malb's temporary solution",
    "created_at": "2007-10-13T02:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/870#issuecomment-5364",
    "user": "mabshoff"
}
```

malb's temporary solution



---

archive/issue_comments_005365.json:
```json
{
    "body": "Attachment [GNUmakefile.in](tarball://root/attachments/some-uuid/ticket870/GNUmakefile.in) by was created at 2007-10-13 07:37:25",
    "created_at": "2007-10-13T07:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/870#issuecomment-5365",
    "user": "was"
}
```

Attachment [GNUmakefile.in](tarball://root/attachments/some-uuid/ticket870/GNUmakefile.in) by was created at 2007-10-13 07:37:25



---

archive/issue_comments_005366.json:
```json
{
    "body": "This is fixed in Singular 3-0-3-2 and an updated spkg can be found at\n http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071020.spkg",
    "created_at": "2007-10-20T18:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/870#issuecomment-5366",
    "user": "malb"
}
```

This is fixed in Singular 3-0-3-2 and an updated spkg can be found at
 http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071020.spkg



---

archive/issue_comments_005367.json:
```json
{
    "body": "This is fixed in Singular 3-0-3-2 and an updated spkg can be found at \n\nhttp://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071020.spkg",
    "created_at": "2007-10-20T18:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/870#issuecomment-5367",
    "user": "malb"
}
```

This is fixed in Singular 3-0-3-2 and an updated spkg can be found at 

http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071020.spkg



---

archive/issue_comments_005368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T18:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/870#issuecomment-5368",
    "user": "was"
}
```

Resolution: fixed
