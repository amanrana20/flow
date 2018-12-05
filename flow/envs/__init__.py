"""Contains all callable environments in Flow."""

from flow.envs.base_env import Env
from flow.envs.multiagent_env import MultiEnv
from flow.envs.bay_bridge.base import BayBridgeEnv
from flow.envs.bottleneck_env import BottleNeckAccelEnv, BottleneckEnv, \
    DesiredVelocityEnv
from flow.envs.green_wave_env import TrafficLightGridEnv, \
    PO_TrafficLightGridEnv, GreenWaveTestEnv
from flow.envs.loop.lane_changing import LaneChangeAccelEnv, \
    LaneChangeAccelPOEnv
from flow.envs.loop.loop_accel import AccelEnv
from flow.envs.loop.loop_accel import AccelCNNDebugEnv, AccelCNNEnv, \
    AccelCNNIDMEnv
from flow.envs.loop.loop_accel import MultiAgentAccelEnv
from flow.envs.loop.loop_merges import TwoLoopsMergePOEnv
from flow.envs.loop.loop_merges import TwoLoopsMergeCNNDebugEnv, \
    TwoLoopsMergeCNNEnv, TwoLoopsMergeCNNIDMEnv
from flow.envs.loop.wave_attenuation import WaveAttenuationEnv, \
    WaveAttenuationPOEnv
from flow.envs.loop.wave_attenuation import WaveAttenuationCNNDebugEnv, \
WaveAttenuationCNNEnv, WaveAttenuationCNNIDMEnv
from flow.envs.loop.wave_attenuation import MultiWaveAttenuationPOEnv
from flow.envs.merge import WaveAttenuationMergePOEnv
from flow.envs.test import TestEnv
from flow.envs.minicity import MinicityCNNIDMEnv,MinicityIDMEnv

__all__ = [
    "Env", "MultiEnv", "AccelEnv", "LaneChangeAccelEnv",
    "LaneChangeAccelPOEnv",
    "GreenWaveTestEnv", "GreenWaveTestEnv", "WaveAttenuationMergePOEnv",
    "TwoLoopsMergePOEnv", "BottleneckEnv", "BottleNeckAccelEnv",
    "WaveAttenuationEnv", "WaveAttenuationPOEnv", "MultiWaveAttenuationPOEnv",
    "TrafficLightGridEnv", "PO_TrafficLightGridEnv", "DesiredVelocityEnv",
    "TestEnv", "BayBridgeEnv", "MultiAgentAccelEnv",
    "AccelCNNDebugEnv", "AccelCNNEnv", "AccelCNNIDMEnv",
    "WaveAttenuationCNNDebugEnv", "WaveAttenuationCNNEnv", \
    "WaveAttenuationCNNIDMEnv", "TwoLoopsMergeCNNDebugEnv", \
    "TwoLoopsMergeCNNEnv", "TwoLoopsMergeCNNIDMEnv","MinicityCNNIDMEnv","MinicityIDMEnv"
]
