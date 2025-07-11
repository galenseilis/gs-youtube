import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ------------------------------
# Transition rates
# ------------------------------
# Attachment/detachment
attach_ER = 0.3
detach_ER = 0.2

attach_Ward = 0.2
detach_Ward = 0.1

attach_ICU = 0.25
detach_ICU = 0.05

# Movement between physical units (must be attached)
ER_to_Ward = 0.4
ER_to_ICU = 0.2

# Discharges (from attached states)
Ward_discharge = 0.1
ICU_discharge = 0.05


# ------------------------------
# Master equation
# ------------------------------
def flow_model(t, P):
    ER_U, ER_A, W_U, W_A, ICU_U, ICU_A = P

    # ER
    dER_U = -attach_ER * ER_U + detach_ER * ER_A
    dER_A = attach_ER * ER_U - detach_ER * ER_A - (ER_to_Ward + ER_to_ICU) * ER_A

    # Ward
    dW_U = ER_to_Ward * ER_A - attach_Ward * W_U + detach_Ward * W_A
    dW_A = attach_Ward * W_U - detach_Ward * W_A - Ward_discharge * W_A

    # ICU
    dICU_U = ER_to_ICU * ER_A - attach_ICU * ICU_U + detach_ICU * ICU_A
    dICU_A = attach_ICU * ICU_U - detach_ICU * ICU_A - ICU_discharge * ICU_A

    return [dER_U, dER_A, dW_U, dW_A, dICU_U, dICU_A]


# ------------------------------
# Initial condition: all patients start in ER_U
# ------------------------------
P_init = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# ------------------------------
# Time setup and solver
# ------------------------------
t_span = (0, 100)
t_eval = np.linspace(*t_span, 500)

sol = solve_ivp(flow_model, t_span, P_init, t_eval=t_eval)

# ------------------------------
# Plotting
# ------------------------------
labels = [
    "ER (Unattached)",
    "ER (Attached)",
    "Ward (Unattached)",
    "Ward (Attached)",
    "ICU (Unattached)",
    "ICU (Attached)",
]

plt.figure(figsize=(12, 7))
for i, label in enumerate(labels):
    plt.plot(sol.t, sol.y[i], label=label)

# Implied discharged probability
remaining_prob = np.sum(sol.y, axis=0)
discharged = 1 - remaining_prob
plt.plot(sol.t, discharged, "--", label="Discharged (Implied)", color="black")

plt.xlabel("Time")
plt.ylabel("Probability")
plt.title("Patient Flow with Attachment States (Master Equation)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
