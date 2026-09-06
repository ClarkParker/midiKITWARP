"""Invariants a JSON Schema cannot express.

The schema checks the shape of each file. This checks the things that only make sense
across files and across releases: referential integrity, identifier stability, the licence
rule, and whether the fallback graph actually terminates.

Named after the check w3c/smufl runs for the same reason — its own docstring says
"checks that a JSON Schema alone can't express".
"""
