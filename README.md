# Football-match-predictor
Predicts the outcome of a Premier league game using Machine Learning algorithm 

# Football Match Outcome Predictor

Football is loved and played by millions of people. The official governing body of football, FIFA (Federation Internationale de Football Association), estimated that there were about 260 million football players and over 1.3 billion are interested. Hence, it is only natural that people would love to speculate the outcome of upcoming matches. This project aims to predict football match outcomes using machine learning algorithms combining various datasets.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms Used](#algorithms-used)
- [Results](#results)
- [Conclusion](#conclusion)

## Introduction

Football Leagues are widely celebrated all around the world. Multiple leagues and tournaments take place simultaneously with viewers and enthusiasts keen to know the outcomes. Predicting football match outcomes using machine learning has been an interesting task for data scientists for years. This project applies machine learning to predict football match outcomes using data from the UEFA Champions League, which covers the best clubs from top leagues in the world as experimental data.

## Features

The algorithm considers multiple features obtained from the datasets to predict the outcome of a given game, eventually leading to the prediction of the tournament outcome and winners. These features include:

- Match date
- Goals
- Home and away grounds
- Fouls
- Shots
- Shots on target
- Corners
- Yellow and red cards
- Match outcome
- Team history
- Individual player stats
- Form
- Referees

## Data

The data used in this project includes English Premier league data. The dataset `epl.csv` includes attributes like match date, goals, home and away grounds, fouls, shots, shots on target, corners, yellow and red cards, match outcome, team history, individual player stats, form, and referees.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/football-match-predictor.git
    cd football-match-predictor
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have the dataset `epl.csv` in the project directory.

## Usage

1. Run the prediction script:
    ```sh
    python EPLPredictor.py
    ```

2. The script will load the dataset, preprocess it, train a random forest classifier, and print the accuracy of the model.

## Algorithms Used

In this project, we used three machine learning techniques:
1. Random Forest
2. Logistic Regression
3. Decision Tree

A detailed comparison is done between these techniques using graphs and tables, and the most suitable method is chosen.

## Results

The accuracy of the prediction model is printed at the end of the script execution. Further details on the model performance and comparisons between different algorithms can be found in the project report.

## Conclusion

This project demonstrates the application of machine learning to predict football match outcomes using historical data. The model considers various features and attributes to deliver accurate predictions. The approach can be further enhanced and utilized in professional prediction scenarios.
