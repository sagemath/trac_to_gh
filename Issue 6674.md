# Issue 6674: only use ASCII characters in patches

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-04 08:22:32

Assignee: tbd

CC:  ncohen rlm

This is a follow-up to #5793.


---

Comment by mvngu created at 2009-08-04 08:29:00

The patch `trac_5793-cliquer-flattened.patch` at #5793 contains non-ASCII characters. This can result in errors and warning messages when loading Sage. Patches should only use ASCII characters. The offending characters from that patch are

```
Östergård
```

The attached patch `trac_6674-use-ascii.patch` changes that to "Ostergard". It also fixes referencing so that `[NisOst2003]` appears as a hyperlink in the HTML version of the reference manual, as it should be. This patch is based on Sage 4.1.1.rc0 and depends on #5793.



Nathann: Can I ask you to review this? The ASCII character issue needs to be fixed before releasing Sage 4.1.1.


---

Comment by mvngu created at 2009-08-04 08:29:00

Changing priority from major to blocker.


---

Comment by mvngu created at 2009-08-04 08:29:11

Changing assignee from tbd to tba.


---

Comment by mvngu created at 2009-08-04 08:29:11

Changing component from algebra to documentation.


---

Comment by ncohen created at 2009-08-04 09:00:01

Hello !!

Actually, I can not apply this patch as I have nothing in my graph.py similar to what your patch tries to replace. I may be using some different version of cliquer. And I look through the patches send by rlm without finding where I stopped

I am currently downloading http://ftp.sh.cvut.cz/MIRRORS/sagemath/src/sage-4.1.tar which I will then compile and upgrade to test this patch. However, it is likely that it will take something like 6~7 hours and I will not be able to give you an answer until then.... Sorry !!! ;-)


---

Comment by mvngu created at 2009-08-04 09:01:38

ncohen: Do you have an account on sage.math?


---

Comment by ncohen created at 2009-08-04 09:16:47

I don't think so... I only have an account on TRAC, but I think that's all... What is sage.math ? ^^;


---

Comment by mvngu created at 2009-08-04 09:22:29

The machine sage.math is mostly used for Sage development. You can browse the account holders' home directories at

http://sage.math.washington.edu/home/

In particular, my development directory is

http://sage.math.washington.edu/home/mvngu/

If you have an account on sage.math, you can get all source and binary releases of the 4.1.1 release cycle at

http://sage.math.washington.edu/home/mvngu/release/

in particular the binary

http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.rc0-sage.math.washington.edu-x86_64-Linux.tar.gz

which has been specifically compiled for sage.math. If you don't have an account on sage.math, you can email William Stein about getting an account on that machine.


---

Comment by schilly created at 2009-08-04 10:45:21

Uhm, I question this a litte bit. It's true that you have to use ASCII only for variable names, but strings and comments can be UTF-8. At least it is technically feasible. You just have to add this line in the first or second one of the .py file:

```
# -*- coding: utf-8 -*-
```

I guess it also works with sphinx, but someone should try.

Or is there a general policy i'm not aware of?!


---

Comment by ncohen created at 2009-08-04 13:45:03

This patch applies fine on my brand new install, but I have two remarks :

- I received no error message nor any warning when starting Sage with the Non-ascii characters and using the corresponding functions, so my report may not be relevant
- There are more occurencies of Ostergard in the following functions : cliques_maximum and cliques_maximal


---

Comment by mvngu created at 2009-08-04 15:14:44

The new patch should have removed all non-ASCII characters. It also removes duplicate citations. That is, don't redefine a reference for each function. Only define a reference once. If you then need to refer to that reference, then use a shorthand notation to refer to that reference. That way, it wouldn't result in warnings when building the reference manual.

Here are the steps to see the warnings caused by patches or library files with non-ASCII characters:
 1. Take a binary or source version of Sage 4.1.1.rc0.
 1. Apply the patches `trac_5793-cliquer-flattened.patch` and `trac_5793-part-6.patch` at ticket #5793. Install the package http://sage.math.washington.edu/home/mvngu/patch/cliquer-1.2.spkg .
 1. Run Sage with `./sage -br main` and exit Sage.
 1. Make an experimental binary version of the patched repository with `./sage -bdist 4.1.1.rc0-exp`. The resulting binary can be found in `SAGE_ROOT/dist`.
 1. Extract the resulting binary and run it with `./sage`. You would see something similar to:

```
[mvngu`@`sage sage-4.1.1.rc0-sage.math-x86_64-Linux]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
The Sage install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(please wait at most a few minutes)...
Do not interrupt this.
---------------------------------------------------------------------------
SyntaxError                               Traceback (most recent call last)
| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |
| Type notebook() for the GUI, and license() for information.        |
/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/IPython/ipmaker.py in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6 
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9 

/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13 
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/all.py in <module>()
     83 from sage.modular.all    import *
     84 from sage.schemes.all    import *
---> 85 from sage.graphs.all     import *
     86 from sage.groups.all     import *
     87 from sage.databases.all  import *

/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/all.py in <module>()
----> 1 
      2 
      3 from graph_generators import graphs, digraphs
      4 from graph_database import GraphDatabase, GenericGraphQuery, GraphQuery
      5 from graph import Graph, DiGraph
      6 from bipartite_graph import BipartiteGraph
      7 from graph_bundle import GraphBundle

/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py in <module>()
    139 ################################################################################

    140 
--> 141 import graph
    142 from   math import sin, cos, pi
    143 from sage.misc.randstate import current_randstate

SyntaxError: Non-ASCII character '\xc3' in file /scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/graph.py on line 10146, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (graph.py, line 10145)
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```



---

Comment by ncohen created at 2009-08-04 16:01:45

This patch fails to apply on my version, and I am afraid I do not know where it comes from. As I still have no answer from William Stein for an account on sage.math, I hope somebody else will be able to try it !
The odd thing is that I am asked to enter the "list of the changes" when I apply the patch, as if I were committing it !


---

Comment by ncohen created at 2009-08-05 07:42:21

Perfect ! I was finally able to retry this patch on sage 4.1.1.rc0 on which it applied without any problem. I then built and started a binary version as described and no errors where reported.

Positive review !


---

Comment by AlexGhitza created at 2009-08-05 12:05:11

I don't have a strong opinion about this, but given the discussion about how to ASCII-cise that name, I looked at the README file of the cliquer package, and the copyright notice has "Patric Ostergard".  So it seems that the author himself has chosen this as the ASCII version of his name.  It might be good to go with that.


---

Attachment

based on Sage 4.1.1.rc1


---

Comment by mvngu created at 2009-08-05 13:11:38

Please refer to the new patch, which is based on Sage 4.1.1.rc1.


---

Comment by ncohen created at 2009-08-05 15:08:14

I applied this on a 4.1.1.rc1, which refused to start before this patch was applied on it. I applied it from the command line using hg import, then re-built Sage.

Nothing wrong to report. Positive review !


---

Comment by mvngu created at 2009-08-07 05:54:35

Resolution: fixed
