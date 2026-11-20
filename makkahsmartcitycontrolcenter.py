# ============================================================
# MAKKAH SMART CITY COMMAND CENTER v1.0
# Educational Python prototype - fictional sample data
# Reconstructed version: not the exact lost original file.
# ============================================================

# MODULE 1 - CITY CONFIGURATION
CITY_NAME = "MAKKAH"
COUNTRY = "SAUDI ARABIA"
PROJECT_VERSION = "1.0"
TOTAL_DISTRICT = 10
SYSTEM_STATUS = "ONLINE"

print("\n======================================")
print("     MAKKAH SMART CITY COMMAND CENTER")
print("======================================")
print("City:", CITY_NAME)
print("Country:", COUNTRY)
print("Project Version:", PROJECT_VERSION)
print("Configured Districts:", TOTAL_DISTRICT)
print("System Status:", SYSTEM_STATUS)

# MODULE 2 - DISTRICT MANAGEMENT SYSTEM
districts = {
    "Central Makkah": {
        "population": 15000,
        "infrastructure": "good",
        "development": 75
    },
    "Northern Makkah": {
        "population": 12000,
        "infrastructure": "moderate",
        "development": 60
    },
    "Southern Makkah": {
        "population": 12000,
        "infrastructure": "moderate",
        "development": 80
    },
    "Western Makkah": {
        "population": 10000,
        "infrastructure": "good",
        "development": 70
    }
}

# MODULE 3 - DISTRICT INFORMATION DISPLAY
print("\n===== MODULE 3: DISTRICT INFORMATION DISPLAY =====")
for district, details in districts.items():
    print("\nDistrict:", district)
    print("Population:", details["population"])
    print("Infrastructure:", details["infrastructure"])
    print("Development:", details["development"], "%")

# MODULE 4 - DISTRICT SEARCH SYSTEM
print("\n===== MODULE 4: DISTRICT SEARCH SYSTEM =====")
search_name = input("Enter district name to search: ")
district_found = False

for district, details in districts.items():
    if district.lower() == search_name.lower():
        district_found = True
        print("\nDistrict Found:", district)
        print("Population:", details["population"])
        print("Infrastructure:", details["infrastructure"])
        print("Development:", details["development"], "%")
        break

if district_found == False:
    print("District Not Found!")

# MODULE 5 - POPULATION ANALYSIS SYSTEM
print("\n===== MODULE 5: POPULATION ANALYSIS =====")
total_population = 0
highest_population = -1
lowest_population = float("inf")
highest_population_district = ""
lowest_population_district = ""

for district, details in districts.items():
    population = details["population"]
    total_population += population

    if population > highest_population:
        highest_population = population
        highest_population_district = district

    if population < lowest_population:
        lowest_population = population
        lowest_population_district = district

total_districts = len(districts)
average_population = total_population / total_districts

print("Total Sample Population:", total_population)
print("Total Sample Districts:", total_districts)
print("Average District Population:", round(average_population, 2))
print("Highest Population District:", highest_population_district, "-", highest_population)
print("Lowest Population District:", lowest_population_district, "-", lowest_population)

# MODULE 6 - INFRASTRUCTURE MANAGEMENT SYSTEM
print("\n===== MODULE 6: INFRASTRUCTURE MANAGEMENT =====")

print("\n--- PART 1: INFRASTRUCTURE STATUS DISPLAY ---")
for district, details in districts.items():
    print(district, ":", details["infrastructure"])

print("\n--- PART 2: INFRASTRUCTURE QUALITY ANALYSIS ---")
for district, details in districts.items():
    status = details["infrastructure"].lower()
    if status == "good":
        quality = "Good Quality"
    elif status == "moderate":
        quality = "Moderate Quality"
    else:
        quality = "Poor Quality"
    print(district, ":", quality)

print("\n--- PART 3: POOR INFRASTRUCTURE DETECTION ---")
poor_count = 0
for district, details in districts.items():
    if details["infrastructure"].lower() == "poor":
        print("Poor Infrastructure Found:", district)
        poor_count += 1
if poor_count == 0:
    print("No district currently marked as poor.")

print("\n--- PART 4: INFRASTRUCTURE STATUS UPDATE ---")
update_name = input("Enter district name for infrastructure update: ")
new_status = input("Enter new status (good/moderate/poor): ").lower()
district_found = False

for district in districts:
    if district.lower() == update_name.lower():
        district_found = True
        if new_status in ["good", "moderate", "poor"]:
            districts[district]["infrastructure"] = new_status
            print("Infrastructure Status Updated Successfully!")
        else:
            print("Invalid status!")
        break

if district_found == False:
    print("District Not Found!")

print("\n--- PART 5: DISTRICT-WISE INFRASTRUCTURE COMPARISON ---")
for district, details in districts.items():
    print(district, ":", details["infrastructure"])

print("\n--- PART 6: INFRASTRUCTURE SUMMARY REPORT ---")
good_count = 0
moderate_count = 0
poor_count = 0

for district, details in districts.items():
    status = details["infrastructure"].lower()
    if status == "good":
        good_count += 1
    elif status == "moderate":
        moderate_count += 1
    elif status == "poor":
        poor_count += 1

total_districts = len(districts)
print("Total Districts:", total_districts)
print("Good Infrastructure:", good_count)
print("Moderate Infrastructure:", moderate_count)
print("Poor Infrastructure:", poor_count)
print("Good Percentage:", round(good_count / total_districts * 100, 2), "%")
print("Moderate Percentage:", round(moderate_count / total_districts * 100, 2), "%")
print("Poor Percentage:", round(poor_count / total_districts * 100, 2), "%")
print("Infrastructure Report Generated!")

# MODULE 7 - DEVELOPMENT TRACKING SYSTEM
print("\n===== MODULE 7: DEVELOPMENT TRACKING =====")

print("\n--- PART 1: DEVELOPMENT PROGRESS DISPLAY ---")
for district, details in districts.items():
    print(district, ":", details["development"], "%")

print("\n--- PART 2: DEVELOPMENT LEVEL CLASSIFICATION ---")
for district, details in districts.items():
    development = details["development"]
    if development >= 80:
        level = "High"
    elif development >= 60:
        level = "Moderate"
    else:
        level = "Low"
    print(district, ":", level)

print("\n--- PART 3: DEVELOPMENT PROGRESS UPDATE ---")
update_name = input("Enter district name for development update: ")
district_found = False

for district in districts:
    if district.lower() == update_name.lower():
        district_found = True
        new_development = int(input("Enter new development percentage: "))
        if 0 <= new_development <= 100:
            districts[district]["development"] = new_development
            print("Development Updated Successfully!")
        else:
            print("Invalid percentage! Enter between 0 and 100.")
        break

if district_found == False:
    print("District Not Found!")

print("\n--- PART 4: HIGHEST & LOWEST DEVELOPMENT DETECTION ---")
highest_development = -1
lowest_development = 101
highest_district = ""
lowest_district = ""

for district, details in districts.items():
    development = details["development"]
    if development > highest_development:
        highest_development = development
        highest_district = district
    if development < lowest_development:
        lowest_development = development
        lowest_district = district

print("Highest Development:", highest_district, "-", highest_development, "%")
print("Lowest Development:", lowest_district, "-", lowest_development, "%")

print("\n--- PART 5: DEVELOPMENT SUMMARY REPORT ---")
high_count = 0
moderate_count = 0
low_count = 0
total_development = 0

for district, details in districts.items():
    development = details["development"]
    total_development += development
    if development >= 80:
        high_count += 1
    elif development >= 60:
        moderate_count += 1
    else:
        low_count += 1

total_districts = len(districts)
average_development = total_development / total_districts
print("Total Districts:", total_districts)
print("High Development Districts:", high_count)
print("Moderate Development Districts:", moderate_count)
print("Low Development Districts:", low_count)
print("Average Development:", round(average_development, 2), "%")
print("Development Report Generated!")

# MODULE 8 - BUDGET MANAGEMENT SYSTEM
print("\n===== MODULE 8: BUDGET MANAGEMENT SYSTEM =====")

print("\n--- PART 1: TOTAL BUDGET DISPLAY ---")
total_budget = 500000000  # Fictional sample budget, SAR
print("City:", CITY_NAME)
print("Total Infrastructure Budget: SAR", total_budget)

print("\n--- PART 2: DISTRICT-WISE BUDGET ALLOCATION ---")
district_budgets = {
    "Central Makkah": 150000000,
    "Northern Makkah": 120000000,
    "Southern Makkah": 110000000,
    "Western Makkah": 120000000
}
for district, amount in district_budgets.items():
    print(district, ": SAR", amount)

print("\n--- PART 3: BUDGET UTILIZATION TRACKING ---")
budget_used = {
    "Central Makkah": 90000000,
    "Northern Makkah": 75000000,
    "Southern Makkah": 60000000,
    "Western Makkah": 80000000
}
for district, amount in budget_used.items():
    print(district, "Used: SAR", amount)

print("\n--- PART 4: REMAINING BUDGET CALCULATION ---")
for district in district_budgets:
    allocated = district_budgets[district]
    used = budget_used[district]
    remaining = allocated - used
    print("\nDistrict:", district)
    print("Allocated Budget: SAR", allocated)
    print("Used Budget: SAR", used)
    print("Remaining Budget: SAR", remaining)

print("\n--- PART 5: BUDGET VALIDATION & UPDATE ---")
district_name = input("Enter district name for budget update: ")

if district_name in district_budgets:
    new_budget = int(input("Enter new budget: "))
    other_budgets = sum(district_budgets.values()) - district_budgets[district_name]

    if new_budget >= 0 and other_budgets + new_budget <= total_budget:
        district_budgets[district_name] = new_budget
        print("Budget Updated Successfully!")
    else:
        print("Invalid Budget! Check the total city budget.")
else:
    print("District Not Found!")

# MODULE 9 - RESOURCE MANAGEMENT SYSTEM
print("\n===== MODULE 9: RESOURCE MANAGEMENT SYSTEM =====")

print("\n--- PART 1: RESOURCE DATA DISPLAY ---")
district_resources = {
    "Central Makkah": {
        "water": 85,
        "electricity": 90,
        "medical_supplies": 75
    },
    "Northern Makkah": {
        "water": 70,
        "electricity": 80,
        "medical_supplies": 65
    },
    "Southern Makkah": {
        "water": 75,
        "electricity": 85,
        "medical_supplies": 80
    },
    "Western Makkah": {
        "water": 80,
        "electricity": 75,
        "medical_supplies": 70
    }
}
print("Resource data loaded for", len(district_resources), "sample districts.")

print("\n--- PART 2: RESOURCE AVAILABILITY TRACKING ---")
for district, resources in district_resources.items():
    print("\nDistrict:", district)
    print("Water Availability:", resources["water"], "%")
    print("Electricity Availability:", resources["electricity"], "%")
    print("Medical Supplies:", resources["medical_supplies"], "%")

print("\n--- PART 3: RESOURCE ALLOCATION & UPDATE ---")
district_name = input("Enter district name for resource update: ")

if district_name in district_resources:
    resource_name = input("Enter resource name (water/electricity/medical_supplies): ").lower()
    if resource_name in district_resources[district_name]:
        new_value = int(input("Enter new availability percentage: "))
        if 0 <= new_value <= 100:
            district_resources[district_name][resource_name] = new_value
            print("Resource Updated Successfully!")
        else:
            print("Invalid Percentage!")
    else:
        print("Resource Not Found!")
else:
    print("District Not Found!")

print("\n--- PART 4: RESOURCE VALIDATION ---")
for district, resources in district_resources.items():
    for resource, value in resources.items():
        if 0 <= value <= 100:
            print(district, "-", resource, ":", "Valid")
        else:
            print(district, "-", resource, ":", "Invalid")

print("\n--- PART 5: RESOURCE SUMMARY REPORT ---")
for district, resources in district_resources.items():
    total_availability = sum(resources.values())
    total_resources = len(resources)
    average_availability = total_availability / total_resources
    print("\nDistrict:", district)
    print("Total Resources:", total_resources)
    print("Average Availability:", round(average_availability, 2), "%")
print("Resource Report Generated!")

# MODULE 10 - PROJECT MANAGEMENT SYSTEM
print("\n===== MODULE 10: PROJECT MANAGEMENT SYSTEM =====")

# PART 1 - PROJECT DATA DISPLAY
print("\n===== PROJECT DATA DISPLAY =====")

projects = {
    "Haram Expansion": {
        "status": "Ongoing",
        "progress": 75
    },
    "Road Development": {
        "status": "Completed",
        "progress": 100
    },
    "Water Network": {
        "status": "Ongoing",
        "progress": 60
    },
    "Hospital Construction": {
        "status": "Planning",
        "progress": 20
    }
}

for project, details in projects.items():
    print("\nProject:", project)
    print("Status:", details["status"])
    print("Progress:", details["progress"], "%")

print("\n===== MODULE 10 PART 1 COMPLETED =====")

