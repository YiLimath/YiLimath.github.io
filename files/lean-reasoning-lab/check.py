"""Regression checks for these fixed teaching fixtures, NOT a proof admission service."""
import argparse
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--lean', help='Optional path to the pinned Lean executable')
args = parser.parse_args()
root = Path(__file__).resolve().parent
prefix = [args.lean] if args.lean else ['lake', 'env', 'lean']
version = subprocess.run(prefix + ['--version'], cwd=root, capture_output=True, text=True, check=True)
if 'version 4.19.0' not in version.stdout:
    raise SystemExit('Use the pinned Lean 4.19.0 toolchain for these fixtures.')
results = []
for file, succeeds, marker in [
    ('Formalization.lean', True, 'does not depend on any axioms'),
    ('Solutions.lean', True, 'does not depend on any axioms'),
    ('fixtures/Broken.lean', False, 'type mismatch'),
    ('fixtures/Incomplete.lean', True, 'sorryAx'),
    ('fixtures/ExtraAxiom.lean', True, 'inventedBound'),
]:
    run = subprocess.run(prefix + [file], cwd=root, capture_output=True, text=True, encoding='utf-8', timeout=60)
    output = run.stdout + run.stderr
    ok = (run.returncode == 0) == succeeds and marker in output
    if file in ('Formalization.lean', 'Solutions.lean'):
        ok = ok and output.count('does not depend on any axioms') == 2
    results.append({'file': file, 'exit_code': run.returncode, 'expected_behavior': ok, 'output': output})
print(json.dumps({'lean': version.stdout.strip(), 'fixtures': results}, ensure_ascii=False, indent=2))
raise SystemExit(0 if all(x['expected_behavior'] for x in results) else 1)
