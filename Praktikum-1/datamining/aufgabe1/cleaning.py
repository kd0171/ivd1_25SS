import pandas as pd

def load_and_clean_data(path, save_to=None):
    # Load the CSV file
    df = pd.read_csv(path)
    
    # Remove extra quotes and whitespace from column names
    df.columns = df.columns.str.strip().str.replace("'", "")
    
    # Remove extra quotes and whitespace from string-type cells
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip().str.replace("'", "")
    
    # Drop unnecessary columns that start with 'Unnamed'
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
    

    # --- Begin: Detect & fix misplaced position data ---

    # Define valid football positions
    positions = {
        "GK", "CB", "RB", "LB", "RWB", "LWB",
        "DM", "CDM", "CM", "AM", "CAM",
        "RM", "LM", "RW", "LW", "CF",
        "RF", "LF", "ST", "SW"
    }


    # Define where positions are allowed
    allowed_position_columns = [
        "Positions Played", "Best Position", "National Team Position", "Club Position"
    ]

    # Define columns that should NOT contain position names
    columns_to_check = [col for col in df.columns if col not in allowed_position_columns]

    # Step 1: Nullify position values that appear in invalid columns (cell by cell)
    for col in columns_to_check:
        for index in df.index:
            val = df.at[index, col]
            if isinstance(val, str) and val.strip() in positions:
                df.at[index, col] = None  # remove misplaced position

    # Step 2: Shift valid positions left (row-wise)
    for index, row in df.iterrows():
        found_positions = [
            row[col] for col in columns_to_check
            if isinstance(row[col], str) and row[col].strip() in positions
        ]

        # Left-align valid position values
        if found_positions:
            for i, col in enumerate(columns_to_check):
                if i < len(found_positions):
                    df.at[index, col] = str(found_positions[i])
                else:
                    # Only clear if the cell previously held a position (optional)
                    current = df.at[index, col]
                    if isinstance(current, str) and current.strip() in positions:
                        df.at[index, col] = None

    # --- End position fix ---

                
    # Drop rows with any missing values
    # df = df.dropna()

    # Save cleaned data to a new file if a path is provided
    if save_to:
        df.to_csv(save_to, index=False)
    
    return df
