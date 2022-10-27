def plot_adducts(IDs, df, metadata = None, transform = False):
    
    """Visualizes identified adducts or in-source fragments.
    A graphical tool for the visualization of correlated XIC traces identified by 
    identify_adducts(). 
    The temporal evolution of selected features is plotted to inspect correlation results 
    and adduct information. 
     
    Parameters
    ----------    
    IDs : list
          A list of IDs (indices) to select correlated features from df.
    
    df: pd.DataFrame
        A two-dimensional DataFrame containing aligned mass spectrometric features
        e.g. generated by align_spectra().
        
    metadata : pd.DataFrame, optional
               A DataFrame containing annotated metadata for the intensity Data.Frame.
               Should contain a column called "mol_formula" for annotation of the plot.
    
    transform : bool, optional
                Whether plotted intensities should be scaled by a log2 function.
    
    Returns
    -------
    Shows a 2D-scatterplot of XIC and returns it as a matplotlib.figure object for
    individual modification.
    
    See Also
    --------
    align_spectra() : For preparation of the input data.
    identify_aducts() : For identification of multiple ion species from one compound.
    matplotlib.plt : For further customization of the returned plot object
    
    """
    
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
        
    if not isinstance(IDs, list):
        raise TypeError("Argument ID should be a list of IDs.")
        
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Argument df should of instance pd.DataFrame.")  
        
    if df.isnull().values.any():
        raise ValueError("Input DataFrame contains missing values.")
        
    ##reduce input data to selected features
    dfp = df.iloc[IDs,:].transpose()                    
    dfp = dfp.reset_index(drop = True) 
    
    ##for plotting information: calculate correlation between features
    quickcorr = dfp.corr()                              
    quickcorr = quickcorr.iloc[0,:]
    quickcorr = quickcorr.round(decimals = 3).astype(str)
    quickcorr = "- R2 = " + quickcorr
    quickcorr = quickcorr.set_axis(IDs)
    
    ##no metadata: show feature ID in the plot
    if metadata is None:
        newcols = pd.DataFrame({"pre": "ID", "int": [str(x) for x in list(dfp.columns)],
                                "corr": quickcorr})
        dfp.columns = newcols[['pre', 'int', 'corr']].T.agg(' '.join)
    
    ##with metadata: show molecular formula    
    if metadata is not None:
        if 'mol_formula' not in metadata.columns:
            raise NameError("Metadata does not contain a mol_formula columns.")
        else:
            newcols = pd.DataFrame({"mf": metadata.loc[IDs, "mol_formula"], "corr": quickcorr})
            dfp.columns = newcols[['mf', 'corr']].T.agg(' '.join)    
    
    if transform == True:
        dfp = np.log2(dfp)
        
        fig =  plt.figure()
        dfp.plot()
        plt.title(f"correlation of temporal feature evolution {*IDs,}" )
        plt.xlabel('scan number')
        plt.ylabel('log2(intensity) [a.u.]')
        ax = plt.subplot()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
                  fancybox = True, shadow = True, ncol = len(IDs))
        plt.show()
        return fig
    
    
    fig =  plt.figure() 
    dfp.plot()
    plt.title(f"correlation of temporal feature evolution {*IDs,}" )
    plt.xlabel('scan number')
    plt.ylabel('intensity [a.u.]')
    ax = plt.subplot()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
              fancybox = True, shadow = True, ncol = len(IDs))
    plt.show()
    return fig