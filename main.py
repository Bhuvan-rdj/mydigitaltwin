from dashboard import show_dashboard
from habit_logger import log_habit
from system_scanner import save_to_csv,scan_directory
def main():
    while True:
        print("\n My Digital Twin-Digital Habit Tracker")
        print("1. Daily logger")
        print("2. Files and Folder Scanner")
        print("3. Visualization Generator")
        print("4. Exit")
        choice=int(input("Enter your choice(1/2/3/4): "))
        if choice==1:
            log_habit()
        elif choice==2:
            folder=input("Enter folder path:").strip()
            try:
                df=scan_directory(folder)
                print(f"Found {len(df)}files")
                save_to_csv(df) 
            except Exception as e:
                    print(f"Error:{e}")
        elif choice == 3:
             show_dashboard()
        
        else:
            print("Program Exited")
            break
if __name__=='__main__':
    main()
