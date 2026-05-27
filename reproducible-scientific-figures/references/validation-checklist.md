# Validation Checklist

Use this checklist before claiming a scientific figure is complete.

## Data Checks

- Source data and figure-ready data paths are known.
- Filtering, grouping, aggregation, and unit conversion are documented.
- Row counts, group counts, panel counts, and missing-value handling are plausible.
- Statistical outputs used in the figure can be traced to code or documented calculations.

## Visual Mapping Checks

- Axis labels and units match the figure-ready data.
- Legend labels match group values.
- Panel labels and order match the figure spec.
- Representative plotted values match the table or statistical output.
- Axis limits and transformations are intentional and documented.
- Error bars, confidence intervals, or significance markers match their source.

## File Checks

- Plotting code exists and can be rerun in the chosen environment.
- SVG or editable vector output exists.
- Preview derivative is labeled as preview.
- Final export role is clear when TIFF/PDF/EPS is produced.
- Manual layout files are downstream derivatives, not replacements for source data or plotting code.

## Report Template

```text
Validation result: pass / partial / fail
Figure id:
Spec path:
Figure-ready data:
Plot code:
Primary SVG:
Preview/final exports:
Checks performed:
Representative value checks:
Open gaps:
Residual risk:
```
