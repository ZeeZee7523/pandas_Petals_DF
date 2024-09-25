# pandas_Petals_DF
# Write a ReadMe file explaining the purpose of your project. Include explanations for your class design and implementation, as well as each class attribute, method, and any limitations that you added.
My python file created a class called C_Data for combined data, that takes 2 inputs file1 and file2. 
In the init function I call the combine_data() function in order to set the self.combined_df attribute to the combination of the 2 files as a dataframe.
In the combine_data() function I read the input files as dataframes and remove the unneeded index columns as well as removing the "species" column from the second dataframe so that it wouldnt appear twice when I merged them based on sample_id.
The correlation, average, median, and standard deviation functions are all pretty simple I just grouped the self.combined_df by species and then did the pandas operation for corresponding to the function, being sure to include numbers only so it doesnt try to compare the sample_id's.
I just made the Stat function in order to organize the mean, median, and standard deviation into one dataframe to make it more compact. I used the describe() function and then had github help me remove the columns I didnt need. I then renamed the "50%" column to "median" since that's what we called it in the questions 
