import numpy as np
scores = np.random.randint(50, 101, size=(5, 3))
subject_mean = scores.mean(axis=0)
centered_scores = scores - subject_mean
print("Original Scores:\n", scores)
print("\nSubject-wise Mean:\n", subject_mean)
print("\nCentered Scores (After Broadcasting):\n", centered_scores)