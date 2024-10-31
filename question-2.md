# Log Event Extraction and Analysis

You will create a Python program that:

1.	Extracts specific lines from a large log file (events.txt) based on user input.
2.	Counts and categorizes certain types of events in these lines, such as “ERROR”, “WARNING”, and “INFO”.
3.	Saves the selected lines along with a summary report into an output file (output.txt), showing the breakdown of event types.

#### Instructions

1.	Select Line Numbers or Ranges: Prompt the user to either select specific line numbers or a range of lines. Allow multiple ranges or individual lines separated by commas (e.g., “1-5, 10, 15-20”).
2.	Categorize Events: After reading the selected lines, count and categorize events based on keywords like “ERROR”, “WARNING”, and “INFO”.
3.	Generate a Summary: In addition to saving the extracted lines, include a summary at the end of the output.txt file, showing the count of each event type (ERROR, WARNING, INFO).
4.	Error Handling: Include robust error handling for cases like invalid line numbers, non-existent lines, or incorrect input formats.

#### Example Input and Output

events.txt
```
INFO - System initialized successfully.
INFO - Starting process A.
ERROR - Unable to establish a database connection.
WARNING - Disk space low on server.
INFO - User login successful.
ERROR - Network timeout while accessing resource.
INFO - File upload completed.
WARNING - High memory usage detected.
ERROR - File not found.
INFO - Scheduled maintenance starting.
WARNING - Deprecated API usage detected.
ERROR - Failed to save file.
INFO - Backup process completed.
INFO - New user registered.
WARNING - SSL certificate expired.
ERROR - Unauthorized access attempt detected.
INFO - Email sent successfully.
WARNING - Low battery on device.
ERROR - Critical process failure.
INFO - System shutdown initiated.
```

Input: “Enter line numbers or ranges (e.g., 1-5, 8, 12-15): 1-3, 5, 10-12”


Output in output.txt:
```
Line 1: INFO - Starting process...
Line 2: ERROR - Connection failed.
Line 3: WARNING - Low memory.
Line 5: INFO - Process resumed.
Line 10: ERROR - Timeout occurred.
Line 11: INFO - Operation successful.
Line 12: WARNING - Deprecated method used.

Summary of Events:
- INFO: 3
- ERROR: 2
- WARNING: 2
```

#### Hints / Addl. learning (optional)

Use regular expressions (`import re`) to make code simpler if you know what pattern to search for in a string (with or without newlines) <br>
Learn regex @ https://regexlearn.com/learn/regex101<br>
Try regex online @ https://regex101.com/

These are essential tools in programming and data processing due to their power and flexibility in text manipulation. I'd suggest you try to learn this.

#### Example:
In events file, you know that the first part of each newline is the event type. You can use regex to read all event types. This is not a good regex though because these words may also appear in other parts of the line too, not just beginning (eg: change `ERROR - File not found.` to `ERROR - File not found ERROR.`. Think of a good regex pattern that works properly in all cases.
```
# Define the regex pattern for event types; search for 3 words you know will exists in file; \b stands for word boundary 
pattern = r'\b(INFO|WARNING|ERROR)\b'

# find all matches in the string
match = re.findall(pattern, str)
print(match)
```
