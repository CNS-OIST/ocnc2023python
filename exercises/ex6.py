# Time-dependent plots

def plotTimeDepData(data, col_names, idx):
    plt.figure(figsize=(8, 5))
    # Display shaded zones for day-night cycle
    day, hours = data[:, 2:4].T
    for i, h in enumerate(hours):
        if h > 19 or h < 7:
            plt.axvspan(i, i+1, color=[0.95, 0.95, 1])
        else:
            plt.axvspan(i, i+1, color=[1, 1, 0.9])
    plt.plot(data[:, idx])
    plt.xlabel('Time [hours]')
    plt.ylabel(col_names[idx])

for idx in range(4, data.shape[1]):
    plotTimeDepData(data, col_names, idx)

# Discard time-related data
col_names2 = col_names[4:]
data2 = data[:,4:]

# Plot all pairs of variable as scatter plots
n = data2.shape[1]
fig, axes = plt.subplots(n, n, figsize=(12, 12), sharex='col', sharey='row')
# For each row
for i in range(n):
    # For each column
    for j in range(n):
        axes[i,j].scatter(data2[:,j], data2[:,i], marker='+')
        # Only add an xlabel for the last row
        if i == n - 1:
            axes[i,j].set_xlabel(col_names2[j])
        # Only add a ylabel for the first column
        if j == 0:
            axes[i,j].set_ylabel(col_names2[i])


# Realtive humidity as a function of temperature
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 4], data[:, 8])
plt.xlabel(col_names[4])
plt.ylabel(col_names[8])
