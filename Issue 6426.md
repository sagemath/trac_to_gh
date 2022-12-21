# Issue 6426: ECHIDNA (Elliptic Curves and Higher Dimensional Analogues)

Issue created by migration from Trac.

Original creator: kohel

Original creation time: 2009-06-26 17:27:06

Assignee: tbd

CC:  cremona craigcitro hlaw was ncalexan mstreng

This is a repository of Magma code for arithmetic geometry and number theory.  The latest spkg is echidna-2.0.spkg, can be downloaded from:

http://echidna.maths.usyd.edu.au/kohel/alg/

This should be tested with the Sage worksheet:

http://echidna.maths.usyd.edu.au/kohel/doc/ECHIDNA.sws

A printed pdf version is here:

http://echidna.maths.usyd.edu.au/kohel/doc/ECHIDNA.pdf

This spkg is submitted for consideration as an optional 
package.



---

Attachment


---

Comment by mhansen created at 2009-06-26 17:44:59

I was wondering why the 'sage.echinda.*' entries were added to setup.py.  Where are these modules coming from?


---

Comment by ncalexan created at 2009-06-26 22:00:30

I installed the spkg but got

```
User error: Identifier 'attach_echidna' has not been declared or assigned
```

when trying `magma.attach_echidna()`.  Presumably my magma paths are not setup correctly?

Also, this patch might be malformed.  (Did you use the hg export -o option?  That stupidly appends rather than overwrites, causing me some grief for a time.)


---

Comment by kohel created at 2009-06-26 23:21:35

Sorry, out of the above patch one only needs the single new function:

    def attach_echidna(self):
        """
        Attach the ECHIDNA code repository.
        """
        from sage.misc.misc import SAGE_ROOT
        self.attach_spec(SAGE_ROOT + '/data/extcode/echidna/echidna.spec') # optional - magma

in sage/interfaces/magma.py file; the other changes are irrelevant.  I attach this file, which 
also incorporates William's patch #6395.


---

Comment by cremona created at 2009-06-28 10:41:46

I added a patch, to replace the entire magma.py which David attached.  Note that the patch was made after applying the (positively reviewd) patch at #6395, so that needs to be applied first.  Both the first two attachments can probably now be deleted.  Trying this out now...


---

Comment by cremona created at 2009-06-28 10:48:30

The function magma.attach_echidna tries to use $SAGE_ROOT/data/extcode/echidna/echidna.spec  but the directory into which echidna has been installed is called data/extcode/echidna-2.0/.  I suggest changing the spkg-install script to make these agree: probably better not to have the version number in that pathname (since then the file magma.py would need changing every time there's a new version).

I did not try changing the spkg myself.  I'll be happy to try this again when David has.

I also changed the milestone to 4.1.1 since the required patch at #6395 has that milestone, but there's still the possibility of both getting into 4.1.


---

Comment by kohel created at 2009-06-28 16:44:11

I changed the spkg-install in echidna-2.0.spkg:

http://echidna.maths.usyd.edu.au/kohel/alg/echidna-2.0.spkg

Moreover, I put in an example in the attached magma.2.py 
and, realising that there was no detach function, added 
both detach_spec and detach_echidna, so users can get back 
to a clean version of magma.


---

Comment by kohel created at 2009-06-28 18:49:24

Oops, I will attach an update, since I forgot to include the error 
message, which results after detaching echidna, in the example for 
detach_echidna.  Moreover, I had to reattach the Magma package files 
since ECHIDNA was overwriting some of Magma's files.

Moreover sage -t magma.py run cleanly for the wrong reasons. Doing

sage -t --optional magma.py

I found that there were lots of errors due to printing changes in 
Magma (tested against version 2.15-7).  To fix the doctests, I had 
to change " to ''.  It is possible that this breaks ReST syntax. 
Does someone want to check and, if so, come up with a solution?


---

Attachment


---

Comment by cremona created at 2009-06-28 19:31:02

I'll have a look.  David, it would make it simpler (or at least more standard) if you attached a patch instead of a replacement file.  It's better since that way the system can keep track of the changes made (and who made them).


---

Comment by cremona created at 2009-06-28 21:55:04

Replaces previous, applies to 4.1.alpha2


---

Attachment

The new spkg works, and the new magma.py is ok (one minor doctest filaure in the __iter__ function which I have fixed).  See my attached match, which applies to 4.1.alpha2 and yields a correct magma.py.

I ran into a lot of problems trying to evaluate the worksheet cells -- some Sage functions ins there (e.g. FunctionField(ZZ)) do not exist.  David, can you include an ordinary python file with these tests and demos in?  And if you have extra stuff implemented in Sage which the worksheet example need, why not include them (on a separate ticket) in Sage?  (There are some in magma.py but not many).

I rebuilt the ref manual and it looks fine.

I don't know what the magma2.py file is for -- I ignored it.


---

Comment by kohel created at 2009-06-29 07:54:44

In order to run the complete worksheet, one needs a could of python
commands:

http://echidna.maths.usyd.edu.au/kohel/alg/sage/elliptic_curves.tgz
http://echidna.maths.usyd.edu.au/kohel/alg/sage/function_fields.tgz

for which I have yet to make a trac ticket (the former file is still 
under development and the latter one is a trivial user convenience).
One just needs to load the all.py in each directory after untarring.

Moreover, for the database commands, the underlying files needed are:

http://echidna.maths.usyd.edu.au/kohel/dbs/CrvG2.tgz
http://echidna.maths.usyd.edu.au/kohel/dbs/IgusaLIX.tgz
http://echidna.maths.usyd.edu.au/kohel/dbs/FldCM.tgz

The file magma.2.py resulted from not choosing "replace" on my first 
resubmission of magma.py, after which I replaced it with a note to 
ignore it (since now the file magma.py is the latest).


---

Comment by AlexGhitza created at 2009-07-11 11:31:29

Changing assignee from tbd to was.


---

Comment by AlexGhitza created at 2009-07-11 11:31:29

Changing component from algebra to number theory.


---

Comment by kedlaya created at 2016-08-19 22:36:46

Ping. Is there still interest in this?
