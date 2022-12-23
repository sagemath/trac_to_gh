# Issue 4381: sage -wthread not passed correctly to ipython

Issue created by migration from https://trac.sagemath.org/ticket/4381

Original creator: jsp

Original creation time: 2008-10-29 19:26:07

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




---

Comment by jsp created at 2008-10-30 14:27:31

Don't know for sure but #3945 could be the culprit.

[http://trac.sagemath.org/sage_trac/ticket/3945](http://trac.sagemath.org/sage_trac/ticket/3945)

Jaap


---

Comment by mabshoff created at 2008-10-30 14:57:58

#3945 is more than likely the culprit here since nothing else touched ipython related scripts in 3.1.2->3.1.3.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-09 23:21:01

After talking to Fernando Perez at SD 11 it is more than a five minute fix in IPython, so we should patch around it for now. In the long term the issue will be fixed in IPython :)

Cheers,

Michael


---

Comment by jsp created at 2008-11-25 23:55:08

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

Attachment


---

Comment by jsp created at 2008-11-26 01:11:15

New patch worked for me!

Positive review,

Jaap


---

Comment by mabshoff created at 2008-11-26 08:50:58

Resolution: fixed


---

Comment by mabshoff created at 2008-11-26 08:50:58

Merged in Sage 3.2.1.alpha1
