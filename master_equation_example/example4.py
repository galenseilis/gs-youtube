import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
arrival_rate = 5.0  # Patients per hour entering ER
ER_to_Ward_rate = 0.3  # Fraction per hour moving to Ward
ER_to_ICU_rate = 0.1  # Fraction per hour moving to ICU
Ward_discharge_rate = 0.2
ICU_discharge_rate = 0.15


def patient_flow(t, y):
    ER, Ward, ICU = y

    # Inflows
    dER_dt = arrival_rate - (ER_to_Ward_rate + ER_to_ICU_rate) * ER
    dWard_dt = ER_to_Ward_rate * ER - Ward_discharge_rate * Ward
    dICU_dt = ER_to_ICU_rate * ER - ICU_discharge_rate * ICU

    return [dER_dt, dWard_dt, dICU_dt]


# Initial state: empty hospital
initial_state = [0, 0, 0]

# Time span
t_span = (0, 50)  # hours
t_eval = np.linspace(*t_span, 300)

# Solve ODE
sol = solve_ivp(patient_flow, t_span, initial_state, t_eval=t_eval)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label="ER")
plt.plot(sol.t, sol.y[1], label="Ward")
plt.plot(sol.t, sol.y[2], label="ICU")
plt.xlabel("Time (hours)")
plt.ylabel("Number of patients")
plt.title("Patient Flow Through Hospital Units")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
