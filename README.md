# TimeGlide

TimeGlide is a floating clock widget application built with Python and Tkinter. It displays the local time, date, and a calendar, and allows users to change the background color, transparency, and time zone.

![Screenshot](Screenshot%20from%202024-11-03%2014-36-52.png)

## Features

- Displays local time and date
- Shows the current month's calendar
- Allows changing the background color
- Adjustable transparency
- Selectable time zone
- Draggable widget

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `pytz` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/moticob/TimeGlide.git
    cd TimeGlide
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Removing the Application

To remove the application entry for the Floating Clock Widget that you created using the `.desktop` file, you simply need to delete the corresponding `.desktop` file from the `~/.local/share/applications/` directory. You can use the following command in your terminal:

```bash
rm ~/.local/share/applications/floating_clock.desktop
```

### Explanation:
- **`rm`**: This command is used to remove files.
- **`~/.local/share/applications/floating_clock.desktop`**: This is the path to the `.desktop` file you want to delete.

### Additional Note:
If you also want to remove any associated files or directories related to the application (like the Python script or icons), you would need to delete those separately, using commands like:

```bash
rm 

floating_widget.py


rm 

Tim.png


```

Be cautious with the `rm` command, as it will permanently delete the specified files without prompting for confirmation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
