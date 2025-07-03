#Write a python program to count how many genes belong to each family using given data and visualise using pandas
import pandas as pd
import matplotlib.pyplot as plt

# --- Data ---
data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}

# --- Create DataFrame ---
df = pd.DataFrame(data)

# --- Count genes per family ---
family_counts = df["Family"].value_counts().sort_values(ascending=False)

# --- Display the counts ---
print("Gene count per family:\n")
print(family_counts)

# --- Plot using pandas' built-in visualization ---
family_counts.plot(kind='bar', color='skyblue', edgecolor='black', figsize=(8, 6))

# --- Beautify the plot ---
plt.title("Number of Genes per Family", fontsize=14, fontweight='bold')
plt.xlabel("Gene Family", fontsize=12)
plt.ylabel("Number of Genes", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# --- Show the plot ---
plt.show()
