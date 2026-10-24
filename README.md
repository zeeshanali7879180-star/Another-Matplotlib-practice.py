📊 Matplotlib Axis Limits and Ticks

A beginner-friendly Python project that demonstrates how to customize axis limits and tick labels in Matplotlib.

This project explains how to control the ranges of the X-axis and Y-axis using xlim() and ylim(), and how to customize the X-axis tick labels using xticks().

It is designed to help beginners understand how to control the appearance and readability of data visualizations using Python.

✨ Features
📈 Line Plot: Create a basic line graph using monthly sales data.
↔️ X-Axis Limits: Control the minimum and maximum values displayed on the X-axis using plt.xlim().
↕️ Y-Axis Limits: Set the minimum and maximum values displayed on the Y-axis using plt.ylim().
🏷️ Custom X-Axis Labels: Replace numeric tick labels with custom labels using plt.xticks().
📊 Sales Visualization: Visualize sales data for four months.
🐍 Beginner-Friendly: Learn essential Matplotlib customization techniques.
🛠️ Technologies Used
Programming Language: Python 3
Library: Matplotlib
Visualization Type: Line Plot
📋 Requirements

To run this project, you need:

Python 3 installed on your computer.
Matplotlib installed in your Python environment.
A code editor, such as PyCharm or Visual Studio Code.
🚀 Installation and Setup
Step 1: Clone the Repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Navigate to the Project Folder
bash
cd YOUR_PROJECT_FOLDER

Step 3: Install Matplotlib
bash
pip install matplotlib

Step 4: Run the Python Program

If your Python file is named axis_customization.py, run:

bash
python axis_customization.py


Note: Replace the example repository URL, project folder, and Python filename with your actual details.

💻 Project Code
python
import matplotlib.pyplot as plt

# Monthly sales data
months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1800]

# Create a line plot
plt.plot(months, sales)

# Set X-axis limits
plt.xlim(1, 4)

# Set Y-axis limits
plt.ylim(0, 2000)

# Customize X-axis tick labels
plt.xticks([1, 2, 3, 4], ['M1', 'M2', 'M3', 'M4'])

# Display the graph
plt.show()

📊 Sample Dataset

The project uses the following monthly sales data:

Month	Sales
M1	1000
M2	1500
M3	1200
M4	1800

The line graph displays the changes in sales across four months.

📖 Matplotlib Concepts Covered
1. Creating a Line Plot

The plt.plot() function creates a line graph using the supplied X-axis and Y-axis data.

python
plt.plot(months, sales)

2. Setting X-Axis Limits

The plt.xlim() function controls the visible range of the X-axis.

python
plt.xlim(1, 4)


This sets the horizontal axis limits from 1 to 4.

3. Setting Y-Axis Limits

The plt.ylim() function controls the visible range of the Y-axis.

python
plt.ylim(0, 2000)


This sets the vertical axis limits from 0 to 2000.

4. Customizing X-Axis Tick Labels

The plt.xticks() function allows you to customize the tick positions and their displayed labels.

python
plt.xticks([1, 2, 3, 4], ['M1', 'M2', 'M3', 'M4'])


This replaces the numeric labels 1, 2, 3, and 4 with M1, M2, M3, and M4.

🎯 Learning Objectives

Through this project, I practiced:

Creating basic line plots using Matplotlib.
Understanding X-axis and Y-axis ranges.
Controlling axis limits using xlim() and ylim().
Customizing axis tick positions and labels.
Visualizing monthly sales data.
Improving the readability of charts.
🔮 Future Improvements

This project can be extended by adding:

Custom Y-axis tick labels using plt.yticks().
Chart titles and axis descriptions.
Grid lines and legends.
Different line colors, markers, and styles.
Bar charts for monthly sales comparisons.
Saving plots as image files.
Real-world datasets for practical visualization.
👨‍💻 Author

Your Name

Aspiring Python Developer | Learning Python and Data Visualization

GitHub: My GitHub Profile
📄 License

This project is created for educational purposes and to develop practical Python data visualization skills.
