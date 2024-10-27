import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)  # For reproducibility
ages = np.random.randint(0, 100, size=500)  # Ages between 0 and 99

plt.figure(figsize=(10, 6))
plt.hist(ages, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Age Distribution in a Hypothetical Population', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(range(0, 101, 5))  # Setting x-ticks from 0 to 100
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
