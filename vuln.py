import os, yaml, sys

apikey="12345678790"
password=apikey
token='ghp_12345abcdefg12345abcdefg12345abcdefg12'
if len(sys.argv) < 2:
    print("Usage: python vuln.py <yaml_file>")
    sys.exit(1)

# FIX: Use yaml.safe_load instead of yaml.load
with open(sys.argv[1], 'r') as f:
    data = yaml.safe_load(f)  # FIXED! No more code execution risk.

print("Parsed data:", data)
