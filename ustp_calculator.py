BLUE = "\033[94m"   # Blue Accent
GOLD = "\033[93m"   # Gold Accent
GREEN = "\033[92m"  # Passing / Honors
RED = "\033[91m"    # Failing / Warning
BOLD = "\033[1m"
RESET = "\033[0m"

def print_banner():
    print(f"\n{BLUE}{'=' * 56}")
    print(f"{BOLD}{GOLD}   UNIVERSITY OF SCIENCE AND TECHNOLOGY OF SOUTHERN PHILIPPINES{RESET}")
    print(f"{BLUE}                STUDENT GWA CALCULATOR                {RESET}")
    print(f"{BLUE}{'=' * 56}{RESET}\n")

def main():
    print_banner()
    student_name = input(f"{GOLD}Enter Student Full Name: {RESET}").strip()
    program_year = input(f"{GOLD}Enter Program & Year (e.g., BSIT 2): {RESET}").strip()
    num_subjects = int(input(f"{GOLD}Enter total number of subjects: {RESET}"))
    
    total_honor_points = 0.0
    total_units = 0.0
    has_failed = False
    
    print(f"\n{BLUE}--- Enter Subject Grades (USTP 1.00 - 5.00 Scale) ---{RESET}")
    for i in range(1, num_subjects + 1):
        print(f"\n{BOLD}Subject #{i}{RESET}")
        units = float(input("  Course Units: "))
        grade = float(input("  USTP Grade (e.g., 1.00, 1.25, 1.50, 3.00): "))
        
        total_honor_points += (grade * units)
        total_units += units
        
        if grade > 3.00:
            has_failed = True

    gwa = total_honor_points / total_units if total_units > 0 else 0.0
    
    if gwa <= 3.00 and not has_failed:
        status = "PASSED"
        status_color = GREEN
        standing = "Dean's List / Regular Standing" if gwa <= 1.75 else "Regular Standing"
    else:
        status = "FAILED / PROBATIONARY"
        status_color = RED
        standing = "Not Eligible for Honors"

    print(f"\n{BOLD}{BLUE}+----------------------------------------------------+")
    print(f"|                 ACADEMIC SUMMARY                   |")
    print(f"+----------------------------------------------------+{RESET}")
    print(f"  Student Name   : {student_name}")
    print(f"  Program / Year : {program_year}")
    print(f"  Total Units    : {total_units:.1f}")
    print(f"  Calculated GWA : {status_color}{gwa:.4f}{RESET}")
    print(f"  Status         : {status_color}{status}{RESET}")
    print(f"  Standing       : {GOLD}{standing}{RESET}")
    print(f"{BOLD}{BLUE}+----------------------------------------------------+{RESET}\n")

if __name__ == "__main__":
    main()