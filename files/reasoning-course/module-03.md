# Module 3: Use the literature

**Deliverable:** A source record and an applicability audit.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/knowledge-retrieval/

## Segment 3.1 · Slide 8: A relevant theorem can still be inapplicable

### Spoken script

Finding a relevant theorem is only the beginning of a theorem application. Return to our maximum example. The source theorem is useful and correct, but its compactness hypothesis is not satisfied by the proposed domain. More retrieval results will not repair that mismatch. The research system must distinguish evidence about what a source says from evidence that its hypotheses hold here. Otherwise a strong retrieval engine can produce a confidently cited invalid argument.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 3.2 · Slide 9: An applicability record

### Spoken script

For each proposed application, preserve the source version and theorem location. Identify which object in our problem plays each role in the theorem. Then write a row for each hypothesis and attach its justification. A missing row is an open obligation, not an invitation to infer that the author probably intended it. Finally, write the conclusion after substituting our objects. This last step catches applications that prove something nearby but not the target. For an advanced class, repeat the exercise with a vanishing theorem and check the geometric category and positivity assumptions carefully.

**Pause question:** What evidence is still missing after we verify that the quotation is accurate?

**Expected discussion:** We still need the object mapping, justification of every hypothesis in the current setting, and confirmation that the instantiated conclusion supports the target.

## Segment 3.3 · Slide 10: Workshop: a useful rejected match

### Spoken script

Open a textbook or paper you already have permission to use. Locate an exact theorem rather than relying on a model's paraphrase. We will prepare one successful application and one near-match that fails a hypothesis. Keeping the rejected match prevents the next search round from repeating the same error. It also documents a possible research direction: perhaps the missing hypothesis can be proved, or perhaps a different theorem is needed. Neither possibility should be recorded as a completed application until the mathematical bridge is supplied.

## Live demonstration

Open a selected source theorem and record its edition or revision and theorem number. Fill a two-column table: source hypothesis and evidence in this problem. Use the compact-domain example as the first rejected application. This is a manual evidence exercise; the Python lab does not implement retrieval.

## Student assignment

Submit a source record, one justified application, and one rejected near-match. Record the search budget and the unresolved hypothesis without inventing a citation.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.
