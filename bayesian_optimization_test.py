import numpy as np
import os
from mock_light_mixer import LightMixer
from ax.service.ax_client import AxClient, ObjectiveProperties, AxPlotConfig
import warnings


def test_parameters_and_objectives():
    script_fname = "bayesian_optimization.py"
    script_content = open(script_fname).read()

    if "..." in script_content:
        warnings.warn(
            f"Please complete the '...' sections in {script_fname} and remove the '...' from each section"
        )

    namespace = {}
    exec(script_content, namespace)

    parameters = namespace["parameters"]

    assert len(parameters) == 3, f"Expected 3 parameters, got {len(parameters)}"
    dict_keys = ["name", "type", "bounds"]
    # check that at minimum dict_keys are present in all items
    for parameter in parameters:
        assert all(
            key in parameter for key in dict_keys
        ), f"Missing keys in {parameter}"

    # check that the type is range
    for parameter in parameters:
        assert (
            parameter["type"] == "range"
        ), f"Expected type to be 'range', got {parameter['type']}"

    # check that the bounds have two elements
    for parameter in parameters:
        assert len(parameter["bounds"]) == 2, f"Expected 2 bounds, got {parameter}"

    # check the lower and upper bounds
    for parameter in parameters:
        assert (
            parameter["bounds"][0] == 0
        ), f"Expected lower bound to be 0, got {parameter['bounds'][0]}"
        assert (
            parameter["bounds"][1] == 255
        ), f"Expected upper bound to be 255, got {parameter['bounds'][1]}"

    # check that the objective is defined
    assert "objectives" in namespace, "Expected objectives to be defined"
    objectives = namespace["objectives"]

    # assert there is only one dictionary item in objectives
    assert len(objectives) == 1, f"Expected 1 objective, got {len(objectives)}"

    # assert "mae" is the key in the objectives dictionary
    assert "mae" in objectives, f"Expected 'mae' to be the key in objectives"

    # assert the value of the key is an instance of ObjectiveProperties
    mae_objective = objectives["mae"]
    assert isinstance(
        mae_objective, ObjectiveProperties
    ), f"Expected dictionary value to be an instance of ObjectiveProperties"

    # assert the minimize attribute is True
    assert (
        mae_objective.minimize
    ), f"Expected the minimize attribute to be True, got {mae_objective.minimize}"


def test_calls():
    script_content = open("bayesian_optimization.py").read()
    namespace = {}
    exec(script_content, namespace)

    # find the LightMixer() object
    mixers = [v for _, v in namespace.items() if isinstance(v, LightMixer)]
    assert (
        len(mixers) == 1
    ), f"Expected one and only one {LightMixer.__name__} object, but it looks like you created {len(mixers)} {LightMixer.__name__} objects"  # noqa: E501
    mixer = mixers[0]
    assert (
        mixer._run_color_experiment_called
    ), f"{LightMixer.run_color_experiment.__name__} not called"
    assert (
        mixer._calculate_objective_called
    ), f"{LightMixer.calculate_objective.__name__} not called"

    # find the AxClient() object
    ax_clients = [v for _, v in namespace.items() if isinstance(v, AxClient)]
    assert (
        len(ax_clients) == 1
    ), f"Expected one and only one {AxClient.__name__} object, but it looks like you created {len(ax_clients)} {AxClient.__name__} objects"  # noqa: E501

    ax_client = ax_clients[0]
    # assert that random_seed is set to 42
    assert (
        ax_client._random_seed == 42
    ), f"Expected {AxClient.__name__} object to have random_seed=42, got {ax_client._random_seed}"  # noqa: E501

    # check that a specific dictionary with {"R": 10, "G": 20, "B": 15} was passed to run_color_experiment
    # Note that the target color experiment is the first that is run, hence the second call
    first_user_call = mixer._history[1]
    first_user_call_check = {
        "R": 255,
        "G": 26,
        "B": 210,
        "ch410": 219.33087856963076,
        "ch440": 248.248387805653,
        "ch470": 282.9731413261822,
        "ch510": 268.15146335347225,
        "ch550": 239.06822906707887,
        "ch583": 240.12586524637015,
        "ch620": 273.09731873935584,
        "ch670": 237.84121011577813,
    }

    # Check if the keys in both dictionaries match
    assert set(first_user_call.keys()) == set(
        first_user_call_check.keys()
    ), "Keys in both dictionaries do not match."

    # Convert the dictionaries to numpy arrays
    first_user_call_array = np.array(list(first_user_call.values()))
    first_user_call_check_array = np.array(list(first_user_call_check.values()))

    # Check if the arrays are close within a tolerance
    assert np.allclose(
        first_user_call_array, first_user_call_check_array, rtol=1e-5
    ), f"Expected first suggested experiment issued to {LightMixer.run_color_experiment.__name__} to be approximately {first_user_call_check}, got {first_user_call}"  # noqa: E501

    # Check that `save_to_json_file` was called from the AxClient object by
    # checking if `ax_client_snapshot.json` exists
    assert os.path.exists(
        "ax_client_snapshot.json"
    ), f"Expected {AxClient.save_to_json_file.__name__} to be called, but `ax_client_snapshot.json` does not exist"  # noqa: E501

    # assert that there is at least one AxPlotConfig
    ax_plot_configs = [v for _, v in namespace.items() if isinstance(v, AxPlotConfig)]
    assert (
        len(ax_plot_configs) >= 1
    ), f"Expected at least one {AxPlotConfig.__name__} object using Ax's built-in plotting methods, but it looks like you created {len(ax_plot_configs)} {AxPlotConfig.__name__} objects"  # noqa: E501
