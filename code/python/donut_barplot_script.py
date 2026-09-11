
"""Final_Donut_BarPlot_Script_SiM
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- 1. Generate Sample Data ---
# We'll create a DataFrame where each row is a 'sample'
# and columns represent the 'subdivisions'.
# The values will represent the quantity or proportion of each subdivision within the sample.

#Subdivision1 = Homo CTO, Subdivision2 = Hetero CTO, Subdivision3 = Homo Cl, Subdivision4 = Hetero Cl, Subdivision5 =. Singles
data = {
    'Subdivision_1': [],
    'Subdivision_2': [],
    'Subdivision_3': [],
    'Subdivision_4': [],
    'Subdivision_5': []

}
num_samples = len(data['Subdivision_1'])
df = pd.DataFrame(data, index=[f'Sample {i+1}' for i in range(num_samples)])

# Ensure values sum to 100% for each sample if representing proportions
# If raw counts, skip this normalization step.
# For this example, we'll assume they are proportions that sum to 100 for visual clarity.
df_normalized = df.div(df.sum(axis=1), axis=0) * 100
df_normalized.dropna(inplace=True)

print("Generated Data (Percentages):")
print(df_normalized)
print("\n")

# --- 2. Prepare Data for Polar Plotting ---
# Number of samples (bars)
N = len(df_normalized)

# The angular range for 315 degrees (7*pi/4 radians)
plot_angle_range = 7 * np.pi / 4

# The width of each bar (angle in radians)
# We subtract a small gap to create visual separation between samples
# Distribute the bars evenly within the plot_angle_range
bar_width = (plot_angle_range / N) * 0.8 # 80% of the angular space per sample
angles = np.linspace(0, plot_angle_range, N, endpoint=False) + bar_width / 2

# Create the figure and a polar axes
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})

# Set the background color for the plot area if desired
# ax.set_facecolor('#f0f0f0')

# --- 3. Plotting the Stacked Bars ---

# Define the inner radius for the donut effect (e.g., 20% of the total radius)
# This value will be the new 'bottom' for the bars, creating the central white space.
inner_radius = 20

# Plot the first subdivision
bars1 = ax.bar(angles, df_normalized['Subdivision_1'], width=bar_width,
               bottom=inner_radius, # Bars now start from this inner radius
               color='#ff0000', edgecolor='white', linewidth=1.5)

#Plot the second subdivision on top of the first
bars2 = ax.bar(angles, df_normalized['Subdivision_2'], width=bar_width,
               bottom=df_normalized['Subdivision_1'] + inner_radius, # Add inner_radius to bottom
               color='#8B008B', edgecolor='white', linewidth=1.5)

# Plot the third subdivision on top of the second
bars3 = ax.bar(angles, df_normalized['Subdivision_3'], width=bar_width,
               bottom=df_normalized['Subdivision_1']+ df_normalized['Subdivision_2']+ inner_radius, # Add inner_radius to bottom
               color='#ff7b7b', edgecolor='white', linewidth=1.5)

#Plot the forth subdivision on top of the second
bars4 = ax.bar(angles, df_normalized['Subdivision_4'], width=bar_width,
               bottom=df_normalized['Subdivision_1'] + df_normalized['Subdivision_2'] + df_normalized['Subdivision_3'] + inner_radius, # Add inner_radius to bottom
               color='#ff69b4', edgecolor='white', linewidth=1.5)

# Plot the fifth subdivision on top of the second
bars5 = ax.bar(angles, df_normalized['Subdivision_5'], width=bar_width,
               bottom=df_normalized['Subdivision_1'] + + df_normalized['Subdivision_2'] + df_normalized['Subdivision_3'] + df_normalized['Subdivision_4'] + inner_radius, # Add inner_radius to bottom
               color='#FFDAB9', edgecolor='white', linewidth=1.5)

# --- 4. Customize the Plot ---

# Set the limits for the radial (y) axis
# The lower limit is now 'inner_radius' to create the donut hole
ax.set_ylim(0, 100+inner_radius) # Adjust upper limit if needed for labels to fit outside 100%

# Set the angular limits to make it a 315 degree angle
ax.set_theta_zero_location("N") # Start from the top (0 degrees)
ax.set_theta_direction(-1)     # Go clockwise
#ax.set_thetamin(0)              # Minimum angle
#ax.set_thetamax(315)            # Maximum angle (315 degrees)

# Remove all default radial labels and ticks
ax.set_yticklabels([])
ax.set_yticks([])

# Explicitly turn off all grid lines (both radial spokes and concentric circles from default grid)
ax.grid(False)

# Re-add custom radial percentage lines (25%, 50%, 75%, 100%) and their labels
# These will appear as concentric arcs
radial_percentage_points = [25, 50, 75, 100]
for pct in radial_percentage_points:
    r = pct + inner_radius # Position of the arc
    # Plot the arc for each percentage line within the defined angular range
    ax.plot(np.linspace(0, plot_angle_range-0.25*bar_width, 100), np.full(100, r),
            color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    # Place text labels for percentages along the North (0 degree) axis for clarity
    #ax.text(0, r, f'{pct}%', ha='center', va='bottom', fontsize=10, color='gray')


# Set the angular (x) axis labels (Sample names)
#ax.set_xticks(angles)
ax.set_xticklabels(df_normalized.index, fontsize=0, color='dimgray')

# Remove the outermost circle (frame) and inner radial lines
ax.spines['polar'].set_visible(False) # This removes the outer circular border and the radial lines from the center.

# Make the plot look cleaner by removing radial ticks
ax.tick_params(axis='x', which='major', pad=15) # Adjust padding for labels

# Add a title
#plt.title("Donut-Shaped Composition of Samples by Subdivision (315 Degree Angle - With Percentage Lines)", va='bottom', fontsize=16, pad=30)

# Add a legend
#ax.legend(loc='lower left', bbox_to_anchor=(1.05, 0.8), fontsize=10, frameon=False)

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Save the plot as a PDF file
plt.savefig('donut_plot.pdf')

# Show the plot
plt.show()
