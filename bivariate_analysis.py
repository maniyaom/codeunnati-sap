import json

df_numerical = [] # Add numerical columns here

df_categorical = [] # Add categorical columns here

datasetName = input('Dataset Name: ')


with open('test.ipynb', 'w') as f:
    cells = []

    for i in df_numerical[:3]:
        for j in df_categorical:
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"#### {i}, {j}"
                ]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Plot the barplot\n",
                    f"sns.barplot(x='{j}', y='{i}', data={datasetName}, color=graph_color)\n",
                    "ax = plt.gca()\n",
                    "ax.set_facecolor(bg_color)\n",
                    f"plt.title('{j} v/s {i}')\n",
                    "plt.grid()\n",
                    "plt.show()\n"
                ]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Plot the barplot\n",
                    f"sns.barplot(x='{j}', y='{i}', data={datasetName}, estimator=min, color=graph_color)\n",
                    "ax = plt.gca()\n",
                    "ax.set_facecolor(bg_color)\n",
                    f"plt.title('{j} v/s {i} (Min)')\n",
                    "plt.grid()\n",
                    "plt.show()\n"
                ]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Plot the barplot\n",
                    f"sns.barplot(x='{j}', y='{i}', data={datasetName}, estimator=max, color=graph_color)\n",
                    "ax = plt.gca()\n",
                    "ax.set_facecolor(bg_color)\n",
                    f"plt.title('{j} v/s {i} (Max)')\n",
                    "plt.grid()\n",
                    "plt.show()\n"
                ]
            })

    # Construct the final notebook JSON
    notebook_content = {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    # Write to file as valid JSON
    json.dump(notebook_content, f, indent=2)