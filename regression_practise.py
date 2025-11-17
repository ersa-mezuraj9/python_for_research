import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# === Simple Linear Regression ===
n = 100
beta_0 = 5  # true intercept
beta_1 = 2  # true slope
np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n)  # generate random predictor values in [0, 10)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n)  # generate response with noise

# Plot the data and true regression line
plt.figure()
plt.plot(x, y, "o", ms=5)  # scatter plot of data
xx = np.array([0, 10])
plt.plot(xx, beta_0 + beta_1 * xx)  # plot true regression line
plt.show()

# Search for optimal slope by minimizing residual sum of squares (RSS)
rss = []
slopes = np.arange(-10, 15, 0.01)  # test a range of slope values
for slope in slopes:
    rss.append(np.sum((y - beta_0 - slope * x)**2))  # compute RSS for each slope

# Find and print the slope with minimum RSS
ind_min = np.argmin(rss)
print(ind_min)
print("Estimate for the slope: ", slopes[ind_min])

# Plot RSS vs slope to visualize the optimization
plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS")
plt.show()

# Fit linear regression using statsmodels (OLS = Ordinary Least Squares)
import statsmodels.api as sm
X = sm.add_constant(x)  # add intercept column
mod = sm.OLS(y, X)  # create OLS model
est = mod.fit()  # fit the model
print(est.summary())  # print detailed regression results

# Multiple Linear Regression
n = 500
beta_2 = -1  # true coefficient for second predictor
x_1 = 10 * ss.uniform.rvs(size=n)  # first predictor
x_2 = 10 * ss.uniform.rvs(size=n)  # second predictor
y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc=0, scale=1, size=n)  # response with two predictors

# Stack predictors into a design matrix
X = np.stack([x_1, x_2], axis=1)

# Plot the data in 3D
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$")

from sklearn.linear_model import LinearRegression

lm = LinearRegression(fit_intercept=True)
lm.fit(X, y)

# Make a prediction for a new sample
X_0 = np.array([2, 4])
lm.predict(X_0.reshape(1, -1))

# Train-test split and evaluate model performance
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)
lm = LinearRegression(fit_intercept=True)
lm.fit(X_train, y_train)
lm.score(X_test, y_test)