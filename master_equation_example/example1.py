import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ------------------------------
# Transition rates (units: 1/time)
# ------------------------------
r01 = 0.4  # ER → Ward
r02 = 0.2  # ER → ICU
r13 = 0.1  # Ward → Discharged
r23 = 0.05  # ICU → Discharged


# ------------------------------
# Master equation: dP/dt = A(P)
# ------------------------------
def patient_flow_odes(t, P):
    P0, P1, P2, P3 = P
    dP0 = -(r01 + r02) * P0
    dP1 = r01 * P0 - r13 * P1
    dP2 = r02 * P0 - r23 * P2
    dP3 = r13 * P1 + r23 * P2  # Discharge accumulates
    return [dP0, dP1, dP2, dP3]


# ------------------------------
# Initial state: all patients start in ER
# ------------------------------
P_initial = [1.0, 0.0, 0.0, 0.0]

# ------------------------------
# Solve the system over time
# ------------------------------
t_start, t_end = 0, 100
t_points = np.linspace(t_start, t_end, 500)

solution = solve_ivp(patient_flow_odes, (t_start, t_end), P_initial, t_eval=t_points)

# ------------------------------
# Plotting the results
# ------------------------------
plt.figure(figsize=(10, 6))
state_labels = ["ER", "Ward", "ICU", "Discharged"]

for i, label in enumerate(state_labels):
    plt.plot(solution.t, solution.y[i], label=label)

plt.title("Patient Flow via Master Equation")
plt.xlabel("Time")
plt.ylabel("Probability")
plt.ylim(0, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
