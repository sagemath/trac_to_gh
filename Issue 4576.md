# Issue 4576: biopython optional package upgrade to 1.49beta

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-11-21 14:58:48

Assignee: mabshoff

Keywords: biopython, optional packages

Biopython 1.49 beta was released November 7th, 2008.  Its a bigger release than the number indicates - one nice thing was a change from requiring Numeric for some things to using numpy consistently, which makes the install simpler and things are more sage-compatible.

The install should be tested on something other than what I have available right now which is an intel mac running 10.5.

The package is at: 
[http://www.d.umn.edu/~mhampton/biopython-1.49b.spkg](http://www.d.umn.edu/~mhampton/biopython-1.49b.spkg)


---

Comment by mhansen created at 2008-11-21 17:05:17

This builds and installs fine on my Ubuntu 8.10 machine.


---

Comment by was created at 2008-11-21 22:26:18

The tarball has a massive amount of meta-crap:

```
...
biopython-1.49b/biopython-1.49b/Tests/MEME/._mast.dna.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/mast.dna.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/._mast.protein.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/mast.protein.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/._mast.protein.tcm.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/mast.protein.tcm.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/._meme.dna.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/meme.dna.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/._meme.protein.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/meme.protein.oops.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/._meme.protein.tcm.txt
biopython-1.49b/biopython-1.49b/Tests/MEME/meme.protein.tcm.txt
```


Note all the ._ files.  OS X sticks them there.  Can you make the 
thing again using sage.math (or any other linux box)?

The install works fine on sage.math:

```
real	0m21.822s
user	0m17.317s
sys	0m2.876s
Successfully installed biopython-1.49b
```


How do I test that it works?  Can you give a few sample commands or explain how to run the biopython test suite?

William


---

Comment by mhampton created at 2008-11-22 00:33:25

I don't have an account on sage.math, maybe its time to get one.  Right now I'm in Thunder Bay, Ontario, so my options are more limited than usual.  I could also try to write something remove all the cruft - perhaps I could delete every file starting with "._"?  

The distributed biopython test suite is in the Tests folder of the spkg, I think it is not installed currently into sage.  To run it you just do "python run_tests.py" within the biopython/Tests directory.  

Here are some simple things to do:


```
Search for nucleotide records of Salvia divinorum (sage of the seers):
from Bio import Entrez, SeqIO
Entrez.email = "hamptonio`@`gmail.com" # Always tell NCBI who you are 
handle = Entrez.esearch(db="Nucleotide", term="salvia divinorum") 
record = Entrez.read(handle)
record["IdList"]
['113715469', '113715388', '111119918', '81230846', '81230845',
'46326321', '1695982', '349139']
```


Take the first record found above and get its GenBank file, parse it, and read the description:

```
from Bio import Entrez, SeqIO
Entrez.email = "hamptonio`@`gmail.com" # Always tell NCBI who you are 
handle = Entrez.efetch(db="nucleotide", id="113715469", rettype="genbank") 
rec = SeqIO.parse(handle,'genbank')
x = rec.next()
x.description
'Salvia divinorum isolate x093 tRNA-Leu (trnL) gene and trnL-trnF
intergenic spacer, partial sequence; chloroplast.'
```


or check its taxononomy:

```
x.annotations['taxonomy']
['Eukaryota', 'Viridiplantae', 'Streptophyta', 'Embryophyta',
'Tracheophyta', 'Spermatophyta', 'Magnoliophyta', 'eudicotyledons',
'core eudicotyledons', 'asterids', 'lamiids', 'Lamiales', 'Lamiaceae',
'Nepetoideae', 'Mentheae', 'Salvia']
```



---

Comment by mhampton created at 2008-11-24 22:48:16

I have made an spkg that I think is clean now.


---

Comment by was created at 2008-11-28 06:51:14

REFEREE REPORT:

1. The crap is gone. :-)

2. I tried out some of the things above and it works.

3. It would be good to have an spkg-check script, which would look like this. This would get run automatically when one does 

```
export SAGE_CHECK="yes"
```

before installing. 
Here's spkg-check, probably:
{{{#!/bin/sh
cd biopython/Tests/
python run_tests.py
```


4. However the test suite itself fails 5 tests.  Can you comment on this?

```
was`@`sage:~/build/sage-3.2.1.alpha1/biopython-1.49b/biopython/Tests$ python run_tests.py
test_Ace ... ok
test_AlignIO ... ok
test_BioSQL ... skipping. Enter your settings in Tests/setup_BioSQL.py (not important if you do not plan to use BioSQL).
ok
test_BioSQL_SeqIO ... skipping. Enter your settings in Tests/setup_BioSQL.py (not important if you do not plan to use BioSQL).
ok
test_CAPS ... ERROR
test_Clustalw ... ok
test_Clustalw_tool ... skipping. Install clustalw or clustalw2 if you want to use Bio.Clustalw.
ok
test_Cluster ... FAIL
test_CodonTable ... ok
test_CodonUsage ... ok
test_Compass ... ok
test_Crystal ... ok
test_DocSQL ... skipping. Install MySQLdb if you want to use Bio.DocSQL.
ok
test_EmbossPrimer ... ok
test_Entrez ... ok
test_Enzyme ... ok
test_FSSP ... ok
test_Fasta ... ok
test_Fasta2 ... ok
test_File ... ok
test_GACrossover ... ok
test_GAMutation ... ok
test_GAOrganism ... ok
test_GAQueens ... ok
test_GARepair ... ok
test_GASelection ... ok
test_GFF ... skipping. Environment is not configured for this test (not important if you do not plan to use Bio.GFF).
ok
test_GFF2 ... skipping. Install MySQLdb if you want to use Bio.GFF.
ok
test_GenBank ... ok
test_GraphicsChromosome ... skipping. Install reportlab if you want to use Bio.Graphics.
ok
test_GraphicsDistribution ... skipping. Install reportlab if you want to use Bio.Graphics.
ok
test_GraphicsGeneral ... skipping. Install reportlab if you want to use Bio.Graphics.
ok
test_HMMCasino ... ok
test_HMMGeneral ... ok
test_HotRand ... ok
test_IsoelectricPoint ... ok
test_KDTree ... ERROR
test_KEGG ... ok
test_KeyWList ... ok
test_Location ... ok
test_LocationParser ... ok
test_LogisticRegression ... ok
test_MEME ... ok
test_MarkovModel ... ok
test_Medline ... ok
test_NCBIStandalone ... ok
test_NCBIXML ... ok
test_NCBI_qblast ... ok
test_NNExclusiveOr ... ok
test_NNGene ... ok
test_NNGeneral ... ok
test_Nexus ... ok
test_PDB ... ok
test_ParserSupport ... ok
test_Pathway ... ok
test_Phd ... ok
test_PopGen_FDist ... skipping. Install FDist if you want to use Bio.PopGen.FDist.
ok
test_PopGen_FDist_nodepend ... ok
test_PopGen_GenePop ... ok
test_PopGen_SimCoal ... skipping. Install SIMCOAL2 if you want to use Bio.PopGen.SimCoal.
ok
test_PopGen_SimCoal_nodepend ... ok
test_ProtParam ... ok
test_Registry ... ok
test_Restriction ... ERROR
test_SCOP_Astral ... ok
test_SCOP_Cla ... ok
test_SCOP_Des ... ok
test_SCOP_Dom ... ok
test_SCOP_Hie ... ok
test_SCOP_Raf ... ok
test_SCOP_Residues ... ok
test_SCOP_Scop ... ok
test_SProt ... ok
test_SVDSuperimposer ... ok
test_SeqIO ... `^Hok
test_SeqIO_online ... ok
test_SeqUtils ... ok
test_SubsMat ... ok
test_UniGene ... ok
test_Wise ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.
ok
test_align ... ok
test_docstrings ... ok
test_geo ... ok
test_interpro ... ok
test_kNN ... ok
test_pairwise2 ... ok
test_prodoc ... ok
test_property_manager ... ok
test_prosite ... ok
test_prosite2 ... ok
test_psw ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.
ok
test_seq ... ok
test_translate ... ok
test_trie ... ERROR
test_triefind ... ERROR

======================================================================
ERROR: test_CAPS
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_tests.py", line 125, in runTest
    self.runSafeTest()
  File "run_tests.py", line 138, in runSafeTest
    cur_test = __import__(self.test_name)
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Tests/test_CAPS.py", line 3, in <module>
    from Bio.Restriction import *
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/Restriction/__init__.py", line 61, in <module>
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/Restriction/Restriction.py", line 96, in <module>
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/Restriction/PrintFormat.py", line 14, in <module>
ImportError: No module named DNAUtils

======================================================================
ERROR: test_KDTree
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_tests.py", line 125, in runTest
    self.runSafeTest()
  File "run_tests.py", line 138, in runSafeTest
    cur_test = __import__(self.test_name)
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Tests/test_KDTree.py", line 1, in <module>
    from Bio.KDTree.KDTree import _neighbor_test, _test
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/KDTree/__init__.py", line 10, in <module>
    #
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/KDTree/KDTree.py", line 13, in <module>
ImportError: cannot import name _CKDTree

======================================================================
ERROR: test_Restriction
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_tests.py", line 125, in runTest
    self.runSafeTest()
  File "run_tests.py", line 138, in runSafeTest
    cur_test = __import__(self.test_name)
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Tests/test_Restriction.py", line 8, in <module>
    from Bio.Restriction import *
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/Restriction/__init__.py", line 61, in <module>
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/Restriction/Restriction.py", line 96, in <module>
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Bio/Restriction/PrintFormat.py", line 13, in <module>
ImportError: cannot import name RanaConfig

======================================================================
ERROR: test_trie
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_tests.py", line 125, in runTest
    self.runSafeTest()
  File "run_tests.py", line 138, in runSafeTest
    cur_test = __import__(self.test_name)
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Tests/test_trie.py", line 6, in <module>
    from Bio import trie
ImportError: cannot import name trie

======================================================================
ERROR: test_triefind
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_tests.py", line 125, in runTest
    self.runSafeTest()
  File "run_tests.py", line 138, in runSafeTest
    cur_test = __import__(self.test_name)
  File "/Users/mh/sagestuff/biopython-1.49b/biopython-1.49b/Tests/test_triefind.py", line 6, in <module>
    from Bio import trie
ImportError: cannot import name trie

======================================================================
FAIL: test_Cluster
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_tests.py", line 125, in runTest
    self.runSafeTest()
  File "run_tests.py", line 162, in runSafeTest
    expected_handle)
  File "run_tests.py", line 263, in compare_output
    % (repr(output_line), repr(expected_line))
AssertionError: 
Output  : 'test_clusterdistance (test_Cluster.TestCluster) ... ERROR\n'
Expected: 'test_clusterdistance (test_Cluster.TestCluster) ... ok\n'

----------------------------------------------------------------------
Ran 95 tests in 147.466s

FAILED (failures=1, errors=5)
You have new mail in /var/mail/was
```



---

Comment by mhampton created at 2008-11-29 14:29:38

I think most of those errors are being tracked [here](http://bugzilla.open-bio.org).  The KDTree failure might be from it not being built by default.  

I still think this optional package should go out, since it is better than what we had before.  In the now distributed biopython-1.47 there is a lot of stuff that doesn't work because it requires Numeric, and a lot of that now works because of their Numeric to numpy migration.  

One reason I want this to go in is so I can write better `@`interact examples and I want people to be able to recreate them.  As far as I know I am the only real user of sage+biopython and I want to give it more exposure.  When the final biopython-1.49 comes out I will make a package for it too.

I will start working on a spkg-check, but I would like this to available sooner rather than later.


---

Comment by was created at 2008-11-29 18:54:14

Based on mhamptom's arguments above, and that this is an *optional* package, and he is the official maintainer, I think this should go in. 

It would be nice if at the end of the install a message were printed about "issues".


---

Comment by mabshoff created at 2008-11-29 21:43:14

Merged in the optional spkg repo and mirrored out.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 21:43:14

Resolution: fixed
