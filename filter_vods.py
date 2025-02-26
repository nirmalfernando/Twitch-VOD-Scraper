import pandas as pd

# Load the Excel file
df = pd.read_excel('twitch_vods.xlsx')

# Convert 'Duration' to total seconds
def duration_to_seconds(duration):
    h, m, s = 0, 0, 0
    parts = duration.split('h')
    if len(parts) == 2:
        h = int(parts[0])
        parts = parts[1]
    else:
        parts = parts[0]

    if 'm' in parts:
        m, parts = parts.split('m')
        m = int(m)
    if 's' in parts:
        s = int(parts.split('s')[0])

    return h * 3600 + m * 60 + s

df['Duration_Seconds'] = df['Duration'].apply(duration_to_seconds)

# Filter videos under 11h59m58s (43198 seconds)
filtered_vods = df[df['Duration_Seconds'] < 43198]

# Save filtered results
filtered_vods.to_excel('filtered_twitch_vods.xlsx', index=False)
print(f"Filtered videos count: {len(filtered_vods)}")
print('Filtered VODs saved to filtered_twitch_vods.xlsx!')