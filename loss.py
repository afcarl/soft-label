
from math import pow, log

def square_loss(yhat, ytrue):
    return pow((yhat-ytrue), 2)


def square_loss_prime(yhat, ytrue):
    return 2*yhat - ytrue



def log_loss(yhat, ytrue):
    return  -1 * ytrue * log(yhat) - (1-ytrue)*log(1-yhat)


def log_loss_prime(yhat, ytrue):
    return  (1 - ytrue )/(1-yhat) - ytrue / yhat


