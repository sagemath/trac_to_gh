# Issue 6328: [with patch, positive review] optional doctest failure -- bugs in the graph theory section of constructions guide

archive/issues_006328.json:
```json
{
    "body": "Assignee: tbd\n\n```\nsage -t -long --optional devel/sage/doc/en/constructions/graph_theory.rst\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 141:\n    sage: print gap.eval(\"Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true )\")  # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[4]>\", line 1, in <module>\n        print gap.eval(\"Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true )\")  # optional gap package###line 141:\n    sage: print gap.eval(\"Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true )\")  # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Variable: 'Gamma' is read only\n\n       executing Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true );\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 145:\n    sage: print gap.eval(\"Adjacency(Gamma,1)\")           # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[5]>\", line 1, in <module>\n        print gap.eval(\"Adjacency(Gamma,1)\")           # optional gap package###line 145:\n    sage: print gap.eval(\"Adjacency(Gamma,1)\")           # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Record Element: <rec> must be a record (not a function)\n\n       executing Adjacency(Gamma,1);\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 147:\n    sage: print gap.eval(\"Adjacency(Gamma,2)\")           # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[6]>\", line 1, in <module>\n        print gap.eval(\"Adjacency(Gamma,2)\")           # optional gap package###line 147:\n    sage: print gap.eval(\"Adjacency(Gamma,2)\")           # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Record Element: <rec> must be a record (not a function)\n\n       executing Adjacency(Gamma,2);\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 149:\n    sage: print gap.eval(\"Adjacency(Gamma,3)\")           # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[7]>\", line 1, in <module>\n        print gap.eval(\"Adjacency(Gamma,3)\")           # optional gap package###line 149:\n    sage: print gap.eval(\"Adjacency(Gamma,3)\")           # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Record Element: <rec> must be a record (not a function)\n\n       executing Adjacency(Gamma,3);\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 151:\n    sage: print gap.eval(\"IsEdge( Gamma, [ 1, 2 ] )\")    # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[8]>\", line 1, in <module>\n        print gap.eval(\"IsEdge( Gamma, [ 1, 2 ] )\")    # optional gap package###line 151:\n    sage: print gap.eval(\"IsEdge( Gamma, [ 1, 2 ] )\")    # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Error, usage: IsEdge( <Graph>, <obj> )\n\n       executing IsEdge( Gamma, [ 1, 2 ] );\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 153:\n    sage: print gap.eval(\"Vertices( Gamma )\")            # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[9]>\", line 1, in <module>\n        print gap.eval(\"Vertices( Gamma )\")            # optional gap package###line 153:\n    sage: print gap.eval(\"Vertices( Gamma )\")            # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Error, no 1st choice method found for `Vertices' on 1 arguments\n\n       executing Vertices( Gamma );\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 163:\n    sage: print gap.eval(\"Distance( Gamma, 1, 3 )\")      # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[2]>\", line 1, in <module>\n        print gap.eval(\"Distance( Gamma, 1, 3 )\")      # optional gap package###line 163:\n    sage: print gap.eval(\"Distance( Gamma, 1, 3 )\")      # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Error, usage: Distance( <Graph>, <Int> or <List>, <Int> or <List> [, <PermGrou\\\n    p> ] )\n\n       executing Distance( Gamma, 1, 3 );\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst\", line 173:\n    sage: print gap.eval(\"Distance( Gamma, 1, 2 )\")      # optional gap package\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[2]>\", line 1, in <module>\n        print gap.eval(\"Distance( Gamma, 1, 2 )\")      # optional gap package###line 173:\n    sage: print gap.eval(\"Distance( Gamma, 1, 2 )\")      # optional gap package\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 480, in eval\n        result = Expect.eval(self, input_line, **kwds)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 975, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 722, in _eval_line\n        raise RuntimeError, message\n    RuntimeError: Gap produced error output\n    Error, usage: Distance( <Graph>, <Int> or <List>, <Int> or <List> [, <PermGrou\\\n    p> ] )\n\n       executing Distance( Gamma, 1, 2 );\n**********************************************************************\n3 items had failures:\n   6 of  10 in __main__.example_5\n   1 of   3 in __main__.example_6\n   1 of   3 in __main__.example_7\n***Test Failed*** 8 failures.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6328\n\n",
    "closed_at": "2009-09-09T11:14:52Z",
    "created_at": "2009-06-16T15:05:16Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] optional doctest failure -- bugs in the graph theory section of constructions guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6328",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

```
sage -t -long --optional devel/sage/doc/en/constructions/graph_theory.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 141:
    sage: print gap.eval("Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true )")  # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        print gap.eval("Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true )")  # optional gap package###line 141:
    sage: print gap.eval("Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true )")  # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Variable: 'Gamma' is read only

       executing Gamma := Graph( G, [1..3], OnPoints, function(x,y) return A[x][y] = 1; end,true );
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 145:
    sage: print gap.eval("Adjacency(Gamma,1)")           # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[5]>", line 1, in <module>
        print gap.eval("Adjacency(Gamma,1)")           # optional gap package###line 145:
    sage: print gap.eval("Adjacency(Gamma,1)")           # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Record Element: <rec> must be a record (not a function)

       executing Adjacency(Gamma,1);
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 147:
    sage: print gap.eval("Adjacency(Gamma,2)")           # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[6]>", line 1, in <module>
        print gap.eval("Adjacency(Gamma,2)")           # optional gap package###line 147:
    sage: print gap.eval("Adjacency(Gamma,2)")           # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Record Element: <rec> must be a record (not a function)

       executing Adjacency(Gamma,2);
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 149:
    sage: print gap.eval("Adjacency(Gamma,3)")           # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[7]>", line 1, in <module>
        print gap.eval("Adjacency(Gamma,3)")           # optional gap package###line 149:
    sage: print gap.eval("Adjacency(Gamma,3)")           # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Record Element: <rec> must be a record (not a function)

       executing Adjacency(Gamma,3);
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 151:
    sage: print gap.eval("IsEdge( Gamma, [ 1, 2 ] )")    # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[8]>", line 1, in <module>
        print gap.eval("IsEdge( Gamma, [ 1, 2 ] )")    # optional gap package###line 151:
    sage: print gap.eval("IsEdge( Gamma, [ 1, 2 ] )")    # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Error, usage: IsEdge( <Graph>, <obj> )

       executing IsEdge( Gamma, [ 1, 2 ] );
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 153:
    sage: print gap.eval("Vertices( Gamma )")            # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[9]>", line 1, in <module>
        print gap.eval("Vertices( Gamma )")            # optional gap package###line 153:
    sage: print gap.eval("Vertices( Gamma )")            # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Error, no 1st choice method found for `Vertices' on 1 arguments

       executing Vertices( Gamma );
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 163:
    sage: print gap.eval("Distance( Gamma, 1, 3 )")      # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[2]>", line 1, in <module>
        print gap.eval("Distance( Gamma, 1, 3 )")      # optional gap package###line 163:
    sage: print gap.eval("Distance( Gamma, 1, 3 )")      # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Error, usage: Distance( <Graph>, <Int> or <List>, <Int> or <List> [, <PermGrou\
    p> ] )

       executing Distance( Gamma, 1, 3 );
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/graph_theory.rst", line 173:
    sage: print gap.eval("Distance( Gamma, 1, 2 )")      # optional gap package
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[2]>", line 1, in <module>
        print gap.eval("Distance( Gamma, 1, 2 )")      # optional gap package###line 173:
    sage: print gap.eval("Distance( Gamma, 1, 2 )")      # optional gap package
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 975, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 722, in _eval_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Error, usage: Distance( <Graph>, <Int> or <List>, <Int> or <List> [, <PermGrou\
    p> ] )

       executing Distance( Gamma, 1, 2 );
**********************************************************************
3 items had failures:
   6 of  10 in __main__.example_5
   1 of   3 in __main__.example_6
   1 of   3 in __main__.example_7
***Test Failed*** 8 failures.
```

Issue created by migration from https://trac.sagemath.org/ticket/6328





---

archive/issue_comments_050420.json:
```json
{
    "body": "My feeling is that this entire section on using Grape is a waste of electrons because of Sage's massive improvments in this area of graph theory since this was first written. Unless I hear a complaint soon, I will delete the whole thing.",
    "created_at": "2009-06-16T23:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6328#issuecomment-50420",
    "user": "https://github.com/wdjoyner"
}
```

My feeling is that this entire section on using Grape is a waste of electrons because of Sage's massive improvments in this area of graph theory since this was first written. Unless I hear a complaint soon, I will delete the whole thing.



---

archive/issue_comments_050421.json:
```json
{
    "body": "Attachment [trac_6328.patch](tarball://root/attachments/some-uuid/ticket6328/trac_6328.patch) by @wdjoyner created at 2009-06-17 13:46:20\n\napplies to 4.0.2.rc1",
    "created_at": "2009-06-17T13:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6328#issuecomment-50421",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_6328.patch](tarball://root/attachments/some-uuid/ticket6328/trac_6328.patch) by @wdjoyner created at 2009-06-17 13:46:20

applies to 4.0.2.rc1



---

archive/issue_comments_050422.json:
```json
{
    "body": "Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild constructions html (resp., pdf) went fine and sage -t -long --optional devel/sage/doc/en/constructions/graph_theory.rst passes.",
    "created_at": "2009-06-17T13:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6328#issuecomment-50422",
    "user": "https://github.com/wdjoyner"
}
```

Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild constructions html (resp., pdf) went fine and sage -t -long --optional devel/sage/doc/en/constructions/graph_theory.rst passes.



---

archive/issue_comments_050423.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-09-08T23:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6328#issuecomment-50423",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_014867.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-09T11:14:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6328",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6328#event-14867"
}
```



---

archive/issue_comments_050424.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T11:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6328#issuecomment-50424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
