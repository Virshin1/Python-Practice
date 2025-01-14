# Complex Python Program #34

```python
import random
import logging
import time

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('anomalous_activity_detector.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.activity_log = []
        self.login_count = 0

    def login(self, password_attempt):
        if password_attempt == self.password:
            self.login_count += 1
            self.activity_log.append(f'Login attempt: successful')
            logger.info(f'User {self.username} logged in successfully.')
            return True
        else:
            self.activity_log.append(f'Login attempt: failed')
            logger.warning(f'User {self.username} failed to log in.')
            return False

    def logout(self):
        self.activity_log.append('Logout')
        logger.info(f'User {self.username} logged out.')


class ActivityDetector:
    def __init__(self, users):
        self.users = users
        self.anomalous_activity = []

    def detect_anomalous_activity(self):
        for user in self.users:
            # Check for excessive login attempts
            if user.login_count > 5:
                self.anomalous_activity.append(f'User {user.username} has made {user.login_count} login attempts.')
                logger.warning(f'Suspicious login activity detected for user {user.username}.')

            # Check for login attempts at unusual times
            for activity in user.activity_log:
                if activity.startswith('Login attempt'):
                    login_time = time.strptime(activity.split(' ')[0], '%Y-%m-%d %H:%M:%S')
                    if login_time.tm_hour < 6 or login_time.tm_hour > 22:
                        self.anomalous_activity.append(f'User {user.username} attempted to log in at {login_time}.')
                        logger.warning(f'Suspicious login time detected for user {user.username}.')

            # Check for failed login attempts followed by successful login attempts
            failed_logins = [activity for activity in user.activity_log if activity.startswith('Login attempt: failed')]
            successful_logins = [activity for activity in user.activity_log if activity.startswith('Login attempt: successful')]
            for failed_login, successful_login in zip(failed_logins, successful_logins):
                failed_login_time = time.strptime(failed_login.split(' ')[0], '%Y-%m-%d %H:%M:%S')
                successful_login_time = time.strptime(successful_login.split(' ')[0], '%Y-%m-%d %H:%M:%S')
                if (successful_login_time - failed_login_time).seconds < 60:
                    self.anomalous_activity.append(f'User {user.username} failed to log in at {failed_login_time} and then successfully logged in at {successful_login_time}.')
                    logger.warning(f'Suspicious login pattern detected for user {user.username}.')


def generate_random_users(n):
    users = []
    for i in range(n):
        username = f'user{i}'
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
        users.append(User(username, password))
    return users


def simulate_user_activity(users):
    for user in users:
        # Simulate login and logout events
        for i in range(random.randint(1, 10)):
            if random.random() < 0.5:
                user.login(user.password)
            else:
                user.logout()

        # Simulate anomalous activities
        if random.random() < 0.1:
            # Excessive login attempts
            for i in range(random.randint(6, 10)):
                user.login(random.choice('abcdefghijklmnopqrstuvwxyz'))

        if random.random() < 0.1:
            # Login attempts at unusual times
            for i in range(random.randint(1, 3)):
                now = time.gmtime()
                login_time = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday,
                                                 random.randint(0, 5), random.randint(0, 59), random.randint(0, 59),
                                                 now.tm_wday, now.tm_yday, now.tm_isdst))
                activity = f'Login attempt: failed at {time.strftime("%Y-%m-%d %H:%M:%S", login_time)}'
                user.activity_log.append(activity)
                logger.warning(f'Suspicious login time detected for user {user.username}.')

        if random.random() < 0.1:
            # Failed login attempts followed by successful login attempts
            for i in range(random.randint(1, 3)):
                now = time.gmtime()
                failed_login_time = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday,
                                                         random.randint(0, 5), random.randint(0, 59), random.randint(0, 59),
                                                         now.tm_wday, now.tm_yday, now.tm_isdst))
                failed_activity = f'Login attempt: failed at {time.strftime("%Y-%m-%d %H:%M:%S", failed_login_time)}'
                user.activity_log.append(failed_activity)
                successful_login_time = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday,
                                                             random.randint(6, 23), random.randint(0, 59), random.randint(0, 59),
                                                             now.tm_wday, now.tm_yday, now.tm_isdst))
                successful_activity = f'Login attempt: successful at {time.strftime("%Y-%m-%d %H:%M:%S", successful_login_time)}'
                user.activity_log.append(successful_activity)
                logger.warning(f'Suspicious login pattern detected for user {user.username}.')


if __name__ == '__main__':
    # Generate random users
    users = generate_random_users(10)

    # Simulate user activity
    simulate_user_activity(users)

    # Detect anomalous activity
    activity_detector = ActivityDetector(users)
    activity_detector.detect_anomalous_activity()

    # Print anomalous activity
    if activity_detector.anomalous_activity:
        for activity in activity_detector.anomalous_activity:
            print(activity)
    else:
        print('No anomalous activity detected.')
```