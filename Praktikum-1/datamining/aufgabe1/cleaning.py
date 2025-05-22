import pandas as pd

def load_and_clean_data(path, save_to=None):
    # Load the CSV file
    df = pd.read_csv(path)
    
    # Strip extra quotes and whitespace from column names
    df.columns = df.columns.str.strip().str.replace("'", "")

    # Strip extra quotes and whitespace from string-type cells
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip().str.replace("'", "")

    # Drop unnecessary columns that start with 'Unnamed'
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

    # --- Begin: Repeatedly shift left if 'Nationality' contains a position ---
    # Define the set of valid football position abbreviations
    positions = {
        "GK", "CB", "RB", "LB", "RWB", "LWB",
        "DM", "CDM", "CM", "AM", "CAM",
        "RM", "LM", "RW", "LW", "CF",
        "RF", "LF", "ST", "SW"
    }

    # Get list of column names to preserve their original order
    column_list = list(df.columns)

    # Convert all columns to 'object' type to allow mixing strings and numbers safely
    df[column_list] = df[column_list].astype("object")

    # Proceed only if 'Nationality' column exists
    if "Nationality" in df.columns:
        # Get the index position of the 'Nationality' column
        nationality_idx = column_list.index("Nationality")

        # Iterate through each row in the DataFrame
        for index in df.index:
            while True:
                # Get the current value in the 'Nationality' column
                current_val = df.at[index, "Nationality"]

                # If the value is a position (e.g., 'ST', 'GK'), shift values to the left
                if isinstance(current_val, str) and current_val.strip() in positions:
                    # Shift all values one column to the left, starting from 'Nationality'
                    for j in range(nationality_idx + 1, len(column_list)):
                        left_col = column_list[j - 1]
                        right_col = column_list[j]
                        value_to_move = df.at[index, right_col]
                        # Assign the value, converting to string if needed
                        df.at[index, left_col] = value_to_move if pd.isna(value_to_move) else str(value_to_move)
                    # Note: The last column will remain unchanged on each shift
                else:
                    # Exit loop when 'Nationality' no longer contains a position
                    break

    # --- End shift on Nationality column ---

    # Optional: Drop rows with any missing values
    # df = df.dropna()

    # Save cleaned data to a new file if a path is provided
    if save_to:
        df.to_csv(save_to, index=False)
    
    return df
