def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    
    if num_followers == 0:
        return 0
    
    average_audience_followers = sum(audiences_followers) / num_followers

    return average_audience_followers * (num_followers ** 1.2)