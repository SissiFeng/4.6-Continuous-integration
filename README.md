# Bayesian Optimization
Adapt a Bayesian optimization script to perform color matching.

## The assignment
The tests are failing right now because the [`bayesian_optimization.py`](bayesian_optimization.py) script is not fully implemented. Fixing this up will make the tests green. Wherever you see `...` within the script requires you to write your own code. See below for instructions.

Refer to [the Ax Service API tutorial](https://ax.dev/tutorials/gpei_hartmann_service.html) if you get stuck.

### Ax parameter configuration

Use `"R"`, `"G"`, and `"B"` as the parameter names. Use 0 and 255 as lower and upper
*integer* bounds, respectively. Note that Python interprets 0.0 and 255.0 as
continuous variables ("floats"), and 0 and 255 as integers. As an example, the
2D Branin function parameters would look like:

```python
parameters = [
   {"name": "x1", "type": "range", "bounds": [-5.0, 10.0]},
   {"name": "x2", "type": "range", "bounds": [0.0, 10.0]},
]
```

Likewise, the parameter configuration for the Hartmann6 function would look like:
```python
[
    {"name": "x1", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "x2", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "x3", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "x4", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "x5", "type": "range", "bounds": [0.0, 1.0]},
    {"name": "x6", "type": "range", "bounds": [0.0, 1.0]},
]
```

See the ["Set up experiment"](https://ax.dev/tutorials/gpei_hartmann_service.html#2.-Set-up-experiment) section from the Ax Service API tutorial for additional context.

### Using the LightMixer class

In this assignment, you will use the `run_color_experiment` and `calculate_objective` methods from the [LightMixer](src/mock_light_mixer/_mock_light_mixer.py) class contained in the `mock_light_mixer` package, which comes preinstalled in your Codespace. Here is some example code for how to use it:

```python
from mock_light_mixer import LightMixer

target_color = {"R": 255, "G": 127, "B": 63}

parameterization = {"R": 10, "G": 20, "B": 15}

mixer = LightMixer(target_color=target_color)

# Use the run_color_experiment method from the instantiated LightMixer class to
# run an experiment with a certain parameterization
R = parameterization["R"]
G = parameterization["G"]
B = parameterization["B"]
sensor_data = mixer.run_color_experiment(R, G, B)
```

Likewise, you can use the `calculate_objective` method to calculate the objective function value for a given parameterization:

```python
from mock_light_mixer import LightMixer

target_color = {"R": 255, "G": 127, "B": 63}

sensor_data = {
    "ch410": 102.2,
    "ch440": 220.4,
    "ch470": 225.6,
    "ch510": 178.8,
    "ch550": 191.6,
    "ch583": 204.4,
    "ch620": 217.2,
    "ch670": 230.0,
}

mixer = LightMixer(target_color=target_color)

objective_function_value = mixer.calculate_objective(sensor_data)
```

This objective is the mean absolute error (MAE) between the target sensor data and the observed sensor data. While you do not need to implement this yourself, for your reference, the MAE between the values in two dictionaries with identical keys can be computed as shown below. Note that the keys from `dict1` are used to index the values for both `dict1` and `dict2`.

```python
from sklearn.metrics import mean_absolute_error

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 4, 'c': 7}

keys = dict1.keys()
dict1_values = [dict1[key] for key in keys]
dict2_values = [dict2[key] for key in keys]

mae = mean_absolute_error(dict1_values, dict2_values)
print(mae)
# 2.0
```

NOTE: the code above assumes the values are all numeric.

### Stuck?

Refer to https://ax.dev/tutorials/gpei_hartmann_service.html and the course tutorial content.

### Run command
`pytest`

You can also use the "Testing" sidebar extension to easily run individual tests.