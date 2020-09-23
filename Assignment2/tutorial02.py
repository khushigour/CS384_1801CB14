# All decimal 3 places

# Function to compute mean
import math

def check_list(first_list):
    for x in first_list:
        if type(x)==str:
            return False
    return True

def mean(first_list):
    if(check_list(first_list)):
        sum = 0
        for x in first_list:
            sum += x
        mean_value = sum/len(first_list)
        return round(mean_value,2)
    else:
        return 0



# Function to compute median. You cant use Python functions
def median(first_list):



# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):



# Function to compute variance. You cant use Python functions
def variance(first_list):



# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):



# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    return summation_value
