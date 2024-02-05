import pandas as pd

def clean(input1, input2, output):

    df_1 = pd.read_csv(input1)
    df_2 = pd.read_csv(input2)

    # Merge the two input files based on the ID value
    df_merged = pd.merge(df_1, df_2, left_on='respondent_id', right_on='id')

    # Drop rows with missing values
    df_cleaned = df_merged.dropna()

    # Drop rows where job value contains 'insurance' or 'Insurance'
    df_cleaned = df_cleaned[~df_cleaned['job'].str.contains('insurance|Insurance')]

    # Drop redundant ID column
    df_cleaned = df_cleaned.drop(columns=['id'])

    return df_cleaned


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file (csv)')
    parser.add_argument('input2', help='Data file (csv)')
    parser.add_argument('output', help='Cleaned data file (csv)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2, args.output)
    cleaned.to_csv(args.output, index=False)