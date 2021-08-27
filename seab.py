import seaborn as sns
import matplotlib.pyplot as plt
tip_data = sns.load_dataset('tips')
#sns.scatterplot(x="tip", y="total_bill", data=tip_data, hue='size', size='size', sizes=(70, 280), style='size', palette='Set3', color=".5", marker="*")
#sns.lineplot(x="tip", y="total_bill", data=tip_data, hue="size", markers=True, dashes=False)
#sns.catplot(x='tip', y='total_bill', data=tip_data, row='size', kind='smoker')
#sns.barplot(x='tip', y='total_bill', data=tip_data, hue='size', ci=68)
sns.countplot(x='tip', data=tip_data, saturation=1.4, palette='Set3',linewidth=5, edgecolor=sns.color_palette("dark", 3))
plt.show()
