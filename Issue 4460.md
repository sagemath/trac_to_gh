# Issue 4460: add link to PDF manuals in doc/html/index.html

archive/issues_004460.json:
```json
{
    "body": "Assignee: tba\n\nAdding a link to the PDF versions of the manuals from the /html/index.html page. Both, useful locally and on the website. But I don't know how this page is generated (i get errors or nothing happens) and it isn't even under revision control. Here my improvised patch:\n\n\n```\nadd in /sage/devel/doc-main/html/index.html.in at line 88:\n------------\n <ul>\n\t    <li> <font size=+2><a href=\"../paper-$(PAPER)/\" class=\"title\">PDF Versions</a></font>\n\t      <br>\n\t  </ul>\n-------------\n```\n\n\nAn enhancement would be to link to each .pdf file directly, something like \"link to html (PDF)\" for each link.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4460\n\n",
    "created_at": "2008-11-07T10:09:25Z",
    "labels": [
        "documentation",
        "critical",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "add link to PDF manuals in doc/html/index.html",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4460",
    "user": "schilly"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/4460





---

archive/issue_comments_032908.json:
```json
{
    "body": "Attachment [trac_4460_pdf_links.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460_pdf_links.patch) by mpatel created at 2009-07-08 19:09:51\n\nIncludes pdf.png",
    "created_at": "2009-07-08T19:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32908",
    "user": "mpatel"
}
```

Attachment [trac_4460_pdf_links.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460_pdf_links.patch) by mpatel created at 2009-07-08 19:09:51

Includes pdf.png



---

archive/issue_comments_032909.json:
```json
{
    "body": "To generate the icon I used ImageMagick:\n\n```\nconvert $SAGE_ROOT/local/share/moin/htdocs/applets/FCKeditor/editor/filemanager/browser/default/images/icons/pdf.gif $SAGE_ROOT/doc/en/website/static/pdf.png\n```\n",
    "created_at": "2009-07-08T19:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32909",
    "user": "mpatel"
}
```

To generate the icon I used ImageMagick:

```
convert $SAGE_ROOT/local/share/moin/htdocs/applets/FCKeditor/editor/filemanager/browser/default/images/icons/pdf.gif $SAGE_ROOT/doc/en/website/static/pdf.png
```




---

archive/issue_comments_032910.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2009-07-08T19:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32910",
    "user": "mpatel"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_032911.json:
```json
{
    "body": "Note: [attachment:trac_4460_pdf_links.patch] depends on the [attachment:ticket:6485:trac_6485_website_links.patch trac_6485_website_links.patch] at #6485.",
    "created_at": "2009-07-09T08:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32911",
    "user": "mpatel"
}
```

Note: [attachment:trac_4460_pdf_links.patch] depends on the [attachment:ticket:6485:trac_6485_website_links.patch trac_6485_website_links.patch] at #6485.



---

archive/issue_comments_032912.json:
```json
{
    "body": "Can someone check the form and function of the updated page in multiple browsers on Mac OS X?",
    "created_at": "2009-07-14T04:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32912",
    "user": "mpatel"
}
```

Can someone check the form and function of the updated page in multiple browsers on Mac OS X?



---

archive/issue_comments_032913.json:
```json
{
    "body": "This is with both Safari and Firefox on a Mac.\n\nIf I open the file SAGE_ROOT/devel/sage/doc/output/en/index.html, the links work fine.\n\nOn the other hand, if I click on the \"Help\" button from the notebook, then click on \"Fast static versions of the Documentation\", then the I see pdf links but they don't work: I get messages like \"The resource /pdf/en/tutorial/SageTutorial.pdf cannot be found.\"",
    "created_at": "2009-07-22T00:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32913",
    "user": "jhpalmieri"
}
```

This is with both Safari and Firefox on a Mac.

If I open the file SAGE_ROOT/devel/sage/doc/output/en/index.html, the links work fine.

On the other hand, if I click on the "Help" button from the notebook, then click on "Fast static versions of the Documentation", then the I see pdf links but they don't work: I get messages like "The resource /pdf/en/tutorial/SageTutorial.pdf cannot be found."



---

archive/issue_comments_032914.json:
```json
{
    "body": "Apply only this patch.",
    "created_at": "2009-07-22T23:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32914",
    "user": "mpatel"
}
```

Apply only this patch.



---

archive/issue_comments_032915.json:
```json
{
    "body": "Attachment [trac_4460-pdf_links_v2.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460-pdf_links_v2.patch) by mpatel created at 2009-07-22 23:19:41\n\nReplying to [comment:6 jhpalmieri]:\n> On the other hand, if I click on the \"Help\" button from the notebook, then click on \"Fast static versions of the Documentation\", then the I see pdf links but they don't work: I get messages like \"The resource /pdf/en/tutorial/SageTutorial.pdf cannot be found.\"\nThanks very much for catching this.  I think v2 covers both the static and offline docs.\n\nAside:  In the drive for internationalization, perhaps we should instead map `doc/common/output` to, e.g., `http://localhost:8000/doc/static` and serve `index.html` as `http://localhost:8000/doc/static/html/` + `LANG` + `/index.html`.\n\nCorrection:  That should be\n\n```\nconvert $SAGE_ROOT/local/share/moin/htdocs/applets/FCKeditor/editor/filemanager/browser/default/images/icons/pdf.gif $SAGE_ROOT/devel/sage/doc/en/website/static/pdf.png\n```\n",
    "created_at": "2009-07-22T23:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32915",
    "user": "mpatel"
}
```

Attachment [trac_4460-pdf_links_v2.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460-pdf_links_v2.patch) by mpatel created at 2009-07-22 23:19:41

Replying to [comment:6 jhpalmieri]:
> On the other hand, if I click on the "Help" button from the notebook, then click on "Fast static versions of the Documentation", then the I see pdf links but they don't work: I get messages like "The resource /pdf/en/tutorial/SageTutorial.pdf cannot be found."
Thanks very much for catching this.  I think v2 covers both the static and offline docs.

Aside:  In the drive for internationalization, perhaps we should instead map `doc/common/output` to, e.g., `http://localhost:8000/doc/static` and serve `index.html` as `http://localhost:8000/doc/static/html/` + `LANG` + `/index.html`.

Correction:  That should be

```
convert $SAGE_ROOT/local/share/moin/htdocs/applets/FCKeditor/editor/filemanager/browser/default/images/icons/pdf.gif $SAGE_ROOT/devel/sage/doc/en/website/static/pdf.png
```




---

archive/issue_comments_032916.json:
```json
{
    "body": "Looks good to me.\n\n> Aside: In the drive for internationalization, perhaps we should instead map doc/common/output to, e.g., http://localhost:8000/doc/static and serve index.html as http://localhost:8000/doc/static/html/ + LANG + /index.html.\n\nI have no opinion about this, but if you want to do something about it, let's move it to another ticket.",
    "created_at": "2009-07-22T23:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32916",
    "user": "jhpalmieri"
}
```

Looks good to me.

> Aside: In the drive for internationalization, perhaps we should instead map doc/common/output to, e.g., http://localhost:8000/doc/static and serve index.html as http://localhost:8000/doc/static/html/ + LANG + /index.html.

I have no opinion about this, but if you want to do something about it, let's move it to another ticket.



---

archive/issue_comments_032917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T06:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32917",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_032918.json:
```json
{
    "body": "Is there an option to turn off this linking to the PDF version of the documents from the HTML version? Currently, we distribute the standard documentation in two standalone formats: as PDF and as HTML; see\n\nhttp://www.sagemath.org/help.html\n\nThe HTML version currently doesn't link to the PDF version, and I think there should be an option to stay with the current situation. If I understand the patch correctly, there is no option to turn off the linking to the PDF version (correct me if I'm wrong). That would be unfortunate as we would need to build both the HTML and PDF versions and distribute them as one single compressed (huge) file.",
    "created_at": "2009-07-23T06:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32918",
    "user": "mvngu"
}
```

Is there an option to turn off this linking to the PDF version of the documents from the HTML version? Currently, we distribute the standard documentation in two standalone formats: as PDF and as HTML; see

http://www.sagemath.org/help.html

The HTML version currently doesn't link to the PDF version, and I think there should be an option to stay with the current situation. If I understand the patch correctly, there is no option to turn off the linking to the PDF version (correct me if I'm wrong). That would be unfortunate as we would need to build both the HTML and PDF versions and distribute them as one single compressed (huge) file.



---

archive/issue_comments_032919.json:
```json
{
    "body": "That's a good idea.  With the patch at #6187, it should be straightforward to add a command-line option that selects, in effect, a different layout for the \"website\" document.  I'll try to implement this soon.  I don't mind side-lining this ticket for another update and review.",
    "created_at": "2009-07-23T08:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32919",
    "user": "mpatel"
}
```

That's a good idea.  With the patch at #6187, it should be straightforward to add a command-line option that selects, in effect, a different layout for the "website" document.  I'll try to implement this soon.  I don't mind side-lining this ticket for another update and review.



---

archive/issue_comments_032920.json:
```json
{
    "body": "Apply only this patch.",
    "created_at": "2009-07-24T08:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32920",
    "user": "mpatel"
}
```

Apply only this patch.



---

archive/issue_comments_032921.json:
```json
{
    "body": "Attachment [trac_4460-pdf_links_v3.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460-pdf_links_v3.patch) by mpatel created at 2009-07-24 08:30:48\n\nVersion 3 adds an option `--no-pdf-links` to the doc builder.  Try\n* `sage -docbuild website html --no-pdf-links -S -a`\n* `sage -docbuild website html -S -a`\nNote: `-S -a` forces a rewrite.\n\nSince #6187 awaits further inspection, I suggest that we keep waiting on this ticket.  Meanwhile, feel free to populate the website's empty sidebar.  Quick references?",
    "created_at": "2009-07-24T08:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32921",
    "user": "mpatel"
}
```

Attachment [trac_4460-pdf_links_v3.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460-pdf_links_v3.patch) by mpatel created at 2009-07-24 08:30:48

Version 3 adds an option `--no-pdf-links` to the doc builder.  Try
* `sage -docbuild website html --no-pdf-links -S -a`
* `sage -docbuild website html -S -a`
Note: `-S -a` forces a rewrite.

Since #6187 awaits further inspection, I suggest that we keep waiting on this ticket.  Meanwhile, feel free to populate the website's empty sidebar.  Quick references?



---

archive/issue_comments_032922.json:
```json
{
    "body": "The new patch `trac_4460-pdf_links_v3.patch` will need to be moved to another enhancement ticket.",
    "created_at": "2009-07-26T07:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32922",
    "user": "mvngu"
}
```

The new patch `trac_4460-pdf_links_v3.patch` will need to be moved to another enhancement ticket.



---

archive/issue_comments_032923.json:
```json
{
    "body": "Replying to [comment:13 mvngu]:\n> The new patch `trac_4460-pdf_links_v3.patch` will need to be moved to another enhancement ticket.\nNo problem.  I'll wait until there's more feedback on #6187.",
    "created_at": "2009-07-27T07:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32923",
    "user": "mpatel"
}
```

Replying to [comment:13 mvngu]:
> The new patch `trac_4460-pdf_links_v3.patch` will need to be moved to another enhancement ticket.
No problem.  I'll wait until there's more feedback on #6187.



---

archive/issue_comments_032924.json:
```json
{
    "body": "It seems that `doc/en/website/static/pdf.png` --- a new file --- from [attachment:trac_4460-pdf_links_v2.patch] is missing in v4.1.1.alpha1.",
    "created_at": "2009-07-28T14:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32924",
    "user": "mpatel"
}
```

It seems that `doc/en/website/static/pdf.png` --- a new file --- from [attachment:trac_4460-pdf_links_v2.patch] is missing in v4.1.1.alpha1.



---

archive/issue_comments_032925.json:
```json
{
    "body": "add doc/en/website/static/pdf.png to MANIFEST.in",
    "created_at": "2009-07-28T17:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32925",
    "user": "mvngu"
}
```

add doc/en/website/static/pdf.png to MANIFEST.in



---

archive/issue_comments_032926.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-28T17:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32926",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_032927.json:
```json
{
    "body": "Attachment [trac_4460-manifest.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460-manifest.patch) by mvngu created at 2009-07-28 17:44:57\n\nI'm reopening this ticket since the patch `trac_4460-pdf_links_v2.patch` resulted in a corrupted repository in Sage 4.1.1.alpha1. The patch `trac_4460-manifest.patch` should resolve this issue of corrupt repo. So apply patches in this order:\n1. `trac_4460-pdf_links_v2.patch`\n2. `trac_4460-manifest.patch`\nOnly `trac_4460-manifest.patch` needs to be reviewed.\n\n\n\nmpatel: Can you please open another ticket for the patch `trac_4460-pdf_links_v3.patch` and upload that patch there?",
    "created_at": "2009-07-28T17:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32927",
    "user": "mvngu"
}
```

Attachment [trac_4460-manifest.patch](tarball://root/attachments/some-uuid/ticket4460/trac_4460-manifest.patch) by mvngu created at 2009-07-28 17:44:57

I'm reopening this ticket since the patch `trac_4460-pdf_links_v2.patch` resulted in a corrupted repository in Sage 4.1.1.alpha1. The patch `trac_4460-manifest.patch` should resolve this issue of corrupt repo. So apply patches in this order:
1. `trac_4460-pdf_links_v2.patch`
2. `trac_4460-manifest.patch`
Only `trac_4460-manifest.patch` needs to be reviewed.



mpatel: Can you please open another ticket for the patch `trac_4460-pdf_links_v3.patch` and upload that patch there?



---

archive/issue_comments_032928.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-28T17:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32928",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_032929.json:
```json
{
    "body": "Looks good.  Sorry I missed this the first time around.",
    "created_at": "2009-07-28T18:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32929",
    "user": "jhpalmieri"
}
```

Looks good.  Sorry I missed this the first time around.



---

archive/issue_comments_032930.json:
```json
{
    "body": "Replying to [comment:16 mvngu]:\n> mpatel: Can you please open another ticket for the patch `trac_4460-pdf_links_v3.patch` and upload that patch there?\nAbsolutely.  Please see #6653.",
    "created_at": "2009-07-29T09:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32930",
    "user": "mpatel"
}
```

Replying to [comment:16 mvngu]:
> mpatel: Can you please open another ticket for the patch `trac_4460-pdf_links_v3.patch` and upload that patch there?
Absolutely.  Please see #6653.



---

archive/issue_comments_032931.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-30T01:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32931",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_032932.json:
```json
{
    "body": "Merged:\n1. `trac_4460-pdf_links_v2.patch`\n2. `trac_4460-manifest.patch`",
    "created_at": "2009-07-30T01:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4460#issuecomment-32932",
    "user": "mvngu"
}
```

Merged:
1. `trac_4460-pdf_links_v2.patch`
2. `trac_4460-manifest.patch`
