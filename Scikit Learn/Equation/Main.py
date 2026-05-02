# Import the libraries
from random import randint
from sklearn.linear_model import LinearRegression
# Create limits
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100
# Create empty lists
TRAIN_INPUT = []
TRAIN_OUTPUT = []
# Generate training data
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    d = randint(0, TRAIN_SET_LIMIT)
    # Your equation
    op = (7*a) + (3*b) + (4*c) + (9*d)
    TRAIN_INPUT.append([a, b, c, d])
    TRAIN_OUTPUT.append(op)
# Train model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)
# Test data
X_TEST = [[10, 20, 30, 40]]
# Expected:
# 7*10 + 3*20 + 4*30 + 9*40 = 610
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_
# Output
print('Outcome: {}'.format(outcome))
print('Coefficients: {}'.format(coefficients))