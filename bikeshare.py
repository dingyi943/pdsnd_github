import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please input city name (chicago, new york city or washington): ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "City name is invalid! Please input 'chicago', 'new york city' or 'washington': ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Please input month name (input 'all' to apply no month filter): ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please input day of week (input 'all' to apply no day filter): ").lower()

    print('-'*40)
    return city, month, day


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
    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(int(
        df['month'].mode().values[0]))
    )

    # TO DO: display the most common day of week
    print("The most common day of the week: {}".format(str(
        df['day_of_week'].mode().values[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        int(df['start_hour'].mode().values[0]))
    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("The most common start station is: {} ".format(
        df['Start Station'].mode().values[0])
    )



    # TO DO: display most commonly used end station

    print("The most common end station is: {} ".format(
        df['End Station'].mode().values[0])
    )

    # TO DO: display most frequent combination of start station and end station trip

    df['station_combi'] = df['Start Station'] + " " + df['End Station']
    print("The most common start and end station combo is: {} ".format(
        df['station_combi'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['duration'] = df['End Time'] - df['Start Time']
    print("The total travel time is: {} ".format(
        df['duration'].sum())
    )


    # TO DO: display mean travel time
    print("The mean travel time is: {} ".format(
        df['duration'].mean())
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here are the counts of various user types:")
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    # TO DO: Display counts of gender
    print("Here are the counts of gender:")
    city = input("Please input city name: ").lower()
    if city == 'washington':
        print("counts of gender is not available in washington")
        print("earliest, most recent and most common year of birth are not available in washington")
    else:
        genders = df['Gender'].value_counts()
        print(genders)
        earliest = int(df['Birth Year'].min())
        print("The earliest birth year is: {}".format(earliest))
        most_recent = int(df['Birth Year'].max())
        print("The most recent birth year is: {}".format(most_recent))
        most_common = int(df['Birth Year'].mode().values[0])
        print("The most common birth year is: {}".format(most_common))

    # TO DO: Display earliest, most recent, and most common year of birth



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Display 5 lines raw data as requested by the user."""

    start = 0

    raw_data = input("Would you like to see 5 lines raw data? yes or no: ").lower()
    while True:
        if raw_data =='no':
            break

        else:

            print(df.iloc[start:start + 5])
            start += 5
            end_display = input("Would you like to continue? yes or no: ").lower()
            if end_display != 'yes':
                break





def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
