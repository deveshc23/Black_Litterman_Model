import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import safe_inverse


def black_litterman_posterior(pi, sigma, p, q, omega, tau=0.05):
    n = len(pi)
    
    
    pi = np.array(pi).reshape(-1, 1)
    q = np.array(q).reshape(-1, 1)     
    
    
    p = np.array(p).reshape(q.shape[0], n) 
    
    
    if np.isscalar(omega) or isinstance(omega, float):
        omega = np.array([[omega]])
    else:
        omega = np.array(omega).reshape(q.shape[0], q.shape[0])

    tau_sigma = tau * sigma
    inv_tau_sigma = safe_inverse(tau_sigma)
    inv_omega = safe_inverse(omega)
    
    middle_term = p.T @ inv_omega @ p
    v_inv = inv_tau_sigma + middle_term
    v = safe_inverse(v_inv)

    right_term = (inv_tau_sigma @ pi) + (p.T @ inv_omega @ q)
    m = v @ right_term

    return m.flatten(), v


def optimal_weights(mu_pred, sigma_pred, risk_aversion=2.5):
    inv_sigma = safe_inverse(sigma_pred)
    weights = (1.0 / risk_aversion) * (inv_sigma @ mu_pred)
    weights = weights / weights.sum()
    return weights


if __name__ == "__main__":
    pass
