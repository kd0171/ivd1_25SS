import pandas as pd

def load_and_clean_data(path, save_to=None):
    try:
        # Read CSV using single quote as quote character to preserve values like 'CF,ST'
        df = pd.read_csv(path, quotechar="'")
    except Exception as e:
        print(f"[ERROR] Failed to read CSV file: {e}")
        print("Preview of first 10 lines for debugging:\n")
        with open(path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f.readlines()):
                print(f"{i+1}: {line.strip()}")
                if i >= 9:
                    break
        raise e

    # Step 1: Convert 'Positions Played' to a list of positions
    if "Positions Played" in df.columns:
        df["Positions List"] = df["Positions Played"].apply(
            lambda x: [item.strip().replace("'", "") for item in x.split(",")] if isinstance(x, str) else []
        )

    # Step 2: Clean column names (remove leading/trailing spaces and single quotes)
    df.columns = df.columns.str.strip().str.replace("'", "")

    # Step 3: Clean string cells in each column (remove leading/trailing spaces and single quotes)
    for col in df.select_dtypes(include='object').columns:
        if col == "Positions List":
            continue  # Skip cleaning list-type column
        df[col] = df[col].str.strip().str.replace("'", "")

    # Step 4: Remove unnecessary columns that start with 'Unnamed'
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

    # Step 5: Save the cleaned data to a file if requested
    if save_to:
        df.to_csv(save_to, index=False)

    return df
