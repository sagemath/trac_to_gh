# Issue 2565: logging is extremely broken

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-03-17 04:45:21

Assignee: cwitty

Keywords: log, logging, html, dvi

The logging facilities in misc/log.py are extremely broken.

The DVI logger produces a symlink to `$SAGE_ROOT/devel/doc/commontex/macros.tex`. There's no devel/doc directory; there's no doc/commontex directory anywhere in the Sage tree, and there's no file macros.tex anywhere in the Sage tree!

The optional directory that can be specified in the constructor does not actually accept a directory name. If you try `L.('/tmp')` it will fail, because it tries to create a directory such as `/tmp-2008-blah`, which fails because I'm running Sage as a user and can't create directories in the root directory.

The HTML logger works a bit better, but when starting it, it does not find the `xdg-open` command, even though that is installed on my system.

The view() command should allow the user to specify a viewer; it's silly that the only way to tell Sage which viewer to use is with an environment variable.

It would also be nice if there was a text logger available in log.py. I know there's the IPython logging system, but it would be nice if those text-based logging capabilities were available from log.py.


---

Comment by mabshoff created at 2008-03-17 04:51:28

Changing priority from minor to major.


---

Comment by ddrake created at 2008-03-17 11:05:29

The `log.patch.1` patch fixes the directory problems and the xdg-open problem. It also removes the MathML logger (by commenting it out and removing from all.py) since it depends on a bunch of files that aren't shipped with Sage, so it cannot possibly work. The patch also fixes DVI viewing by removing the symlink to macros.tex; a simple example of the output compiled without any extra files, so removing that from the generated TeX file seems okay for now.

I am also seeing a problem where the output and input are off by 1: the output from command #n is shown in the generated file after comment #n+1.


---

Comment by mabshoff created at 2008-03-17 12:06:31

Hi Dan,

please attach mercurial patches so that you can get credited for them automatically in the repo.

Cheers,

Michael


---

Comment by ddrake created at 2008-03-18 00:22:41

Mercurial patch attached. I just learned about patch queues and did a 'qdiff' instead of 'export qtip'. :)

The patch, btw, is against 2.10.3.


---

Comment by ddrake created at 2008-03-19 05:23:27

The attached patch fixes all issues mentioned in the report, and adds a text logger.

There is an off-by-one error in the IPython input/output history; I don't know if that is a genuine bug, but I had to account for it, and it was tricky.


---

Comment by dfdeshom created at 2008-03-27 04:06:51

Replying to [comment:2 ddrake]:
> The `log.patch.1` patch fixes the directory problems and the xdg-open problem. It also removes the MathML logger (by commenting it out and removing from all.py) w.

Hi Dan, thanks for seeing this. Could you completely remove this class (log_mathml)? It's not that useful anymore.

The patch looks good and the logger works! I have 2 requests: it would be nice if the docs specified that the log directory has to be a *relative* path. Also: when you instantiate the logger, you could return a message saying where the log file is being saved

```
sage: log_text()
Logging all commands to ~/custom/sage/log/log-2008-03-26-202848/logfile.txt
```



---

Comment by ddrake created at 2008-03-27 06:35:33

Replying to [comment:7 dfdeshom]:
> The patch looks good and the logger works! I have 2 requests: it would be nice if the docs specified that the log directory has to be a *relative* path. Also: when you instantiate the logger, you could return a message saying where the log file is being saved

```
sage: log_text()
Logging all commands to ~/custom/sage/log/log-2008-03-26-202848/logfile.txt
```

> 

I've added the message, removed the MathML logger, and will update the patch momentarily. As for the paths, it's not necessary to use relative paths: you can do

```
sage: log_text('/tmp')
```

and you get a directory in the `/tmp` directory. If you don't begin the path with a slash, it gets put into your home directory: doing `log_text('foo')` logs into a directory like `/home/drake/foo/log-2008-03-27-151949`.


---

Attachment


---

Comment by mabshoff created at 2008-03-27 07:50:05

Both issues have been addressed:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11.alpha1, Release Date: 2008-03-22                 |
| Type notebook() for the GUI, and license() for information.        |
sage: log_text()
Now logging to /home/mabshoff/.sage/log/log-2008-03-27-004430/sagelog.txt
Text Logger
sage:
Exiting SAGE (CPU time 0m0.01s, Wall time 0m7.41s).
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11.alpha1, Release Date: 2008-03-22                 |
| Type notebook() for the GUI, and license() for information.        |
sage: log_text("/tmp")
Now logging to /tmp/log-2008-03-27-004454/sagelog.txt
Text Logger
sage:
Exiting SAGE (CPU time 0m0.02s, Wall time 0m8.70s).
```

So: positive review!


---

Comment by mabshoff created at 2008-03-27 07:50:46

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-27 07:50:46

Resolution: fixed
