import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    m = np.array(x_t)
    n = np.array(h_prev)
    return np.tanh(m@Wx + n@Wh + b)
