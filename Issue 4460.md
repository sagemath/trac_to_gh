# Issue 4460: add link to PDF manuals in doc/html/index.html

Issue created by migration from https://trac.sagemath.org/ticket/4460

Original creator: schilly

Original creation time: 2008-11-07 10:09:25

Assignee: tba

Adding a link to the PDF versions of the manuals from the /html/index.html page. Both, useful locally and on the website. But I don't know how this page is generated (i get errors or nothing happens) and it isn't even under revision control. Here my improvised patch:


```
add in /sage/devel/doc-main/html/index.html.in at line 88:
------------
 <ul>
	    <li> <font size=+2><a href="../paper-$(PAPER)/" class="title">PDF Versions</a></font>
	      <br>
	  </ul>
-------------
```


An enhancement would be to link to each .pdf file directly, something like "link to html (PDF)" for each link.



---

Attachment

Includes pdf.png


---

Comment by mpatel created at 2009-07-08 19:12:34

To generate the icon I used ImageMagick:

```
convert $SAGE_ROOT/local/share/moin/htdocs/applets/FCKeditor/editor/filemanager/browser/default/images/icons/pdf.gif $SAGE_ROOT/doc/en/website/static/pdf.png
```



---

Comment by mpatel created at 2009-07-08 19:13:02

Changing priority from critical to minor.


---

Comment by mpatel created at 2009-07-09 08:39:03

Note: [attachment:trac_4460_pdf_links.patch] depends on the [attachment:ticket:6485:trac_6485_website_links.patch trac_6485_website_links.patch] at #6485.


---

Comment by mpatel created at 2009-07-14 04:02:11

Can someone check the form and function of the updated page in multiple browsers on Mac OS X?


---

Comment by jhpalmieri created at 2009-07-22 00:35:41

This is with both Safari and Firefox on a Mac.

If I open the file SAGE_ROOT/devel/sage/doc/output/en/index.html, the links work fine.

On the other hand, if I click on the "Help" button from the notebook, then click on "Fast static versions of the Documentation", then the I see pdf links but they don't work: I get messages like "The resource /pdf/en/tutorial/SageTutorial.pdf cannot be found."


---

Comment by mpatel created at 2009-07-22 23:05:40

Apply only this patch.


---

Attachment

Replying to [comment:6 jhpalmieri]:
> On the other hand, if I click on the "Help" button from the notebook, then click on "Fast static versions of the Documentation", then the I see pdf links but they don't work: I get messages like "The resource /pdf/en/tutorial/SageTutorial.pdf cannot be found."
Thanks very much for catching this.  I think v2 covers both the static and offline docs.

Aside:  In the drive for internationalization, perhaps we should instead map `doc/common/output` to, e.g., `http://localhost:8000/doc/static` and serve `index.html` as `http://localhost:8000/doc/static/html/` + `LANG` + `/index.html`.

Correction:  That should be

```
convert $SAGE_ROOT/local/share/moin/htdocs/applets/FCKeditor/editor/filemanager/browser/default/images/icons/pdf.gif $SAGE_ROOT/devel/sage/doc/en/website/static/pdf.png
```



---

Comment by jhpalmieri created at 2009-07-22 23:42:48

Looks good to me.

> Aside: In the drive for internationalization, perhaps we should instead map doc/common/output to, e.g., http://localhost:8000/doc/static and serve index.html as http://localhost:8000/doc/static/html/ + LANG + /index.html.

I have no opinion about this, but if you want to do something about it, let's move it to another ticket.


---

Comment by mvngu created at 2009-07-23 06:57:01

Resolution: fixed


---

Comment by mvngu created at 2009-07-23 06:57:01

Is there an option to turn off this linking to the PDF version of the documents from the HTML version? Currently, we distribute the standard documentation in two standalone formats: as PDF and as HTML; see

http://www.sagemath.org/help.html

The HTML version currently doesn't link to the PDF version, and I think there should be an option to stay with the current situation. If I understand the patch correctly, there is no option to turn off the linking to the PDF version (correct me if I'm wrong). That would be unfortunate as we would need to build both the HTML and PDF versions and distribute them as one single compressed (huge) file.


---

Comment by mpatel created at 2009-07-23 08:23:25

That's a good idea.  With the patch at #6187, it should be straightforward to add a command-line option that selects, in effect, a different layout for the "website" document.  I'll try to implement this soon.  I don't mind side-lining this ticket for another update and review.


---

Comment by mpatel created at 2009-07-24 08:17:12

Apply only this patch.


---

Attachment

Version 3 adds an option `--no-pdf-links` to the doc builder.  Try
 * `sage -docbuild website html --no-pdf-links -S -a`
 * `sage -docbuild website html -S -a`
Note: `-S -a` forces a rewrite.

Since #6187 awaits further inspection, I suggest that we keep waiting on this ticket.  Meanwhile, feel free to populate the website's empty sidebar.  Quick references?


---

Comment by mvngu created at 2009-07-26 07:26:46

The new patch `trac_4460-pdf_links_v3.patch` will need to be moved to another enhancement ticket.


---

Comment by mpatel created at 2009-07-27 07:40:50

Replying to [comment:13 mvngu]:
> The new patch `trac_4460-pdf_links_v3.patch` will need to be moved to another enhancement ticket.
No problem.  I'll wait until there's more feedback on #6187.


---

Comment by mpatel created at 2009-07-28 14:58:17

It seems that `doc/en/website/static/pdf.png` --- a new file --- from [attachment:trac_4460-pdf_links_v2.patch] is missing in v4.1.1.alpha1.


---

Comment by mvngu created at 2009-07-28 17:39:09

add doc/en/website/static/pdf.png to MANIFEST.in


---

Comment by mvngu created at 2009-07-28 17:44:57

Changing status from closed to reopened.


---

Attachment

I'm reopening this ticket since the patch `trac_4460-pdf_links_v2.patch` resulted in a corrupted repository in Sage 4.1.1.alpha1. The patch `trac_4460-manifest.patch` should resolve this issue of corrupt repo. So apply patches in this order:
 1. `trac_4460-pdf_links_v2.patch`
 1. `trac_4460-manifest.patch`
Only `trac_4460-manifest.patch` needs to be reviewed.



mpatel: Can you please open another ticket for the patch `trac_4460-pdf_links_v3.patch` and upload that patch there?


---

Comment by mvngu created at 2009-07-28 17:44:57

Resolution changed from fixed to 


---

Comment by jhpalmieri created at 2009-07-28 18:40:27

Looks good.  Sorry I missed this the first time around.


---

Comment by mpatel created at 2009-07-29 09:14:47

Replying to [comment:16 mvngu]:
> mpatel: Can you please open another ticket for the patch `trac_4460-pdf_links_v3.patch` and upload that patch there?
Absolutely.  Please see #6653.


---

Comment by mvngu created at 2009-07-30 01:46:34

Resolution: fixed


---

Comment by mvngu created at 2009-07-30 01:46:34

Merged:
 1. `trac_4460-pdf_links_v2.patch`
 1. `trac_4460-manifest.patch`
