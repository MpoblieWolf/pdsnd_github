import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = check_user_input("Which city would you like to see data for? chicago, new york city or washington?\n", "c")



    month = check_user_input("Please enter a month to filter your data by, january to june, or enter 'all'\n", "m")


    day = check_user_input("Please enter the day of the week you want to filter the data by, monday to sunday, or enter 'all'\n", "d")

    print('-'*40)
    return city, month, day

def check_user_input(user_input, input_type):

    while True:
        input_user_entered = input(user_input).lower()
        try:
            if input_user_entered in ['chicago', 'new york city', 'washington'] and input_type == 'c':
                break
            elif input_user_entered in months_list and input_type == 'm':
                break
            elif input_user_entered in day_list and input_type == 'd':
                break
            else:
                if input_type == 'c':
                    print("This is not one of the three cities! required input must be: chicago, new york city or washington")
                if input_type == 'm':
                    print("Input is wrong, you need to enter one of the months. Input must be: january, february, march, april, may, june or all")
                if input_type == 'd':
                    print("Input is wrong, you need to enter the days of the week. Input must be: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all")
        except ValueError:
            print("Your input is incorrect, please try again")

    return input_user_entered

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'februrary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)


    common_day = df['day_of_week'].mode()[0]
    print('The most common day is: ', common_day)


    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('The most common hour is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', common_start_station)


    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', common_end_station)


    frequent_trip = df.groupby(['Start Station', 'End Station']).count()
    print('The most frequent combination of start and end station is: ', frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)


    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    print('The count of user types is: ', user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('The counts of gender are: ', gender_types)
    except KeyError:
        print('The counts of gender are: \nThere is no data for this month.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df['Birth Year'].min()
        print('The earliest birth year is: ', earliest_birthyear)
    except KeyError:
        print('The earliest birth year is: \nThere is no data for this month.')

    try:
        recent_birthyear = df['Birth Year'].max()
        print('The most recent birth year is: ', recent_birthyear)
    except KeyError:
        print('The most recent birth year is: \nThere is no data for this month.')

    try:
        common_birthyear = df['Birth Year'].mode()
        print('The most common birth year is: ', common_birthyear)
    except KeyError:
        print('The most common birth year is: \nThere is no data for this month')

    recent_birthyear = df

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# TO DO: create a function that requires input to display the raw data
def view_data_rows(df):
    row = 0
    while True:
        view_row_data = input("Would you like to view 5 rows of raw data? for 'Yes' enter 'Y' for 'No' enter 'N'.\n").lower()
        if view_row_data == 'y':
            print(df.iloc[row: row + 5])
            row += 5
            view_row_data = input("Do you wish to continue?: ").lower()
        elif view_raw_data == 'n':
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data_rows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
