# Issue 4825: extract worksheets embedded in pdf files

archive/issues_004825.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @dandrake\n\nThis is an ongoing discussion on sage-devel right now.\n\nBasically, we'd like to embed an sws file in a pdf and then be able to upload the pdf file to the notebook and have the notebook automatically extract the sws file and create the worksheet.\n\nWe can use pdfminer to extract the data.  Here's a sample program which extracts the first embedded file in a pdf named 'foo.pdf'.\n\n\n```\nfrom pdflib.pdfparser import PDFDocument, PDFParser\nimport sys\nstdout = sys.stdout\n\ndoc = PDFDocument()\nfp = file('foo.pdf', 'rb')\nparser = PDFParser(doc, fp)\ndoc.initialize()\n\nfor xref in doc.xrefs:\n    for objid in xref.objids():\n        try:\n            obj = doc.getobj(objid)\n        except:\n            continue\n        if isinstance(obj,dict) and 'Type' in obj and obj['Type'].name == \"Annot\":\n            if 'Subtype' in obj and obj['Subtype'].name == \"FileAttachment\":\n                # We have an attached file!\n                filespec = obj['FS']\n                # Look for embedded file; we could try to extract the\n                # filename too (and make sure it's an sws file). but that is platform dependent.  See page\n                # 182 (Section 3.10.2) of\n                # http://www.adobe.com/devnet/acrobat/pdfs/pdf_reference_1-7.pdf.\n                if 'EF' in filespec:\n                    fileobj = filespec['EF']['F']\n                    embeddedspec = filespec['EF']\n                    stdout.write(fileobj.resolve().get_data())\n                    # Just output the first file found.\n                    exit()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4825\n\n",
    "created_at": "2008-12-18T09:08:05Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "extract worksheets embedded in pdf files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4825",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

CC:  @dandrake

This is an ongoing discussion on sage-devel right now.

Basically, we'd like to embed an sws file in a pdf and then be able to upload the pdf file to the notebook and have the notebook automatically extract the sws file and create the worksheet.

We can use pdfminer to extract the data.  Here's a sample program which extracts the first embedded file in a pdf named 'foo.pdf'.


```
from pdflib.pdfparser import PDFDocument, PDFParser
import sys
stdout = sys.stdout

doc = PDFDocument()
fp = file('foo.pdf', 'rb')
parser = PDFParser(doc, fp)
doc.initialize()

for xref in doc.xrefs:
    for objid in xref.objids():
        try:
            obj = doc.getobj(objid)
        except:
            continue
        if isinstance(obj,dict) and 'Type' in obj and obj['Type'].name == "Annot":
            if 'Subtype' in obj and obj['Subtype'].name == "FileAttachment":
                # We have an attached file!
                filespec = obj['FS']
                # Look for embedded file; we could try to extract the
                # filename too (and make sure it's an sws file). but that is platform dependent.  See page
                # 182 (Section 3.10.2) of
                # http://www.adobe.com/devnet/acrobat/pdfs/pdf_reference_1-7.pdf.
                if 'EF' in filespec:
                    fileobj = filespec['EF']['F']
                    embeddedspec = filespec['EF']
                    stdout.write(fileobj.resolve().get_data())
                    # Just output the first file found.
                    exit()
```


Issue created by migration from https://trac.sagemath.org/ticket/4825





---

archive/issue_comments_036510.json:
```json
{
    "body": "3.3 is foremost about the ReST transition, so all tickets should be opened against 3.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-19T11:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36510",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

3.3 is foremost about the ReST transition, so all tickets should be opened against 3.4.

Cheers,

Michael



---

archive/issue_comments_036511.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36511",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036512.json:
```json
{
    "body": "pdfminer is about 350Kb of code.",
    "created_at": "2009-12-09T15:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36512",
    "user": "https://github.com/jasongrout"
}
```

pdfminer is about 350Kb of code.



---

archive/issue_comments_036513.json:
```json
{
    "body": "I feel like maybe this is possible now?",
    "created_at": "2014-09-18T02:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36513",
    "user": "https://github.com/kcrisman"
}
```

I feel like maybe this is possible now?



---

archive/issue_comments_036514.json:
```json
{
    "body": "Unsure if this should be closed, as it could conceivably be useful for historical purposes.  Thoughts?",
    "created_at": "2020-03-29T02:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36514",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Unsure if this should be closed, as it could conceivably be useful for historical purposes.  Thoughts?



---

archive/issue_comments_036515.json:
```json
{
    "body": "sagenb is gone, so...",
    "created_at": "2020-08-25T09:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36515",
    "user": "https://github.com/dimpase"
}
```

sagenb is gone, so...



---

archive/issue_comments_036516.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-25T09:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36516",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036517.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36517",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005071.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-08-29T15:28:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4825#event-5071"
}
```



---

archive/issue_comments_036518.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-29T15:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4825#issuecomment-36518",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
