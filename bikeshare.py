import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/udacity/python/project/bikeshare-2/chicago.csv',
              'new york city': '/udacity/python/project/bikeshare-2/new_york_city.csv',
              'washington': '/udacity/python/project/bikeshare-2/washington.csv' }

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
    while True:
        city = input("Which city's data do you wish to explore, Chicago, New York city or Washington?: ")
        if city.lower() in ['chicago', 'new york city', 'nyc', 'new york', 'ny', 'washington']:
            if city.lower() in ['nyc', 'new york' ,'ny']:
                city='new york city'
            break
        elif city.lower() == 'quit':
            quit()
        else:
            print('Sorry, you must enter Chicago, New York city, Washington or quit')
    print()
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Do you want to view the data by month? January, February, March, April, May, June or All: ")
        if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'all', 'jan', 'feb', 'mar', 'apr' , 'may', 'jun']:
            if month.lower() == 'jan':
                month='january'
            elif month.lower() == 'feb':
                month='february'
            elif month.lower() == 'mar':
                month='march'
            elif month.lower() == 'apr':
                month='april'
            elif month.lower() == 'may':
                month='may'
            elif month.lower() == 'jun':
                month='june'
            break
        elif month.lower() == 'quit':
            quit()
        else:
            print('Sorry, you must enter a valid month - January, February, March, April, May, June, All or quit:')
    print()
    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Do you want to view the data by day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All: ")
        if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all', 'mon' , 'mo', 'tue', 'tues' , 'tu','wed', 'weds' , 'we','thu', 'thur' , 'th','fri', 'fr','sat', 'sa','sun', 'su' ]:
            if day.lower() in ['mon' , 'mo']:
                day='Monday'
            elif day.lower() in ['tue', 'tues' , 'tu']:
                day='Tuesday'
            elif day.lower() in ['wed', 'weds' , 'we']:
                day='Wednesday'
            elif day.lower() in ['thu', 'thur' , 'th']:
                day='Thursday'
            elif day.lower() in ['fri', 'fr']:
                day='Friday'
            elif day.lower() in ['sat', 'sa']:
                day='Saturday'
            elif day.lower() in ['sun', 'su']:
                day='Sunday'

            break
        elif day.lower() == 'quit':
            quit()
        else:
            print('Sorry, you must enter a valid day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All or quit')

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
    df=pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

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

    # display the most common month
    print('The most common month for journeys is month', df['month'].mode()[0])

    # display the most common day of week
    print('The most common day of week for journeys is', df['day_of_week'].mode()[0])

    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used station for starting journeys is', df['Start Station'].mode()[0])

    # display most commonly used end station
    
    print('The most commonly used station for finishing a journey is', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start and End Stations'] = df['Start Station'] +' to '+ df['End Station']
    print('The most frequent journey is the route from', df['Start and End Stations'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The Total trip time for these trips is', df['Trip Duration'].sum(), 'seconds')

    # display mean travel time
    print('The mean trip time for these trip is', df['Trip Duration'].mean(), 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of user types : ')
    for user_type, count in df['User Type'].value_counts().items():
        print(' '*8, user_type , count)
     #df['User Type'].value_counts())
    print()
    # Display counts of gender
    if 'Gender' in df:
        print('Count of user Gender : ')
        for gender, count in df['Gender'].value_counts().items():
            print(' '*8, gender , count)
    else:
        print('Sorry we do not have Gender information for', city.title())
    print()
    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        print('The earliest year of birth : ', int(df['Birth Year'].min()))
        print('The most recent  year of birth: ', int(df['Birth Year'].max()))
        print('The most common  year of birth : ', int(df['Birth Year'].mode()))
    else:
        print('Sorry we do not have Birth Year information for', city.title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   
def main():
    # loop until the user indicates they do not wish to continue
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        row_count=0
        while True:
            raw_data=input('\nWould you like view some raw_data? Enter yes or no.\n')
            
            if raw_data.lower() == 'yes' or raw_data.lower() == 'y':
                temp_df=df[row_count:row_count+5]
                for row in temp_df.to_dict('records'):
                    print('{')
                    for k,g in row.items():
                        print(' '*8, k ,'  :  ', g)
                    print('}\n')
                row_count+=5

            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower() != 'y' and restart.lower() != 'go on so':
            break



if __name__ == "__main__":
	main()
