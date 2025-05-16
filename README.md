# prem-elo
A python project for reimaging ranking premier league seasons by using ELO rather than the traditional points system using historical data from premier league matches soruced from Kaggle: https://www.kaggle.com/datasets/evangower/premier-league-matches-19922022.

## Features

- Calculates Elo ratings for all Premier League teams in a given season.
- Uses a custom Elo update formula with adjustable sensitivity and K-factor.
- Reads match data from a CSV file (`premier-league-matches.csv`).
- Plots Elo rating progression for selected teams across all gameweeks.
- Outputs detailed Elo changes and league table after each gameweek.

## Requirements

- Python 3.x
- pandas
- matplotlib

Install dependencies with:

```bash
pip install pandas matplotlib
```

## Usage

1. Place the `premier-league-matches.csv` file in the project directory.
2. Run the script:

```bash
python calc.py
```

3. The script will:
   - Process the matches for the season specified by `SEASONEND` in `calc.py`.
   - Print Elo changes and league tables for each gameweek.
   - Display a plot of Elo ratings for selected teams (default: Arsenal, Manchester City).

## File Descriptions

- **calc.py**: Main script for Elo calculation and visualization.
- **premier-league-matches.csv**: Historical Premier League match results. Columns include:
  - `Season_End_Year`, `Wk`, `Date`, `Home`, `HomeGoals`, `AwayGoals`, `Away`, `FTR`

## Customization

- To change the season analyzed, modify the `SEASONEND` variable in `calc.py`.
- To plot different teams, edit the `teamname` list near the end of `calc.py`.
- Adjust `K_FACTOR` and `SENSITIVITY` in `calc.py` to experiment with Elo calculation dynamics.

## Example Output

- Console output for each gameweek, showing match results and Elo changes.
- Matplotlib plot showing Elo rating progression for selected teams.
