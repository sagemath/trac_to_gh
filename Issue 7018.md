# Issue 7018: Looking for trees with search_doc("tree") is a bad idea

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-09-26 07:19:47

Assignee: tba

CC:  ddrake

I understand the word "tree" may be the only way to get this result, the other words being less common or not mathematics-related... Even though :

```
sage: search_doc("tree")
html/en/installation/source.html:226:tree. This can take close to an hour on some machines. Depending on the
html/en/installation/source.html:246:build tree to <tt class="docutils literal"><span class="pre">/usr/local</span></tt>. You might also copy the <tt class="docutils literal"><span class="pre">sage-*/sage</span>html/en/installation/index.html:59:<li class="toctree-l1"><a class="reference external" href="introduction.html">Introduction</a></li>
html/en/installation/index.html:62:<li class="toctree-l1"><a class="reference external" href="binary.html">Pre-built Binary Install</a><ul>
html/en/installation/index.html:63:<li class="toctree-l2"><a class="reference external" href="binary.html#linux-and-os-x">Linux and OS X</a></li>
html/en/installation/index.html:64:<li class="toctree-l2"><a class="reference external" href="binary.html#microsoft-windows">Microsoft Windows</a></li>
html/en/installation/index.html:69:<li class="toctree-l1"><a class="reference external" href="source.html">Install from Source Code</a><ul>
html/en/installation/index.html:70:<li class="toctree-l2"><a class="reference external" href="source.html#steps-to-install-from-source">Steps to Install from Source</a></li>
html/en/installation/index.html:71:<li class="toctree-l2"><a class="reference external" href="source.html#installation-in-a-multiuser-environment">Installation in a Multiuser Environment</a></li>
html/en/installation/index.html:72:<li class="toctree-l2"><a class="reference external" href="source.html#special-notes">Special Notes</a></li>
html/en/installation/index.html:77:<li class="toctree-l1"><a class="reference external" href="icon.html">Desktop icon</a></li>
html/en/installation/index.html:80:<li class="toctree-l1"><a class="reference external" href="documentation.html">The Documentation</a></li>
html/en/numerical_sage/index.html:72:<li class="toctree-l1"><a class="reference external" href="numerical_tools.html">Numerical Tools</a><ul>
html/en/numerical_sage/index.html:73:<li class="toctree-l2"><a class="reference external" href="numpy.html">NumPy</a></li>
html/en/numerical_sage/index.html:74:<li class="toctree-l2"><a class="reference external" href="scipy.html">SciPy</a></li>

```

and much more below, as class=doctree is in all the lines... ;-)

Nathann


---

Comment by jhpalmieri created at 2010-01-20 02:49:07

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-01-20 02:49:07

Here is a patch.  This implements two new keywords for searching, one of which addresses the issue in this ticket.  These work for `search_src`, `search_doc`, and `search_def`.

 - You can now do `search_doc('tree', whole_word=True)`, and it will look for 'tree' as a whole word, not returning matches for 'toctree' or 'trees'.

 - You can now do `search_src('TreE', ignore_case=True)`, and it will return matches for 'TREE', 'Tree', 'tree', etc., completely ignoring case.  (By default, all searches continue to be case-sensitive, so `search_src('TreE')` returns no matches.)


---

Comment by ddrake created at 2010-01-21 00:09:45

Changing status from needs_review to positive_review.


---

Attachment

This looks good, works as advertised, and passes all doctests. Positive review.


---

Comment by mvngu created at 2010-01-23 15:50:52

Resolution: fixed


---

Comment by nthiery created at 2010-04-18 08:40:07

See also discussion on sage-combinat-devel: http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/8560fa9a2eda7712
