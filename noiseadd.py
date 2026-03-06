import numpy as np
salaries = np.array([50000, 60000, 1000000, 55000])
def add_laplace_noise(data, sensitivity, epsilon):
    beta = sensitivity / epsilon
    noise = np.random.laplace(0, beta, len(data))
    return data + noise
sensitive_avg = np.mean(salaries)
private_avg = np.mean(add_laplace_noise(salaries, sensitivity=1000000, epsilon=1))

print(f"True Average: {sensitive_avg}")
print(f"Private Average: {private_avg}")