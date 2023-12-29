# Competition-1

Summary:
The code processes variations of "St. Albans," and standardizes them to a consistent format. It capitalizes each word, removes periods and commas and handles a specific case ("St.Al bans") by replacing it with "St Albans." The result is a list of cleaned and standardized names.

The code takes a list of names with various formats, cleans them by standardizing capitalization and handling specific cases, and produces a new list of cleaned names. The primary tools used are string manipulation, list comprehensions, and uses: .join(), .replace() and .split() methods.

For each name in the original list (names):
    Replace the specific case "St.Al bans" with "St Albans."
    Replace periods and commas with spaces.
    Split the modified string into a list of words.
    Capitalize each word in the list.
    Join the capitalized words back into a single string.
    The result is a list of cleaned and standardized names stored in "new_names."
