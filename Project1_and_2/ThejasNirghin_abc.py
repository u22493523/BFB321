#This module looks at the quantities different inventory items and determines a weighted importance for each item, ranking them into A, B, and C catergories from highest to lowest contribution.
#5.1 The tier split changed much because I created an 'A' item and a 'C' item, it replaced the top and bottom items due the extremely high and low items that I created.
#5.2 The tier count for 'A' remained the same, whereas 'B' decreased by 1 and 'C' increased by one.

skus = [
{"sku": "BRK-100", "demand": 2000, "cost": 45},
{"sku": "GSK-220", "demand": 1500, "cost": 30},
{"sku": "BLT-010", "demand": 10000, "cost": 2},
{"sku": "BRG-330", "demand": 800, "cost": 60},
{"sku": "SEAL-500","demand": 3000, "cost": 5},
{"sku": "MTR-700", "demand": 50, "cost": 800},
{"sku": "WSH-050", "demand": 20000, "cost": 0.5},
{"sku": "CBL-900", "demand": 400, "cost": 25},
]

def usage_value(demand, cost):
    return demand * cost
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

total_value = sum(item["value"] for item in skus_sorted)

running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"])

tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)

skus = [
{"sku": "BRK-100", "demand": 2000, "cost": 45},
{"sku": "GSK-220", "demand": 1500, "cost": 30},
{"sku": "BLT-010", "demand": 10000, "cost": 2},
{"sku": "BRG-330", "demand": 800, "cost": 60},
{"sku": "SEAL-500","demand": 3000, "cost": 5},
{"sku": "MTR-700", "demand": 50, "cost": 800},
{"sku": "WSH-050", "demand": 20000, "cost": 0.5},
{"sku": "CBL-900", "demand": 400, "cost": 25},
{"sku": "GOO-111", "demand": 600, "cost": 3},
{"sku": "TOY-222", "demand": 7000, "cost": 25},
]

def usage_value(demand, cost):
    return demand * cost
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

total_value = sum(item["value"] for item in skus_sorted)

running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"])

tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)

skus = [
{"sku": "BRK-100", "demand": 2000, "cost": 45},
{"sku": "GSK-220", "demand": 1500, "cost": 30},
{"sku": "BLT-010", "demand": 10000, "cost": 2},
{"sku": "BRG-330", "demand": 800, "cost": 60},
{"sku": "SEAL-500","demand": 3000, "cost": 5},
{"sku": "MTR-700", "demand": 50, "cost": 800},
{"sku": "WSH-050", "demand": 20000, "cost": 0.5},
{"sku": "CBL-900", "demand": 400, "cost": 25},
]

def usage_value(demand, cost):
    return demand * cost
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

total_value = sum(item["value"] for item in skus_sorted)

running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

def assign_tier(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"
for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"])

tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)

def usage_value(demand, cost):
    return demand * cost

def classify_inventory(skus_list):
    for item in skus_list:
        item["value"] = usage_value(item["demand"], item["cost"])
        
    # Step 3: Sort descending by value
    skus_sorted = sorted(skus_list, key=lambda item: item["value"], reverse=True)
    
    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100
        
    def assign_tier(cum_pct):
        if cum_pct <= 80:
            return "A"
        elif cum_pct <= 95:
            return "B"
        else:
            return "C"
            
    for item in skus_sorted:
        item["tier"] = assign_tier(item["cum_pct"])

        skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500","demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
]

classified_list = classify_inventory(skus)


tier_counts = {"A": 0, "B": 0, "C": 0}

print("--- Inventory Classification Report ---")
for item in classified_list:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])
    tier_counts[item["tier"]] += 1

print("\nTier Counts:", tier_counts)