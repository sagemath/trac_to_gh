# Issue 1839: [with script; needs review and integration] sage-crap: incorporate this script into sage and start using it before each release.

Issue created by migration from https://trac.sagemath.org/ticket/1839

Original creator: was

Original creation time: 2008-01-18 22:04:27

Assignee: malb




---

Comment by mabshoff created at 2008-01-18 22:07:37

Changing assignee from malb to mabshoff.


---

Comment by mabshoff created at 2008-01-18 22:07:37

Changing component from commutative algebra to packages.


---

Comment by was created at 2008-04-05 22:21:08

I BSD license this file

```
* Copyright (c) 2008, William Stein (with permission)
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions are met:
*     * Redistributions of source code must retain the above copyright
*       notice, this list of conditions and the following disclaimer.
*     * Redistributions in binary form must reproduce the above copyright
*       notice, this list of conditions and the following disclaimer in the
*       documentation and/or other materials provided with the distribution.
*     * Neither the name of the Sage Project nor the
*       names of its contributors may be used to endorse or promote products
*       derived from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY WILLIAM STEIN ``AS IS'' AND ANY
* EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
* WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
* DISCLAIMED. IN NO EVENT SHALL William Stein BE LIABLE FOR ANY
* DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
* (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
* ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
* SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```



---

Comment by was created at 2008-04-06 07:57:37

See http://8tb.us/home/boothby/crap.patch


---

Attachment

The attached patch integrates sage-crap, and works on my machines. (debian xeon / ubuntu 32bit)


---

Comment by mabshoff created at 2008-05-06 11:02:25

A couple remarks:

 * is this script still destructive? In that care it should be mentioned in the help
 * the script does deal with spkgs and not tars per se - maybe the help in sage-sage should be changed?

Other than we might want to add a -crapall option since that is likely the default way one would deploy such a script, i.e. before a release. Maybe even adding a crap score might be a good thing :)

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-15 21:35:42

Changing keywords from "" to "editor_wstein".


---

Comment by was created at 2008-06-15 22:10:34

The referee report is above by malb.  William Stein will do the work to fix this patch.


---

Comment by was created at 2008-06-15 23:30:10

Example of using this with runlevel=1 on sage-3.0.3.alpha2 -- where we see there is some crap!:

```
was@sage:~/build/sage-3.0.3.alpha2$ ./sage -crap sage-3.0.3.alpha2.tar 
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2.tar
runlevel=  1
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/src-gmp/.DS_Store: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/src/.DS_Store: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src/.DS_Store.1: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src/.DS_Store: empty
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src-gmp/.DS_Store.1: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src-gmp/.DS_Store: empty
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/.DS_Store.1: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.aux: LaTeX auxiliary file
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.dvi: TeX DVI
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.toc: UNKNOWN
cddlibman.toc: LaTeX  table of contents
```



---

Attachment

part 2 of the patch


---

Comment by was created at 2008-06-19 23:02:36

I requested boothby to review this.


---

Comment by was created at 2008-07-08 00:32:58

I consider my having read over it as a review and my little integration patch as part of that.


---

Comment by mabshoff created at 2008-07-08 00:38:55

Merged in Sage 3.0.4.rc0. I also give this ticket a positive review and all issues that crop up will be dealt with on follow up tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-08 00:42:05

Merged in Sage 3.0.4.rc0


---

Comment by mabshoff created at 2008-07-08 00:42:05

Resolution: fixed
