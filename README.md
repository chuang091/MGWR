# MGWR Reproduction Attempt

## File Structure

- [`Main4.shp`](./Main4.shp): Taipei City shapefile (~7000 records)
- [`Main5.shp`](./Main5.shp): Taipei City Experimental Area (~100 records)
- [`Report.md`](./Report.md): MGWR report generation
- [`MGWR.py`](./MGWR.py): Main script for MGWR analysis
- [`exist.py`](./exist.py): Arcpy testing script
- **[`validation.ipynb`](./validation.ipynb)**: Validation notebook for results checking and model comparison (Highlighted Work)

## Report

### Coefficient Estimation Summary:
| Explanatory Variable (Standardized) | Mean   | Std Dev | Min     | Median  | Max     |
|-------------------------------------|--------|---------|---------|---------|---------|
| Intercept (Scaled)                  | -0.0050 | 0.3149  | -1.1777 | -0.0022 | 1.9704  |
| busC (Scaled)                       | -0.1539 | 0.2081  | -3.3429 | -0.1644 | 1.7352  |
| metroC (Scaled)                     | 0.1211  | 0.0003  | 0.1205  | 0.1211  | 0.1215  |
| bikeC (Scaled)                      | 0.2322  | 0.0005  | 0.2311  | 0.2321  | 0.2330  |
| roadC (Scaled)                      | 0.4421  | 0.1092  | -0.1106 | 0.4526  | 1.5665  |
| popDenC (Scaled)                    | 0.1678  | 0.0068  | 0.1605  | 0.1650  | 0.1800  |

---

### Model Diagnostics:
- **R-Squared**: 0.8991
- **Adjusted R-Squared**: 0.8800
- **AICc**: 6541.2567
- **Sigma-Squared**: 0.1200
- **Sigma-Squared MLE**: 0.1009
- **Effective Degrees of Freedom**: 5955.0022

---

### Explanatory Variables and Neighborhood Summary:
| Explanatory Variable (Standardized) | Neighbors (% of Features) | Significance (% of Features) |
|-------------------------------------|----------------------------|-----------------------------|
| Intercept (Scaled)                  | 30 (0.42%)                 | 1084 (15.31%)               |
| busC (Scaled)                       | 30 (0.42%)                 | 2890 (40.81%)               |
| metroC (Scaled)                     | 7082 (100%)                | 7082 (100%)                 |
| bikeC (Scaled)                      | 7082 (100%)                | 7082 (100%)                 |
| roadC (Scaled)                      | 30 (0.42%)                 | 6369 (89.93%)               |
| popDenC (Scaled)                    | 5417 (76.49%)              | 7082 (100%)                 |

---

### Optimal Bandwidth Search History:
| Iteration | Intercept (Scaled) | busC (Scaled) | metroC (Scaled) | bikeC (Scaled) | roadC (Scaled) | popDenC (Scaled) | AICc         |
|-----------|--------------------|---------------|-----------------|----------------|----------------|------------------|--------------|
| 1         | 30                 | 30            | 7082            | 7082           | 4388           | 7082             | 7169.7451    |
| 2         | 30                 | 30            | 7082            | 7082           | 30             | 5417             | 6541.2567    |

---

### Bandwidth Summary:
| Explanatory Variable (Standardized) | Optimal Number of Neighbors | Effective Number of Parameters | Adjusted Alpha Value | Adjusted Pseudo-t Critical Value |
|-------------------------------------|-----------------------------|-------------------------------|----------------------|----------------------------------|
| Intercept (Scaled)                  | 30                          | 569.60                        | 0.0001               | 3.9248                           |
| busC (Scaled)                       | 30                          | 325.23                        | 0.0002               | 3.7874                           |
| metroC (Scaled)                     | 7082                        | 1.01                          | 0.0493               | 1.9667                           |
| bikeC (Scaled)                      | 7082                        | 1.04                          | 0.0482               | 1.9757                           |
| roadC (Scaled)                      | 30                          | 229.03                        | 0.0002               | 3.6991                           |
| popDenC (Scaled)                    | 5417                        | 1.08                          | 0.0461               | 1.9948                           |

---

## Known Bugs

- Saving the Feature Class may fail due to unknown reasons.

# Validation Method Review

![Validation Method](./Val.jpg)

- **[`validation.ipynb`](./validation.ipynb)**: This Jupyter notebook contains the validation process and comparison of model results, allowing us to check the accuracy and robustness of the MGWR reproduction.
