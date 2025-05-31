import csv

def analyze_firewall_rules(csv_file):
    risky_ports = ['22', '3389']
    risky_rules = []
    duplicate_rules = set()
    seen_rules = set()

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rule = (row['source_ip'], row['destination_ip'], row['port'], row['protocol'], row['action'])
            if rule in seen_rules:
                duplicate_rules.add(rule)
            else:
                seen_rules.add(rule)

            if row['source_ip'] == '0.0.0.0/0' and row['port'] in risky_ports and row['action'] == 'ALLOW':
                risky_rules.append(rule)

    print("🔥 Risky Rules (open to all):")
    for rule in risky_rules:
        print("  ", rule)

    print("\n🔁 Duplicate Rules:")
    for rule in duplicate_rules:
        print("  ", rule)

if __name__ == '__main__':
    analyze_firewall_rules('firewall_rules.csv')
