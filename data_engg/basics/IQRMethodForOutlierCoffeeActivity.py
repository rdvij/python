import pandas as pd
import sys as sys

def describe_dataframe(df):
    """
    This function takes a pandas DataFrame as input and returns its descriptive statistics.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to describe.
    
    Returns:
    pd.DataFrame: A DataFrame containing descriptive statistics of the input DataFrame.
    """
    return df.describe()

# read CSV file into DataFrame
df = pd.read_csv('coffee_farm_activities.csv')

## Descriptive statistics : In which season is activity pruning mostly done?

def describe_activities_by_season(df):
    """
    This function analyzes the activities by season in the given DataFrame.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing coffee farming activities.
    
    Returns:
    pd.Series: A series containing counts of pruning activities by season.
    """

    # Create seasons_activity_df with columns for each activity
    seasons_activity_df = pd.DataFrame()

    seasons_activity_df['pruning'] = df[df['activity_type'] == 'pruning']['season'].value_counts()
    seasons_activity_df['watering'] = df[df['activity_type'] == 'watering']['season'].value_counts()
    seasons_activity_df['fertilising'] = df[df['activity_type'] == 'fertilising']['season'].value_counts()
    seasons_activity_df['weeding'] = df[df['activity_type'] == 'weeding']['season'].value_counts()
    seasons_activity_df['harvesting'] = df[df['activity_type'] == 'harvesting']['season'].value_counts()
    seasons_activity_df['pest_control'] = df[df['activity_type'] == 'pest_control']['season'].value_counts()
    seasons_activity_df['shade_management'] = df[df['activity_type'] == 'shade_management']['season'].value_counts()
    seasons_activity_df['drying'] = df[df['activity_type'] == 'drying']['season'].value_counts()
    seasons_activity_df['sorting'] = df[df['activity_type'] == 'sorting']['season'].value_counts()
    seasons_activity_df['packaging'] = df[df['activity_type'] == 'packaging']['season'].value_counts()
    seasons_activity_df['transporting'] = df[df['activity_type'] == 'transporting']['season'].value_counts()
    seasons_activity_df['mulching'] = df[df['activity_type'] == 'mulching']['season'].value_counts()
    seasons_activity_df['grafting'] = df[df['activity_type'] == 'grafting']['season'].value_counts()

    return seasons_activity_df

print("Pruning activity counts by season:")
#print(describe_activities_by_season(df))

                                    ## ## ## ## Basic Activity and Season Analysis ## ## ## ##

# Check if harvesting activity is done in any other season apart from 'harvest_season'
harvesting_seasons = df[df['activity_type'] == 'harvesting']['season'].unique()
#print("\nUnique seasons for harvesting activity:")
#print(harvesting_seasons)

# Check if drying and sorting is done in seasons other than 'harvest_season'
drying_seasons = df[df['activity_type'] == 'drying']['season'].unique()
sorting_seasons = df[df['activity_type'] == 'sorting']['season'].unique()
#print("\nUnique seasons for drying activity:")
#print(drying_seasons)
#print("\nUnique seasons for sorting activity:")
#print(sorting_seasons)

# Check if transporting is done in seasons other than 'harvest_season'
transporting_seasons = df[df['activity_type'] == 'transporting']['season'].unique()
#print("\nUnique seasons for transporting activity:")
#print(transporting_seasons)

## ## ## ## End of Basic Activity and Season Analysis ## ## ## ##

# First calculate frequency at which harvesting is done in each season, and then use those numbers for
# outlier detection. ## ## ## ##

def check_harvesting_outliers(df, activity_type='harvesting', season='wet_season'):
    """
    This function checks for outliers in harvesting activity during the wet season using the IQR method.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing coffee farming activities.
    
    Returns:
    dict: A dictionary containing Q1, Q3, IQR, lower bound, upper bound, and outlier status.
    """
    # Calculate frequency of harvesting activity by season
    harvesting_freq = df[df['activity_type'] == activity_type]['season'].value_counts()

    # Focus on wet season frequency
    wet_season_freq = harvesting_freq.get(season, 0)

    # Calculate Q1, Q3, and IQR
    Q1 = harvesting_freq.quantile(0.25)
    Q3 = harvesting_freq.quantile(0.75)
    IQR = Q3 - Q1

    # Calculate lower and upper bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Check if wet season frequency is an outlier
    is_outlier = wet_season_freq < lower_bound or wet_season_freq > upper_bound

    return {
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'wet_season_freq': wet_season_freq,
        'is_outlier': is_outlier
    }


if __name__ == "__main__":

    if len(sys.argv) != 3:
        # Add failure icon in print message below
        print("❌ Usage: python IQRMethodForOutlierCoffeeActivity.py <season> <activity_type>")
        sys.exit(1)

    season = sys.argv[1]
    activity = sys.argv[2]

    if season is None or activity is None:
        print("❌ Please provide both season and activity type as command line arguments.")
        sys.exit(1)
    
    if season not in df['season'].unique():
        print(f"❌ Season '{season}' not found in the dataset.")
        sys.exit(1)

    if activity not in df['activity_type'].unique():
        print(f"❌ Activity type '{activity}' not found in the dataset.")
        sys.exit(1)

    outlier_info = check_harvesting_outliers(df, activity_type=activity, season=season)
    print("✅ Outlier analysis completed successfully.")
    print("\n")
    print(f"\n{activity.capitalize()} activity outlier analysis for {season}:")
    if outlier_info['is_outlier']:
        # Add an outlier icon(scatter plot) in print message below
        print(f"📊 The frequency of {activity} activity in {season} ({outlier_info['wet_season_freq']}) is an outlier.")
    else:
        print(f"✅ The frequency of {activity} activity in {season} ({outlier_info['wet_season_freq']}) is not an outlier.")