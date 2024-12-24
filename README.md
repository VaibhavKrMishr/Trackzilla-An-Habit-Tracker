# Trackzilla: An Habit Tracker

Trackzilla is a desktop application written in Python using the Tkinter library. It helps users track their habits, mark progress, and visualize streaks on a calendar. The application is designed to be user-friendly and lightweight, packaged as an executable file, so no additional installations are required.

##Note
Its my CS50 Final Project.

## Features

- **Add Habits**: Easily add new habits to track.
- **Mark Progress**: Mark habits as completed for the day.
- **Streak Tracking**: Automatically track streaks for each habit.
- **Calendar View**: Visualize progress with a calendar highlighting completed days.
- **Delete Habits**: Remove habits when they are no longer needed.
- **Data Persistence**: Saves your habits and progress locally to "habits.txt".

## How It Works

1. Launch the application.
2. Add a new habit using the input box and the "Add Habit" button.
3. Each habit appears in a scrollable list.
4. Use the "Done" button to mark the habit as completed for the day.
5. View your progress on a calendar next to each habit.
6. Use the "Delete" button to remove a habit.

## Interface

The application has an intuitive and clean interface:

- **Header**: Input field to add new habits.
- **Habit List**: Displays all tracked habits with options to mark progress and delete.
- **Calendar**: Highlights days with completed habits in green.

## Installation

Trackzilla is distributed as a standalone executable. You do not need Python or any external libraries to run it.

1. Download the executable file.
2. Double-click the executable to start the application.
3. All data will be saved locally in the same directory as the application.

## How to Use

- **Adding Habits**: Type the name of the habit in the input box and press Enter or click the "Add Habit" button.
- **Marking Progress**: Click the "Done" button next to a habit to mark it as completed for the current day.
- **Deleting Habits**: Use the "Delete" button next to a habit to remove it.
- **Viewing Progress**: Check the calendar to see which days have been marked as completed (highlighted in green).

## Requirements

- Windows, macOS, or Linux.
- No additional software or libraries are required as the executable includes all dependencies.

## Development

### Code Overview

Trackzilla is built using the following:

- **Python**: Core programming language.
- **Tkinter**: Used for building the GUI.
- **Calendar and Datetime Libraries**: For managing dates and generating calendars.

### Core Functionalities

- **Habit Management**: Add, delete, and update habits.
- **Progress Tracking**: Update streaks and mark completion.
- **Calendar Visualization**: Display completed days for habits.
- **Data Persistence**: Stores habits and progress in a `habits.txt` file.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions, feedback, or issues, feel free to contact me via my GitHub: [@vaibhavkrmishr](https://github.com/vaibhavkrmishr).

