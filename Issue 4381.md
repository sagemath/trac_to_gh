# Issue 4381: sage -wthread not passed correctly to ipython

archive/issues_004381.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mhansen burcin\n\nOff sage-3.1.3 passing the argument -wthread is not correct. The argument -wthread must be the first argument passed to ipython in order to take effect.\n\nSee the changes from sage-3.1.2 to sage-3.1.3 in the file $SAGE_ROOT/local/bin/sage-sage:\n\n\n\n```\n[jaap@paix bin]$ diff sage-sage ../../../sage-3.1.2/local/bin/sage-sage\n51d50\n<     echo \"  -combinat <...> -- run sage-combinat patch management script\"\n188a188,203\n> SAGE_STARTUP=\"\n> import sage.misc.misc; print \\\n> sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg()); \\\n> from sage.misc.interpreter import preparser; preparser(True);\\\n> import sage.all_cmdline; sage.all_cmdline._init_cmdline(globals());\\\n> from sage.all import Integer, RealNumber;\\\n> import os; os.chdir(\\\"$CUR\\\");\\\n> import sage.misc.interpreter;\\\n> from sage.misc.interpreter import attached_files\\\n> \"\n> \n> if [ \"$SAGE_IMPORTALL\" != \"no\" ]; then\n>    SAGE_STARTUP_COMMAND=\"$SAGE_STARTUP\"\";from sage.all_cmdline import *\"\n> else\n>    SAGE_STARTUP_COMMAND=\"$SAGE_STARTUP\"\n> fi\n189a205,206\n> SAGE_STARTUP_COMMAND=\"$SAGE_STARTUP_COMMAND\"\";_=sage.misc.interpreter.load_startup_file(\\\"$SAGE_STARTUP_FILE\\\")\"\n> export SAGE_STARTUP_COMMAND\n200c217\n<     sage-ipython \"$@\" -i\n---\n>     sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n251,257d267\n< if [ $1 = '-combinat' -o $1 = '--combinat' ]; then\n<     cd \"$CUR\"\n<     shift\n<     sage-combinat \"$@\"\n<     exit $?\n< fi\n< \n514c524\n<    sage-ipython  $LOGOPT -rcfile=\"$IPYTHONRC\" -i -c \"$SAGE_STARTUP_COMMAND\" \"$@\" \n---\n>    sage-ipython  $LOGOPT -rcfile=\"$IPYTHONRC\" -c \"$SAGE_STARTUP_COMMAND\" \"$@\"\n[jaap@paix bin]$ \n\n\n```\n\n\n\ncwitty to the rescue?\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4381\n\n",
    "created_at": "2008-10-29T19:26:07Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "sage -wthread not passed correctly to ipython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4381",
    "user": "jsp"
}
```
Assignee: cwitty

CC:  mhansen burcin

Off sage-3.1.3 passing the argument -wthread is not correct. The argument -wthread must be the first argument passed to ipython in order to take effect.

See the changes from sage-3.1.2 to sage-3.1.3 in the file $SAGE_ROOT/local/bin/sage-sage:



```
[jaap@paix bin]$ diff sage-sage ../../../sage-3.1.2/local/bin/sage-sage
51d50
<     echo "  -combinat <...> -- run sage-combinat patch management script"
188a188,203
> SAGE_STARTUP="
> import sage.misc.misc; print \
> sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg()); \
> from sage.misc.interpreter import preparser; preparser(True);\
> import sage.all_cmdline; sage.all_cmdline._init_cmdline(globals());\
> from sage.all import Integer, RealNumber;\
> import os; os.chdir(\"$CUR\");\
> import sage.misc.interpreter;\
> from sage.misc.interpreter import attached_files\
> "
> 
> if [ "$SAGE_IMPORTALL" != "no" ]; then
>    SAGE_STARTUP_COMMAND="$SAGE_STARTUP"";from sage.all_cmdline import *"
> else
>    SAGE_STARTUP_COMMAND="$SAGE_STARTUP"
> fi
189a205,206
> SAGE_STARTUP_COMMAND="$SAGE_STARTUP_COMMAND"";_=sage.misc.interpreter.load_startup_file(\"$SAGE_STARTUP_FILE\")"
> export SAGE_STARTUP_COMMAND
200c217
<     sage-ipython "$@" -i
---
>     sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
251,257d267
< if [ $1 = '-combinat' -o $1 = '--combinat' ]; then
<     cd "$CUR"
<     shift
<     sage-combinat "$@"
<     exit $?
< fi
< 
514c524
<    sage-ipython  $LOGOPT -rcfile="$IPYTHONRC" -i -c "$SAGE_STARTUP_COMMAND" "$@" 
---
>    sage-ipython  $LOGOPT -rcfile="$IPYTHONRC" -c "$SAGE_STARTUP_COMMAND" "$@"
[jaap@paix bin]$ 


```



cwitty to the rescue?

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/4381





---

archive/issue_comments_032233.json:
```json
{
    "body": "Don't know for sure but #3945 could be the culprit.\n\n[http://trac.sagemath.org/sage_trac/ticket/3945](http://trac.sagemath.org/sage_trac/ticket/3945)\n\nJaap",
    "created_at": "2008-10-30T14:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32233",
    "user": "jsp"
}
```

Don't know for sure but #3945 could be the culprit.

[http://trac.sagemath.org/sage_trac/ticket/3945](http://trac.sagemath.org/sage_trac/ticket/3945)

Jaap



---

archive/issue_comments_032234.json:
```json
{
    "body": "#3945 is more than likely the culprit here since nothing else touched ipython related scripts in 3.1.2->3.1.3.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T14:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32234",
    "user": "mabshoff"
}
```

#3945 is more than likely the culprit here since nothing else touched ipython related scripts in 3.1.2->3.1.3.

Cheers,

Michael



---

archive/issue_comments_032235.json:
```json
{
    "body": "After talking to Fernando Perez at SD 11 it is more than a five minute fix in IPython, so we should patch around it for now. In the long term the issue will be fixed in IPython :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T23:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32235",
    "user": "mabshoff"
}
```

After talking to Fernando Perez at SD 11 it is more than a five minute fix in IPython, so we should patch around it for now. In the long term the issue will be fixed in IPython :)

Cheers,

Michael



---

archive/issue_comments_032236.json:
```json
{
    "body": "After applying the patch to sage-3.2.1.alpha0:\n\n\n\n```\n mhansen: after installing wxPython in sage-3.2.1.alph0 I get:\n<jaap> [jaap@paix sage-3.2.1.alpha0]$ ./sage -wthread\n<jaap> ----------------------------------------------------------------------\n<jaap> | Sage Version 3.2.1.alpha0, Release Date: 2008-11-23                |\n<jaap> | Type notebook() for the GUI, and license() for information.        |\n<jaap> ----------------------------------------------------------------------\n<jaap> ------------------------------------------------------------\n<jaap>    File \"<ipython console>\", line 1\n<jaap>      /home/jaap/downloads/sage-3.2.1.alpha0/local/bin/sage-startup\n<jaap>      ^\n<jaap> SyntaxError: invalid syntax\n<mhansen> Hmm...\n```\n",
    "created_at": "2008-11-25T23:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32236",
    "user": "jsp"
}
```

After applying the patch to sage-3.2.1.alpha0:



```
 mhansen: after installing wxPython in sage-3.2.1.alph0 I get:
<jaap> [jaap@paix sage-3.2.1.alpha0]$ ./sage -wthread
<jaap> ----------------------------------------------------------------------
<jaap> | Sage Version 3.2.1.alpha0, Release Date: 2008-11-23                |
<jaap> | Type notebook() for the GUI, and license() for information.        |
<jaap> ----------------------------------------------------------------------
<jaap> ------------------------------------------------------------
<jaap>    File "<ipython console>", line 1
<jaap>      /home/jaap/downloads/sage-3.2.1.alpha0/local/bin/sage-startup
<jaap>      ^
<jaap> SyntaxError: invalid syntax
<mhansen> Hmm...
```




---

archive/issue_comments_032237.json:
```json
{
    "body": "Attachment [trac_4381.patch](tarball://root/attachments/some-uuid/ticket4381/trac_4381.patch) by mhansen created at 2008-11-26 00:19:37",
    "created_at": "2008-11-26T00:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32237",
    "user": "mhansen"
}
```

Attachment [trac_4381.patch](tarball://root/attachments/some-uuid/ticket4381/trac_4381.patch) by mhansen created at 2008-11-26 00:19:37



---

archive/issue_comments_032238.json:
```json
{
    "body": "New patch worked for me!\n\nPositive review,\n\nJaap",
    "created_at": "2008-11-26T01:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32238",
    "user": "jsp"
}
```

New patch worked for me!

Positive review,

Jaap



---

archive/issue_comments_032239.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-26T08:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32239",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032240.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-26T08:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4381#issuecomment-32240",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha1
