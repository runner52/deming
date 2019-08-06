## What is Heming Prediction?

It is a tool that generates based on reading from an input text file:

1. slope and y-intercept of a heming regression
2. predictions based on input value 

## Requirements 
To run the package successfully you need to have the following requirements:

* Linux OS
* python 3.7

## How to execute the tool 

In your terminal run:
`pip3 install python-dateutil`

`pip3 install DateTime`

Make sure you have an input file with the following format:
>obesrvaciones

>yyyy-mm-dd hh:mm b a

>...

>predicciones

>yyyy-mm-dd hh:mm a

>...

`python3 inputFile outputFile`


# Note: 
* input file example is in 'examples/input.txt'
* output file example is in 'examples/output.txt'
* the input file observations range must not exceed 1 year, otherwise the command won't run. 
* **a**: independent variable value
* **b**: dependent variable value


The output file will have the following output format:
1. slope and y intercept values
2. Mean Absolute Error and Mean Square Error per month for the list of observations based on comparing the true values to the values obtained from the regression line
3. Predictions of output based on input value

The output file will look like this:
 
>slope y-intercept

>Month1 mae mse

>...

>yyyy-mm-dd y

# Note:
**mae**: mean absolute error

**mse**: mean square error
