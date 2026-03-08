import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Load data
df = pd.read_csv("LipSync Assistant — User Research Survey.csv")

# Rename columns for easier use
df.columns = ['user_type', 'uses_captions', 'caption_helpfulness', 
              'uses_lipreading', 'animated_mouth_useful', 'best_platform', 'other_thoughts']

# Fix one response that said "Hearing impaired" to group cleanly
df['user_type'] = df['user_type'].replace('Hearing impaired', 'Hard of Hearing')

# Colors
colors = ['#e07070', '#7090d0', '#70c090', '#c070c0', '#d0a050']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('LipSync Assistant — User Research Findings\n{len(df)} Respondents', 
             fontsize=16, fontweight='bold', y=0.98)

# --- Chart 1: Who responded ---
ax1 = axes[0, 0]
user_counts = df['user_type'].value_counts()
wedges, texts, autotexts = ax1.pie(user_counts.values, labels=user_counts.index, 
                                    autopct='%1.0f%%', colors=colors,
                                    startangle=90, pctdistance=0.75)
for text in texts: text.set_fontsize(11)
for autotext in autotexts: autotext.set_fontsize(10), autotext.set_fontweight('bold')
ax1.set_title('Who Responded', fontsize=13, fontweight='bold', pad=15)

# --- Chart 2: Would animated mouth help? ---
ax2 = axes[0, 1]
mouth_counts = df['animated_mouth_useful'].value_counts()
bar_colors = {'Yes': '#70c090', 'Maybe': '#d0a050', 'No': '#e07070'}
bars = ax2.bar(mouth_counts.index, mouth_counts.values, 
               color=[bar_colors.get(x, '#aaaaaa') for x in mouth_counts.index],
               edgecolor='white', linewidth=1.5, width=0.5)
for bar, val in zip(bars, mouth_counts.values):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
             str(val), ha='center', fontweight='bold', fontsize=12)
ax2.set_title('Would Animated Mouth Help?', fontsize=13, fontweight='bold')
ax2.set_ylabel('Number of Respondents')
ax2.set_ylim(0, max(mouth_counts.values) + 1)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# --- Chart 3: Caption helpfulness ratings ---
ax3 = axes[1, 0]
rating_counts = df['caption_helpfulness'].value_counts().sort_index()
bars3 = ax3.bar(rating_counts.index.astype(str), rating_counts.values,
                color='#7090d0', edgecolor='white', linewidth=1.5, width=0.5)
for bar, val in zip(bars3, rating_counts.values):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
             str(val), ha='center', fontweight='bold', fontsize=12)
ax3.set_title('Caption Helpfulness Rating (1–5)', fontsize=13, fontweight='bold')
ax3.set_xlabel('Rating')
ax3.set_ylabel('Number of Respondents')
ax3.set_ylim(0, max(rating_counts.values) + 1)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# --- Chart 4: Best platform ---
ax4 = axes[1, 1]
# Expand multi-answer responses
platforms = []
for val in df['best_platform'].dropna():
    if 'All of the above' in str(val):
        platforms.extend(['YouTube', 'Zoom', 'TV Streaming', 'In-person learning'])
    else:
        platforms.append(val.strip())

platform_counts = pd.Series(platforms).value_counts()
bars4 = ax4.barh(platform_counts.index, platform_counts.values,
                 color='#c070c0', edgecolor='white', linewidth=1.5)
for bar, val in zip(bars4, platform_counts.values):
    ax4.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
             str(val), va='center', fontweight='bold', fontsize=12)
ax4.set_title('Most Useful Platform', fontsize=13, fontweight='bold')
ax4.set_xlabel('Number of Respondents')
ax4.set_xlim(0, max(platform_counts.values) + 1)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('survey_analysis.png', dpi=150, bbox_inches='tight')
print("Charts saved!")

# Print key findings
total = len(df)
yes_maybe = df['animated_mouth_useful'].isin(['Yes', 'Maybe']).sum()
print(f"\nKEY FINDINGS ({total} respondents):")
print(f"- {yes_maybe}/{total} said animated mouth would be useful or potentially useful")
print(f"- {df['uses_captions'].eq('Always').sum()}/{total} always use closed captions")
print(f"- Average caption helpfulness rating: {df['caption_helpfulness'].mean():.1f}/5")
print(f"- {df['uses_lipreading'].isin(['Yes','Sometimes']).sum()}/{total} use lipreading or visual cues")