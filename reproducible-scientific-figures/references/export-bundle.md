# Export Bundle

Use a bundle so the figure can be regenerated, inspected, refined, and submitted without losing provenance.

## Recommended Bundle

```text
figure_id/
  data/
    figure_ready_data.csv
    data_dictionary.md
  scripts/
    make_figure.R or make_figure.py
  outputs/
    figure.svg
    figure.pdf
    figure_preview.png
  provenance/
    figure_spec.yaml or figure_spec.json
    validation_report.md
```

## Output Roles

- `figure.svg`: preferred editable code-generated master.
- `figure.pdf`: vector derivative for review, LaTeX, or journal workflows when useful.
- `figure_preview.png`: preview only. Do not treat as the authority figure.
- `figure.tif` or `figure.tiff`: final raster export only when required by the target workflow.
- `manual_layout_project`: Illustrator, Inkscape, PowerPoint, or equivalent downstream edit file.

## Naming

- Include figure id and version when multiple versions coexist.
- Use `_preview` for preview derivatives.
- Use `_submission` only for files prepared for a specific submission target.
- Avoid overwriting previous final exports unless the user explicitly approved replacement or the script writes to a clearly versioned output.

## Manual Layout

When a manual layout step is needed, preserve the code-generated SVG/PDF. The manual layout project and final export are downstream artifacts. Record any manual edits that affect scientific interpretation, labels, panel order, scale, or annotations.
