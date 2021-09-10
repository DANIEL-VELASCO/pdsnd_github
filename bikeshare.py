import time
import pandas as pd
import numpy as np


pd.set_option('display.max_columns', None)


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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        # Ask the user for a name.
        city = input("Please tell me which city would you like to explore : ")
        city = city.lower()

        try:
            CITY_DATA[city]
        except:
            print("\n Please enter Chicago, New York city or Washington \n")


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may','june','july','august','september','october','november','december']


    months_in_data = ['all','january', 'february', 'march', 'april', 'may','june']

    month=''
    in_data=False

    while month not in months or in_data==False:
        month = input("Fabulous!...now please tell me which month would you like to explore : ")
        month = month.lower()

        if month in months and month in months_in_data :
            in_data = True
        elif month in months and month not in months_in_data:
            print("\n Oops!..It seems the month you specified is not within the data\n")
        else:
            print("\n Please enter a valid month name")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    daysOfWeek = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    day = ''
    while day not in daysOfWeek:
        day = input("\nNice!... now please tell me which day would you like to explore : ")
        day = day.lower()

        if day not in daysOfWeek:
            print("\nPlease enter a valid day")


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

    # load data file into a dataframe
    print("\nLoading dataset...\n")
    df = pd.read_csv(CITY_DATA[city])
    print("\nDone!\n")

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']== month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # Reset indices of the filtered dataframe
    df.reset_index( drop=True, inplace=True)

    print("\nCheck out this information about your data:\n")
    print(df.describe(include='all'))

    return df

def display_data(df):

    """Displays 5 lines of data if the user type yes
    Args:
        df - dataframe to be displayed
    """


    visualize_data = ''
    start_index = 0
    last_index = 5

    while visualize_data != 'no' and last_index < len(df):
        visualize_data = input("\nWould you like to see 5 lines of your data ? please type yes or no\n")
        visualize_data = visualize_data.lower()

        if visualize_data not in ['yes','no']:
            print('\n Please enter yes or no')
        else:
            print(df.iloc[start_index:last_index,:])
            start_index += 5
            last_index += 5




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_freq_month = df['month'].value_counts().index.tolist()[0]
    counts_most_freq_month = df['month'].value_counts()[most_freq_month]

    months_names = ['January','February','March','April','May','June','July','August','September','October','November','December']
    print("the most common month is {} occurring {} times".format(months_names[most_freq_month-1],counts_most_freq_month))


    # TO DO: display the most common day of week
    most_freq_day = df['day_of_week'].value_counts().index.tolist()[0]
    count_most_freq_day = df['day_of_week'].value_counts()[most_freq_day]
    print("the most common day of the week is {} occurring {} times".format(most_freq_day,count_most_freq_day))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour       # Extracts the hour from the start_hour field
    most_freq_start_hour = df['start_hour'].value_counts().index.tolist()[0]
    count_most_freq_start_hour = df['start_hour'].value_counts()[most_freq_start_hour]
    print("the most common start hour is {} occurring {} times".format(most_freq_start_hour,count_most_freq_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_freq_start_station = df['Start Station'].value_counts().index.tolist()[0]
    counts_most_freq_start_station = df['Start Station'].value_counts()[most_freq_start_station]
    print("the most common start station is {} occurring {} times".format(most_freq_start_station,counts_most_freq_start_station))


    # TO DO: display most commonly used end station
    most_freq_end_station = df['End Station'].value_counts().index.tolist()[0]
    counts_most_freq_end_station = df['End Station'].value_counts()[most_freq_end_station]
    print("the most common end station is {} occurring {} times".format(most_freq_end_station,counts_most_freq_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_stations'] = df['Start Station'] + ' - ' + df['End Station']
    most_frequent_combination = df['start_end_stations'].value_counts().index.tolist()[0]
    counts_most_frequent_combination = df['start_end_stations'].value_counts()[most_frequent_combination]
    print("the most common combination of start and end stations trip is {} occurring {} times".format(most_frequent_combination,counts_most_frequent_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is {} seconds'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is {} seconds'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city,df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_per_user_types = df['User Type'].value_counts()
    print('\nCounts of user types:\n')
    print(count_per_user_types)

    if city != 'washington':
        # TO DO: Display counts of gender
        print('\nCounts of gender:\n')
        count_per_gender = df['Gender'].value_counts()
        print(count_per_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nThe earlisest birth year is {}'.format(str(df['Birth Year'].min())))
        print('\nThe most recent birth year is {}'.format(str(df['Birth Year'].max())))
        print('\nThe most common birth year is {}'.format(str(df['Birth Year'].value_counts().index.tolist()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city,df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
