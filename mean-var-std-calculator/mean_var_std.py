import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    numpy_array = np.array(list).reshape((3,3))
  
    mean_ax0 = np.mean(numpy_array, axis=0)
    mean_ax1 = np.mean(numpy_array, axis=1)
    mean_flat = np.mean(numpy_array.flatten())

    var_ax0 = np.var(numpy_array, axis=0)
    var_ax1 = np.var(numpy_array, axis=1)
    var_flat = np.var(numpy_array.flatten())

    std_ax0 = np.std(numpy_array, axis=0)
    std_ax1 = np.std(numpy_array, axis=1)
    std_flat = np.std(numpy_array.flatten())

    max_ax0 = np.max(numpy_array, axis=0)
    max_ax1 = np.max(numpy_array, axis=1)
    max_flat = np.max(numpy_array.flatten())

    min_ax0 = np.min(numpy_array, axis=0)
    min_ax1 = np.min(numpy_array, axis=1)
    min_flat = np.min(numpy_array.flatten())

    sum_ax0 = np.sum(numpy_array, axis=0)
    sum_ax1 = np.sum(numpy_array, axis=1)
    sum_flat = np.sum(numpy_array.flatten())

    calculations = {
      'mean' : [mean_ax0.tolist(), mean_ax1.tolist(), mean_flat],
      'variance' : [var_ax0.tolist(), var_ax1.tolist(), var_flat],
      'standard deviation' : [std_ax0.tolist(), std_ax1.tolist(), std_flat],
      'max' : [max_ax0.tolist(), max_ax1.tolist(), max_flat],
      'min' : [min_ax0.tolist(), min_ax1.tolist(), min_flat],
      'sum' : [sum_ax0.tolist(), sum_ax1.tolist(), sum_flat]
      
    }
  

    return calculations