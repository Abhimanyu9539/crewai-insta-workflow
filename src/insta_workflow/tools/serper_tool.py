"""
Serper Tool for Trend Research
Handles real-time search data using Serper API for trend analysis and content research
"""
import os 
import requests
import json
from typing import List, Dict, Any, Optional
from datetime import datetime
import time

from crewai_tools import SerperDevTool