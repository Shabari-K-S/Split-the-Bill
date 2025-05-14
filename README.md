# Split the Bill

A modern, user-friendly mobile application built with Python and Flet framework that helps users split bills and calculate tips easily.

![Split the Bill App](https://raw.githubusercontent.com/Shabari-K-S/Split-the-Bill/preview.png)

## Features

- 💰 Calculate bill splits among multiple people
- 💡 Easy-to-use interface with intuitive controls
- 🎯 Support for different tip percentages (0%, 5%, 10%, 15%, 20%)
- 📱 Mobile-friendly design
- 🎨 Clean and modern UI with Roboto font

## Prerequisites

- Python 3.9 or higher
- Flet package

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Shabari-K-S/Split-the-Bill.git
    cd Split-the-Bill
    ```

2. Install the required packages:

    ```bash
    pip install flet
    ```

## Usage

Run the application using Python:

```bash
python main.py
```

The application will launch and you can:

1. Enter the bill amount
2. Select a tip percentage
3. Enter the number of people
4. View the calculated amount per person automatically

## How it Works

The application automatically calculates the total per person based on:

- The total bill amount
- Selected tip percentage
- Number of people sharing the bill

The calculation happens in real-time as you input the values.

## Project Structure

```text
Split-bill/
├── main.py           # Main application file
└── README.md         # Project documentation

```

## Acknowledgments

- Built with [Flet](https://flet.dev/) - A Python framework for building interactive multi-platform applications
- Uses Roboto font from Google Fonts
