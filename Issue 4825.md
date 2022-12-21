# Issue 4825: extract worksheets embedded in pdf files

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-18 09:08:05

Assignee: boothby

CC:  ddrake

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



---

Comment by mabshoff created at 2008-12-19 11:36:22

3.3 is foremost about the ReST transition, so all tickets should be opened against 3.4.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-23 02:51:39

Changing type from defect to enhancement.


---

Comment by jason created at 2009-12-09 15:10:35

pdfminer is about 350Kb of code.


---

Comment by kcrisman created at 2014-09-18 02:29:04

I feel like maybe this is possible now?


---

Comment by boothby created at 2020-03-29 02:08:23

Unsure if this should be closed, as it could conceivably be useful for historical purposes.  Thoughts?


---

Comment by dimpase created at 2020-08-25 09:29:41

sagenb is gone, so...


---

Comment by dimpase created at 2020-08-25 09:29:41

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-08-25 09:29:59

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-29 15:28:09

Resolution: invalid
