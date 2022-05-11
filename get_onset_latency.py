import numpy as np
from scipy.signal import find_peaks

# Compute n% peak latency for diff averages (1D only)
# Returns index for percent latency
def get_onset_latency(epoch, s_ix, e_ix, percent=0.5, dev_from_0 = 0.005):
    # First find peak amplitude
    peaks = find_peaks(epoch[s_ix:e_ix])[0]+s_ix
    peak_ix = peaks[np.argmin(np.abs(peaks - np.mean((s_ix,e_ix))))]
    peak = epoch[peak_ix]

    # Compute half of peak amplitude
    perc_peak = peak * percent

    # Extract time points before peak
    pre_peak = epoch[0:peak_ix]

    # Find closest point to perc_peak
    for i in range(peak_ix-1, 0, -1):
        if (pre_peak[i] - perc_peak) <= dev_from_0:
            return i
        
    return None # didn't find an adequate point