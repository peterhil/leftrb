# Leftrb/LLRB

Leftrb is a Left-Leaning Red-Black (LLRB) implementation of 2–3 balanced binary
search trees in Python.

This is a straightforward port of the Java code presented by Robert Sedgewick in
[his paper]((http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf)) and in the
book [Algorithms, 4th Edition](http://algs4.cs.princeton.edu/home/), which is written
by Robert Sedgewick and Kevin Wayne. By their permission, the [original GPL v3 licensed Java
code](http://www.cs.princeton.edu/~rs/talks/LLRB/Java/RedBlackBST.java)
is licensed as LGPL v3, and ported to Python.

## Overview

A balanced binary search tree (BBST) maintains elements in sorted order under dynamic 
updates (inserts and deletes) and can support various order-specific queries.

Red-black trees are the de facto standard BBST algorithms, and are the underlying
data structure for symbol-table implementations within C++, Java, Python, BSD Unix,
Linux and many other modern systems.

All red–black trees are based on implementing 2-3 or 2-3-4 trees within a binary tree,
using  red links to bind together internal nodes into 3-nodes or 4-nodes. Search, insert
and delete operations are O(log n) and space requirements are O(n).

However, many traditional implementations have lots of repetitive code on the symmetric
branches of rotation and deletion operations. So they are not easy to reason about and 
augment with other properties, which is what BBST's are often used for: They are used
to implement other common data structures like Priority Queues and Interval Trees.

The LLRB method of implementing 2-3 trees is a recent improvement over the traditional
implementation — it maintains an additional invariant that all red links must lean left
except during inserts and deletes. Because of this, they can be implemented by adding
just a few lines of code to standard BST algorithms.

The LLRB tree is based on combining three ideas:

- Use a recursive implementation.
- Require that all 3-nodes lean left.
- Perform rotations on the way up the tree (after the recursive calls).

The LLRB approach was discovered relatively recently (in 2008) by Robert Sedgewick
of Princeton University. For original code and more information read the paper *"Left-leaning Red-Black Trees"* at [http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf](http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf)

## Installation

From Python package index:  

    pip install leftrb

or from Github source:  

    git clone https://github.com/peterhil/leftb.git
    cd leftrb 
    python setyp.py install

## About

Leftrb/LLRB was written by [Peter Hillerström](http://composed.nu/peterhil/).  
Follow me on Twitter [@peterhil](http://www.twitter.com/peterhil)!
