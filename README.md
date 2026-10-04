# refactor-description-consistency
A human-annotated dataset of 200 refactoring PRs (Extract Method, Extract Class, Move Method/Field) checking whether the code changes match the PR title and description.

Section 2: Dataset Description
2.1 Source
All pull requests (PRs) come from AIDev, a public dataset of PRs authored by autonomous coding agents on GitHub (OpenAI Codex, GitHub Copilot, Cursor, Google Jules, Devin, Claude Code), released for the MSR 2026 Mining Challenge.
Hugging Face repository: hao-li/AIDev (license: CC-BY-4.0)
Table used: all_pull_request.parquet, which contains every agentic PR in the dataset (2,743,854 PRs in the version we used)
Revision: branch main, commit c63c8a57a2de34fc03fa83722412824af4d8753b
Data downloaded on Oct 1, 2026
2.2 Collection procedure
The selection was done in Python (pandas, pyarrow) in Google Colab, in three steps.
Step 1: Identify refactoring PRs. We loaded the id, agent and title columns of all_pull_request and kept every PR whose title contains a word starting with "refactor" (refactor, refactoring, refactored…), case-insensitive:
all_pr["title"].fillna("").str.contains(r"\brefactor", case=False, regex=True) 
Step 2: Load the description of these PRs. For the PRs kept in Step 1, we loaded id, agent, title, body and html_url.
Step 3: Tag the refactoring type. We concatenated the title and the description (body), lower-cased the text, and searched it for the following patterns. A verb and its object may be separated by up to 40 characters, which catches phrases like "extract validation logic into a helper function".
Category
Verb
Object words
extract_method
extract / extracted / extracts / extracting
method, function, helper
move_method
move / moved / moves / moving
method, function
extract_class
extract (any form)
class, classes, module, component, service, interface
extract_field
extract (any form)
field, attribute, property, constant, variable
move_field
move (any form)
field, attribute, property, constant, variable

The exact regular expressions are:

patterns = {
    "extract_method": r"\bextract(?:ed|s|ing)?\b[\w\s`'\"-]{0,40}\b(?:method|function|helper)s?\b",
    "move_method":    r"\bmov(?:e|ed|es|ing)\b[\w\s`'\"-]{0,40}\b(?:method|function)s?\b",
    "extract_class":  r"\bextract(?:ed|s|ing)?\b[\w\s`'\"-]{0,40}\b(?:class|classes|module|component|service|interface)\b",
    "extract_field":  r"\bextract(?:ed|s|ing)?\b[\w\s`'\"-]{0,40}\b(?:field|attribute|property|properties|constant|variable)s?\b",
    "move_field":     r"\bmov(?:e|ed|es|ing)\b[\w\s`'\"-]{0,40}\b(?:field|attribute|property|properties|constant|variable)s?\b",
}
PRs matching none of these patterns were excluded. Our study focuses on refactorings whose description makes a concrete, checkable claim about the operation performed.
Result of the selection:
Category
# PRs
extract_method
2,197
extract_class
909
move_method
423
extract_field
368
move_field
242






2.3 Sampling for annotation
To avoid ambiguity, we kept only PRs whose title and description match exactly one category; PRs matching several categories were excluded. We then drew a stratified random sample of 40 PRs per type (200 PRs total) and split it across the 4 team members (50 each, 10 per type) 
2.4 Data instance and columns
One row = one pull request.
Column
Type
Description
id
int
Unique PR identifier (from AIDev / GitHub API)
agent
string
Coding agent that authored the PR (Codex, Copilot, Cursor, Jules, Devin, Claude Code)
title
string
PR title
body
string
PR description (Markdown) written by the agent
html_url
string
Link to the PR on GitHub, used by annotators to inspect the code changes
refactoring_type
string
the single refactoring category the PR matched (extract_method, move_method, extract_class, extract_field or move_field) 
consistency_label
string
Annotation: consistent, inconsistent, unavailable or out_of_scope (see guidelines)
notes
string
Annotator's justification for the label, mainly for inconsistent and out of scope  PRs 

2.5 Missing data and known limitations
No code diffs in the source table. all_pull_request holds only PR metadata. Annotators inspect the code changes on GitHub through html_url.
Unavailable PRs. Some PRs were deleted, made private, or belong to repositories that no longer exist. These are labelled unavailable and excluded from the analysis.
Empty descriptions. Some PRs have an empty or null body. For these, the category tag comes from the title alone.
Keyword-based selection. Categories describe what the PR says it did, not what the code actually changed. This is intended, since comparing the two is the goal of the study. It also means some PRs may be mis-tagged (e.g. a description mentioning "move" for an unrelated reason). Such PRs are labelled out_of_scope during annotation.
2.6 Annotation effort
The internal annotation took about 1 to 2 hours for each 50 Pull Request. This covers reading the title and description, opening the PR on GitHub, checking each claim of the description against the code changes, and assigning a label.That is about 1.5-2.5 minutes per PR . PRs with large diffs or long descriptions take longer.


