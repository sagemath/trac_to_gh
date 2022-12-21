# Issue 975: Library incompatibilities when launching external applications

Issue created by migration from Trac.

Original creator: bober

Original creation time: 2007-10-23 19:26:12

Assignee: mabshoff

(See http://groups.google.com/group/sage-devel/browse_thread/thread/78f8b6afea8ca8c8 for some discussion of this bug.)

When sage launches an external application (for example, eog, or singular) it does so with LD_LIBRARY_PATH set to sage defaults. This is necessary for some applications (e.g. singular), but it breaks other applications on some systems (e.g. eog, when running on bober's laptop).

The following examples all take place on bober's laptop, which is a 32-bit Core Duo recently upgraded to Ubuntu 7.10. (Presumably, the problems were not there under Ubuntu 7.04 so this is a system specific defect.)

Some typical examples are


```
sage: !eog
eog: symbol lookup error: /usr/lib/libxml2.so.2: undefined symbol: gzopen64

sage: !gimp
gimp: symbol lookup error: /usr/lib/libcairo.so.2: undefined symbol: FT_Library_SetLcdFilter

sage: !gvim
gvim: symbol lookup error: /usr/lib/libcairo.so.2: undefined symbol: FT_Library_SetLcdFilter
```


Also, this extends to a problem with python package locations, for example (glchess is a python program, which, on Ubuntu, at least, has most of its files installed under `/usr/lib/python2.5/site-packages/glchess`)


```
sage: !glchess
Traceback (most recent call last):
  File "/usr/games/glchess", line 18, in <module>
    from glchess.glchess import start_game
ImportError: No module named glchess.glchess
```


A basic temporary workaround is to change certain instances of `os.system(command)` to
`os.system("LD_LIBRARY_PATH='' " + command)`. This may allow plot().show() to work correctly in some cases, for example.

A possible better fix described by mabshoff is 

  The problem is that application like singular would fail if LD_LIBRARY_PATH was unset. One solution would be to come up with a white list of applications that are "Sage internal" or alternatively check if in case we do '!foo' whether there is a foo in $SAGE_LOCAL/bin and execute with LD_LIBRARY_PATH or alternatively if foo isn't in $SAGE_LOCAL/bin execute with the old LD_LIBRARY_PATH before sage-env changed it [and not with an empty one!]


---

Comment by mabshoff created at 2007-10-24 01:46:01

Changing status from new to assigned.


---

Comment by was created at 2007-11-02 18:13:17

comment from Fernando Perez

```
 
On 11/2/07, William Stein <wstein`@`gmail.com> wrote:
 
> Ah, that's very very nice.  OK, I would really like
> to see that implemented.   Maybe Fernando Perez could
> tell us how to hook into IPython to make that happen....
 
Should be fairly straightforward.  In iplib.py, around line 500,
you'll find this code:
 
        # Functions to call the underlying shell.
 
        # The first is similar to os.system, but it doesn't return a value,
        # and it allows interpolation of variables in the user's namespace.
        self.system = lambda cmd: \
                      shell(self.var_expand(cmd,depth=2),
                            header=self.rc.system_header,
                            verbose=self.rc.system_verbose)
 
        # These are for getoutput and getoutputerror:
        self.getoutput = lambda cmd: \
                         getoutput(self.var_expand(cmd,depth=2),
                                   header=self.rc.system_header,
                                   verbose=self.rc.system_verbose)
 
        self.getoutputerror = lambda cmd: \
                              getoutputerror(self.var_expand(cmd,depth=2),
                                             header=self.rc.system_header,
                                             verbose=self.rc.system_verbose)
 
where 'shell', 'getoutput' and 'getoutputerror' are all defined in
IPython.genutils.
 
Simply take the ipython instance, and before you hand it to the user
for 'live' usage, change its
.system attribute to be your own routine which is similar to the above
lambda, but does the additional extra checks you want.
 
Basically code like (this is just a sketch):
 
import new
 
old_system = ipython_instance.system
 
def sage_system(self,cmd):
  if cmd_in_sage_programs():
    old_system(cmd)
  else:
    try:
      update_environment()
      old_system(cmd)
    finally:
      restore_environment()
 
ipython_instance.system = new.instancemethod(ipython_instance,sage_system)
 
 
This is obviously incomplete, but it should give you an idea of what's needed.
 
Cheers,
 
f
 }}}


---

Comment by was created at 2007-12-11 02:53:54


```
> 
> 
> sage: hg_sage.commit()
> cd "/home/wdj/wdj/sagefiles/sage-2.8.13.alpha1/devel/sage" && hg diff  | less
> cd "/home/wdj/wdj/sagefiles/sage-2.8.13.alpha1/devel/sage" && hg commit
> emacs: symbol lookup error: /usr/lib/libcairo.so.2: undefined symbol:
> FT_Library_SetLcdFilter
> transaction abort!
> rollback completed
> abort: edit failed: emacs exited with status 127
> 

This is a library conflict.   I know how to fix it, by unsetting some environment
variables before calling emacs.   This is trac #975:
    http://trac.sagemath.org/sage_trac/ticket/975

For now, if you put this in your SAGE_ROOT/local/bin/ it will be a work-around:
   (1) Make a file SAGE_ROOT/local/bin/emacs
   (2) Put this in it:

#!/bin/sh
unset LD_LIBRARY_PATH
unset DYLD_LIBRARY_PATH
/usr/bin/emacs $`@`

   (3) make it executable:
        chmod +x SAGE_ROOT/local/bin/emacs

William
```



---

Attachment


---

Comment by jason created at 2007-12-12 00:28:02

The update-environment.patch takes care of the case:

!eog

or other commands using the shell "!" function.  However, this does not address other searches for libraries.  So, for example, plot(x,0,1).show() still does *not* pop up a window.

The following will pop up a window, though:


```
sage: import os
sage: os.environ['LD_LIBRARY_PATH']=os.environ['SAGE_ORIG_LD_LIBRARY_PATH']
sage: plot(x,1,2).show()
```


Note that using os.environ like this exposes a memory leak on FreeBSD and possibly Mac OSX (see http://docs.python.org/lib/os-procinfo.html and http://www.freebsd.org/cgi/man.cgi?query=putenv&sektion=3 for example).  Also, probably messes up other things that depend on the modified LD_LIBRARY_PATH

I have no idea how to set the LD_LIBRARY_PATH for the show() command, for example.


---

Comment by jason created at 2008-01-10 05:16:41

Modifies the browsers returned to use "native-execute".  Use in conjunction with the native-execute.patch


---

Attachment

Apply to sage-scripts.  Creates new "native-execute" command that resets the LD_LIBRARY_PATH variable.


---

Comment by jason created at 2008-01-10 05:25:40

Changing priority from minor to major.


---

Comment by jason created at 2008-01-10 05:27:12

All three patches should be applied, with the native-execute patch applied to sage-scripts.  The first patch fixes the "!eog" problem from the original ticket.  The last two patches allow plot().show() to open an external window.


---

Comment by mabshoff created at 2008-01-10 05:37:48

Nice work, looks good to me.

Cheers,

Michael


---

Comment by jason created at 2008-01-10 06:35:34

Thanks.  The last two patches implemented Robert Bradshaw's idea.


---

Comment by mabshoff created at 2008-01-10 06:38:52

Merged in Sage 2.10.alpha1.


---

Comment by mabshoff created at 2008-01-10 06:38:52

Resolution: fixed


---

Comment by mabshoff created at 2008-01-13 17:37:26

There is one problem: `sage -sdist` only copies all scripts from `local/bin` starting with `sage-`, so rename the native-execute-script and fix `sage/misc/viewer.py` with the attached patch.

The fact that `sage -sdist` only copies files with certain prefixes is *not* documented.

Cheers,

Michael
