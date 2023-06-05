import time
import pandas as pd
import numpy as np

"""
city_csv_path = <your filepath here>

CITY_DATA = { 'chicago': city_csv_path + 'chicago.csv',
              'new york city': city_csv_path + 'new_york_city.csv',
              'washington': city_csv_path + 'washington.csv' }
"""
              
"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
"""


CITY_MONTH = {'All':0, 'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6}

CITY_DAY = {'All':7, 'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}


print('Hello! Let\'s explore some US bikeshare data!')

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the day of week to filter by, or 'all' to apply no day filter
    """
    
    
    
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input('Enter a valid city (chicago, washington, or new york city): ').lower()
        if city in CITY_DATA:
            #print('Thanks, one moment while we fetch the data')
            print(city)
            # Exit Program
            break
        elif city == 'end':
            break
        else:
            print('Try again.')
            continue


# get user input for day of week (all, monday, tuesday, ... sunday)
# grab month

    while True: 
        month = input('Enter a valid month (All, January, February, March, April, May, June): ').title()
        if month in CITY_MONTH:
            print(month)
            break    
        elif month == 'End':
            break
        else:
            print('Try again.')
            continue


# get user input for day of week (all, monday, tuesday, ... sunday)         
# grab day of week (dow)

    while True:
        day = input('Enter a valid day of the week (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ').title()
        if day in CITY_DAY:
            #print('Thanks, one moment while we fetch the data')
            print(day)
            break 
        elif day == 'End':
            break
        else:
            print('Try again.')
            continue
            break

    print('-'*40)
    #print(city, month, day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the day of week to filter by, or 'all' to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    bikeshare_df = pd.read_csv(CITY_DATA[city])
    

    bikeshare_df['Start Time'] = pd.to_datetime(bikeshare_df['Start Time'])


    bikeshare_df['Month'] = bikeshare_df['Start Time'].dt.month_name()
    bikeshare_df['Day_of_Week'] = bikeshare_df['Start Time'].dt.day_name()
    bikeshare_df['Hour'] = bikeshare_df['Start Time'].dt.hour
    

    if month != 'All':
        bikeshare_df = bikeshare_df[bikeshare_df['Month'] == month]

    if day != 'All':
        bikeshare_df = bikeshare_df[bikeshare_df['Day_of_Week'] == day]
    #bikeshare_df.head()
    print(month, day)
    return bikeshare_df


def time_stats(bikeshare_df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if month != 'All':
        print(f'You selected {month} as your month.')  
    else: 
        print('The busiest month of the year is: ')
        print(bikeshare_df['Month'].value_counts().idxmax())
    
    if day != 'All':
        print(f'You selected {day} as your day.')
    else: 
        print('The busiest day of the week is: ')
        print(bikeshare_df['Day_of_Week'].value_counts().idxmax())
    
    print('The busiest hour of the day (on a 24 hour model) is: ')
    print(bikeshare_df['Hour'].value_counts().idxmax())

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(bikeshare_df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    st_station = bikeshare_df['Start Station'].value_counts().idxmax()
    print('The most used start station is: ', st_station)
    print()
    # display most commonly used end station
    end_stations = bikeshare_df['End Station'].value_counts().idxmax()
    print('The most used end station is: ', end_stations)
    print()
    # display most frequent combination of start station and end station trip
    most_used_route = bikeshare_df[['Start Station', 'End Station']].value_counts().idxmax()
    print('The most used route is: ', most_used_route)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(bikeshare_df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = bikeshare_df['Trip Duration'].sum()/60
    print('The total travel time of bikeshare users is: ', total_travel_time)

    # display mean travel time
    avg_travel_time = bikeshare_df['Trip Duration'].mean()/60
    print('The average travel time of bikeshare users is: ', avg_travel_time)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(bikeshare_df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = bikeshare_df['User Type'].value_counts().idxmax()
    print('The more popular user type of our riders is: ', user_type)

    
    # Display counts of gender
    if city != 'washington':
        gender = bikeshare_df['Gender'].value_counts().idxmax()
        print('The more common gender of our riders is: ', gender)

        # Display earliest, most recent, and most common year of birth
        #bikeshare_df['Birth Year'].describe()
        youngest_rider = bikeshare_df['Birth Year'].max()
        print('The youngest rider was born in: ', youngest_rider)
        oldest_rider = bikeshare_df['Birth Year'].min()
        print('The oldest rider was born in: ' , oldest_rider)
        most_commom_yob = bikeshare_df['Birth Year'].mode()[0] #value_counts().head(1)#.max()
        print('The most common year of birth for our riders: ', most_commom_yob) #yob = year of birth

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def raw_data(bikeshare_df):
    bikeshare_df = bikeshare_df.sort_values(by=['Start Time'])
    bikeshare_df_stacked = bikeshare_df.stack()
    
    #display 5 rows at a time
    
    count = 0
    columns = bikeshare_df.shape[1]
    while True:
        r_data = input('Would you like to see some of the raw data? Enter yes or no. ').lower()
        if r_data != 'yes':
            print('OK, no more raw data.')
            break
        else:
            print(bikeshare_df_stacked[(columns*count*5):(columns*(count*5+5))])
            count +=1 

            
def main():
    while True:
        city, month, day = get_filters()
        bikeshare_df = load_data(city, month, day)

        time_stats(bikeshare_df)
        station_stats(bikeshare_df)
        trip_duration_stats(bikeshare_df)
        user_stats(bikeshare_df)
        raw_data(bikeshare_df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you for your time and interest. Goodbye.')
            break


if __name__ == "__main__":
	main()
