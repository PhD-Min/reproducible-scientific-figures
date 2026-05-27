---
name: reproducible-scientific-figures
description: Build reproducible scientific figure pipelines from raw or processed data to figure-ready tables, plotting code, editable SVG outputs, preview derivatives, and validation reports. Use when Codex is asked to create, revise, audit, or repair research figures; generate plots from CSV/XLSX/R/Python outputs; prepare data-to-SVG workflows; validate that plotted values match source data; or hand off figures for Illustrator, Inkscape, PowerPoint, Word, LaTeX, or submission packages.
---

# Reproducible Scientific Figures

Use this skill to make scientific figures reproducible artifacts, not one-off images. The default deliverable is a traceable bundle: figure-ready data, plotting code, editable SVG, optional preview/export derivatives, and validation notes.

## Core Rules

- Do not draw directly from unknown or undocumented data. First identify source data, transformations, units, grouping fields, and the intended figure claim.
- Separate figure design from the reusable workflow. The skill provides the pipeline and validation gates; a project or task-specific figure spec defines the exact plot type, panels, aesthetics, dimensions, and journal constraints.
- Prefer code-generated, editable SVG as the primary working figure unless the project requires another editable/vector master. PNG/JPEG are previews only unless explicitly defined as accepted submission derivatives.
- Preserve the chain from data to code to output. Do not replace a reproducible figure with manual-only edits unless the manual step is recorded as a downstream derivative.
- Validate before claiming the figure is complete. At minimum, check that the plotted data source, output files, units, panels, legends, and representative values match the figure spec.

## Workflow

1. Define or locate the figure spec.
   - Use an existing project spec when available.
   - If no spec exists, draft a minimal spec with figure purpose, input data, plot type, grouping, axes, units, panels, outputs, and validation checks.
   - For detailed fields, read `references/figure-spec-schema.md`.

2. Build figure-ready data.
   - Read source data and processing code before plotting when they exist.
   - Create a dedicated figure-ready table for each figure or panel group.
   - Keep raw data, processed data, and figure-ready data conceptually separate.
   - Record filtering, aggregation, statistics, confidence intervals, missing-value handling, and unit conversions.

3. Write or revise plotting code.
   - Use the project's language and plotting stack when clear: R/ggplot2, Python/matplotlib, Python/plotnine, or another local convention.
   - Keep styling reproducible in code where possible.
   - Use manual layout tools such as Illustrator, Inkscape, PowerPoint, or Affinity only as downstream refinement steps, not as substitutes for missing data or missing plotting code.

4. Export the figure bundle.
   - Required: figure-ready data, plotting code, editable SVG, and validation report.
   - Usually useful: PDF vector export and PNG preview.
   - Optional by target: TIFF, EPS, PPTX, DOCX insertion copy, or submission package export.
   - For export expectations, read `references/export-bundle.md`.

5. Validate and report.
   - Confirm all expected files exist.
   - Compare representative plotted values, axis ranges, labels, units, legend groups, and panel counts against the figure-ready data.
   - Confirm the SVG is the working master and preview derivatives are labeled as previews.
   - Run `scripts/validate_figure_bundle.py` when the bundle has a JSON or YAML spec.
   - For validation details, read `references/validation-checklist.md`.

## Risk Gates

- Low risk: list files, inspect specs, copy original files unchanged, generate preview derivatives, or run read-only validation.
- Medium risk: rename/move figure bundle files, revise plotting code, regenerate SVG from known data, or update validation reports.
- High risk: change statistical processing, change data filters, alter figure claims, replace a manuscript/submission figure, change DPI/color/profile, convert final formats, or overwrite existing figure masters.
- For high-risk work, state assumptions, keep outputs separate from authority files, and ask for confirmation before overwriting or changing scientific meaning.

## Resources

- `references/figure-pipeline.md`: end-to-end data-to-SVG pipeline and role definitions.
- `references/figure-spec-schema.md`: minimal and extended figure spec fields.
- `references/export-bundle.md`: recommended output bundle and derivative naming.
- `references/validation-checklist.md`: QA gates before reporting success.
- `scripts/validate_figure_bundle.py`: read-only spec and file-presence validator.
- `examples/basic-line-figure/`: minimal example bundle using synthetic data.
