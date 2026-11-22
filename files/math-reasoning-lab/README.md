# Mathematical reasoning workbench

Python 3.9+, standard library only.

Run `python ledger.py`, `python workbench.py`, then `python -m unittest -v test_workbench.py`.

The fixtures stipulate evidence; they do not compute cohomology or verify mathematics. The tutorial explains eight stages, expected outcomes, and production limitations. `workbench.py` allows cyclic candidate graphs but only grounded arguments enter its least-fixed-point closure. It stores one supporting route, not all minimal supports. Reviews bind to content digests; they are not authenticated signatures.

The snapshot implementation assumes one writer. It is not a database, proof checker, security boundary, or complete event-sourcing system.
