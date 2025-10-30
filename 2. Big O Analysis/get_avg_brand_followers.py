def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    
    for handle in all_handles:
        for infl in handle:
            if brand_name in infl:
                count += 1
    return count / len(all_handles)