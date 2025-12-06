import pandas as pd
import sys as sys
dataFrameHousing = pd.read_csv("feature_engg/housing_data.csv")

def iqr_method(group):
    """Return both lower and upper bounds as named columns"""
    q1 = group.quantile(0.25)
    q3 = group.quantile(0.75)

    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return pd.Series({
        "pps_lower_iqr_cb": lower,
        "pps_upper_iqr_cb": upper
    })

def detect_and_print_outliers_using_price(dataFrameHousing):
    outliers_by_price_series = iqr_method(dataFrameHousing["price"])
    #print(outliers_by_price_series)

    outliers_by_price = dataFrameHousing[
        (dataFrameHousing["price"] < outliers_by_price_series["pps_lower_iqr_cb"])
        | (dataFrameHousing["price"] > outliers_by_price_series["pps_upper_iqr_cb"])
    ]

    print("\n\n")
    print("** Number of outliers detected:", outliers_by_price.shape[0])
    print("\n *******  **  Outliers: **  ******* \n")
    print(outliers_by_price)

def detect_and_print_outliers_using_price_per_sqft(dataFrameHousing):

# Add a derived column (price_per_sqft) to dataFrameHousing for better understanding of outliers
    dataFrameHousing["price_per_sqft"] = dataFrameHousing["price"] / dataFrameHousing["size_sqft"]

    outliers_by_ppsqft_series = iqr_method(dataFrameHousing["price_per_sqft"])
    #print(" *** *** *** *** Outlier bounds for price_per_sqft using IQR method: *** *** *** *** ")
    #print(outliers_by_ppsqft_series)

    outliers_by_ppsqft = dataFrameHousing[
        (dataFrameHousing["price_per_sqft"] < outliers_by_ppsqft_series["pps_lower_iqr_cb"])
        | (dataFrameHousing["price_per_sqft"] > outliers_by_ppsqft_series["pps_upper_iqr_cb"])
    ]
    print("\n\n")
    print("** Number of outliers detected:", outliers_by_ppsqft.shape[0])
    print("\n *******  **  Outliers: **  ******* \n")
    print(outliers_by_ppsqft)

def detect_and_print_outliers_using_multiple_features_grouped(dataFrameHousing):
    
    # Add a derived column (price_per_sqft) to dataFrameHousing for better understanding of outliers
    dataFrameHousing["price_per_sqft"] = dataFrameHousing["price"] / dataFrameHousing["size_sqft"]
    
    #Group by City, price_per_sqft and bedrooms
    bounds = dataFrameHousing.groupby(["city", "bedrooms"])["price_per_sqft"].apply(iqr_method).reset_index()

    bounds = bounds.pivot(index=["city", "bedrooms"], columns="level_2", values="price_per_sqft").reset_index()

    bounds.columns.name = None
    bounds = bounds.rename(columns={"lower": "pps_lower_iqr_cb", "upper": "pps_upper_iqr_cb"})

    dataFrameHousing = dataFrameHousing.merge(bounds, on=["city", "bedrooms"], how="left")
    
    outliers_multiple_features = dataFrameHousing[
        (dataFrameHousing["price_per_sqft"] < dataFrameHousing["pps_lower_iqr_cb"])
        | (dataFrameHousing["price_per_sqft"] > dataFrameHousing["pps_upper_iqr_cb"])
    ]

    print("\n\n")
    print("** Number of outliers detected:", outliers_multiple_features.shape[0])
    print("\n *******  **  Outliers: **  ******* \n")
    print(outliers_multiple_features)

#In main function use supplied parameter to  decide which IQR function to call
def main(IQRmethodToUse = None):
    if dataFrameHousing.empty:
        print("DataFrame is empty. Exiting.")
        return
    if dataFrameHousing.isnull().values.any():
        print("DataFrame contains null values. Please clean the data before proceeding.")
        return
    if not all(col in dataFrameHousing.columns for col in ["price", "size_sqft", "city", "bedrooms"]):
        print("DataFrame does not contain required columns. Please check the data.")
        return
    if IQRmethodToUse == "price":
        detect_and_print_outliers_using_price(dataFrameHousing)

    elif IQRmethodToUse == "price_per_sqft":
        detect_and_print_outliers_using_price_per_sqft(dataFrameHousing)
    
    elif IQRmethodToUse == "multiple_features":
        detect_and_print_outliers_using_multiple_features_grouped(dataFrameHousing)
    
    elif IQRmethodToUse == "":
        print("No valid IQR method specified. Please choose from 'price', 'price_per_sqft', or 'multiple_features'.")
        print("For IQRMethodToUse parameter, you can pass 'price', 'price_per_sqft', or 'multiple_features'.")
        print("Example: from command line: python IQRMethodForOutliershousing.py price_per_sqft or " \
        "for multiple features python IQRMethodForOutliershousing.py multiple_features")
        return

if __name__ == "__main__":
    main()
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()