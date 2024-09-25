

    # One of the first tools used to understand species is physical measurements. One such famous dataset is Fisher's Iris data set, in which Ronald Fisher examined the physical traits of 3 different species of irises, in an attempt to distinguish between them. Download the data from Canvas to address the following prompts.
    #     Combine the datasets to create a single DataFrame that contains the sample id, species, petal length, petal width, sepal length, and sepal width for each sample.
    #     Calculate the correlation between each variable for all species in thd data set (there should be a total of 6 different comparisons).
    #     Calculate the average of each variable for all species in the data set.
    #     Calculate the median of each variable for all species in the data set.
    #     Calculate the standard deviation of each variable for all species in the data set.

    # Which species of irises are most similar/are least similar? Reference your measurements in part 1 to support your positions.
# So the different species compare in a rather complex way, for petals the setosa and virginica have very similar correlations between their length and width, at .219 and .291 respectively, while the versicolor has a very different petal correlation of -.241.
# This contrasts though with the average size of the petals themselves with the setosa having the smallest petals at 1.487 by 0.251, while the virginica has the largest at 5.475 by 1.988, and the versicolor is much closer to the virginica at 4.291 by 1.346.
# The setosa's petals at least seem to be a scaled down version of the virginica that grows in a similar way, while the versicolor's petals are similar to the virginica's in size but it has its own unique petal shape.

# The correlation between the petal data and sepal data didnt seem to be very large, with only one value being over .10 which was for setosa's petal length and sepal width at -.290.
# moving on to sepal length to width correlations there's another complication, the setosa and versicolor have very similar correlations of .118 and .155 respectively, while the virginica has a very different correlation of -.528.
# I could keep comparing the sepal data but I think it's clear that it's not simple enough to just say that one species is more similar to another, however in the case of petals the setosa and virginica are similar in length-v-width-correlation but the setosa is much smaller, while the versicolor is similar in size to the virginica with a different shape.

    # Write a ReadMe file explaining the purpose of your project. Include explanations for your class design and implementation, as well as each class attribute, method, and any limitations that you added.
import pandas as pd

class C_Data:
    file1=""
    file2=""
    combined_df=pd.DataFrame()
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.combined_df= self.combine_data()
        print(self.combined_df.head())

    def combine_data(self):

        #I had to ask github how to remove the unnamed column from the files it gave this: 
        #To remove a column from a DataFrame in pandas, you can use the drop method. Here is the step-by-step plan:
# Import the pandas library.
# Load the CSV files into DataFrames.
# Use the drop method to remove the unwanted column.
# Merge the DataFrames on the sample_id column.

        df1 = pd.read_csv(self.file1,index_col=False)
        df1=df1.drop(columns=['Unnamed: 0',], errors='ignore')
        df2 = pd.read_csv(self.file2,index_col=False)
        df2=df2.drop(columns=['Unnamed: 0','species'], errors='ignore')
        combined = pd.merge(df1, df2, on='sample_id')
        return combined

    def correlation(self):
        correlation_matrix = self.combined_df.groupby("species").corr(numeric_only=True)
        return correlation_matrix
        

    def average(self):
        return self.combined_df.groupby("species").mean(numeric_only=True)

    def dfmedian(self):
        return self.combined_df.groupby("species").median(numeric_only=True)

    def standard_deviation(self):
        return self.combined_df.groupby("species").std(numeric_only=True)
    
    def StatDF(self):
        stats_df=self.combined_df.groupby('species').describe()
        
        # I had to ask github for a lot of help on how to remove the columns from the grouped data frame but I understand how it works now
        stats_df = stats_df.drop(columns=[('sepal_length', 'count'), ('sepal_length', 'min'), ('sepal_length', '25%'), ('sepal_length', '75%'), ('sepal_length', 'max'),
                                      ('sepal_width', 'count'), ('sepal_width', 'min'), ('sepal_width', '25%'), ('sepal_width', '75%'), ('sepal_width', 'max'),
                                      ('petal_length', 'count'), ('petal_length', 'min'), ('petal_length', '25%'), ('petal_length', '75%'), ('petal_length', 'max'),
                                      ('petal_width', 'count'), ('petal_width', 'min'), ('petal_width', '25%'), ('petal_width', '75%'), ('petal_width', 'max')])
        stats_df = stats_df.rename(columns={'50%': 'median'}, level=1)

        return stats_df
    

fishers_iris = C_Data('Petal_Data.csv', 'Sepal_Data.csv')
print("\nStats Data Frame\n")
print(fishers_iris.StatDF())
print("\nCorrelation Data Frame\n")
print(fishers_iris.correlation())
print("\nAverage Data Frame\n")
print(fishers_iris.average())
print("\nMedian Data Frame\n")
print(fishers_iris.dfmedian())
print("\nStandard Deviation Data Frame\n")
print(fishers_iris.standard_deviation())
