import os
import datetime
import random
import psutil

def open_application(app_name):
    """Opens system applications based on user input."""
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "command prompt": "cmd.exe",
        "file explorer": "explorer.exe",
        "chrome": "start chrome",
        "task manager": "taskmgr"
    }

    if app_name in apps:
        os.system(apps[app_name])
        print(f"Assistant: Opening {app_name.capitalize()}...")
    else:
        print("Assistant: Sorry, I can't find that application.")

def manage_files(action, filename):
    """Handles file creation and deletion based on user input."""
    if action == "create":
        with open(filename, "w") as f:
            f.write("Hello! This is a new file.")
        print(f"Assistant: File '{filename}' created successfully.")
    elif action == "delete":
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Assistant: File '{filename}' deleted.")
        else:
            print("Assistant: File not found.")
    else:
        print("Assistant: Invalid file command.")

def perform_calculation(expression):
    """Performs basic math calculations based on user input."""
    try:
        result = eval(expression)
        print(f"Assistant: Result is {result}")
    except:
        print("Assistant: Invalid math expression.")

def check_system_status():
    """Checks battery and CPU usage."""
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else "N/A"
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Assistant: 🔋 Battery: {battery_percent}% | 💻 CPU Usage: {cpu_usage}%")

def tell_joke():
    """Tells a random joke."""
    jokes = [
        "Why did the computer go to therapy? It had too many bugs! 😂",
        "Why was the math book sad? It had too many problems! 🤣"
    ]
    print("Assistant:", random.choice(jokes))

def motivate():
    """Gives a motivational quote."""
    quotes = [
        "Success is not final, failure is not fatal: it is the courage to continue that counts. 💪",
        "Believe in yourself! Every expert was once a beginner. 🚀"
    ]
    print("Assistant:", random.choice(quotes))

def check_time_or_date(query):
    """Checks the current time or date based on user request."""
    if "time" in query:
        print("Assistant: The current time is", datetime.datetime.now().strftime("%H:%M ⏰"))
    elif "date" in query:
        print("Assistant: Today's date is", datetime.datetime.now().strftime("%Y-%m-%d 📅"))

def assistant():
    """Main function to run the chatbot."""
    print("Assistant: Hello! How can I assist you today? 😊 (Type 'exit' to stop)")

    while True:
        user_input = input("You: ").lower()

        # Check for exit command
        if user_input in ["exit", "bye", "quit"]:
            print("Assistant: Goodbye! Have a great day! 👋")
            break

        # Open applications
        elif "open" in user_input:
            app_name = user_input.replace("open ", "").strip()
            open_application(app_name)

        # File management
        elif "create file" in user_input:
            filename = user_input.replace("create file ", "").strip()
            manage_files("create", filename)
        elif "delete file" in user_input:
            filename = user_input.replace("delete file ", "").strip()
            manage_files("delete", filename)

        # Math calculations
        elif any(op in user_input for op in ["+", "-", "*", "/"]):
            perform_calculation(user_input)

        # Check system status
        elif "check battery" in user_input or "check system" in user_input or "cpu usage" in user_input:
            check_system_status()

        # Tell a joke
        elif "joke" in user_input:
            tell_joke()

        # Motivate
        elif "motivate" in user_input:
            motivate()

        # Check time or date
        elif "time" in user_input or "date" in user_input:
            check_time_or_date(user_input)

        else:
            print("Assistant: Sorry, I don't understand that command.")

# Run the chatbot
assistant()
