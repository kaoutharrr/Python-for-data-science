# DataTable Learning Guide 📊

A comprehensive educational guide to master data manipulation and visualization for the Python DataTable project.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Core Concepts to Master](#core-concepts-to-master)
- [Exercise Breakdown](#exercise-breakdown)
- [Learning Path](#learning-path)
- [Key Skills Required](#key-skills-required)
- [Common Pitfalls](#common-pitfalls)

## 🎯 Project Overview

This project teaches three fundamental data science skills:

1. **Loading and validating datasets** from CSV files
2. **Visualizing time-series data** with line plots
3. **Exploring correlations** between different datasets

**Dataset Source:** Gapminder.org (CC-BY License)
- Life expectancy by country and year
- Population data by country and year
- GDP per capita (PPP adjusted) by country and year

**Learning Goals:**
- Understand tabular data structures
- Master data loading with error handling
- Create meaningful visualizations
- Identify patterns and correlations in real-world data

## 📚 Prerequisites

### Environment Requirements

**Python Version:** Must use Python 3.10

**Required Libraries:**
- **pandas**: For data manipulation and CSV handling
- **matplotlib**: For creating plots and visualizations
- **seaborn**: Alternative visualization library (optional)
- **flake8**: For code quality checking

### Project Structure Standards

**Every Python file must follow this pattern:**
- Main function containing all logic
- Conditional execution using `if __name__ == "__main__"`
- No code in the global scope
- All functions must have documentation strings
- All exceptions must be caught and handled

**Code Quality Requirements:**
- Use flake8 for linting (alias as `norminette`)
- Explicit imports only (no wildcard imports like `from pandas import *`)
- No global variables allowed
- Functions should not crash unexpectedly

## 🧠 Core Concepts to Master

### 1. Understanding DataFrames

**What is a DataFrame?**
A two-dimensional labeled data structure similar to a spreadsheet or database table. It has:
- Rows representing individual records
- Columns representing different attributes
- Labels for both rows and columns
- Each column can have a different data type

**Key Properties:**
- **Shape**: The dimensions (number of rows, number of columns)
- **Columns**: Names of each column
- **Index**: Row labels (can be numeric or named)
- **Data types**: Each column has a specific type (integer, float, string, etc.)

**Essential Operations:**
- Reading from CSV files
- Viewing structure and dimensions
- Selecting specific rows or columns
- Filtering data based on conditions
- Handling missing or invalid data

### 2. CSV File Handling

**What You Need to Know:**
- CSV (Comma-Separated Values) format structure
- How to validate file paths
- Different types of errors that can occur when loading files
- How to handle malformed data
- Reading CSV into DataFrame structures

**Common Challenges:**
- File not found or incorrect path
- Empty or corrupted files
- Incorrect file format
- Encoding issues
- Missing values in data

### 3. Data Visualization Principles

**Line Plots:**
- Best for showing trends over time
- X-axis typically represents time (years)
- Y-axis represents the measured value
- Multiple lines can show comparisons

**Scatter Plots:**
- Show relationship between two variables
- Each point represents one observation
- Useful for identifying correlations
- Patterns indicate relationships

**Essential Elements of Good Plots:**
- **Title**: Clear description of what's shown
- **Axis Labels**: What each axis represents (with units)
- **Legend**: Identifies different data series
- **Scale**: Appropriate range for the data
- **Readability**: Clear fonts, colors, and sizing

### 4. Data Type Conversion

**Understanding Numeric Representations:**

**Suffixes in Large Numbers:**
Population data often uses abbreviations:
- K = Thousand (1,000)
- M = Million (1,000,000)
- B = Billion (1,000,000,000)

Example: "5.2M" means 5,200,000 people

**Why This Matters:**
- These strings cannot be used for mathematical operations
- Must be converted to actual numbers
- Need to handle the conversion carefully to avoid errors

**Year Columns as Data:**
The CSV files have years as column names (1800, 1801, etc.)
- These need to be treated as data points, not just labels
- You may need to extract and use them as numeric values
- Understanding the data structure is crucial

## 📝 Exercise Breakdown

### Exercise 00: Load My Dataset

**Learning Objectives:**
- File path validation and error handling
- Reading CSV files into DataFrames
- Extracting and displaying dimensions
- Returning appropriate values or None on failure

**What Makes This Exercise Challenging:**
- Must handle multiple error scenarios gracefully
- Need to understand function return types
- Should print dimensions in specific format
- Must validate data loaded correctly

**Skills Developed:**
- Defensive programming
- Error handling strategies
- Type hints and annotations
- Function design patterns

### Exercise 01: Draw My Country

**Learning Objectives:**
- Filtering data for specific countries
- Extracting time-series data (years and values)
- Creating line plots with proper formatting
- Adding titles, labels, and legends

**What Makes This Exercise Challenging:**
- Data is organized with years as columns
- Need to understand how to extract and plot this structure
- Must make the plot readable and informative
- Campus country may vary by student

**Skills Developed:**
- Data selection and filtering
- Time-series visualization
- Plot customization
- Understanding data orientation

**Key Insight:**
You're visualizing how one country's life expectancy changed from 1800 to 2100 (historical and projected data)

### Exercise 02: Compare My Country

**Learning Objectives:**
- Loading and manipulating population data
- Comparing multiple countries on one plot
- Handling data with special formatting (M, B suffixes)
- Restricting display to specific year ranges

**What Makes This Exercise Challenging:**
- Population values may have suffix notation (5.2M, 1.3B)
- Must convert these to actual numbers for plotting
- Need to plot multiple lines with different colors/styles
- Limited to years 1800-2050 only

**Skills Developed:**
- String parsing and conversion
- Multi-line plotting
- Data transformation
- Legend management for multiple series

**Key Insight:**
Comparing population growth patterns reveals different demographic trends between countries

### Exercise 03: Draw My Year

**Learning Objectives:**
- Loading multiple related datasets
- Extracting data for a specific year (1900) across all countries
- Creating scatter plots to show correlations
- Understanding relationship between two variables

**What Makes This Exercise Challenging:**
- Working with two different CSV files simultaneously
- Need to align data from both files by country
- Creating a scatter plot (different from line plots)
- Interpreting the correlation visually

**Skills Developed:**
- Multi-dataset operations
- Data alignment and merging concepts
- Scatter plot creation
- Correlation analysis

**Key Question to Answer:**
Does higher GDP per capita correlate with longer life expectancy? This is a fundamental question in development economics.

## 🛣️ Learning Path

### Phase 1: Python Fundamentals Review
- Function definitions and docstrings
- Type hints and annotations
- Exception handling (try/except blocks)
- File I/O operations
- Main function pattern

### Phase 2: Pandas Basics
- DataFrame structure and properties
- Reading CSV files
- Selecting rows and columns
- Filtering data by conditions
- Understanding data types
- Handling missing values

### Phase 3: Data Manipulation
- Extracting specific columns
- Converting between data types
- Parsing string formats to numbers
- Working with year-based columns
- Reshaping data as needed

### Phase 4: Matplotlib Fundamentals
- Creating figures and axes
- Line plots for time series
- Scatter plots for correlations
- Adding titles, labels, and legends
- Customizing colors and styles
- Displaying and saving plots

### Phase 5: Integration
- Combining data loading and visualization
- Error handling throughout pipeline
- Creating reusable functions
- Building complete programs

## 🎯 Key Skills Required

### 1. Error Handling Strategy
- Anticipate what can go wrong
- Use try-except blocks appropriately
- Return meaningful error indicators (None, error messages)
- Don't let programs crash unexpectedly

### 2. Data Structure Understanding
- Know how your data is organized
- Understand row vs column orientation
- Recognize when data needs transformation
- Plan your approach before coding

### 3. Visualization Design
- Think about what story your plot tells
- Make plots self-explanatory
- Use appropriate plot types for your data
- Ensure readability and clarity

### 4. Code Organization
- Separate concerns (loading, processing, visualization)
- Reuse functions across exercises
- Keep functions focused on single tasks
- Document your intentions

### 5. Debugging Approach
- Print data shapes and types frequently
- Verify data at each step
- Test with small subsets first
- Check edge cases

## ⚠️ Common Pitfalls

### Data Loading Issues
- **Not handling file paths correctly**: Always validate paths exist
- **Ignoring file format errors**: CSV might be malformed
- **Forgetting to return None on error**: Must handle failures gracefully
- **Not checking data dimensions**: Verify loaded data makes sense

### Data Manipulation Mistakes
- **Assuming data types**: Always check what type your data is
- **Not handling special characters**: M and B suffixes need conversion
- **Forgetting about missing values**: Data might have gaps
- **Wrong data selection**: Understand loc vs iloc, rows vs columns

### Visualization Problems
- **Missing labels or titles**: Makes plots meaningless
- **Wrong plot type**: Line vs scatter matters
- **Unreadable legends**: Too many items or poor placement
- **Incorrect axis ranges**: Data might be cut off or too sparse
- **Not showing the plot**: Remember to display it

### Code Quality Issues
- **Code in global scope**: Everything must be in functions
- **Missing docstrings**: All functions need documentation
- **Wildcard imports**: Must use explicit imports
- **Uncaught exceptions**: Will invalidate your exercise
- **Not following flake8**: Code must pass linting

### Conceptual Misunderstandings
- **Not understanding the data structure**: Years as columns is unusual
- **Mixing up rows and columns**: Common when filtering
- **Ignoring year ranges**: Exercise 02 specifies 1800-2050
- **Wrong year selection**: Exercise 03 requires year 1900 specifically

## 📖 Recommended Learning Resources

### Official Documentation
- **Pandas Documentation**: Complete guide to DataFrame operations
- **Matplotlib Documentation**: All plotting functions explained
- **Python Exception Handling**: Understanding try/except patterns

### Key Topics to Study
- DataFrame indexing and selection
- CSV file I/O in Python
- Matplotlib pyplot interface
- Type conversion and parsing
- Error handling best practices

### Practice Suggestions
- Explore the Gapminder datasets manually first
- Try loading and viewing data in interactive Python
- Experiment with different plot styles
- Practice filtering data by various criteria
- Test your error handling with bad inputs

## 🎓 Assessment Criteria

Your work will be evaluated on:
- **Functionality**: Does it work as specified?
- **Error Handling**: Does it handle errors gracefully?
- **Code Quality**: Does it pass flake8?
- **Documentation**: Are functions documented?
- **Structure**: Follows required patterns?
- **Visualization**: Clear and properly labeled?

## 💡 Final Tips

- **Start with Exercise 00 and perfect it**: It's reused in all other exercises
- **Test with different countries**: Make sure it works generically
- **Verify your plots visually**: Do they make sense?
- **Read error messages carefully**: They tell you what's wrong
- **Don't rush**: Understanding is more important than speed
- **Ask "why" not just "how"**: Understand the concepts, not just the syntax

Good luck with your data science journey! 🚀
