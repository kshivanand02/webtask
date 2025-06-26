# webtask

Install Selenium using pip install selenium in your terminal or command prompt.

Download the correct ChromeDriver version matching your Chrome (v137) and place chromedriver.exe in the same folder as your script.

Set up Instagram login credentials in the script (USERNAME, PASSWORD).

Initialize the WebDriver with proper options like --start-maximized.

Open Instagram login page using driver.get(...) and wait for elements to load.

Login to Instagram by locating the username and password input fields and sending keys.

Handle pop-ups like "Save Info" and "Turn On Notifications" by clicking "Not Now" if visible.

Search for the target user using the search box input and simulate Enter key presses to navigate.

Click the 'Follow' button if available, otherwise skip if already followed.

Extract profile data (name, bio, posts, followers, following) a
