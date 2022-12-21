# Issue 7784: sagenb -- either include setup.cfg if it is human-written or put it in the .hgignore file

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-29 08:26:16

Assignee: was

CC:  mvngu robert.marik

Observe in sagenb-0.4.8:

```
flat:src wstein$ hg status
M setup.py
? release_notes.txt
? setup.cfg
flat:src wstein$ more setup.cfg
[egg_info]
tag_build =
tag_date = 0
tag_svn_revision = 0
```



This makes me think it is human written?  http://www.python.org/doc/2.1.3/dist/setup-config.html


---

Comment by mpatel created at 2010-01-25 03:41:41

Update .hgignore.


---

Comment by mpatel created at 2010-01-25 03:43:14

Changing priority from major to minor.


---

Comment by mpatel created at 2010-01-25 03:43:14

Changing status from new to needs_review.


---

Attachment

In the patch, I've added `setup.cfg` and `release_notes.txt` and attempted to remove unnecessary entries.  Please feel free to go further.


---

Comment by mpatel created at 2010-01-25 04:08:07

I think I should restore `push` and `pull`.


---

Attachment

Include `pull` and `push`.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 04:30:05

Replying to [comment:3 mpatel]:
> I think I should restore `push` and `pull`.
V2 does this.


---

Comment by mpatel created at 2010-02-01 03:38:24

Changing type from enhancement to defect.


---

Comment by mpatel created at 2010-02-01 03:38:24

Changing priority from minor to critical.


---

Attachment

Add Makefile; update .hgignore and spkg-related files.  Apply only this patch.


---

Comment by mpatel created at 2010-02-01 03:40:56

The [attachment:trac_7784-sagenb_spkg_files.patch new patch] cleans up some build-related files.  This "blocks" #8051.


---

Comment by mpatel created at 2010-02-01 03:46:03

I haven't decided yet what to do about `release_notes.txt`, so I haven't updated it.  If we can auto-generate it, that would be great.


---

Comment by mvngu created at 2010-02-01 04:29:13

Replying to [comment:7 mpatel]:
> I haven't decided yet what to do about `release_notes.txt`, so I haven't updated it.  If we can auto-generate it, that would be great.

I have been using the script at the following site to generate release notes for Sage:

http://bitbucket.org/mvngu/rnotes/

I think an option could be added to that script to generate release notes for sagenb. The current usage for the script is

```
./generate_release_notes sage-x.y.z
```

A possible option for generating sagenb specific release notes is

```
./generate_release_notes sage-x.y.z -sagenb
```

This would generate a release note for all sagenb specific tickets closed in the Sage x.y.z milestone. It's possible that during a particular milestone, more than one version of sagenb is released and integrated into Sage. Another possibility is 

```
./generate_release_notes sagenb-x.y.z
```

This would generate a release note for sagenb x.y.z.


---

Comment by mpatel created at 2010-02-01 06:39:59

Changing assignee from was to mpatel.


---

Comment by mpatel created at 2010-02-01 06:39:59

Thanks!  I'll definitely take a closer look (though not immediately).  I assume we'll make it separate ticket so we don't hold up this one.


---

Comment by mpatel created at 2010-02-01 07:47:33

Changing assignee from mpatel to was.


---

Comment by mvngu created at 2010-02-02 23:26:18

Looks good to me. Apply the attachment [trac_7784-sagenb_spkg_files.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7784/trac_7784-sagenb_spkg_files.patch) to [sagenb-0.7.2.spkg](http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg) under the directory `sagenb-0.7.2/src/sagenb`.


---

Comment by mvngu created at 2010-02-02 23:26:18

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-03 02:17:07

Resolution: fixed
