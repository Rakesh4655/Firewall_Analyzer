import csv
import matplotlib.pyplot as plt
from collections import Counter

def visualize_rules(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        actions = [row['action'] for row in reader]

    counts = Counter(actions)
    labels = counts.keys()
    sizes = counts.values()

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Firewall Rule Actions (Allow vs Deny)')
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    visualize_rules('firewall_rules.csv')
