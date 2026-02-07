# MODULE 1 - Introduction to Data Science and Statistical Thinking


## Data Science Terminology

- **Data Science** - The science of using technology and statistical analysis to derive value from data.

- **Data** - Observations gathered, with context (Who, What, Where, When, Why & How).

- **Data Scientist** - A person who is curious, logical & ehtical who does data science

  - Perform statistical analysis
  
  - Programmatically build predictive models

  - Manage systems created and content used

- **People who help data scientists** - Data Engineer (builds tools, no analysis), Data Analyst (analysis, no modelling), Business Analyst (understands specific needs)

- **Predictive Modeling** - Using historical data, statistical algorithms, and machine learning to identify patterns and forecast future outcomes or behaviors

- **Data Governance** - Security, Ethics, Privacy. How do we make sure we don't hurt people and protect out participants. Data integrity.

**Other terms:**

- Data Set, Data Wrangling, Data Modeling, Data Mining, Data Visualization, Big Data, Machine Learning, Primary Data, Secondary Data, Big Data

### Types of Data

- `Nominal Data` - Labeling data, such as gender, or yes/no.

- `Ordinal Data` - Non-numeric rankable data, such as a pain scale.

- `Interval Data` - Numerica values that are equidistant from each other.

- `Ratio Data` - Data that can be combared, such as 5 boys verse 9 girls.


## Statistical Thinking

- **Statistics** - The science of collecting, organizing, summarizing & analyzing data to answer questions and/or draw conclusions.

### Types of Statistics:

- **Descriptive Statistics** - Used to summarize data.

- **Inferential Statistics** - Use to infer an answer, or determin relationships.

- **Beware misleading stats!**

### Statistical Terminology

- **Population** - An entire set of interest, i.e. all domestic cats.

- **Sample** - A subets of the population that is preferably collected randomly.

- **Distribution** - The entire range of values in a data set and their frequency, generally will look like a bell, or 'normal distribution'.

### Central Tendency 

- One of many values that describes the center of a data set.

- This isuseful point to quickly tell the story of the data.

- When data is normalized, the value at the 95th percentile is helpful because `2 * sigma == standard_deviation`.

- **The Confidence Interval** is `2 * sigma`.


## 3 Ways to Use Central Tendency:

1. **Mean** (`μ`, mu) --> The average.

    - Sample Mean (`x̅`, 'x-bar') --> Mathmatical symbol when using a sample of a population.

    - Good for nominal data, outliers are fine. How many of a gender? How many people choose Pepsi over Moxie?

    - The **Standard Deviation** is the average distance from the Mean of each value.

3. **Median** --> Value at the 50th percentile, 'the number in the middle'.

    - Good for interval and ratio data that is not excessively skewed. Most commonly used. What is the average salary?

4. **Mode** --> Value or values that occurs most frequently, A Bimodal Distribution may indicate the need to split data further

    - Good for nominal data, outliers are fine. How many of a gender? How many people choose Pepsi over Moxie?

### **ASSOCIATED FORMULA**

> list = [1, 2, 3, 4]

> n = len(list)

> mean = sum(list) / n

> sample_n = n - 1

> sample_mean = sum(list) / sample_n


## Standard Deviation and Variance

- **Variation** - Differences or changes in an item.

- Stastics analyze ranges and changes, such as **the spread of data**.

- Without seeing this spread, values like `mean` mean nothing as it lacks context.

- This spread is analyized with `Standard Deviation` and `Variance`.

- **The Empirical Rule**, aka the 68-95-99.7 Rule, relates to a unimodal normal distrubution.

  - 1-sigma = 68% of data falls between -1 * SD and 1 * SD

  - 2-sigma = 95% of data falls between -2 * SD and 2 * SD

  - 3-sigma = 97.9% of data falls between -3 * SD and 3 * SD

  - 2-sigma is also know as **The Confidence Interval**

- Using the **Z-Score** you can describe the location of a raw value in relation to the mean and standard deviation.

  - This can tell you where on the x-axis the value may land (positive or negative).

  - Used to transform data to a Standard Normal Distribution when there is variation in the sigma values. When normalized the center, or `Mood` becomes 0 (zero) and sigma becomes 1 (one).

### **ASSOCIATED FORMULA**

> summation = sum([x - mean for x in list])

> sample_summation = sum([y - sample_mean for y in list])

> standard_deviation = ((1 / n) * (summation ** 2)) ** 1/2

> sample_standard_deviation = ((1 / sample_n) * (sampled_summation ** 2)) ** 1/2

> sigma = (val_at_95th_percentile - mean) / 2

**OR**

> sigma = standard_deviation / 2

> variance = standard_deviation ** 2

> sample_variance = sample_standard_deviation ** 2

> z_score = (known_value - mean) / sigma  <!-- When data is normalized -->


## Distibution Types

- The *Standard Normal Distrubition* curve is also know as the **z-Distribution**, or **t-Distrubution** for a sample.

- **z-Distribution** - Standard Normal Distribution

- **t-Distribution** - Normalized Distribution of Sample, typically a wider and 'flatter' curve. Moves the confidence interval. Good for small sample sizes.

### When To Use Population, or Sample, Formula?

`Is *sigma*, or *SD*, available?`

  - Yes - Use z-Distribution

  - No - Estimate *sigma* and use t-Distribution

`Is Sample Size >= 30?`

  - Yes - Use z-Distribution

  - No - Use t-Distribution


## Covariance

- **Covariance** is the measure of the linear relationship between two variables.

- The covariance answers the questions, *Does a relationship exist?*

- The numeric value for covariance is insignificant, but **the polarity (pos or neg) is what is import**.

- For instance, a negative covariance means there is a linear relationship that is trending downward.

- If the value is close to zero, then a relationship does not exist.

- Covariance gives no indication about the strength of a relationship.

### **ASSOCIATED FORMULA**

> x_axis_summation = sum([x - mean for x in x_axis_list])

> y_axis_summation = sum([y - mean for y in y_axis_list])

> covariance = (x_axis_summation)(y_axis_summation)/n


## Correlation

- **Correlation** is the *STRENGTH* of a relationship between two variables.

- **Pearson Correlation Coefficient**, aka *Pearson r* or little r, will be between -1 and 1, where 1 +-1 is a strong correlation and near 0 is low correlation.

- For instance, where X goes up and Y goes down, the r value will be near -1.

- **Correlation does NOT mean causation!** A relation may feel strong, but as a scientist you must accept the numbers & adjust your hypothesis as needed.

### **ASSOCIATED FORMULA**

> *r* = covariance / (x_standard_deviation * y_standard_deviation)