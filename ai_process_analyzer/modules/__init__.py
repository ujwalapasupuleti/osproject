"""
AI Process Analyzer Modules Package

This package includes:
- collector: Handles system metric collection
- analyzer: Detects anomalies and identifies bottlenecks
- forecaster: Predicts short-term resource usage trends
- recommender: Generates optimization suggestions
"""

from .collector import collect_metrics
from .analyzer import detect_anomalies, identify_bottlenecks
from .forecaster import forecast_cpu
from .recommender import recommend_optimizations

__all__ = [
    "collect_metrics",
    "detect_anomalies",
    "identify_bottlenecks",
    "forecast_cpu",
    "recommend_optimizations"
]

__version__ = "0.1.0"
__author__ = "Code GPT"
