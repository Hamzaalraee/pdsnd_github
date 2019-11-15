import pandas as pd

city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

'''
Making Things Easier With Libraries
'''

cities = ['new york city', 'chicago', 'washington']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'none']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'None']

print("\n          _______LET'S FIND OUT SOME DATA FOR BIKE SHARE_______\n")


def data_filter():
    global month
    global day
    global city_a
    print(' ')

    """
        Asks user to Choose a city, month, and day to analyze.
        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by
            (str) day - name of the day of week to filter by
        """
# ------------ City input ---------------
    while True:
        city = input(f'Please enter the city name you would like to see data for: {cities} \n>')
        city_a = city.lower()
        if city_a[-1] == ' ':
            print('DO NOT ENTER SPACE.')
            continue
        else:
            pass
        if city_a not in cities:
            print(f'Please make sure your spelling are correct')
            continue
        else:
            print('-' * 40)
            break

# ------------ Analysing Question ------------
    q = input('Would you like to filter data by month or day or both or no filter ?: ')
    if q == 'month':
        day = 'none'
        while True:
            month = input(
                'The name of month which you want filter by OR none  \n(Jan, Feb, Mar, Apr, May, Jun): \n>')
            if month[-1] == ' ':
                print('DO NOT ENTER SPACE .')
                continue
            else:
                pass
            if month.lower() not in months:
                print('Please Try Again!')
                continue
            else:
                print('-' * 40)
                break

    if q == 'day':
        month = 'none'
        while True:
            day = input('''The name of day which you want filter by OR none 
(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) \n>''')
            if day[-1] == ' ':
                print('DO NOT ENTER SPACE.')
                continue
            else:
                pass
            if day.title() not in days:
                print('Please Try Again:')
                continue
            else:
                print('-' * 40)
                break

    if q == 'both':
        while True:
            month = input(
                'The name of month which you want filter by OR none \n(Jan, Feb, Mar, Apr, May, Jun): \n>')
            if month[-1] == ' ':
                print('DO NOT ENTER SPACE.')
                continue
            else:
                pass
            if month.lower() not in months:
                print('Please Try Again!')
                continue
            else:
                print('-' * 40)
                break

        while True:
            day = input('''The name of day which you want filter by OR none 
(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) \n>''')
            if day[-1] == ' ':
                print('DO NOT ENTER SPACE.')
                continue
            else:
                pass
            if day.title() not in days:
                print('Please Try Again:')
                continue
            else:
                print('-' * 40)
                break

    if q == 'none':
        month = 'none'
        day = 'none'
    return city_a,month,day


def get_data(city1, month1, day1):
    global df
    global month
    global day
    '''
    :param city1: Get the selected city from input
    :param month1: If applying filter by month it well get it from input
    :param day1: If applying filter by day it well get it from input
    :return: Filtering data as user required
    '''
    df = pd.read_csv(city_data[city1])

# ---------- Change 'Start Time' column type to acquire month and day ---------
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

# filtering data as user required
    if month != 'none':
        month = months.index(month1) + 1
        df = df[df['month'] == month]
    else:
        pass

    if day != 'none':
        df = df[df['Day of Week'] == day1.title()]
    else:
        pass

    return df


def common_time(df):
    '''Displays most popular travel times'''
    print('-' * 40)
    print('Calculating The Most Popular Times of Travel...\n')

    common_month = df['month'].mode()[0]
    print(f'Most Common Month: {common_month}')

    common_day = df['Day of Week'].mode()[0]
    print(f'Most Common day: {common_day}')

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'Most Common Hour: {common_hour}')


def common_station(df):
    '''Displays Most Common Start And End Stations'''
    print('-' * 40)
    print('Calculating Common Start And End Stations...\n')

    start_station = df['Start Station'].value_counts().idxmax()
    print(f'Popular start station: {start_station}.')

    end_station = df['End Station'].value_counts().idxmax()
    print(f'Popular end station: {end_station}.')

    df['routes'] = df['Start Station']+ " " + df['End Station']
    a = df['routes'].value_counts().idxmax()
    print(f'Most Combined Stations: {a}.')


def trip(df):
    '''Displays total and AVG time travel'''
    print('-' * 40)
    print('Calculating Total and Avg Trip Duration...\n')

    total_travel = sum(df['Trip Duration'])
    print(f'Total travel Time: {total_travel}')

    avg = df['Trip Duration'].mean()
    print(f'Average travel time: {avg}')


def user_info(df, city_a):
    """Displays statistics on bikeshare users."""
    print('-' * 40)
    print('Calculating Users Type...\n')

    print('Counts of users type: ')
    print(df['User Type'].value_counts())
    print('')

# -------- Displays Users Gender For Chicago and New York Data --------

    if city_a != 'washington':
        print('-' * 40)
        print('Calculating counts of gender... \n')

        print('Counts of gender: ')
        gender = df['Gender'].value_counts()
        print(f'{gender}')

# -------- Display earliest, most recent, and most common year of birth --------

        earliest = df['Birth Year'].min()
        earliest1 = int(earliest)
        print('-' * 40)
        print(f'The earliest birth year is: {earliest1}')

        most_recent = df['Birth Year'].max()
        most_recent1 = int(most_recent)
        print(f'The latest birth year is: {most_recent1}')

        most_common = df['Birth Year'].mode().values[0]
        most_common1 = int(most_common)
        print(f'The most common birth year is: {most_common1}')


def raw(df):
    """
    Display contents of the DATA file to the display as the user wish.
    """

    start = 0
    end = 5

    show = input("\nDo you love to see the raw data? Enter yes or no").lower()

    if show == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end, :])
            start += 5
            end += 5

            end_show = input("Do you wish to continue? Enter yes or no").lower()
            if end_show == 'no':
                break


def main():

    while True:
        city_a, month, day = data_filter()
        df = get_data(city_a, month, day)

        common_time(df)
        common_station(df)
        trip(df)
        user_info(df, city_a)
        raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nShutting Down...')
            break


if __name__ == "__main__":
    main()