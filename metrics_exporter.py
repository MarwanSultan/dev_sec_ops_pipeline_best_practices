from prometheus_client import start_http_server, Gauge
import time
import xml.etree.ElementTree as ET

TEST_TOTAL = Gauge('pytest_total_tests', 'Total number of tests')
TEST_PASSED = Gauge('pytest_passed_tests', 'Number of tests passed')
TEST_FAILED = Gauge('pytest_failed_tests', 'Number of tests failed')
TEST_SKIPPED = Gauge('pytest_skipped_tests', 'Number of tests skipped')

def parse_junit_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    total = int(root.attrib.get('tests', 0))
    failures = int(root.attrib.get('failures', 0))
    skipped = int(root.attrib.get('skipped', 0))
    passed = total - failures - skipped
    return total, passed, failures, skipped

def update_metrics():
    total, passed, failed, skipped = parse_junit_xml('results.xml')
    TEST_TOTAL.set(total)
    TEST_PASSED.set(passed)
    TEST_FAILED.set(failed)
    TEST_SKIPPED.set(skipped)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        update_metrics()
        time.sleep(30)
