import matplolib.pyplot as plt
import numpy
import seaborn as sns
import pandas as pd



def cummulative_cdf(data, ax=None, x_label=None, legend_label=None, linestyle='-', color=None):
    if x_label:
        data = data.rename(x_label)
    ax = sns.distplot(data, bins=10000,
                      hist_kws=dict(cumulative=True, density=True, histtype='step', alpha=1, linestyle=linestyle),
                      kde=False, color=color, ax=ax, label=legend_label)
    ax.set_ylim(0, 1)
    ax.ylabel = 'occurence'
    # fix vertical line at end
    # from https://stackoverflow.com/a/52921726/9072188

    axpolygons = [poly for poly in ax.get_children() if isinstance(poly, mpl.patches.Polygon)]
    for poly in axpolygons:
        poly.set_xy(poly.get_xy()[:-1])



def non_cumulative_cdf(data, label_fontsize = 10, x_label = None ):
	# data should be a pandas series
	# label should be a string (f.e. column name of data ( pandas series))
    
	plt.ylabel( 'occurence', fontsize = label_fontsize)
	plt.plot(np.sort(data),np.linspace(0,1,len(data)),label = label)
    	if x_label:
        	plt.xlabel( x_label, fontsize = label_fontsize)



def histplot(data, nbins = 100, label_fontsize = 10 ,x_label = None):

	# data should be a pandas series
	# label, unit as string
	
	plt.hist(data, bins = nbins)
	plt.ylabel( 'occurence', fontsize = label_fontsize)
	if x_label:
		plt.xlabel(x_label, fontsize = label_fontsize)

def statistics(data, unit):
    mu = df.mean()
    median = np.median(df)
    sigma = df.std()
    maximum = round(max(df),6)
    minimum = round(min(df),6)
    return '\n'.join((
            f'mean = {round(mu,2) } {unit}',
            f'median = {round(median,2)} {unit}',
            f'standard deviation = {round(sigma,2)} {unit}',
            f'max = {maximum} {unit}' ,
            f'min = {minimum} {unit}'))

def addstatstoplot(data, unit, fontsize = 10):
	
	props = dict(boxstyle = 'round', facecolor = 'white', alpha = 0.35)
	plt.text(plt.axis()[1] * 0.7, plt.axis()[3] * 0.7, statistics(data, unit), fontsize=fontsize,
            verticalalignment='top', bbox=props)
