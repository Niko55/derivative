
#Batch gradient descent
while True:
    theta_grad = evaluate_grad(J, corpus, theta)
    theta = theta - alpha*theta_grad

#Stochastic Gradient Descent    
while True:
    window = sample_window(corpus)
    theta_grad = evaluate_grad(J, window, theta)
    theta = theta - alpha*theta_grad