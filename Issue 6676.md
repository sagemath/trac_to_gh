# Issue 6676: DeprecationWarning on twisted after starting notebook().

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-06 07:53:58

Assignee: was

When I start Sage on Solaris, as soon as I type notebook(), I get a 'DeprecationWarning'. It does not give a good impression to get this after the running the first command one is likely to want to run. It says 'the md5 module is deprecated; use hashlib instead'.

Hence I suggest this is fixed asap, as its going to be the first impression someone gets of Sage.

Dave

kirkby`@`t2:[/scratch/kirkby/sage-4.1.1.rc0] $ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: notebook()
The notebook files are stored in: /rootpool2/local/kirkby/.sage//sage_notebook
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
/scratch/kirkby/sage-4.1.1.rc0/local/lib/python2.6/site-packages/twisted/persisted/sob.py:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import os, md5, sys
2009-08-06 00:48:56-0700 [-] Log opened.
2009-08-06 00:48:56-0700 [-] twistd 8.2.0 (/scratch/kirkby/sage-4.1.1.rc0/local/bin/python 2.6.2) starting up.
2009-08-06 00:48:56-0700 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-08-06 00:48:56-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8000
2009-08-06 00:48:56-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x3e00328>
/scratch/kirkby/sage-4.1.1.rc0/local/bin/sage-native-execute: xdg-open: not found
| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |
| Type notebook() for the GUI, and license() for information.        |
 



---

Comment by flawrence created at 2009-09-15 02:11:37

This appears to be a duplicate of #6555


---

Comment by was created at 2009-11-07 04:18:09

Changing status from new to needs_review.


---

Comment by was created at 2009-11-07 04:18:09

This fixes the problem:

   http://wstein.org/home/wstein/patches/twisted-8.2.0.p1.spkg


---

Comment by mhansen created at 2009-11-07 05:07:37

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-07 05:07:37

Looks good to me.  I also added the .patch files for the two new changes.  The merged spkg can be found at http://sage.math.washington.edu/home/mhansen/twisted-8.2.0.p1.spkg


---

Comment by mhansen created at 2009-11-07 05:07:46

Resolution: fixed
