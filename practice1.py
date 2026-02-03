
def mean_s(n):
    """

    Parameter n: a list of float numbers that represents a sample data 
    
    Returns: the arithmatic mean (average) of n (the sample data)   

    Examples: 
        mean_s([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]) returns 6.0
        mean_s([105.1, 105.2, 88.5, 84.5, 73.5]) returns 91.36  
        
    Write the code for this function using the mean formula.  
    
    Do not use statistics/math library functions or functions from other
    mported modules (i.e. pandas, numpy). 

    """
    return sum(n)/len(n)    

 
def stdev_s(n):
    """

    Parameter n: a list of float numbers that represents a sample data 
    
    Returns: the standard deviation of the sample   

    Examples: 
        stdev_s([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]) returns 3.0277
        stdev_s([105.1, 105.2, 88.5, 84.5, 73.5]) returns 13.73456 
        
    Write the code for this function using the sample standard deviation formula. 
    
    You can call other user-defined functions you created as part of this exercise.
    
    Do not use statistics/math library functions or functions from other
    mported modules (i.e. pandas, numpy).

    """
    return (1/(len(n)-1)*(sum(n)/(len(n)-1))) ** 1/2


def stdev_p(n):
    """
    Parameter n: a list of float numbers that represents a population data 
    
    Returns: the standard deviation of the population   

    Examples: 
        stdev_p([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]) returns 2.872281
        stdev_p([105.1, 105.2, 88.5, 84.5, 73.5]) returns 12.28456
        
    Write the code for this function using the population standard deviation formula. 
    
    You can call other user-defined functions you created as part of this exercise.
    
    Do not use statistics/math library functions or functions from other
    mported modules (i.e. pandas, numpy).

    """
    return (1/len(n)*(sum(n)/len(n))) ** 1/2
 


def cov_s(x,y):
    """

    Parameters x, y: lists of float numbers that represents two variables of a sample data 
    
    Returns: the covariance between variable x and y   

    Examples: 
        cov_s([1.5, 2.5, 3.5, 4.5, 5.5], [105.1, 105.2, 88.5, 84.5, 73.5]) returns -20.98
        
    Write the code for this function using the sample covariance formula. 
    
    You can call other user-defined functions you created as part of this exercise.
    
    Do not use statistics/math library functions or functions from other
    mported modules (i.e. pandas, numpy).

    """
    return (sum(x)*sum(y))/(len(x)-1)

def cov_p(x,y):
    """

    Parameters x, y: lists of float numbers that represents two variables of a population data 
    
    Returns: the covariance between variable x and y   

    Examples: 
        cov_p([1.5, 2.5, 3.5, 4.5, 5.5], [105.1, 105.2, 88.5, 84.5, 73.5]) returns -16.78
        
    Write the code for this function using the population covariance formula. 
    
    You can call other user-defined functions you created as part of this exercise.

    Do not use statistics/math library functions or functions from other
    mported modules (i.e. pandas, numpy).

    """
    return (sum(x)*sum(y))/len(x)


def corr_r(x,y):
    """
    
    Parameters x, y: lists of float numbers that represents two variables of a sample data 
    
    Returns: the Pearson R of the sample data   

    Examples: 
        corr_r([1.5, 2.5, 3.5, 4.5, 5.5], [105.1, 105.2, 88.5, 84.5, 73.5]) returns -0.96587
        
    Write the code for this function using the Pearson-R correlation formula. 
    
    You can call other user-defined functions you created as part of this exercise.

    Do not use statistics/math library functions or functions from other
    mported modules (i.e. pandas, numpy).

    """
    sOne = (1/(len(x)-1)*(sum(x)/(len(x)-1))) ** 1/2
    sTwo = (1/(len(y)-1)*(sum(y)/(len(y)-1))) ** 1/2
    return ((sum(x)*sum(y))/len(x))/((sOne*sTwo)**1/2)



