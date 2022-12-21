# Issue 3624: cookbook documentation chapter: coding theory

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-07-09 12:59:24

Assignee: tba

I've put a draft for the coding theory chapter for the cookbook.tex document in 
http://sage.math.washington.edu/home/wdj/cookbook/
To possibly make it easier, I've created this tarball of the directory:
http://sage.math.washington.edu/home/wdj/cookbook2008-07-09.tar.gz


---

Comment by mabshoff created at 2008-07-10 13:23:00

This is unrelated to coercion and should not be assigned against the coercion milestone. Right now 3.0.6 is the default milestone, so please assign new tickets against that milestone.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-10 13:24:41

Is this TeX code stand alone or is there a patch in there somewhere for the new cookbook? If so we should create the cookbook and migrate chapter by chapter over from the old construction manual. Once that is done we remove const.tex and all the other bits related to it.

Cheers,

Michael


---

Comment by wdj created at 2008-07-10 14:44:20

I put a standalone latex file there (http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex) for just that chapter (not in manual style) but also the full latex setup for a new subdirectory of SAGE_ROOT/devel/doc. I don't know how to make a patch to add a cookbook subdirectory to devel/doc. The programming guide discusses adding new files at http://sage.scipy.org/sage/doc/html/prog/node72.html The book http://hgbook.red-bean.com/hgbook.html is hard to search through since the index is for page numbers but the html is in sections, not page numbers.


---

Comment by mvngu created at 2008-10-29 11:22:11

fixes typos in sage-coding-cookbook.tex


---

Attachment

Replying to [comment:3 wdj]:
> I put a standalone latex file there (http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex) for just that chapter (not in manual style) but also the full latex setup for a new subdirectory of SAGE_ROOT/devel/doc. 


I've attached a patch to your file [sage-coding-cookbook.tex](http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex). It mainly fixes typos. I'm still waiting for sage-3.1.4 to finish building on my machine, so at the moment I can't review the sample code in your file.


---

Comment by mvngu created at 2010-03-07 02:11:48

Ticket #8466 supersedes the current ticket.


---

Comment by rws created at 2014-03-20 16:56:35

I took the latest corrected version of the paper, converted it to ReST using pandoc, and fixed that document, including a few typos. I converted the EPS figures to PNG using inkscape. The file is included in the toctree and the general index under number theory because I didn't want a toplevel entry. Maybe replace number theory with discrete math?
----
New commits:


---

Comment by rws created at 2014-03-20 16:56:35

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-05-08 07:06:14


```
sage -t --long src/doc/en/thematic_tutorials/coding_theory.rst
    Error: TAB character found at lines 860,864,865,.,.,.,1064
```



```
+Included in Sage is the group theory package GAP [GAP]_ and GUAVA [GUAVA]_, GA
P’s coding
+theory package. All of GUAVA’s functions can be accessed within Sage.
+   (calling Steve Linton’s C programs in GAP),
+#. Boolean-valueTraceback (most recent call last):
  File "/home/ralf/sage/local/bin/patchbot/patchbot.py", line 468, in test_a_ticket
    res = plugin(ticket, is_git=True, baseline=baseline, **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 149, in non_ascii
    exclude_new(ticket, regex=r'[^\x00-\x7F]', msg="Non-ascii characters", **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 143, in exclude_new
    raise ValueError(full_msg)
ValueError: Non-ascii characters inserted on 35 non-empty lines
```



---

Comment by rws created at 2014-05-08 07:06:14

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-05-13 07:14:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-05-13 07:15:06

Changing status from needs_work to needs_review.


---

Comment by knsam created at 2014-08-11 08:35:23

Could you please rebase this on top of current release (and/or tell me how to do it)? This would be immensely helpful. 

/p/s/ This should be an easy review for me but I have forgotten how to rebase a branch on top of another.


---

Comment by git created at 2014-08-11 08:39:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by knsam created at 2014-08-14 17:49:30

Changing status from needs_review to positive_review.


---

Comment by knsam created at 2014-08-14 17:49:30

I am setting this to Positive Review! Thank to the authors and editor for the great work on this branch!


---

Comment by rws created at 2014-08-14 17:52:12

Thanks for the review!


---

Comment by vbraun created at 2014-08-15 07:35:16

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2014-08-15 07:35:16

PDF docs don't build

```
l.14519 \end{gather}
                    
? 
! Emergency stop.
\math`@`cr`@``@``@` ...`@` \`@`ne \add`@`amps \maxfields`@` \omit 
                                                  \kern -\alignsep`@` \iftag`@` ...
l.14519 \end{gather}
                    
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on thematic_tutorials.log.
 [23make[1]: *** [thematic_tutorials.pdf] Error 1
make[1]: Leaving directory `/home/release/Sage/src/doc/output/latex/en/thematic_tutorials'
]
```



---

Comment by git created at 2014-08-15 13:40:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-08-15 13:41:48

Changing status from needs_work to positive_review.


---

Comment by rws created at 2014-08-15 13:41:48

I really thought I had tested this.


---

Comment by vbraun created at 2014-08-16 09:32:11

Resolution: fixed
