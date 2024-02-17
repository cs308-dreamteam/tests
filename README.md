# Tests Documentation

## Unit Tests

### Setup
setUp(): Initializes common variables used across different tests. This includes the base URL, headers, and mock user names.

### Test Cases

#### Authorization Tests
test_invalid_auth_token(): Ensures that the API rejects requests with invalid authentication tokens.
test_unauthorized_access(): Tests access control for protected endpoints.

#### Response Tests
test_response_time_for_recom(): Checks if the recommendation endpoint responds within an acceptable time frame.
test_empty_response_handling(): Verifies that the API does not return null or empty responses.

#### Data Integrity Tests
test_get_recommendation_return_types(): Validates the structure and data types of the recommendation response.
test_successful_recommendations_fetching(): Ensures the recommendation endpoint fetches data correctly.

#### User Interaction Tests
test_successful_rating_change(): Tests the ability to update song ratings.
test_follow_user_invalid_data(): Checks the handling of invalid data when following a user.
test_add_song_successfully(): Validates the addition of new songs to the database.
test_get_top5_successfully(): Ensures the top 5 songs are fetched correctly for a user.

#### Error Handling Tests
test_invalid_request_body(): Tests the API's response to requests with missing or invalid body parameters.
test_register_weak_password(): Checks the registration process for weak passwords.
test_verify_incorrect_code(): Validates the verification process with an incorrect code.
test_delete_song_unauthorized(): Ensures that unauthorized users cannot delete songs.

#### Special Cases
test_verify_correct_code(): Tests the verification process with a correct code, including database interactions.
test_delete_song_successfully(): Validates the deletion of a song by authorized users.
test_add_song_unauthorized(): Ensures unauthorized users cannot add songs.
test_get_top5_unauthorized(): Checks unauthorized access to the top 5 songs endpoint.


## Performance and Functional Tests

### AddSongSeleniumTest.py
#### What does this test do??

#### Monitoring System Resources: (CPU Usage: 43.2%, Memory Usage: 81.7%)
Uses psutil to monitor CPU and memory usage in real-time.
Runs the monitoring in a separate thread to avoid blocking the main script.

#### Setting Up the Webdriver:
Configures the Chrome WebDriver with specific options (like detaching the browser upon script completion) to simulate the song addition process.
#### Automated Browser Interaction:
Navigates to a specified URL.
Finds and fills in login credentials.
Submits the login form.
Waits for the next page to load.
Navigates to an "Add Song" page.
Fills in song details (title, artist, album, genre, rating).
Submits the song details.
#### Time Measurement: (Throughput Time: 1.1517219543457031)
Measures the time taken for the script to execute from start to finish.


### RemoveSongSeleniumTest.py
#### What does this test do??

#### System Resource Monitoring: (CPU Usage: 51.4%, Memory Usage: 85.2%)
Uses psutil to track CPU and memory usage while the script runs.
Runs this monitoring in a separate thread.

#### Webdriver Configuration:
Sets up the Chrome WebDriver to simulate the song removal process with options such as detaching the browser after script completion.

#### Automated Browser Actions:
Opens the specified URL in a browser.
Locates and fills in the username and password fields.
Submits the login form.
Waits for the subsequent page to load.
Finds and clicks the button to delete a specific song.

#### Performance Measurement: (Throughput Time: 1.044651985168457)
Calculates the time taken by the script from start to finish. 


### getRecomSeleniumTest.py
#### What does this test do??

#### System Resource Monitoring: (CPU Usage: 47.5%, Memory Usage: 84.1%)
Utilizes psutil to monitor CPU and memory usage in real-time.
Operates the monitoring in a separate thread.

#### Webdriver Setup:
Configures Chrome WebDriver to simulate the recommendation getting process with specific options, including detaching the browser after the script completes.

#### Automated Browser Interactions:
Opens the specified URL in a browser.
Logs in using provided credentials.
Navigates to the recommendation page.
Iteratively fetches and prints the names of songs recommended in different tabs:
- Friend Recommendations
- Our Recommendations
- Spotify Recommendations

#### Performance Metrics: (Throughput Time: 5.692904949188232)
Measures the total execution time of the script.

