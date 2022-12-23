# Issue 4336: [with suggested solution] Bug in handling attached pyx-files

Issue created by migration from https://trac.sagemath.org/ticket/4336

Original creator: SimonKing

Original creation time: 2008-10-22 16:36:08

Assignee: cwitty

CC:  robertwb

Keywords: attachments, cython

I attached a pyx-file:

```
sage: attach f5.pyx
Compiling /home/king/Projekte/f5/f5.pyx...
```


Then I changed the file on the disk, and pressed the `Enter` key in Sage. This should result in a recompilation of `f5.pyx`, but instead I got this traceback:

```
sage:
Compiling /home/king/Projekte/f5/f5.pyx...
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/interpreter.pyc in sage_prefilter(self, block, continuation)
    394         for i in range(len(B)):
    395             L = B[i]
--> 396             M = do_prefilter_paste(L, continuation or (not first))
    397             first = False
    398             # The L[:len(L)-len(L.lstrip())]  business here preserves

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/interpreter.pyc in do_prefilter_paste(line, continuation)
    190                         _ip.runlines('%%run -i "%s"'%preparse_file_named(F))
    191                     elif F.endswith('.spyx') or F.endswith('.pyx'):
--> 192                         X = load_cython(F)
    193                         __IPYTHON__.push(X)
    194                     else:

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/interpreter.pyc in load_cython(name)
    340     cur = os.path.abspath(os.curdir)
    341     try:
--> 342         mod, dir  = cython.cython(name, compile_message=True, use_cache=True)
    343     except (IOError, OSError, RuntimeError), msg:
    344         print "Error compiling cython file:\n%s"%msg

/home/king/SAGE/devel/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/cython.pyc in cython(filename, verbose, compile_message, use_cache, create_local_c_file, annotate, sage_namespace, create_local_so_file)
    311                                         for fname in additional_source_files])
    312
--> 313     pyx = '%s/%s.pyx'%(build_dir, name)
    314     open(pyx,'w').write(F)
    315     setup="""

UnboundLocalError: local variable 'name' referenced before assignment
```


Afterwards, leaving Sage was impossible using `quit` -- I got the same traceback again and had to quit with `Ctrl-D`.

I think the problem is in lines 299-311 of `cython.py`, which is

```
    if create_local_so_file:
        name = base
    else:
        global sequence_number
        if not sequence_number.has_key(base):
            sequence_number[base] = 0
            name = '%s_%s'%(base, sequence_number[base])

            # increment the sequence number so will use a different one next time.
            sequence_number[base] += 1

    additional_source_files = ",".join(["'"+os.path.abspath(os.curdir)+"/"+fname+"'" \
                                        for fname in additional_source_files])
```


If I'm not mistaken, there is a wrong indentation, and it should be

```
    if create_local_so_file:
        name = base
    else:
        global sequence_number
        if not sequence_number.has_key(base):
            sequence_number[base] = 0
        name = '%s_%s'%(base, sequence_number[base])

        # increment the sequence number so will use a different one next time.
        sequence_number[base] += 1

    additional_source_files = ",".join(["'"+os.path.abspath(os.curdir)+"/"+fname+"'" \
                                        for fname in additional_source_files])
```


Problem 1: I have no idea how I can force Sage to use the modified `cython.py`, hence I can not test my changes. 

Problem 2: `hg_sage.commit()` did not work, since it claimed that nothing was changed (although `cython.py` did change). So, no patch.

Can you give me a solution to Problems 1 and 2? And does my suggested solution works?
Cheers
      Simon



---

Comment by mabshoff created at 2008-10-22 19:10:38

Added RobertWB to the CC since he worked on the Cython recompilation patch. 

Simon: Are you sure you edited the right cython.py - there are several copies in the tree.

Cheers,

Michael


---

Comment by SimonKing created at 2008-10-22 19:15:46

Dear Michael,

Replying to [comment:1 mabshoff]:
> Simon: Are you sure you edited the right cython.py - there are several copies in the tree.

I chose local/lib/python2.5/site-packages/sage/misc/cython.py

Which should I take instead?


---

Comment by mabshoff created at 2008-10-22 19:19:55

Replying to [comment:2 SimonKing]:
> Dear Michael,
> 
> Replying to [comment:1 mabshoff]:
> > Simon: Are you sure you edited the right cython.py - there are several copies in the tree.
> 
> I chose local/lib/python2.5/site-packages/sage/misc/cython.py
> 
> Which should I take instead?

Take the one in $SAGE_ROOT/devel/sage/..

Cheers,

Michael


---

Comment by SimonKing created at 2008-10-22 19:25:44

Dear Michael, dear Robert,

Replying to [comment:3 mabshoff]:
> > Which should I take instead?
> 
> Take the one in $SAGE_ROOT/devel/sage/..

Did already. It works, the traceback disappears. Patch'll follow!

Cheers,
    Simon


---

Attachment

Fixes a bug that occurs when an attached .pyx file is changed


---

Comment by mabshoff created at 2008-10-27 02:25:22

Simon's patch is correct. This was actually broken by the patch in #4238.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 02:54:27

Resolution: fixed


---

Comment by mabshoff created at 2008-10-27 02:54:27

Merged in Sage 3.2.alpha1
