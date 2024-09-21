import os
from ax.service.ax_client import AxClient, ObjectiveProperties
from mock_light_mixer import LightMixer
import plotly.graph_objects as go

num_iter = 27

target_color = {"R": 255, "G": 127, "B": 63}

# Instantiate the LightMixer class with the target color
mixer = LightMixer(target_color=target_color)

# Define the parameters per the README.md file instructions
parameters = ...  # IMPLEMENT

# define the objective with the name "mae" (mean absolute error) and minimize=True
objectives = ...  # IMPLEMENT

# Instantiate the AxClient class with `random_seed=42` for reproducibility
ax_client = AxClient(random_seed=42)

# Pass the parameters and objectives
ax_client.create_experiment(parameters=parameters, objectives=objectives)


def evaluate(parameterization):
    """
    Evaluates the objective function for a given parameterization.

    Parameters
    ----------
    parameterization : dict
        A dictionary containing the parameters for the color experiment. The
        keys of the dictionary should match the arguments of the
        run_color_experiment method of the LightMixer class.

    Returns
    -------
    dict
        A dictionary containing the mean absolute error (mae) of the objective
        function. The key is 'mae' and the value is the computed mean absolute
        error.

    Examples
    --------
    >>> evaluate({"R": 10, "G": 20, "B": 30})
    {'mae': 0.05}
    """
    # Use the run_color_experiment method of the LightMixer class
    sensor_data = ...  # IMPLEMENT

    # Compute the objective function value using the calculate_objective method
    # of the LightMixer class
    results = ...  # IMPLEMENT

    return results


for _ in range(num_iter):
    parameterization, trial_index = ax_client.get_next_trial()
    # e.g., parameterization={"R": 10, "G": 20, "B": 15} and trial_index=0

    results = evaluate(parameterization)
    # e.g., {"mae": 0.5}

    ax_client.complete_trial(trial_index=trial_index, raw_data=results)


best_parameters, metrics = ax_client.get_best_parameters()
true_mismatch = mixer.calculate_rgb_mismatch(**best_parameters)

print(f"Target color: {mixer.target_color}")
print(f"Best observed color: {best_parameters}")
print(f"Color misfit: {round(true_mismatch, 1)}")

# Save the entire Ax experiment to a JSON file named ax_client_snapshot.json
...  # IMPLEMENT

# get the AxClient's optimization trace using the built-in plotting method (objective_optimum can be left off)
optimization_trace = ...  # IMPLEMENT


def to_plotly(axplotconfig):
    """Converts AxPlotConfig to plotly Figure."""
    data = axplotconfig[0]["data"]
    layout = axplotconfig[0]["layout"]
    fig = go.Figure({"data": data, "layout": layout})
    return fig


# Convert the optimization trace to a Plotly figure and save it as an image
fig = to_plotly(optimization_trace)
image_name = "optimization_trace.png"
fig.write_image(image_name)

# Open the image file in Codespaces (or Visual Studio Code)
os.system(f"code {image_name}")
