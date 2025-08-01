# My Digital Life – Digital Habit Tracker

A Python-based digital habit tracker and dashboard that helps you log daily habits, analyze your mood and activities, and scan your file system for organization. Visualize your progress and gain insights into your daily routines!

## Features

- **Daily Habit Logger:**  
  Log your mood, study hours, sleep hours, entertainment hours, and topics studied. Data is saved to both a CSV file and a MySQL database.

- **Visualization Dashboard:**  
  Generate insightful charts:
  - Mood trend over time
  - Average time spent per activity
  - Correlation heatmap between mood and activities
  - Study vs. mood bubble chart
  - Stacked bar chart of daily time allocation

- **File & Folder Scanner:**  
  Scan any directory to generate a CSV report of all files, including size, type, modification time, and path.

## Project Structure

```
my digital life/
  ├── assets/                # Generated charts and plots
  ├── data/                  # CSV logs and reports
  ├── utils/                 # Database connection and creation scripts
  ├── dashboard.py           # Visualization and dashboard code
  ├── habit_logger.py        # Daily habit logger
  ├── system_scanner.py      # File/folder scanner
  ├── main.py                # Main menu/entry point
  ├── requirements.txt       # Python dependencies
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd "my digital life"
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. MySQL Database Setup

- Ensure you have MySQL installed and running.
- The default connection uses:
  - host: `localhost`
  - user: `root`
  - password: `system`
  - database: `daily_habit_tracker`
- You can change these credentials in `utils/db_connect.py` and `utils/db_creation.py` if needed.
- The database and table are created automatically on first run.

### 4. Run the Application

```bash
python main.py
```

## Usage

You will see a menu with the following options:

1. **Daily logger** – Log your daily mood, study, sleep, entertainment, and topics.
2. **Files and Folder Scanner** – Enter a folder path to scan and generate a CSV report.
3. **Visualization Generator** – Generate and save summary charts in the `assets/` folder.
4. **Exit** – Quit the application.

## Dependencies

See `requirements.txt` for the full list. Key packages:
- numpy
- pandas
- matplotlib
- seaborn
- pymysql
- scipy
- cryptography
- fpdf

## Data Storage

- **CSV:** All logs are appended to `data/daily_logs.csv`.
- **MySQL:** All logs are also stored in the `daily_habit_tracker.daily_logs` table.

## Output

- **Charts:** Saved in the `assets/` directory.
- **File scan reports:** Saved as `data/logs.csv`.

## Customization

- Change database credentials in `utils/db_connect.py` and `utils/db_creation.py`.
- Modify or extend logging fields in `habit_logger.py` and database schema in `db_creation.py`.

## License

MIT License.
