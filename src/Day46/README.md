# 📊 Validation Criteria

## ▸ Can you explain variance as information?

Yes. Variance represents the amount of information or spread in the dataset.  
Higher variance means the data points are more spread out and contain more useful information, while lower variance indicates less variability and less informative features.

---

## ▸ Did you standardize your data before applying PCA?

Yes. The data was standardized before applying PCA to ensure that all features contribute equally.  
Since PCA is sensitive to scale, standardization (mean = 0, variance = 1) prevents features with larger values from dominating the results.

---

## ▸ Have you plotted the cumulative explained variance?

Yes. A cumulative explained variance plot was used to understand how much total variance is retained as the number of principal components increases.  
This helps in determining the optimal number of components required.

---

## ▸ Did you justify your choice of n_components?

Yes. The value of `n_components` was selected based on the cumulative explained variance, typically choosing the number of components that retain around 90–95% of the total variance.

---

## ▸ Have you visualized the reduced data in a 2D plot?

Yes. The reduced data was visualized using a 2D scatter plot after applying PCA.  
This helps in understanding cluster separation and improves interpretability of the results.