# Issue 595: get lie to build on all standard machines -- specific problems

archive/issues_000595.json:
```json
{
    "body": "Assignee: was\n\nHere is a problem reported on sage-support by David DeGeorge:\n\n\n```\nDear Developers\nI am running Suse 10.1  and\nsage-2.8.3-32bit-linux-suse10-i686-Linux\nI can't get lie to build. It complains about not finding -lcurses.\nlibcurses.a is\nnot in a standard place (it is in /usr/lib/curses), I tried adding a\nsymbolic link to\n/usr/lib but then the build failed in readline.\n1. Here is the part where -lcurses was the problem\ngcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o\ngettype.o getvalue.o init.o learn.o main.o mem.o node.o onoff.o output.o\npoly.o sym.o print.o getl.o date.o static/*.o box/*.o -lreadline -lcurses\n/usr/lib/gcc/i586-suse-linux/4.1.0/../../../../i586-suse-linux/bin/ld:\ncannot find -lcurses\n2. Here is a part of what happened after I added a link in /usr/lib to\n/usr/lib/curses/libcurses.a\n\ngcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o\ngettype.o getval\nue.o init.o learn.o main.o mem.o node.o onoff.o output.o poly.o sym.o\nprint.o getl.o dat\ne.o static/*.o box/*.o -lreadline -lcurses\nlearn.o: In function `Learn':\nlearn.c:(.text+0x542): warning: the use of `tmpnam' is dangerous, better\nuse `mkstemp'\n/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:\nundefined\nreference to `tgetnum'\n/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:\nundefined\nreference to `tgoto'\n/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:\nundefined\nreference to `tgetflag'\n/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:\nundefined\nreference to `tputs'\n/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:\nundefined\nreference to `tgetent'\n/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:\nundefined\nreference to `tgetstr'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/595\n\n",
    "created_at": "2007-09-05T18:01:06Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "get lie to build on all standard machines -- specific problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/595",
    "user": "was"
}
```
Assignee: was

Here is a problem reported on sage-support by David DeGeorge:


```
Dear Developers
I am running Suse 10.1  and
sage-2.8.3-32bit-linux-suse10-i686-Linux
I can't get lie to build. It complains about not finding -lcurses.
libcurses.a is
not in a standard place (it is in /usr/lib/curses), I tried adding a
symbolic link to
/usr/lib but then the build failed in readline.
1. Here is the part where -lcurses was the problem
gcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o
gettype.o getvalue.o init.o learn.o main.o mem.o node.o onoff.o output.o
poly.o sym.o print.o getl.o date.o static/*.o box/*.o -lreadline -lcurses
/usr/lib/gcc/i586-suse-linux/4.1.0/../../../../i586-suse-linux/bin/ld:
cannot find -lcurses
2. Here is a part of what happened after I added a link in /usr/lib to
/usr/lib/curses/libcurses.a

gcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o
gettype.o getval
ue.o init.o learn.o main.o mem.o node.o onoff.o output.o poly.o sym.o
print.o getl.o dat
e.o static/*.o box/*.o -lreadline -lcurses
learn.o: In function `Learn':
learn.c:(.text+0x542): warning: the use of `tmpnam' is dangerous, better
use `mkstemp'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetnum'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgoto'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetflag'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tputs'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetent'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetstr'
```


Issue created by migration from https://trac.sagemath.org/ticket/595





---

archive/issue_comments_003065.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2007-09-05T18:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3065",
    "user": "was"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_003066.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-09-05T18:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3066",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_003067.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-06T21:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3067",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003068.json:
```json
{
    "body": "There is a new lie.spkg at \n\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/lie-2.2.2.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-09-07T00:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3068",
    "user": "mabshoff"
}
```

There is a new lie.spkg at 

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/lie-2.2.2.p3.spkg

Cheers,

Michael



---

archive/issue_comments_003069.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T00:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3069",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_003070.json:
```json
{
    "body": "posted, hence done.",
    "created_at": "2007-09-07T00:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3070",
    "user": "was"
}
```

posted, hence done.



---

archive/issue_comments_003071.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-07T00:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3071",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_003072.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-07T00:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3072",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T01:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/595#issuecomment-3073",
    "user": "was"
}
```

Resolution: fixed
