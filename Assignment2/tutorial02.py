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
        return mean_value
    else:
        return 0

def sorting(first_list): 
    n = len(first_list)  
    for i in range(n-1):  
        for j in range(0, n-i-1): 
            if first_list[j] > first_list[j+1] : 
                first_list[j], first_list[j+1] = first_list[j+1], first_list[j] 
     

# Function to compute median. You cant use Python functions
def median(first_list):
    if(check_list(first_list)):
        new_list = list(first_list)
        sorting(new_list)
        n= len(first_list)
        if n%2==0:
            median_value = new_list[n/2-1]+new_list[n/2]
        else:
            median_value = new_list[n//2]
            return median_value
    else:
        return 0



# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    if(check_list(first_list)):
        n = len(first_list)
        m1 = mean(first_list)
        sum = 0
        for x in first_list:
            sum += (x-m1)*(x-m1)
        standard_deviation_value = math.sqrt(sum/n)
        return standard_deviation_value
    else:
        return 0


# Function to compute variance. You cant use Python functions
def variance(first_list):
    if(check_list(first_list)):
        variance_value = standard_deviation(first_list)**2
        return variance_value
    else:
        return 0



# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    return nse_value

# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    return skewness_value

    
# def sorting(first_list):
#     # Sorting Logic
#     return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    return kurtosis_value
     


# Function to compute sum. You cant use Python functions
def summation(first_list):
    return summation_value
        
