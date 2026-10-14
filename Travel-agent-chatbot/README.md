# Travel Agent

Travel Agent is a simple interactive chatbot that helps users view sample travel packages, check destination details, and see whether a package is available.

## Features

- Displays all travel packages and their availability
- Shows destination, trip duration, and price
- Reports whether a package is currently available or unavailable
- Handles basic greetings and simple travel-related questions
- Runs in the terminal using Python

## Available Packages

| Destination | Days | Price | Status |
|-------------|------|-------|--------|
| Goa | 4 | Rs. 12000 | Available |
| Kerala | 5 | Rs. 15000 | Available |
| Manali | 6 | Rs. 18000 | Unavailable |
| Jaipur | 3 | Rs. 10000 | Available |
| Ooty | 3 | Rs. 8000 | Unavailable |

## How to Run

1. Open a terminal in the Travel-agent-chatbot folder.
2. Run the script:

   ```bash
   python travel_agent.py
   ```

3. You can type commands such as:
   - `hi` / `hello` to start a conversation
   - `all packages` to view all available destinations
   - a destination name such as `Goa` or `Kerala` to get package details
   - `exit` to stop the chatbot

## Example Interaction

```text
You: hello
Travel Agent: Hello! Where would you like to travel?

You: all packages
Available Travel Packages:
Goa - 4 days, Price: Rs. 12000 - Available
Kerala - 5 days, Price: Rs. 15000 - Available

You: Goa
--- Travel Package Details ---
Destination: Goa
Duration: 4 days
Price: Rs. 12000
Status: Package is available.
```

## Technologies Used

- Python 3
- Standard Python library only

## Notes

This project is a basic rule-based chatbot and uses predefined travel data rather than an external AI service or database.
