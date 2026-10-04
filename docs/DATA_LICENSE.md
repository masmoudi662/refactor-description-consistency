# Dataset License

The dataset in this repository (the `data/` folder and the annotations in
`annotations/`) is released under the
[Creative Commons Attribution 4.0 International license (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Full legal text: https://creativecommons.org/licenses/by/4.0/legalcode

You are free to share and adapt the dataset for any purpose, including
commercially, as long as you give appropriate credit, link to the license, and
indicate if you made changes.

The code in this repository (for example the Potato configuration) is covered
by the MIT license in the `LICENSE` file, not by this license.

## Source and attribution

The pull requests come from the AIDev dataset (Hugging Face: `hao-li/AIDev`),
released for the MSR 2026 Mining Challenge under CC BY 4.0. AIDev contains
public GitHub pull requests authored by autonomous coding agents. If you use
this dataset, please also credit AIDev.

## Changes made to the source data

- Selected pull requests whose title contains a word starting with "refactor".
- Added a `refactoring_type` tag (extract_method, move_method, extract_class,
  extract_field, move_field) using keyword patterns on the title and description.
- Drew a stratified random sample of 200 pull requests (40 per type, seed 42).
- Added a `consistency_label` and `notes` column, filled in by human annotators.

## Credit for the annotations

Annotation setup and labels: Aymen Masmoudi, Belhassen Khefacha, Bivek Dhruv,
and Raafat Saeed, University of Michigan-Flint (ARI 410/510, Fall 2026),
together with the classmates who annotated.

## Suggested citation

> ARI 410/510 team (Masmoudi, Khefacha, Dhruv, Saeed). "Refactoring PR
> Description-Code Consistency Dataset", 2026. Built on AIDev (hao-li/AIDev),
> CC BY 4.0. Licensed under CC BY 4.0.
