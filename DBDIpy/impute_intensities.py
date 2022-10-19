def impute_intensities(df, method = "linear"):        """    Fills NaN values contained in a DataFrame consisting of rows of aligned ion intensity.        Extracted Ion Chromatograms often are not of the same length. To generate a set of     uniform-length ion intensity series, a multi-step imputation approach is used:        I) A baseline is added for all features from the beginning to the end of the experiment.        II) Missing values within the detected signal region are interpolated.    The returned DataFrame is suitable for time series analysis or other multivariate statistics.        Parameters    ----------        df: A DataFrame containing missing (NaN) values to impute.        method: Intepolation method to be used; default is "linear".             Supported imputation methods are all methods methods from             pandas.DataFrame.interpolate() and            scipy.interpolate.interp1d().        Returns    -------    DataFrame of equal length ion intensity series without NaN.        """        import math    from tqdm import tqdm    import random    import pandas as pd        ##check if user imput is valid    if not isinstance(df, pd.DataFrame):        raise TypeError('Argument for df should be of instance pandas.DataFrame.')            if method not in ("linear", "time", "index", "pad", "nearest", "zero", "slinear",                       "quadratic", "cubic", "spline", "barycentric", "polynomial",                      "krogh", "from_derivatives"):        raise ValueError("Invalid imputation method.")            ##define function for addition of a baseline     def baselinefill():        s_min = v.min()        fill_min = s_min - s_min * 0.01        fill_max = s_min + s_min * 0.01          return round(random.uniform(fill_min, fill_max),2)        ##fill the DataFrame row by row    for i, v in tqdm(df.iterrows(), desc='progress'):                                            ##part 1: filling NaN within data region        vnotNA = v.notna()                                                   vnotNA[::1].idxmax()                                                 vnotNA[::-1].idxmax()                                              datareg = v[vnotNA[::1].idxmax():vnotNA[::-1].idxmax()]               datareg = datareg.interpolate(method = method)                                      v[vnotNA[::1].idxmax():vnotNA[::-1].idxmax()] = datareg             ##part : adding a baseline        v[v.isna()] = v[v.isna()].apply(lambda x: baselinefill() if math.isnan(x) else x)    return df