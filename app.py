import streamlit as st
import random

# Set the page configuration (MUST be the first Streamlit command)
st.set_page_config(
    page_title="Econometrics Key Terms Quiz",
    page_icon="✏️",

)

# CSS styling
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


###########
chapter_1_quiz_data = [
    {"term": "Constant or Intercept",
     "information": "The value of the dependent variable when all independent variables are zero in a regression model.",
     "options": ["Dependent Variable", "Constant or Intercept", "Residual", "Bias", "Slope Coefficient", "Independent Variable", "Stochastic Error Term"],
     "answer": "Constant or Intercept"},
    {"term": "Cross-sectional",
     "information": "Data collected from different subjects or entities at a single point in time.",
     "options": ["Time-series", "Cross-sectional", "Panel Data", "Historical Data", "Forecast Data", "Residual Data", "Multivariate Data"],
     "answer": "Cross-sectional"},
    {"term": "Dependent Variable",
     "information": "The outcome variable in a model that is influenced by independent variables.",
     "options": ["Independent Variable", "Dependent Variable", "Residual", "Constant or Intercept", "Stochastic Error Term", "Bias", "Response Variable"],
     "answer": "Dependent Variable"},
    {"term": "Estimated Regression Equation",
     "information": "A regression model with coefficients replaced by their estimated values from sample data.",
     "options": ["Regression Equation", "Estimated Regression Equation", "Multivariate Regression", "Simple Regression", "Residual Equation", "Linear Model", "Deterministic Model"],
     "answer": "Estimated Regression Equation"},
    {"term": "Expected Value",
     "information": "The mean of a random variable's probability distribution.",
     "options": ["Expected Value", "Median", "Mode", "Variance", "Sample Mean", "Weighted Mean", "Standard Deviation"],
     "answer": "Expected Value"},
    {"term": "Independent Variable",
     "information": "Variables used to explain variations in the dependent variable.",
     "options": ["Dependent Variable", "Independent Variable", "Stochastic Error Term", "Covariate", "Response Variable", "Predictor Variable", "Bias Term"],
     "answer": "Independent Variable"},
    {"term": "Linear",
     "information": "A relationship where changes in one variable are proportional to changes in another.",
     "options": ["Linear", "Non-linear", "Exponential", "Quadratic", "Logarithmic", "Polynomial", "Proportional"],
     "answer": "Linear"},
    {"term": "Multivariate Regression Model",
     "information": "A model with multiple independent variables predicting a dependent variable.",
     "options": ["Simple Regression", "Multivariate Regression Model", "Logistic Regression", "Panel Regression", "Linear Regression", "Polynomial Regression", "Bayesian Regression"],
     "answer": "Multivariate Regression Model"},
    {"term": "Regression Analysis",
     "information": "Statistical technique to estimate relationships between variables, often used to infer causality.",
     "options": ["Regression Analysis", "Correlation", "ANOVA", "Covariance Analysis", "T-Test", "Variance Analysis", "Hypothesis Testing"],
     "answer": "Regression Analysis"},
    {"term": "Residual",
     "information": "The difference between observed and predicted values of the dependent variable.",
     "options": ["Error Term", "Residual", "Bias", "Variance", "Standard Deviation", "Mean Error", "Prediction Error"],
     "answer": "Residual"},
    {"term": "Slope Coefficient",
     "information": "The rate of change in the dependent variable for a unit increase in an independent variable.",
     "options": ["Slope Coefficient", "Intercept", "Variance", "Regression Coefficient", "Partial Coefficient", "Predictor Coefficient", "Standard Coefficient"],
     "answer": "Slope Coefficient"},
    {"term": "Stochastic Error Term",
     "information": "A term accounting for random variations not captured by the model.",
     "options": ["Deterministic Term", "Stochastic Error Term", "Residual", "Bias Term", "Noise Term", "Random Term", "Prediction Error"],
     "answer": "Stochastic Error Term"}
]

chapter_2_quiz_data = [
    {"term": "Degrees of Freedom",
     "information": "Calculated as \(n - k - 1\), where \(n\) is the sample size and \(k\) is the number of predictors.",
     "options": ["Degrees of Freedom", "Sample Variance", "Predictor Degrees", "Residual Degrees", "Independent Degrees", "Model Degrees", "Error Variance"],
     "answer": "Degrees of Freedom"},
    {"term": "Estimate",
     "information": "A value calculated from data that approximates a population parameter.",
     "options": ["Estimator", "Estimate", "Prediction", "Model Output", "Parameter Approximation", "Forecast", "Sample Mean"],
     "answer": "Estimate"},
    {"term": "Estimator",
     "information": "A method for computing an estimate of a population parameter from sample data.",
     "options": ["Estimator", "Prediction Model", "Sample Statistic", "Confidence Estimator", "Regression Model", "Expected Value", "Parameter Guess"],
     "answer": "Estimator"},
    {"term": "Multivariate Regression Coefficient",
     "information": "Represents the impact of an independent variable on the dependent variable while controlling for other variables.",
     "options": ["Correlation Coefficient", "Multivariate Regression Coefficient", "Variance", "Partial Correlation", "Covariance", "Beta Coefficient", "Effect Size"],
     "answer": "Multivariate Regression Coefficient"},
    {"term": "Ordinary Least Squares (OLS)",
     "information": "A method to estimate parameters by minimizing the sum of squared residuals.",
     "options": ["OLS", "Linear Regression", "Maximum Likelihood", "Least Squares Estimation", "Bayesian Regression", "Mean Squared Estimation", "Parameter Minimization"],
     "answer": "Ordinary Least Squares (OLS)"},
    {"term": "R^2",
     "information": "Indicates the proportion of variance in the dependent variable explained by the model.",
     "options": ["R^2", "Adjusted R^2", "Variance Ratio", "Correlation Coefficient", "Explained Variance", "Model Fit", "Prediction Power"],
     "answer": "R^2"},
    {"term": "Adjusted R^2",
     "information": "A modified R^2 adjusted for the number of predictors to compare models with different numbers of predictors.",
     "options": ["R^2", "Adjusted R^2", "Residual Variance", "Fit Index", "Explained Variance", "Parameter Fit", "Model Fit"],
     "answer": "Adjusted R^2"},
    {"term": "Total, Explained, and Residual Sums of Squares",
     "information": "Components that decompose the variation in the dependent variable.",
     "options": ["Residual Sum", "Explained Variance", "Total, Explained, and Residual Sums of Squares", "Variance Components", "Prediction Sum", "Model Fit Sums", "Error Variance"],
     "answer": "Total, Explained, and Residual Sums of Squares"}
]

chapter_3_quiz_data = [
    {"term": "Review the literature and develop the theoretical model",
     "information": "Assess prior research and construct a model based on theory.",
     "options": ["Specify Model", "Review Literature", "Document Results", "Analyze Data", "Develop Model", "Test Model", "Theoretical Assessment"],
     "answer": "Review the literature and develop the theoretical model"},
    {"term": "Specify the model",
     "information": "Select relevant independent variables and the functional form.",
     "options": ["Estimate Coefficients", "Specify the model", "Test Model", "Develop Model", "Select Variables", "Functional Form", "Model Development"],
     "answer": "Specify the model"},
    {"term": "Hypothesize the expected signs",
     "information": "Predict the direction of the coefficients based on theory.",
     "options": ["Evaluate Signs", "Hypothesize Signs", "Test Signs", "Model Predictions", "Theoretical Predictions", "Predict Coefficients", "Variable Directions"],
     "answer": "Hypothesize the expected signs"},
    {"term": "Collect and clean data",
     "information": "Gather and prepare data for analysis.",
     "options": ["Collect and clean data", "Estimate Parameters", "Evaluate Data", "Prepare Dataset", "Data Wrangling", "Data Cleaning", "Data Collection"],
     "answer": "Collect and clean data"},
    {"term": "Estimate and evaluate",
     "information": "Use statistical methods to estimate parameters and assess model performance.",
     "options": ["Document Results", "Estimate and evaluate", "Test Predictions", "Model Assessment", "Parameter Estimation", "Performance Evaluation", "Analyze Results"],
     "answer": "Estimate and evaluate"},
    {"term": "Document the results",
     "information": "Present findings with a clear explanation of the model and conclusions.",
     "options": ["Specify Model", "Document the results", "Review Results", "Present Findings", "Model Documentation", "Report Results", "Explain Model"],
     "answer": "Document the results"}
]


chapter_4_quiz_data = [
    {"term": "Biased Estimator",
     "information": "An estimator whose expected value does not equal the true parameter value.",
     "options": ["Biased Estimator", "Unbiased Estimator", "Efficient Estimator", "BLUE", "Consistent Estimator", "Sampling Estimator", "Approximate Estimator"],
     "answer": "Biased Estimator"},
    {"term": "BLUE",
     "information": "Best Linear Unbiased Estimator, as per the Gauss–Markov Theorem.",
     "options": ["BLUE", "Efficient Estimator", "Best Predictor", "Gauss–Markov Estimator", "Consistent Estimator", "Optimal Estimator", "Linear Regression Estimator"],
     "answer": "BLUE"},
    {"term": "Classical Error Term",
     "information": "The error term in a classical regression model that meets certain assumptions.",
     "options": ["Classical Error Term", "Residual Term", "Stochastic Error Term", "Bias Term", "Prediction Error", "Noise Term", "Variance Term"],
     "answer": "Classical Error Term"},
    {"term": "Efficiency",
     "information": "An estimator with the smallest variance among unbiased estimators.",
     "options": ["Efficiency", "Consistency", "Optimality", "BLUE", "Unbiasedness", "Precision", "Estimator Variance"],
     "answer": "Efficiency"},
    {"term": "Gauss–Markov Theorem",
     "information": "States that OLS estimators are BLUE under certain assumptions.",
     "options": ["Gauss–Markov Theorem", "OLS Assumptions", "Efficiency Principle", "Least Squares Theorem", "Regression Principle", "Estimation Theorem", "BLUE Assumption"],
     "answer": "Gauss–Markov Theorem"},
    {"term": "Sampling Distribution of β̂",
     "information": "The distribution of an estimator across different samples.",
     "options": ["Sampling Distribution of β̂", "Estimator Distribution", "Parameter Distribution", "Beta Variance", "Sample Mean Distribution", "Population Distribution", "Sampling Variance"],
     "answer": "Sampling Distribution of β̂"},
    {"term": "Standard Error",
     "information": "An estimate of the standard deviation of an estimator.",
     "options": ["Standard Error", "Mean Error", "Residual Variance", "Standard Deviation", "Prediction Error", "Variance Estimator", "Error Term"],
     "answer": "Standard Error"},
    {"term": "Standard Normal Distribution",
     "information": "A normal distribution with a mean of 0 and a standard deviation of 1.",
     "options": ["Standard Normal Distribution", "Normal Distribution", "Standardized Variable", "Gaussian Distribution", "Z-Score Distribution", "Log-Normal Distribution", "Uniform Distribution"],
     "answer": "Standard Normal Distribution"},
    {"term": "Classical Assumptions",
     "information": "Assumptions ensuring that OLS estimators are BLUE.",
     "options": ["Classical Assumptions", "Regression Assumptions", "BLUE Assumptions", "OLS Conditions", "Gauss–Markov Conditions", "Efficiency Assumptions", "Estimation Assumptions"],
     "answer": "Classical Assumptions"},
    {"term": "Unbiased Estimator",
     "information": "An estimator whose expected value equals the parameter being estimated.",
     "options": ["Unbiased Estimator", "Biased Estimator", "Efficient Estimator", "Consistent Estimator", "BLUE", "Optimal Estimator", "Estimator Mean"],
     "answer": "Unbiased Estimator"}
]


chapter_5_quiz_data = [
    {"term": "Alternative Hypothesis",
     "information": "The hypothesis suggesting a significant effect or relationship.",
     "options": ["Alternative Hypothesis", "Null Hypothesis", "Research Hypothesis", "Directional Hypothesis", "Test Hypothesis", "Critical Hypothesis", "Significance Hypothesis"],
     "answer": "Alternative Hypothesis"},
    {"term": "Confidence Interval",
     "information": "The range within which a parameter is expected to lie with a given probability.",
     "options": ["Confidence Interval", "Prediction Interval", "Variance Range", "Critical Range", "Standard Error Range", "Sampling Interval", "Parameter Estimate"],
     "answer": "Confidence Interval"},
    {"term": "Critical Value",
     "information": "The threshold value to determine statistical significance.",
     "options": ["Critical Value", "P-Value", "Z-Score", "T-Statistic", "Significance Level", "Confidence Value", "Threshold Value"],
     "answer": "Critical Value"},
    {"term": "Decision Rule",
     "information": "A guideline for making a decision based on statistical testing.",
     "options": ["Decision Rule", "Testing Rule", "Significance Guideline", "Hypothesis Rule", "Evaluation Rule", "Critical Rule", "Statistical Rule"],
     "answer": "Decision Rule"},
    {"term": "F-Test",
     "information": "A test comparing model fits by analyzing variances.",
     "options": ["F-Test", "T-Test", "ANOVA", "Variance Test", "Chi-Square Test", "Likelihood Ratio Test", "Correlation Test"],
     "answer": "F-Test"},
    {"term": "Level of Significance",
     "information": "The probability of rejecting the null hypothesis when it is true.",
     "options": ["Level of Significance", "Confidence Level", "P-Value", "Critical Value", "Error Rate", "Significance Threshold", "Hypothesis Level"],
     "answer": "Level of Significance"},
    {"term": "Null Hypothesis",
     "information": "The hypothesis suggesting no effect or relationship.",
     "options": ["Null Hypothesis", "Alternative Hypothesis", "Directional Hypothesis", "Zero Hypothesis", "Base Hypothesis", "Control Hypothesis", "No-Effect Hypothesis"],
     "answer": "Null Hypothesis"},
    {"term": "One-Sided Test",
     "information": "A test considering deviations in only one direction from the null hypothesis.",
     "options": ["One-Sided Test", "Two-Sided Test", "Directional Test", "Significance Test", "Critical Test", "Hypothesis Test", "Single-Tailed Test"],
     "answer": "One-Sided Test"},
    {"term": "P-Value",
     "information": "The probability of observing a result at least as extreme as the one observed, given that the null hypothesis is true.",
     "options": ["P-Value", "Critical Value", "Significance Level", "Confidence Level", "T-Statistic", "F-Statistic", "Z-Score"],
     "answer": "P-Value"},
    {"term": "Seasonal Dummies",
     "information": "Dummy variables representing seasonal effects in time-series data.",
     "options": ["Seasonal Dummies", "Time Dummies", "Fixed Effects", "Random Effects", "Seasonal Variances", "Trend Dummies", "Temporal Dummies"],
     "answer": "Seasonal Dummies"},
    {"term": "T-Statistic",
     "information": "A statistic used to test hypotheses about individual regression coefficients.",
     "options": ["T-Statistic", "Z-Statistic", "F-Statistic", "P-Value", "Regression Coefficient", "Standard Error", "Hypothesis Test"],
     "answer": "T-Statistic"},
    {"term": "Two-Sided Test",
     "information": "A test considering deviations in both directions from the null hypothesis.",
     "options": ["Two-Sided Test", "One-Sided Test", "Bilateral Test", "Directional Test", "Critical Test", "Dual Hypothesis Test", "Double-Tailed Test"],
     "answer": "Two-Sided Test"},
    {"term": "Type I Error",
     "information": "Incorrectly rejecting the true null hypothesis.",
     "options": ["Type I Error", "Type II Error", "False Positive", "False Negative", "Significance Error", "Hypothesis Error", "Critical Error"],
     "answer": "Type I Error"},
    {"term": "Type II Error",
     "information": "Failing to reject a false null hypothesis.",
     "options": ["Type II Error", "Type I Error", "False Negative", "False Positive", "Critical Error", "Significance Error", "Hypothesis Error"],
     "answer": "Type II Error"}
]


chapter_6_quiz_data = [
    {"term": "Expected Bias",
     "information": "The bias expected in the coefficient estimate.",
     "options": ["Expected Bias", "Omitted Bias", "Specification Bias", "Coefficient Bias", "Systematic Bias", "Error Bias", "Model Bias"],
     "answer": "Expected Bias"},
    {"term": "Irrelevant Variable",
     "information": "A variable that, when included, does not affect the dependent variable.",
     "options": ["Irrelevant Variable", "Omitted Variable", "Exogenous Variable", "Uncorrelated Variable", "Random Variable", "Noise Variable", "Insignificant Variable"],
     "answer": "Irrelevant Variable"},
    {"term": "Omitted Variable",
     "information": "A relevant variable excluded from the model.",
     "options": ["Omitted Variable", "Irrelevant Variable", "Excluded Variable", "Misspecified Variable", "Dropped Variable", "Unaccounted Variable", "Hidden Variable"],
     "answer": "Omitted Variable"},
    {"term": "Omitted Variable Bias",
     "information": "The bias in estimated coefficients caused by excluding a relevant variable.",
     "options": ["Omitted Variable Bias", "Specification Bias", "Model Bias", "Exclusion Bias", "Estimation Bias", "Systematic Bias", "Variable Bias"],
     "answer": "Omitted Variable Bias"},
    {"term": "Sensitivity Analysis",
     "information": "Analysis that examines how results vary with changes in model specifications.",
     "options": ["Sensitivity Analysis", "Scenario Analysis", "Specification Analysis", "Model Variance", "Robustness Analysis", "Impact Analysis", "Parameter Analysis"],
     "answer": "Sensitivity Analysis"},
    {"term": "Sequential Specification Search",
     "information": "An iterative approach to model specification.",
     "options": ["Sequential Specification Search", "Iterative Model Search", "Sequential Variable Selection", "Specification Criteria", "Model Refinement", "Stepwise Regression", "Iterative Estimation"],
     "answer": "Sequential Specification Search"},
    {"term": "Specification Error",
     "information": "Errors resulting from incorrect model specifications.",
     "options": ["Specification Error", "Omitted Error", "Model Error", "Bias Error", "Systematic Error", "Residual Error", "Estimation Error"],
     "answer": "Specification Error"},
    {"term": "Specification Criteria",
     "information": "Guidelines for selecting model variables.",
     "options": ["Specification Criteria", "Variable Selection Criteria", "Model Guidelines", "Estimation Guidelines", "Selection Rules", "Model Selection", "Estimation Criteria"],
     "answer": "Specification Criteria"}
]

chapter_7_quiz_data = [
    {"term": "Double-Log Functional Form",
     "information": "A model where both dependent and independent variables are in log form.",
     "options": ["Double-Log Functional Form", "Semilog Functional Form", "Log-Linear Form", "Logarithmic Transformation", "Log-Log Model", "Polynomial Model", "Linear Model"],
     "answer": "Double-Log Functional Form"},
    {"term": "Elasticity",
     "information": "The responsiveness of one variable to changes in another.",
     "options": ["Elasticity", "Sensitivity", "Responsiveness", "Proportionality", "Price Elasticity", "Demand Elasticity", "Variable Responsiveness"],
     "answer": "Elasticity"},
    {"term": "Interaction Term",
     "information": "A variable formed by multiplying two variables to capture their combined effect.",
     "options": ["Interaction Term", "Dummy Interaction", "Cross Term", "Product Term", "Combined Term", "Joint Effect", "Regression Term"],
     "answer": "Interaction Term"},
    {"term": "Intercept Dummy",
     "information": "A dummy variable affecting only the intercept in a regression.",
     "options": ["Intercept Dummy", "Slope Dummy", "Indicator Variable", "Binary Intercept", "Regression Dummy", "Intercept Adjustment", "Fixed Effect"],
     "answer": "Intercept Dummy"},
    {"term": "Lag",
     "information": "A time delay in the effect of an independent variable.",
     "options": ["Lag", "Lead", "Time Delay", "Temporal Effect", "Variable Shift", "Offset", "Regression Lag"],
     "answer": "Lag"},
    {"term": "Linear in the Coefficients",
     "information": "A model linear with respect to its coefficients.",
     "options": ["Linear in the Coefficients", "Linear in the Variables", "Nonlinear Model", "Linear Form", "Polynomial in Coefficients", "Log-Linear Form", "Coefficient Proportionality"],
     "answer": "Linear in the Coefficients"},
    {"term": "Linear in the Variables",
     "information": "A model with variables in their original, non-transformed form.",
     "options": ["Linear in the Variables", "Linear in the Coefficients", "Untransformed Variables", "Original Form", "Log-Linear Model", "Polynomial Variables", "Proportional Variables"],
     "answer": "Linear in the Variables"},
    {"term": "Log",
     "information": "The natural logarithmic transformation of a variable.",
     "options": ["Log", "Natural Log", "Exponential Log", "Logarithm", "Base Log", "Linear Log", "Transformation Log"],
     "answer": "Log"},
    {"term": "Natural Log",
     "information": "The logarithm with base \(e\).",
     "options": ["Natural Log", "Log", "Base-E Log", "Exponential Log", "Logarithmic Base", "Standard Log", "Log Transformation"],
     "answer": "Natural Log"},
    {"term": "Polynomial Functional Form",
     "information": "A regression form with variables raised to a power.",
     "options": ["Polynomial Functional Form", "Linear Form", "Quadratic Form", "Exponential Form", "Logarithmic Form", "Nonlinear Form", "Polynomial Regression"],
     "answer": "Polynomial Functional Form"},
    {"term": "Semilog Functional Form",
     "information": "A model with either the dependent or independent variable in log form.",
     "options": ["Semilog Functional Form", "Log-Linear Model", "Double-Log Model", "Logarithmic Form", "Partial Log Model", "Nonlinear Model", "Linear Log Form"],
     "answer": "Semilog Functional Form"},
    {"term": "Slope Dummy",
     "information": "A dummy variable affecting only the slope in a regression.",
     "options": ["Slope Dummy", "Intercept Dummy", "Gradient Dummy", "Regression Adjustment", "Fixed Slope", "Variable Dummy", "Slope Indicator"],
     "answer": "Slope Dummy"}
]

chapter_8_quiz_data = [
    {"term": "Dominant Variable",
     "information": "A variable with a strong influence in a regression model.",
     "options": ["Dominant Variable", "Key Variable", "Significant Predictor", "Independent Variable", "Major Coefficient", "Influential Variable", "Strong Predictor"],
     "answer": "Dominant Variable"},
    {"term": "Imperfect Multicollinearity",
     "information": "When independent variables are highly correlated, but not perfectly.",
     "options": ["Imperfect Multicollinearity", "Perfect Multicollinearity", "Partial Multicollinearity", "Weak Multicollinearity", "Variable Correlation", "Collinear Variables", "Independent Multicollinearity"],
     "answer": "Imperfect Multicollinearity"},
    {"term": "Perfect Multicollinearity",
     "information": "When independent variables are perfectly correlated.",
     "options": ["Perfect Multicollinearity", "Imperfect Multicollinearity", "Exact Collinearity", "Linear Dependence", "Variable Correlation", "Perfect Correlation", "Complete Multicollinearity"],
     "answer": "Perfect Multicollinearity"},
    {"term": "Redundant Variable",
     "information": "A variable that adds no unique information.",
     "options": ["Redundant Variable", "Irrelevant Variable", "Omitted Variable", "Insignificant Variable", "Collinear Variable", "Noise Variable", "Constant Variable"],
     "answer": "Redundant Variable"},
    {"term": "Simple Correlation Coefficient",
     "information": "Measures the strength and direction of the linear relationship between two variables.",
     "options": ["Simple Correlation Coefficient", "Pearson Correlation", "Linear Correlation", "Regression Coefficient", "Spearman Coefficient", "Covariance", "Variance Ratio"],
     "answer": "Simple Correlation Coefficient"},
    {"term": "Variance Inflation Factor (VIF)",
     "information": "Measures how much the variance of a coefficient is inflated due to multicollinearity.",
     "options": ["Variance Inflation Factor (VIF)", "Variance Factor", "Inflation Coefficient", "Collinearity Index", "Correlation Index", "Coefficient Variance", "Multicollinearity Factor"],
     "answer": "Variance Inflation Factor (VIF)"}
]

chapter_9_quiz_data = [
    {"term": "Durbin–Watson Test",
     "information": "A test for detecting autocorrelation in the residuals of a regression analysis.",
     "options": ["Durbin–Watson Test", "Breusch–Godfrey Test", "Lagrange Multiplier Test", "Autocorrelation Test", "Residual Test", "Serial Correlation Test", "Time Series Test"],
     "answer": "Durbin–Watson Test"},
    {"term": "First-Order Autocorrelation Coefficient",
     "information": "Measures the correlation between consecutive residuals in a time series.",
     "options": ["First-Order Autocorrelation Coefficient", "Lag-1 Correlation", "Serial Correlation Coefficient", "Autocorrelation Coefficient", "Partial Correlation", "Time-Lag Coefficient", "Residual Correlation"],
     "answer": "First-Order Autocorrelation Coefficient"},
    {"term": "First-Order Serial Correlation",
     "information": "The correlation between consecutive observations' error terms in a time series model.",
     "options": ["First-Order Serial Correlation", "Second-Order Serial Correlation", "Autocorrelation", "Lagged Correlation", "Temporal Correlation", "Error Term Correlation", "Sequential Correlation"],
     "answer": "First-Order Serial Correlation"},
    {"term": "Generalized Least Squares (GLS)",
     "information": "A regression method used to handle cases where error terms exhibit heteroskedasticity or autocorrelation.",
     "options": ["Generalized Least Squares (GLS)", "Ordinary Least Squares (OLS)", "Weighted Least Squares", "Maximum Likelihood Estimation", "Ridge Regression", "Heteroskedastic Regression", "Autocorrelation Regression"],
     "answer": "Generalized Least Squares (GLS)"},
    {"term": "Impure Serial Correlation",
     "information": "Serial correlation caused by model specification errors.",
     "options": ["Impure Serial Correlation", "Pure Serial Correlation", "Model Error Correlation", "Specification Bias", "Residual Correlation", "Autocorrelation Error", "Noise Correlation"],
     "answer": "Impure Serial Correlation"},
    {"term": "Lagrange Multiplier (LM) Test",
     "information": "A statistical test used to check for omitted variables or serial correlation.",
     "options": ["Lagrange Multiplier (LM) Test", "Durbin–Watson Test", "Breusch–Godfrey Test", "Specification Test", "Omitted Variable Test", "Serial Correlation Test", "Residual Test"],
     "answer": "Lagrange Multiplier (LM) Test"},
    {"term": "Negative Serial Correlation",
     "information": "When consecutive error terms have a negative correlation.",
     "options": ["Negative Serial Correlation", "Positive Serial Correlation", "First-Order Serial Correlation", "Autocorrelation", "Residual Correlation", "Reverse Correlation", "Lagged Correlation"],
     "answer": "Negative Serial Correlation"},
    {"term": "Newey–West Standard Errors",
     "information": "Standard errors adjusted for autocorrelation and heteroskedasticity in time series data.",
     "options": ["Newey–West Standard Errors", "White Standard Errors", "Robust Standard Errors", "Heteroskedasticity-Adjusted Errors", "Autocorrelation Errors", "Corrected Standard Errors", "Time Series Standard Errors"],
     "answer": "Newey–West Standard Errors"},
    {"term": "Positive Serial Correlation",
     "information": "When consecutive error terms have a positive correlation.",
     "options": ["Positive Serial Correlation", "Negative Serial Correlation", "First-Order Serial Correlation", "Autocorrelation", "Residual Correlation", "Forward Correlation", "Lagged Correlation"],
     "answer": "Positive Serial Correlation"},
    {"term": "Prais–Winsten Method",
     "information": "A method for correcting serial correlation in time series regression.",
     "options": ["Prais–Winsten Method", "Newey–West Adjustment", "Generalized Least Squares", "Durbin–Watson Method", "Serial Correlation Adjustment", "Time Series Correction", "Regression Correction Method"],
     "answer": "Prais–Winsten Method"},
    {"term": "Pure Serial Correlation",
     "information": "Serial correlation arising naturally in a correctly specified model.",
     "options": ["Pure Serial Correlation", "Impure Serial Correlation", "Autocorrelation", "Natural Correlation", "Residual Correlation", "Corrected Serial Correlation", "First-Order Serial Correlation"],
     "answer": "Pure Serial Correlation"}
]


chapter_10_quiz_data = [
    {"term": "Breusch–Pagan Test",
     "information": "A test used to detect heteroskedasticity in regression models.",
     "options": ["Breusch–Pagan Test", "White Test", "Lagrange Multiplier Test", "Durbin–Watson Test", "Heteroskedasticity Test", "Autocorrelation Test", "Variance Ratio Test"],
     "answer": "Breusch–Pagan Test"},
    {"term": "Heteroskedasticity",
     "information": "Occurs when the variance of the error terms varies across observations.",
     "options": ["Heteroskedasticity", "Homoskedasticity", "Variance Inflation", "Error Variance", "Residual Variance", "Autocorrelation", "Serial Correlation"],
     "answer": "Heteroskedasticity"},
    {"term": "Heteroskedasticity-Corrected Standard Errors",
     "information": "Standard errors adjusted for heteroskedasticity to improve inference.",
     "options": ["Heteroskedasticity-Corrected Standard Errors", "Robust Standard Errors", "Newey–West Standard Errors", "White-Corrected Errors", "Residual Adjusted Errors", "Variance-Corrected Errors", "Autocorrelation-Corrected Errors"],
     "answer": "Heteroskedasticity-Corrected Standard Errors"},
    {"term": "Impure Heteroskedasticity",
     "information": "Heteroskedasticity arising from model specification errors.",
     "options": ["Impure Heteroskedasticity", "Pure Heteroskedasticity", "Specification Error", "Model Bias", "Residual Variance", "Systematic Variance", "Incorrect Model Variance"],
     "answer": "Impure Heteroskedasticity"},
    {"term": "Proportionality Factor",
     "information": "A factor that scales variance in heteroskedastic models.",
     "options": ["Proportionality Factor", "Variance Factor", "Scaling Factor", "Coefficient Multiplier", "Regression Factor", "Error Scaling Factor", "Variance Multiplier"],
     "answer": "Proportionality Factor"},
    {"term": "Pure Heteroskedasticity",
     "information": "Heteroskedasticity inherent in the data and not due to specification error.",
     "options": ["Pure Heteroskedasticity", "Impure Heteroskedasticity", "Data Variance", "Intrinsic Variance", "Model-Free Variance", "Specification-Free Variance", "Natural Variance"],
     "answer": "Pure Heteroskedasticity"},
    {"term": "White Test",
     "information": "A statistical test for heteroskedasticity that does not require specific assumptions about the form of heteroskedasticity.",
     "options": ["White Test", "Breusch–Pagan Test", "Variance Test", "Lagrange Multiplier Test", "Residual Test", "Homoskedasticity Test", "Error Variance Test"],
     "answer": "White Test"}
]

chapter_12_quiz_data = [
    {"term": "Cointegration",
     "information": "Indicates a long-term equilibrium relationship between two or more non-stationary time series.",
     "options": ["Cointegration", "Correlation", "Stationarity", "Unit Root Relationship", "Trend Analysis", "Dynamic Link", "Equilibrium Relationship"],
     "answer": "Cointegration"},
    {"term": "Dickey–Fuller Test",
     "information": "A test used to determine whether a time series is stationary or has a unit root.",
     "options": ["Dickey–Fuller Test", "Augmented Dickey–Fuller Test", "Stationarity Test", "Unit Root Test", "ADF Test", "Time Series Stability Test", "Trend Test"],
     "answer": "Dickey–Fuller Test"},
    {"term": "Distributed Lag Model",
     "information": "A model that includes lagged values of an independent variable to capture delayed effects.",
     "options": ["Distributed Lag Model", "Dynamic Lag Model", "Lagged Variable Model", "Autoregressive Model", "Time-Delay Model", "Variable Lag Model", "Causal Lag Model"],
     "answer": "Distributed Lag Model"},
    {"term": "Dynamic Model",
     "information": "A model that includes lagged dependent variables to capture persistence over time.",
     "options": ["Dynamic Model", "Lagged Dependent Model", "Autoregressive Model", "Time Series Model", "Causal Dynamic Model", "Persistence Model", "Lag Structure Model"],
     "answer": "Dynamic Model"},
    {"term": "Granger Causality",
     "information": "A statistical hypothesis test to determine whether one time series can predict another.",
     "options": ["Granger Causality", "Predictive Causality", "Time Series Causality", "Dynamic Prediction Test", "Causal Relationship Test", "Lag Prediction Test", "Regression Causality"],
     "answer": "Granger Causality"},
    {"term": "Nonstationary",
     "information": "A time series whose statistical properties change over time.",
     "options": ["Nonstationary", "Stationary", "Random Walk", "Trend Stationary", "Unit Root Process", "Time-Dependent Series", "Unstable Series"],
     "answer": "Nonstationary"},
    {"term": "Random Walk",
     "information": "A time series where changes are purely random, often used to model non-stationary processes.",
     "options": ["Random Walk", "Unit Root Process", "Stationary Walk", "Brownian Motion", "Time-Dependent Randomness", "Trend Process", "Random Process"],
     "answer": "Random Walk"},
    {"term": "Spurious Correlation",
     "information": "A misleading correlation between two variables due to a common trend rather than a causal relationship.",
     "options": ["Spurious Correlation", "Coincidental Correlation", "False Relationship", "Trend Correlation", "Pseudo-Correlation", "Common Trend Correlation", "Misleading Correlation"],
     "answer": "Spurious Correlation"},
    {"term": "Stationary",
     "information": "A time series with constant mean, variance, and autocovariance over time.",
     "options": ["Stationary", "Nonstationary", "Trend Stationary", "Unit Root Process", "Time-Invariant Series", "Stable Series", "Equilibrium Series"],
     "answer": "Stationary"},
    {"term": "Unit Root",
     "information": "A characteristic of non-stationary time series, often tested to identify trends.",
     "options": ["Unit Root", "Stationarity", "Random Walk", "Trend Process", "Time Series Root", "Equilibrium Test", "Root Process"],
     "answer": "Unit Root"}
]


quiz_data = (
    chapter_1_quiz_data +
    chapter_2_quiz_data +
    chapter_3_quiz_data +
    chapter_4_quiz_data +
    chapter_5_quiz_data +
    chapter_6_quiz_data +
    chapter_7_quiz_data +
    chapter_8_quiz_data +
    chapter_9_quiz_data +
    chapter_10_quiz_data +
    chapter_12_quiz_data
)


# Shuffle questions and answers
if 'shuffled_quiz_data' not in st.session_state:
    shuffled_quiz_data = quiz_data.copy()
    for q in shuffled_quiz_data:
        random.shuffle(q['options'])
    random.shuffle(shuffled_quiz_data)
    st.session_state.shuffled_quiz_data = shuffled_quiz_data

# Initialize session state variables
default_values = {
    'current_index': 0,
    'score': 0,
    'selected_option': None,
    'answer_submitted': False,
}
for key, value in default_values.items():
    st.session_state.setdefault(key, value)

# Quiz functionality


def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False

    # Reshuffle questions and answers
    shuffled_quiz_data = quiz_data.copy()
    for q in shuffled_quiz_data:
        random.shuffle(q['options'])
    random.shuffle(shuffled_quiz_data)
    st.session_state.shuffled_quiz_data = shuffled_quiz_data


def submit_answer():
    if st.session_state.selected_option is not None:
        st.session_state.answer_submitted = True
        correct_answer = st.session_state.shuffled_quiz_data[st.session_state.current_index]['answer']
        if st.session_state.selected_option == correct_answer:
            st.session_state.score += 10
    else:
        st.warning("Please select an option before submitting.")


def next_question():
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False


# Quiz Interface
st.title("Econometrics Key Terms Quiz")
progress_bar_value = (st.session_state.current_index + 1) / \
    len(st.session_state.shuffled_quiz_data)
st.metric(label="Score", value=f"{
          st.session_state.score} / {len(st.session_state.shuffled_quiz_data) * 10}")
st.progress(progress_bar_value)

# Current Question
question_item = st.session_state.shuffled_quiz_data[st.session_state.current_index]
st.subheader(f"Question {st.session_state.current_index + 1}")
st.write(question_item['information'])  # Display only the description

options = question_item['options']
correct_answer = question_item['answer']

# Answer Selection and Feedback
if st.session_state.answer_submitted:
    for option in options:
        label = option
        if option == correct_answer:
            st.success(f"{label} (Correct answer)")
        elif option == st.session_state.selected_option:
            st.error(f"{label} (Incorrect answer)")
        else:
            st.write(label)
else:
    for i, option in enumerate(options):
        if st.button(option, key=i, use_container_width=True):
            st.session_state.selected_option = option

# Navigation
if st.session_state.answer_submitted:
    if st.session_state.current_index < len(st.session_state.shuffled_quiz_data) - 1:
        st.button('Next', on_click=next_question)
    else:
        st.write(f"Quiz completed! Your score is: {
                 st.session_state.score} / {len(st.session_state.shuffled_quiz_data) * 10}")
        if st.button('Restart', on_click=restart_quiz):
            pass
else:
    st.button('Submit', on_click=submit_answer)
