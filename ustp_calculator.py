def main():
    print("=== USTP GWA Calculator ===")
    student_name = input("Enter Student Full Name: ")
    num_subjects = int(input("Enter total number of subjects: "))
    
    total_honor_points = 0.0
    total_units = 0.0
    
    print("\n--- Enter Grades (1.00 = Highest, 3.00 = Pass, 5.00 = Fail) ---")
    for i in range(1, num_subjects + 1):
        print(f"\nSubject #{i}:")
        units = float(input("  Course Units (e.g., 3.0): "))
        grade = float(input("  USTP Grade (1.00 - 5.00): "))
        
        total_honor_points += (grade * units)
        total_units += units

    gwa = total_honor_points / total_units if total_units > 0 else 0.0
    
    print(f"\n--- Results for {student_name} ---")
    print(f"Total Units Registered: {total_units}")
    print(f"Calculated GWA: {gwa:.4f}")

if __name__ == "__main__":
    main()