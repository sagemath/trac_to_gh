# Issue 6674: only use ASCII characters in patches

archive/issues_006674.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nathanncohen @rlmill\n\nThis is a follow-up to #5793.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6674\n\n",
    "created_at": "2009-08-04T08:22:32Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "only use ASCII characters in patches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

CC:  @nathanncohen @rlmill

This is a follow-up to #5793.

Issue created by migration from https://trac.sagemath.org/ticket/6674





---

archive/issue_comments_054748.json:
```json
{
    "body": "The patch `trac_5793-cliquer-flattened.patch` at #5793 contains non-ASCII characters. This can result in errors and warning messages when loading Sage. Patches should only use ASCII characters. The offending characters from that patch are\n\n```\n\u00d6sterg\u00e5rd\n```\nThe attached patch `trac_6674-use-ascii.patch` changes that to \"Ostergard\". It also fixes referencing so that `[NisOst2003]` appears as a hyperlink in the HTML version of the reference manual, as it should be. This patch is based on Sage 4.1.1.rc0 and depends on #5793.\n\n\n\nNathann: Can I ask you to review this? The ASCII character issue needs to be fixed before releasing Sage 4.1.1.",
    "created_at": "2009-08-04T08:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54748",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_5793-cliquer-flattened.patch` at #5793 contains non-ASCII characters. This can result in errors and warning messages when loading Sage. Patches should only use ASCII characters. The offending characters from that patch are

```
Östergård
```
The attached patch `trac_6674-use-ascii.patch` changes that to "Ostergard". It also fixes referencing so that `[NisOst2003]` appears as a hyperlink in the HTML version of the reference manual, as it should be. This patch is based on Sage 4.1.1.rc0 and depends on #5793.



Nathann: Can I ask you to review this? The ASCII character issue needs to be fixed before releasing Sage 4.1.1.



---

archive/issue_comments_054749.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-08-04T08:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54749",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_054750.json:
```json
{
    "body": "Changing assignee from tbd to tba.",
    "created_at": "2009-08-04T08:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54750",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing assignee from tbd to tba.



---

archive/issue_comments_054751.json:
```json
{
    "body": "Changing component from algebra to documentation.",
    "created_at": "2009-08-04T08:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54751",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from algebra to documentation.



---

archive/issue_comments_054752.json:
```json
{
    "body": "Hello !!\n\nActually, I can not apply this patch as I have nothing in my graph.py similar to what your patch tries to replace. I may be using some different version of cliquer. And I look through the patches send by rlm without finding where I stopped\n\nI am currently downloading http://ftp.sh.cvut.cz/MIRRORS/sagemath/src/sage-4.1.tar which I will then compile and upgrade to test this patch. However, it is likely that it will take something like 6~7 hours and I will not be able to give you an answer until then.... Sorry !!! ;-)",
    "created_at": "2009-08-04T09:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54752",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!

Actually, I can not apply this patch as I have nothing in my graph.py similar to what your patch tries to replace. I may be using some different version of cliquer. And I look through the patches send by rlm without finding where I stopped

I am currently downloading http://ftp.sh.cvut.cz/MIRRORS/sagemath/src/sage-4.1.tar which I will then compile and upgrade to test this patch. However, it is likely that it will take something like 6~7 hours and I will not be able to give you an answer until then.... Sorry !!! ;-)



---

archive/issue_comments_054753.json:
```json
{
    "body": "ncohen: Do you have an account on sage.math?",
    "created_at": "2009-08-04T09:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

ncohen: Do you have an account on sage.math?



---

archive/issue_comments_054754.json:
```json
{
    "body": "I don't think so... I only have an account on TRAC, but I think that's all... What is sage.math ? ^^;",
    "created_at": "2009-08-04T09:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54754",
    "user": "https://github.com/nathanncohen"
}
```

I don't think so... I only have an account on TRAC, but I think that's all... What is sage.math ? ^^;



---

archive/issue_comments_054755.json:
```json
{
    "body": "The machine sage.math is mostly used for Sage development. You can browse the account holders' home directories at\n\nhttp://sage.math.washington.edu/home/\n\nIn particular, my development directory is\n\nhttp://sage.math.washington.edu/home/mvngu/\n\nIf you have an account on sage.math, you can get all source and binary releases of the 4.1.1 release cycle at\n\nhttp://sage.math.washington.edu/home/mvngu/release/\n\nin particular the binary\n\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.rc0-sage.math.washington.edu-x86_64-Linux.tar.gz\n\nwhich has been specifically compiled for sage.math. If you don't have an account on sage.math, you can email William Stein about getting an account on that machine.",
    "created_at": "2009-08-04T09:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54755",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_054756.json:
```json
{
    "body": "Uhm, I question this a litte bit. It's true that you have to use ASCII only for variable names, but strings and comments can be UTF-8. At least it is technically feasible. You just have to add this line in the first or second one of the .py file:\n\n```\n# -*- coding: utf-8 -*-\n```\nI guess it also works with sphinx, but someone should try.\n\nOr is there a general policy i'm not aware of?!",
    "created_at": "2009-08-04T10:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54756",
    "user": "https://github.com/haraldschilly"
}
```

Uhm, I question this a litte bit. It's true that you have to use ASCII only for variable names, but strings and comments can be UTF-8. At least it is technically feasible. You just have to add this line in the first or second one of the .py file:

```
# -*- coding: utf-8 -*-
```
I guess it also works with sphinx, but someone should try.

Or is there a general policy i'm not aware of?!



---

archive/issue_comments_054757.json:
```json
{
    "body": "This patch applies fine on my brand new install, but I have two remarks :\n\n- I received no error message nor any warning when starting Sage with the Non-ascii characters and using the corresponding functions, so my report may not be relevant\n- There are more occurencies of Ostergard in the following functions : cliques_maximum and cliques_maximal",
    "created_at": "2009-08-04T13:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54757",
    "user": "https://github.com/nathanncohen"
}
```

This patch applies fine on my brand new install, but I have two remarks :

- I received no error message nor any warning when starting Sage with the Non-ascii characters and using the corresponding functions, so my report may not be relevant
- There are more occurencies of Ostergard in the following functions : cliques_maximum and cliques_maximal



---

archive/issue_comments_054758.json:
```json
{
    "body": "The new patch should have removed all non-ASCII characters. It also removes duplicate citations. That is, don't redefine a reference for each function. Only define a reference once. If you then need to refer to that reference, then use a shorthand notation to refer to that reference. That way, it wouldn't result in warnings when building the reference manual.\n\nHere are the steps to see the warnings caused by patches or library files with non-ASCII characters:\n1. Take a binary or source version of Sage 4.1.1.rc0.\n2. Apply the patches `trac_5793-cliquer-flattened.patch` and `trac_5793-part-6.patch` at ticket #5793. Install the package http://sage.math.washington.edu/home/mvngu/patch/cliquer-1.2.spkg .\n3. Run Sage with `./sage -br main` and exit Sage.\n4. Make an experimental binary version of the patched repository with `./sage -bdist 4.1.1.rc0-exp`. The resulting binary can be found in `SAGE_ROOT/dist`.\n5. Extract the resulting binary and run it with `./sage`. You would see something similar to:\n\n```\n[mvngu@sage sage-4.1.1.rc0-sage.math-x86_64-Linux]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nThe Sage install tree may have moved.\nRegenerating Python.pyo and .pyc files that hardcode the install PATH\n(please wait at most a few minutes)...\nDo not interrupt this.\n---------------------------------------------------------------------------\nSyntaxError                               Traceback (most recent call last)\n| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |\n| Type notebook() for the GUI, and license() for information.        |\n/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/IPython/ipmaker.py in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/bin/ipy_profile_sage.py in <module>()\n      5     preparser(True)\n      6 \n----> 7     import sage.all_cmdline\n      8     sage.all_cmdline._init_cmdline(globals())\n      9 \n\n/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13 \n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/all.py in <module>()\n     83 from sage.modular.all    import *\n     84 from sage.schemes.all    import *\n---> 85 from sage.graphs.all     import *\n     86 from sage.groups.all     import *\n     87 from sage.databases.all  import *\n\n/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/all.py in <module>()\n----> 1 \n      2 \n      3 from graph_generators import graphs, digraphs\n      4 from graph_database import GraphDatabase, GenericGraphQuery, GraphQuery\n      5 from graph import Graph, DiGraph\n      6 from bipartite_graph import BipartiteGraph\n      7 from graph_bundle import GraphBundle\n\n/scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py in <module>()\n    139 ################################################################################\n\n    140 \n--> 141 import graph\n    142 from   math import sin, cos, pi\n    143 from sage.misc.randstate import current_randstate\n\nSyntaxError: Non-ASCII character '\\xc3' in file /scratch/mvngu/sage-4.1.1.rc0-sage.math-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/graph.py on line 10146, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (graph.py, line 10145)\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```",
    "created_at": "2009-08-04T15:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The new patch should have removed all non-ASCII characters. It also removes duplicate citations. That is, don't redefine a reference for each function. Only define a reference once. If you then need to refer to that reference, then use a shorthand notation to refer to that reference. That way, it wouldn't result in warnings when building the reference manual.

Here are the steps to see the warnings caused by patches or library files with non-ASCII characters:
1. Take a binary or source version of Sage 4.1.1.rc0.
2. Apply the patches `trac_5793-cliquer-flattened.patch` and `trac_5793-part-6.patch` at ticket #5793. Install the package http://sage.math.washington.edu/home/mvngu/patch/cliquer-1.2.spkg .
3. Run Sage with `./sage -br main` and exit Sage.
4. Make an experimental binary version of the patched repository with `./sage -bdist 4.1.1.rc0-exp`. The resulting binary can be found in `SAGE_ROOT/dist`.
5. Extract the resulting binary and run it with `./sage`. You would see something similar to:

```
[mvngu@sage sage-4.1.1.rc0-sage.math-x86_64-Linux]$ ./sage
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

archive/issue_comments_054759.json:
```json
{
    "body": "This patch fails to apply on my version, and I am afraid I do not know where it comes from. As I still have no answer from William Stein for an account on sage.math, I hope somebody else will be able to try it !\nThe odd thing is that I am asked to enter the \"list of the changes\" when I apply the patch, as if I were committing it !",
    "created_at": "2009-08-04T16:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54759",
    "user": "https://github.com/nathanncohen"
}
```

This patch fails to apply on my version, and I am afraid I do not know where it comes from. As I still have no answer from William Stein for an account on sage.math, I hope somebody else will be able to try it !
The odd thing is that I am asked to enter the "list of the changes" when I apply the patch, as if I were committing it !



---

archive/issue_comments_054760.json:
```json
{
    "body": "Perfect ! I was finally able to retry this patch on sage 4.1.1.rc0 on which it applied without any problem. I then built and started a binary version as described and no errors where reported.\n\nPositive review !",
    "created_at": "2009-08-05T07:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54760",
    "user": "https://github.com/nathanncohen"
}
```

Perfect ! I was finally able to retry this patch on sage 4.1.1.rc0 on which it applied without any problem. I then built and started a binary version as described and no errors where reported.

Positive review !



---

archive/issue_comments_054761.json:
```json
{
    "body": "I don't have a strong opinion about this, but given the discussion about how to ASCII-cise that name, I looked at the README file of the cliquer package, and the copyright notice has \"Patric Ostergard\".  So it seems that the author himself has chosen this as the ASCII version of his name.  It might be good to go with that.",
    "created_at": "2009-08-05T12:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54761",
    "user": "https://github.com/aghitza"
}
```

I don't have a strong opinion about this, but given the discussion about how to ASCII-cise that name, I looked at the README file of the cliquer package, and the copyright notice has "Patric Ostergard".  So it seems that the author himself has chosen this as the ASCII version of his name.  It might be good to go with that.



---

archive/issue_comments_054762.json:
```json
{
    "body": "Attachment [trac_6674-use-ascii.patch](tarball://root/attachments/some-uuid/ticket6674/trac_6674-use-ascii.patch) by mvngu created at 2009-08-05 13:10:27\n\nbased on Sage 4.1.1.rc1",
    "created_at": "2009-08-05T13:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54762",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6674-use-ascii.patch](tarball://root/attachments/some-uuid/ticket6674/trac_6674-use-ascii.patch) by mvngu created at 2009-08-05 13:10:27

based on Sage 4.1.1.rc1



---

archive/issue_comments_054763.json:
```json
{
    "body": "Please refer to the new patch, which is based on Sage 4.1.1.rc1.",
    "created_at": "2009-08-05T13:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Please refer to the new patch, which is based on Sage 4.1.1.rc1.



---

archive/issue_comments_054764.json:
```json
{
    "body": "I applied this on a 4.1.1.rc1, which refused to start before this patch was applied on it. I applied it from the command line using hg import, then re-built Sage.\n\nNothing wrong to report. Positive review !",
    "created_at": "2009-08-05T15:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54764",
    "user": "https://github.com/nathanncohen"
}
```

I applied this on a 4.1.1.rc1, which refused to start before this patch was applied on it. I applied it from the command line using hg import, then re-built Sage.

Nothing wrong to report. Positive review !



---

archive/issue_events_015747.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-07T05:54:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6674#event-15747"
}
```



---

archive/issue_comments_054765.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-07T05:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6674#issuecomment-54765",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
