def combine_config_results(config, results):
    """Add configs to results"""
    for key, result in results.items():
        result.update(config[key])
        
    return results