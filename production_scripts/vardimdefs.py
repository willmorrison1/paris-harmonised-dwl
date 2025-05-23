# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:58:56 2024

@author: willm
"""
import definitions as defs

vardimdefs = [
    {
        "level": 3,
        "type": "variable",
        "L2_name": "u",
        "L3_fun": "mean",
        "name": "u",
        "standard_name": "eastward_wind",
        "units": defs.WS_UNITS,
        "cell_methods": "time: mean",
        "comment": 'Averaged eastward wind component. Averaged over all valid'
        ' samples within the time aggregation interval.',
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "v",
        "L3_fun": "mean",
        "name": "v",
        "standard_name": "northward_wind",
        "units": defs.WS_UNITS,
        "cell_methods": "time: mean",
        "comment": 'Averaged northward wind component. Averaged over all valid'
        ' samples within the time aggregation interval.',
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "flag_low_signal_warn",
        "L3_fun": "pc",
        "name": "flag_low_signal_warn",
        "long_name": "flag_low_signal_warn",
        "units": "%",
        "comment": (
            'The scan has a signal intensity below a threshold required for a '
            'non-suspect retrieval. Use retreival with caution.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "flag_low_signal_removed",
        "L3_fun": "pc",
        "name": "flag_low_signal_removed",
        "long_name": "flag_low_signal_removed",
        "units": "%",
        "comment": (
            'The scan has a signal intensity below a threshold required for a '
            'valid retrieval. Retrieval rejected.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "flag_suspect_retrieval_warn",
        "L3_fun": "pc",
        "name": "flag_suspect_retrieval_warn",
        "long_name": "flag_suspect_retrieval_warn",
        "units": "%",
        "comment": (
            'The scan is suspect based on tests unique to each system model. '
            'Use retreival with caution. Missing values indicate no QC test performed.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "flag_suspect_retrieval_removed",
        "L3_fun": "pc",
        "name": "flag_suspect_retrieval_removed",
        "long_name": "flag_suspect_retrieval_removed",
        "units": "%",
        "comment": (
            'The scan is suspect based on system model specific tests. '
            'Retrieval rejected.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "flag_ws_out_of_range_removed",
        "L3_fun": "pc",
        "name": "flag_ws_out_of_range",
        "long_name": "flag_ws_out_of_range",
        "units": "%",
        "comment":  (
            f'The retrieval exceed the horizontal wind speed threshold of '
            f'{defs.MAX_VALID_WS} {defs.WS_UNITS}. Retrieval rejected.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "n_rays_in_scan",
        "L3_fun": "mean",
        "name": "n_rays_in_scan",
        "long_name": "number_of_rays_in_scan",
        "units": defs.UNITLESS_UNITS,
        "comment":  (
            'The number of rays in a given scan. E.g. 12 for a VAD scan that '
            'has 12 samples within one scan'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "raw_gate_length",
        "L3_fun": "mean",
        "name": "raw_gate_length",
        "long_name": "raw_gate_length",
        "units": "m",
        "comment":  (
            'The gate length of the raw data prior to L3 aggregation.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "L2_name": "n_pulses",
        "L3_fun": "mean",
        "name": "n_pulses",
        "long_name": "number_of_pulses_in_ray",
        "units": defs.UNITLESS_UNITS,
        "comment":  (
            'The number of pulses in a given ray. The more pulses the higher'
            'the integration time. Available for StreamLine models.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "name": "ws",
        "standard_name": "wind_speed",
        "units": defs.WS_UNITS,
        "comment":  (
            'Horizontal wind speed calculated from eastward_wind and northward_wind.'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "name": "wd",
        "standard_name": "wind_from_direction",
        "units": defs.WS_UNITS,
        "comment":  (
            'Horizontal wind direction clockwise from true north, calculated '
            'from eastward_wind and northward_wind.'
        ),
    },
    {
        "level": 3,
        "type": "dimension",
        "name": "time",
        "standard_name": "time",
        "comment":  (
                'End of aggregation interval (interval length: {time_window_s} s).'
        ),
    },
    {
        "level": 3,
        "type": "dimension",
        "name": "altitude",
        "standard_name": "altitude",
        "units": "m",
        "reference_geoid": "EGM96",
        "comment":  (
                'Altitude of centre of range gate above sea level.'
        ),
    },
    {
        "level": 3,
        "type": "dimension",
        "name": "station",
        "long_name": "station",
        "units": "m",
        "comment": 'The code that uniquely identifies the measurement station.',
    },
    {
        "level": 3,
        "type": "variable",
        "name": "system_id",
        "long_name": "system_unique_id",
        "units": defs.UNITLESS_UNITS,
        "comment":  (
            'The specific system (instrument) currently deployed at the measurement station'
        ),
    },
    {
        "level": 3,
        "type": "variable",
        "name": "station_lat",
        "standard_name": "latitude",
        "units": "degrees_north",
        "comment":  'The decimal latitude of the measurement station',
    },
    {
        "level": 3,
        "type": "variable",
        "name": "station_lon",
        "standard_name": "longitude",
        "units": "degrees_east",
        "comment": 'The decimal longitude of the measurement station',
    },
    {
        "level": 3,
        "type": "variable",
        "name": "station_height",
        "standard_name": "height",
        "units": "m",
        "comment": (
            'The measurement station height above ground level. The "ground level" '
            'surface is the street level. e.g. if the station is on a rooftop, then the '
            'height is the building rooftop height above street level.'
        )
    },
    {
        "level": 3,
        "type": "variable",
        "name": "station_altitude",
        "standard_name": "altitude",
        "units": "m",
        "reference_geoid": "EGM96",
        "comment": (
            'The measurement station height above sea level.'
        )
    },
]
