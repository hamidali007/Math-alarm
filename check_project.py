from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = ['pubspec.yaml', 'lib/main.dart', 'lib/hr.dart', 'lib/reports.dart', 'lib/sync_status.dart', 'assets/fonts/NotoNaskhArabic-Regular.ttf', '.github/workflows/android-debug.yml']
missing = [p for p in required if not (root / p).is_file()]
if missing:
    print('Missing:', ', '.join(missing))
    sys.exit(1)
source = (root / 'lib/main.dart').read_text(encoding='utf-8')
if 'createHrIsolationGuards' not in source or 'PRAGMA foreign_keys = ON' not in source:
    print('Database safeguards not found')
    sys.exit(1)
print('PASS: required files and safeguard references present (not a Flutter build test)')
