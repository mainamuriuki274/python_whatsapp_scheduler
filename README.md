# CLI PYTHON WHATSAPP SCHEDULER
Python CLI project that takes a few inputs from users; to write their message, include the recipient's phone number, the date and time you want the message sent and once the time reaches it automatically sends the message.

## TASK DESCRIPTION
### WhatsApp Message Scheduler:

Build a CLI app to schedule whatsapp messages and send them automatically once the scheduled time has passed. For example, your app should prompt the user to write a message, their whatsapp number, the recipient’s number and the time they intend to have it sent out. You can save this data on an SQLite Database.

## Why Schedule Whatsapp messages?
From sending messages to people before you forget what you wanted to tell them to wishing your loved ones messages such as "Happy Birthday" and "Happy Anniversary" when the day arrives or even for businesses sending their customers important messages during working hours, scheduling saves you from the hassle of remembering and remembers for you. All you have to do is set the message, the recipient's number and the time and yout message will be delivered at that time.

## How it works
The program utilises [Twilio API for Whatsaapp](https://www.twilio.com/docs/whatsapp/quickstart/python) to **only** send messages and [Python](https://www.python.org/) 's in-built libraries like [datetime](https://docs.python.org/3/library/datetime.html) and [time](https://docs.python.org/3/library/time.html) to schedule the messages. 

## Installation and setup

1. Clone this repository to your local machine using:
    ```bash
        git clone https://github.com/mainamuriuki274/python_whatsapp_scheduler.git
      ```
2. Checkout into the main branch by using:
    ```bash 
       git checkout main
      ```
3. Create a virtualenv on your machine and activate the virtual environment
4. Install all the dependencies by using the package manager [pip](https://pip.pypa.io/en/stable/):
    ```bash
        pip install -r requirements.txt 
     ``` 
5. Navigate to the directory app using:
   ```bash
        cd app/
      ```
 6. Finally, to execute the project run:
    ```bash
        python main.py
       ```


