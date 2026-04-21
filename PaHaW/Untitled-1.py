# -*- coding: utf-8 -*-
"""
UPDATED Python script for loading the PaHaW (Parkinson's Handwriting) Dataset.

This script is now tailored to your specific file directory structure.

PaHaW/
├── metadata.csv
└── drawings/
    ├── dynamic/
    │   ├── d_0001.txt
    │   ├── d_0002.txt
    │   └── ...
    └── static/
        └── ...

This script will:
1. Load `metadata.csv`.
2. Use the 'path' column from the metadata to find the exact
   location of each drawing file (e.g., 'drawings/dynamic/d_0001.txt').
3. Provide a function to load the time-series data from those .txt files.
"""

import pandas as pd
import os
import sys

def load_individual_drawing(filepath):
    """
    Loads a single time-series drawing file.

    The PaHaW text files typically contain space-separated values
    with a header line starting with '#'.

    Args:
        filepath (str): The full path to the .txt file to load.

    Returns:
        pandas.DataFrame: A DataFrame containing the time-series data,
                          or None if the file is not found.
    """
    # Column names are based on the header in the .txt files
    # (e.g., # X Y Z Pressure GripAngle Timestamp InAir)
    COLUMNS = [
        'X', 'Y', 'Z',
        'Pressure', 'GripAngle',
        'Timestamp', 'InAir'
    ]

    try:
        drawing_df = pd.read_csv(
            filepath,
            sep=' ',          # The files are space-separated
            header=None,      # The files have no header row (after comments)
            names=COLUMNS,    # Assign our defined column names
            comment='#'       # This is key: it skips the header line
        )
        return drawing_df

    except FileNotFoundError:
        print(f"Error: Drawing file not found at path: {filepath}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error loading drawing file {filepath}: {e}", file=sys.stderr)
        return None

def load_metadata(metadata_path, root_dir):
    """
    Loads the main metadata file and creates a full path to each drawing.

    Args:
        metadata_path (str): Path to the `metadata.csv` file.
        root_dir (str): Path to the root 'PaHaW' directory.

    Returns:
        pandas.DataFrame: A DataFrame of the metadata with a new
                          'full_path' column, or None if an error occurs.
    """
    try:
        metadata_df = pd.read_csv(metadata_path)
    except FileNotFoundError:
        print(f"Error: Metadata file not found at path: {metadata_path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error loading metadata file: {e}", file=sys.stderr)
        return None

    # Your screenshot confirms the column is named 'path'
    if 'path' not in metadata_df.columns:
        print("Error: Could not find the 'path' column in metadata.csv.", file=sys.stderr)
        return None

    # Create a 'full_path' column by joining the root directory
    # with the relative path from the metadata (e.g., 'drawings/dynamic/d_0001.txt')
    metadata_df['full_path'] = metadata_df['path'].apply(
        lambda rel_path: os.path.join(root_dir, rel_path)
    )

    # Filter for dynamic drawings only, since your thesis uses dynamic data
    # Your 'path' column conveniently contains 'dynamic'
    initial_count = len(metadata_df)
    metadata_df = metadata_df[metadata_df['path'].str.contains('dynamic')].copy()
    print(f"Filtered for dynamic drawings. Kept {len(metadata_df)} out of {initial_count} total records.")

    return metadata_df

# --- This is the main part of the script that runs it ---
if __name__ == "__main__":
    
    # --- IMPORTANT: YOU MUST CHANGE THIS ONE VARIABLE ---
    # Update this path to point to your *main* 'PaHaW' folder
    PAHAW_ROOT_DIR = "C:\Users\evmagante\Downloads\PaHaW\PaHaW"
    # ----------------------------------------------------

    # 1. Define the metadata file path
    METADATA_FILE = os.path.join(PAHAW_ROOT_DIR, 'metadata.csv')

    # 2. Load the metadata
    print(f"Loading metadata from: {METADATA_FILE}")
    metadata_df = load_metadata(METADATA_FILE, PAHAW_ROOT_DIR)

    if metadata_df is not None:
        print("\n--- Metadata Loaded Successfully ---")
        print(f"Total dynamic drawings found: {len(metadata_df)}")
        print("Metadata columns:", metadata_df.columns.tolist())
        print("First 5 rows of metadata:")
        print(metadata_df.head())
        print("------------------------------------\n")

        # 3. Load an example drawing from the metadata
        if not metadata_df.empty:
            # Get the first row as an example
            example_row = metadata_df.iloc[0]
            
            # Your screenshot confirms the H&Y column name
            hy_col = 'H&Y' 
            
            print(f"Loading example drawing for Patient: {example_row['Patient_ID']}")
            print(f"H&Y Score: {example_row[hy_col]}")
            print(f"File path: {example_row['full_path']}")
            
            example_drawing = load_individual_drawing(example_row['full_path'])
            
            if example_drawing is not None:
                print("\n--- Example Drawing Loaded Successfully ---")
                print(f"Total time steps in this drawing: {len(example_drawing)}")
                print("First 5 time steps of drawing:")
                print(example_drawing.head())
                print("-------------------------------------------\n")
            else:
                print("Failed to load the example drawing.")
        else:
            print("Metadata is empty, cannot load example drawing.")
    else:
        print("Failed to load metadata. Please check your paths.")