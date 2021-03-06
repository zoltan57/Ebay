import pandas as pd

def response_to_dataframe(response):
    results = response.dict()['searchResult']['item']

    df = pd.DataFrame()
    df['itemId'] = pd.Series([item['itemId'] for item in results])
    df['title'] = pd.Series([item['title'] for item in results])
    df['condition'] = pd.Series([item['condition']['conditionDisplayName'] for item in results])
    df['currentPrice'] = pd.Series([float(item['sellingStatus']['currentPrice']['value']) for item in results])
    df['sellingState'] = pd.Series([item['sellingStatus']['sellingState'] for item in results])
    df['bidCount'] = pd.Series([int(item['sellingStatus'].get('bidCount', 0)) for item in results])
    df['listingType'] = pd.Series([item['listingInfo']['listingType'] for item in results])
    df['bestOfferEnabled'] = pd.Series([item['listingInfo']['bestOfferEnabled'] for item in results])
    df['buyItNowAvailable'] = pd.Series([item['listingInfo']['buyItNowAvailable'] for item in results])
    df['startTime'] = pd.Series([item['listingInfo']['startTime'] for item in results])
    df['endTime'] = pd.Series([item['listingInfo']['endTime'] for item in results])
    df['watchCount'] = pd.Series([int(item['listingInfo'].get('watchCount', 0)) for item in results])
    df['location'] = pd.Series([item['location'] for item in results])
    df['postalCode'] = pd.Series([item['postalCode'] for item in results])
    df['viewItemURL'] = pd.Series([item['viewItemURL'] for item in results])

    return df
