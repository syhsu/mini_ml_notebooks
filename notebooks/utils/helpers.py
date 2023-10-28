"""helper functions"""


def combine_config_results(config: dict, results: dict) -> dict:
    """Add configs to results"""
    for key, result in results.items():
        result.update(config[key])

    return results
