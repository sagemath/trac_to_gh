# Issue 5390: install_package, optional_package etc might pick the wrong sage installation

Issue created by migration from https://trac.sagemath.org/ticket/5390

Original creator: SimonKing

Original creation time: 2009-02-27 09:45:02

Assignee: mabshoff

Keywords: package installation

`package.py` provides various functions for obtaining a list of installed packages or installing new ones. In all these functions, `os.popen('sage')` is called.

But wouldn't this always try to call a system-wide sage installation? Then it would result in an error, if the running sage instance is from a local installation, and it may install packages in a wrong location if there is both a system wide and a local version of sage.

If this is really the case, then it might be better to give the full path to the currently running sage version, hence

```
os.popen('%s/sage'%(SAGE_ROOT))
```


This is what the attached patch does.


---

Attachment

Make sure that install_package picks the right sage version (sorry, it seems the previous attachment was corrupted)


---

Comment by SimonKing created at 2009-02-27 10:02:33

Replying to [ticket:5390 SimonKing]:
> `package.py` provides various functions for obtaining a list of installed packages or installing new ones. In all these functions, `os.popen('sage')` is called.

Detail: In one case, `os.system('sage -f ...') was called, which the patch also changes into SAGE_ROOT+'/sage'.


---

Comment by mabshoff created at 2009-02-27 12:18:21

Hi Simon,

once Sage has been started `sage-env` sets PATH and LD_LIBRARY_PATH, so from inside Sage the right `sage` script is called. I do not really see a scenario where this patch would fix anything.

I am marking this as needs work, but I really consider this as invalid.

Thoughts?

Cheers,

Michael


---

Comment by SimonKing created at 2009-02-27 18:56:31

Hi Michael,

Replying to [comment:2 mabshoff]:
> once Sage has been started `sage-env` sets PATH and LD_LIBRARY_PATH, so from inside Sage the right `sage` script is called. I do not really see a scenario where this patch would fix anything.

I know that Sage sets PATH, but I thought it would merely add `SAGE_LOCAL/bin` in front, but this folder does not contain `sage` (only `sage.bin`). 

But if I am mistaken then certainly that ticket is invalid. It just struck me when by coincidence I was reading the code.

Cheers
 Simon


---

Comment by mabshoff created at 2009-02-27 22:58:37

Resolution: invalid


---

Comment by mabshoff created at 2009-02-27 22:58:37

Replying to [comment:3 SimonKing]:
> Hi Michael,

Hi Simon,

<SNIP>

> I know that Sage sets PATH, but I thought it would merely add `SAGE_LOCAL/bin` in front, but this folder does not contain `sage` (only `sage.bin`). 
> 
> But if I am mistaken then certainly that ticket is invalid. It just struck me when by coincidence I was reading the code.

Yeah, but even *if* the env was messed up your fix does not resolve the problem since `$SAGE_ROOT` does in that case not get overwritten in sage-env, so you would call the wrong Sage even with your patch.

> Cheers
>  Simon

Cheers,

Michael
