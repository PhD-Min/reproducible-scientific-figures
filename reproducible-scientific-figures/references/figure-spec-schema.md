# Figure Spec Schema

A figure spec defines what the figure should show. The skill defines how to make the figure reproducibly.

## Minimal Fields

Use these fields for a small task:

```yaml
figure_id: Fig_1
purpose: Short statement of the scientific message.
input_data:
  - path/to/source_or_processed_data.csv
figure_ready_data: outputs/Fig_1/figure_ready_data.csv
plot_code: scripts/make_fig_1.R
plot_type: line_plot
x_axis:
  field: year
  label: Year
  unit: calendar_year
y_axis:
  field: response
  label: Response
  unit: index
grouping:
  field: treatment
  label: Treatment
outputs:
  svg: outputs/Fig_1/Fig_1.svg
  preview_png: outputs/Fig_1/Fig_1_preview.png
validation:
  check_file_presence: true
  check_axis_labels: true
  check_representative_values: true
```

## Extended Fields

Use extended fields when the figure is manuscript-critical or multi-panel:

- `research_claim`: the sentence or result the figure supports.
- `source_data`: authority raw inputs and processing scripts.
- `data_dictionary`: units and definitions for fields used in the figure.
- `filters`: inclusion/exclusion rules, time windows, regions, treatments, or cohorts.
- `statistics`: model/test/CI/SE settings and output files.
- `panels`: panel ids, panel-specific data, plot types, labels, and intended message.
- `style`: dimensions, font family, color palette, line weights, marker shapes, legend position, panel layout.
- `exports`: SVG/PDF/PNG/TIFF/EPS/DOCX/PPTX expectations and target use.
- `manual_layout`: allowed downstream layout tool and what may be edited manually.
- `manuscript_links`: caption, text claim, supplement, response letter, or submission package path.
- `validation`: required checks and known residual risks.

## Design Boundary

Do not hard-code one visual style into the skill. Put project-specific aesthetics, journal dimensions, fonts, palettes, panel geometry, and narrative design in the spec or project style guide.
